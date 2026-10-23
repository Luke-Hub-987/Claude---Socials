"""Build the Shopify theme files from the website pages.

    python3 website/build_shopify.py

Writes website/shopify/ with the same folders as a Shopify theme:
  layout/ern.liquid            a clean layout (no old header/footer)
  sections/ern-home.liquid     the home page (free pace plan)
  sections/ern-bar.liquid      the Carb Bar page
  templates/index.json         home page -> ern layout + ern-home section
  templates/page.the-bar.json  /pages/the-bar -> ern layout + ern-bar section
  assets/                      ern.css, ern.js, plan.js and the images

Photos become image pickers and the Klaviyo list IDs become settings in the
theme editor, so nothing needs editing by hand once it's uploaded.
"""
import json
import pathlib
import re
import shutil
import sys

SRC = pathlib.Path(__file__).resolve().parent
OUT = SRC / 'shopify'

KLAVIYO_SETTINGS = [
    {"type": "header", "content": "Klaviyo sign-up forms"},
    {"type": "paragraph", "content": "Sign-ups use a Klaviyo embedded form that adds people to Email List. One form can go in both boxes. Klaviyo > Sign-up forms > the form > the 6-character ID in its address."},
    {"type": "text", "id": "kl_plan_form", "label": "Pace plan form ID", "info": "The embedded form in the plan card. When it's submitted, the plan appears."},
    {"type": "text", "id": "kl_bar_form", "label": "Bar waitlist form ID", "info": "Can be the same form ID as the plan."},
]

CONFIG_JS = ('<script>window.ERN_CONFIG = { klPlanForm: {{ section.settings.kl_plan_form | default: "" | json }}, '
             'klBarForm: {{ section.settings.kl_bar_form | default: "" | json }} };</script>\n'
             '<script src="{{ \'plan.js\' | asset_url }}" defer></script>\n'
             '<script src="{{ \'ern.js\' | asset_url }}" defer></script>\n')


# In Shopify's theme editor: no scroll animations (sections re-render there
# and would stay invisible), and a loud warning if a Klaviyo list ID is
# missing, because then the forms look fine but save nothing.
DESIGN_MODE = (
    '{%- if request.design_mode -%}\n'
    '<style>.ern .rv{opacity:1!important;transform:none!important}</style>\n'
    '{%- if NEEDED -%}\n'
    '<div style="background:#C2362B;color:#fff;font:600 15px/1.4 Arial,sans-serif;padding:12px 16px;text-align:center">'
    'Klaviyo form ID missing: this page can\'t collect emails yet. Click this section and paste the form ID.</div>\n'
    '{%- endif -%}\n'
    '{%- endif -%}\n')


def write_static_messages(path):
    # the runners' messages (proof_data.py) are written into the page itself
    sys.path.insert(0, str(SRC))
    import proof_data
    html = path.read_text()
    a, b = '<!-- messages:start -->\n', '<!-- messages:end -->'
    i, j = html.index(a) + len(a), html.index(b)
    path.write_text(html[:i] + proof_data.render_all() + html[j:])


def founders_photo(alt, brief):
    # the uploaded photo if one is picked in the theme editor, else the current one
    return ('{%- if section.settings.founders_photo -%}'
            '{{ section.settings.founders_photo | image_url: width: 900 | image_tag: alt: "' + alt + '", loading: "lazy" }}'
            '{%- else -%}<img src="{{ \'founders.webp\' | asset_url }}" alt="' + alt + '" width="800" height="800" loading="lazy">'
            '{%- endif -%}')


def convert(html, section_name, extra_settings, page_fix=None, blocks=None):
    style = re.search(r'<style>(.*?)</style>', html, re.S).group(1)
    body = re.search(r'<body[^>]*>(.*)</body>', html, re.S).group(1)
    # scripts: drop the file includes (loaded below), keep the page script
    body = re.sub(r'<script src="(plan|ern)\.js"></script>\n?', '', body)
    if page_fix:
        body = page_fix(body)
    # links between the two pages
    body = body.replace('href="bar.html"', 'href="/pages/the-bar"')
    body = body.replace('href="index.html#get-plan"', 'href="{{ routes.root_url }}#get-plan"')
    body = body.replace('href="index.html"', 'href="{{ routes.root_url }}"')
    body = body.replace('href="/"', 'href="{{ routes.root_url }}"')
    # asset paths -> theme assets
    style = re.sub(r"url\(assets/([^)]+)\)", r"url({{ '\1' | asset_url }})", style)
    body = re.sub(r'src="assets/([^"]+)"', r"""src="{{ '\1' | asset_url }}" """.strip(), body)
    # config + libraries before the page script
    # the libraries load with defer (Shopify's checker flags blocking scripts),
    # so the page script waits for them: deferred files run before DOMContentLoaded
    i = body.rfind('<script>')
    j = body.index('</script>', i)
    page_js = body[i + len('<script>'):j]
    body = (body[:i] + CONFIG_JS + "<script>document.addEventListener('DOMContentLoaded', function(){" +
            page_js + '});</script>' + body[j + len('</script>'):])
    # Klaviyo's embedded forms, by the IDs set in the theme editor
    body = body.replace('klaviyo-form-KLPLAN', 'klaviyo-form-{{ section.settings.kl_plan_form }}')
    body = body.replace('klaviyo-form-KLBAR', 'klaviyo-form-{{ section.settings.kl_bar_form }}')
    needed = []
    if 'kl_plan_form }}' in body: needed.append('section.settings.kl_plan_form == blank')
    if 'kl_bar_form }}' in body: needed.append('section.settings.kl_bar_form == blank')
    schema = {"name": section_name, "tag": "div", "settings": KLAVIYO_SETTINGS + extra_settings,
              "presets": [{"name": section_name}]}
    if blocks:
        schema["blocks"] = blocks
        schema["max_blocks"] = 16
    return ('{% comment %} Built by website/build_shopify.py. Edit the website/ files and rebuild. {% endcomment %}\n'
            '<style>' + style + '</style>\n' + DESIGN_MODE.replace('NEEDED', ' or '.join(needed) or 'false') + body.strip() + '\n\n{% schema %}\n' +
            json.dumps(schema, indent=2) + '\n{% endschema %}\n')


