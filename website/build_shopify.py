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

SRC = pathlib.Path(__file__).resolve().parent
OUT = SRC / 'shopify'

KLAVIYO_SETTINGS = [
    {"type": "header", "content": "Klaviyo"},
    {"type": "text", "id": "plan_list", "label": "Pace plan list ID (Email List)",
     "info": "Klaviyo > Lists & segments > Email List > Settings > List ID"},
    {"type": "text", "id": "waitlist_list", "label": "Bar waitlist list ID"},
    {"type": "text", "id": "results_list", "label": "Race results list ID"},
]

CONFIG_JS = ('<script>window.ERN_CONFIG = { planList: {{ section.settings.plan_list | default: "" | json }}, '
             'waitlistList: {{ section.settings.waitlist_list | default: "" | json }}, '
             'resultsList: {{ section.settings.results_list | default: "" | json }} };</script>\n'
             '<script src="{{ \'plan.js\' | asset_url }}"></script>\n'
             '<script src="{{ \'ern.js\' | asset_url }}"></script>\n')


def founders_photo(alt, brief):
    # the uploaded photo if one is picked in the theme editor, else the current one
    return ('{%- if section.settings.founders_photo -%}'
            '{{ section.settings.founders_photo | image_url: width: 900 | image_tag: alt: "' + alt + '", loading: "lazy" }}'
            '{%- else -%}<img src="{{ \'founders.webp\' | asset_url }}" alt="' + alt + '" width="800" height="800" loading="lazy">'
            '{%- endif -%}')


def convert(html, section_name, extra_settings, page_fix=None):
    style = re.search(r'<style>(.*?)</style>', html, re.S).group(1)
    body = re.search(r'<body[^>]*>(.*)</body>', html, re.S).group(1)
    # scripts: drop the file includes (loaded below), keep the page script
    body = re.sub(r'<script src="(plan|ern)\.js"></script>\n?', '', body)
    if page_fix:
        body = page_fix(body)
    # links between the two pages
    body = body.replace('href="bar.html"', 'href="/pages/the-bar"')
    body = body.replace('href="index.html#get-plan"', 'href="/#get-plan"')
    body = body.replace('href="index.html"', 'href="/"')
    # asset paths -> theme assets
    style = re.sub(r"url\(assets/([^)]+)\)", r"url({{ '\1' | asset_url }})", style)
    body = re.sub(r'src="assets/([^"]+)"', r"""src="{{ '\1' | asset_url }}" """.strip(), body)
    # config + libraries before the page script
    i = body.rfind('<script>')
    body = body[:i] + CONFIG_JS + body[i:]
    schema = {"name": section_name, "tag": "div", "settings": KLAVIYO_SETTINGS + extra_settings,
              "presets": [{"name": section_name}]}
    return ('{% comment %} Built by website/build_shopify.py. Edit the website/ files and rebuild. {% endcomment %}\n'
            '<style>' + style + '</style>\n' + body.strip() + '\n\n{% schema %}\n' +
            json.dumps(schema, indent=2) + '\n{% endschema %}\n')


def home_fix(body):
    body = re.sub(r'<img src="assets/founders\.webp"[^>]*>',
                  founders_photo('Luke and Jamie at the finish of a race', ''), body)
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
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,700;0,800;1,800&family=DM+Serif+Display:ital@0;1&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
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
    home = (SRC / 'index.html').read_text()
    bar = (SRC / 'bar.html').read_text()
    (OUT / 'sections' / 'ern-home.liquid').write_text(convert(home, 'ERN Home', PHOTO, home_fix))
    (OUT / 'sections' / 'ern-bar.liquid').write_text(convert(bar, 'ERN Bar', PHOTO + GRAVEYARD, bar_fix))
    for name, section in (('index.json', 'ern-home'), ('page.the-bar.json', 'ern-bar')):
        tpl = {"layout": "ern", "sections": {"main": {"type": section, "settings": {}}}, "order": ["main"]}
        (OUT / 'templates' / name).write_text(json.dumps(tpl, indent=2) + '\n')
    for f in ('ern.css', 'ern.js', 'plan.js'):
        shutil.copy(SRC / f, OUT / 'assets' / f)
    for f in (SRC / 'assets').iterdir():
        shutil.copy(f, OUT / 'assets' / f.name)
    print('built', sorted(str(p.relative_to(OUT)) for p in OUT.rglob('*') if p.is_file()))


if __name__ == '__main__':
    main()