def home_fix(body):
    body = re.sub(r'<img src="assets/founders\.webp"[^>]*>',
                  founders_photo('Luke and Jamie', ''), body)
    return body


def bar_fix(body):
    body = re.sub(r'<img src="assets/founders\.webp"[^>]*>', founders_photo('Luke and Jamie', ''), body)
    # the Rice Crisp Graveyard: 4 image pickers; the photo row only shows once one is set
    figs = re.findall(r'      <figure><div class="slot"><img src="" alt=""><span class="brief">Failed batch photo</span></div><figcaption>(Ep\. \d)</figcaption></figure>\n', body)
    block = re.search(r'    <div class="yard rv">\n(.*?)    </div>\n', body, re.S)
    new = ['    {%- if section.settings.graveyard_1 or section.settings.graveyard_2 or section.settings.graveyard_3 or section.settings.graveyard_4 -%}\n',
           '    <div class="yard rv">\n']
    for n, cap in enumerate(figs, 1):
        new.append('      {%- if section.settings.graveyard_' + str(n) + ' -%}<figure><div class="slot">'
                   '{{ section.settings.graveyard_' + str(n) + ' | image_url: width: 500 | image_tag: loading: "lazy" }}'
                   '</div><figcaption>' + cap + '</figcaption></figure>{%- endif -%}\n')
    new.append('    </div>\n    {%- endif -%}\n')
    body = body[:block.start()] + ''.join(new) + body[block.end():]
    return body


PHOTO = [{"type": "header", "content": "Photos"},
         {"type": "image_picker", "id": "founders_photo", "label": "Photo of Luke and Jamie",
          "info": "Square works best. Leave empty to keep the current photo."}]
GRAVEYARD = [{"type": "image_picker", "id": "graveyard_%d" % n, "label": "Rice Crisp Graveyard photo %d" % n}
             for n in range(1, 5)]

LAYOUT = '''<!doctype html>
<html lang="{{ request.locale.iso_code }}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ page_title }}{% unless page_title contains shop.name %} | {{ shop.name }}{% endunless %}</title>
  {%- if page_description %}<meta name="description" content="{{ page_description | escape }}">{% endif %}
  <link rel="canonical" href="{{ canonical_url }}">
  {%- if settings.favicon %}<link rel="icon" href="{{ settings.favicon | image_url: width: 64 }}">{% endif %}
  <meta property="og:site_name" content="{{ shop.name }}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{{ page_title | escape }}">
  <meta property="og:url" content="{{ canonical_url }}">
  {%- if page_description %}<meta property="og:description" content="{{ page_description | escape }}">{% endif %}
  <meta property="og:image" content="https:{{ 'ern-share.jpg' | asset_url }}">
  <meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  {{ 'ern.css' | asset_url | stylesheet_tag }}
  {{ content_for_header }}
</head>
<body style="margin:0">
  {{ content_for_layout }}
</body>
</html>
'''


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    for d in ('layout', 'sections', 'templates', 'assets'):
        (OUT / d).mkdir(parents=True)
    (OUT / 'layout' / 'ern.liquid').write_text(LAYOUT)
    write_static_messages(SRC / 'index.html')
    home = (SRC / 'index.html').read_text()
    bar = (SRC / 'bar.html').read_text()
    (OUT / 'sections' / 'ern-home.liquid').write_text(convert(home, 'ERN Home', PHOTO, home_fix))
    (OUT / 'sections' / 'ern-bar.liquid').write_text(convert(bar, 'ERN Bar', PHOTO + GRAVEYARD, bar_fix))
    for name, section in (('index.json', 'ern-home'), ('page.the-bar.json', 'ern-bar')):
        main_section = {"type": section, "settings": {}}
        tpl = {"layout": "ern", "sections": {"main": main_section}, "order": ["main"]}
        (OUT / 'templates' / name).write_text(json.dumps(tpl, indent=2) + '\n')
    for f in ('ern.js', 'plan.js'):
        shutil.copy(SRC / f, OUT / 'assets' / f)
    # theme assets sit in one flat folder, so the fonts are next to ern.css there
    (OUT / 'assets' / 'ern.css').write_text((SRC / 'ern.css').read_text().replace('url(assets/', 'url('))
    for f in (SRC / 'assets').iterdir():
        shutil.copy(f, OUT / 'assets' / f.name)
    print('built', sorted(str(p.relative_to(OUT)) for p in OUT.rglob('*') if p.is_file()))


if __name__ == '__main__':
    main()
