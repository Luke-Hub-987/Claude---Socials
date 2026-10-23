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


# In Shopify's theme editor: no scroll animations (sections re-render there
# and would stay invisible), and a loud warning if a Klaviyo list ID is
# missing, because then the forms look fine but save nothing.
DESIGN_MODE = (
    '{%- if request.design_mode -%}\n'
    '<style>.ern .rv{opacity:1!important;transform:none!important}</style>\n'
    '{%- if section.settings.plan_list == blank or section.settings.waitlist_list == blank or section.settings.results_list == blank -%}\n'
    '<div style="background:#C2362B;color:#fff;font:600 15px/1.4 Arial,sans-serif;padding:12px 16px;text-align:center">'
    'Klaviyo list IDs missing: the forms on this page will NOT save anyone. Click this section and paste all three IDs.</div>\n'
    '{%- endif -%}\n'
    '{%- endif -%}\n')


# Messages from runners, word for word (P143). One list feeds the static page
# and the Shopify blocks. Add more in Shopify: Customize > ERN Home > Add block
# > Message, and paste the exact text. Never write words for anyone.
MESSAGES = [
    {"platform": "instagram", "name": "", "label": "Instagram reply", "result": "−12 min",
     "detail": "Chip time 3:23:58", "text": "‼️\n12 minute pb ❤️"},
    {"platform": "gmail", "name": "Caroline", "label": "", "result": "−13 min",
     "detail": "Dublin Marathon", "text": "Not to get emotional, but you made my day with the plan."},
    {"platform": "instagram", "name": "", "label": "Instagram message", "result": "Goal time hit",
     "detail": "Antwerp Marathon · 3h 28m",
     "text": "Hey Luke hope things are well man! Just wanted to let you know that I ... got the time I was looking for.\n"
             "Not to cringe it up or anything but it was one [of] the best days of my life 😂"},
]
APP = {"instagram": "Instagram", "gmail": "Gmail", "tiktok": "TikTok"}


def message_static(m):
    from html import escape
    who = m["name"] or m["label"] or APP[m["platform"]]
    initial = m["name"][:1].upper() if m["name"] else "★"
    bubbles = ''.join('<p class="bub">%s</p>' % escape(l.strip()) for l in m["text"].split('\n') if l.strip())
    if m["platform"] == "gmail":
        head = ('<div class="gtop"><span class="gm"><i style="color:#EA4335">M</i></span>Inbox</div>'
                '<div class="msg-head"><i class="av">%s</i><div><b>%s</b><small>to Luke</small></div></div>' % (initial, escape(who)))
    else:
        head = ('<div class="msg-head"><i class="av">%s</i><div><b>%s</b><small>%s</small></div><span class="app">%s</span></div>'
                % (initial, escape(who), APP[m["platform"]], APP[m["platform"]]))
    return ('      <div class="msg msg-%s rv"><div class="msg-res"><b>%s</b><span>%s</span></div>'
            '<div class="msg-app">%s<div class="msg-body">%s</div></div></div>\n'
            % (m["platform"], escape(m["result"]), escape(m["detail"]), head, bubbles))


MSG_LIQUID = r"""{%- for block in section.blocks -%}{%- if block.type == 'message' and block.settings.text != blank -%}
{%- assign p = block.settings.platform -%}
{%- capture who -%}{%- if block.settings.name != blank -%}{{ block.settings.name }}{%- elsif block.settings.label != blank -%}{{ block.settings.label }}{%- else -%}{%- case p -%}{%- when 'gmail' -%}Gmail{%- when 'tiktok' -%}TikTok{%- else -%}Instagram{%- endcase -%}{%- endif -%}{%- endcapture -%}
{%- capture app -%}{%- case p -%}{%- when 'gmail' -%}Gmail{%- when 'tiktok' -%}TikTok{%- else -%}Instagram{%- endcase -%}{%- endcapture -%}
{%- if block.settings.name != blank -%}{%- assign initial = block.settings.name | slice: 0 | upcase -%}{%- else -%}{%- assign initial = '★' -%}{%- endif -%}
      <div class="msg msg-{{ p }} rv" {{ block.shopify_attributes }}><div class="msg-res"><b>{{ block.settings.result | escape }}</b><span>{{ block.settings.detail | escape }}</span></div><div class="msg-app">
      {%- if p == 'gmail' -%}<div class="gtop"><span class="gm"><i style="color:#EA4335">M</i></span>Inbox</div><div class="msg-head"><i class="av">{{ initial }}</i><div><b>{{ who | escape }}</b><small>to Luke</small></div></div>
      {%- else -%}<div class="msg-head"><i class="av">{{ initial }}</i><div><b>{{ who | escape }}</b><small>{{ app }}</small></div><span class="app">{{ app }}</span></div>{%- endif -%}
      <div class="msg-body">{%- assign lines = block.settings.text | newline_to_br | split: '<br />' -%}{%- for l in lines -%}{%- assign t = l | strip -%}{%- if t != blank -%}<p class="bub">{{ t | escape }}</p>{%- endif -%}{%- endfor -%}</div></div></div>
{%- endif -%}{%- endfor -%}
"""

MESSAGE_BLOCK = {
    "type": "message", "name": "Message",
    "settings": [
        {"type": "select", "id": "platform", "label": "Where it came from", "default": "instagram",
         "options": [{"value": "instagram", "label": "Instagram"}, {"value": "gmail", "label": "Email (Gmail)"},
                     {"value": "tiktok", "label": "TikTok"}]},
        {"type": "text", "id": "name", "label": "First name (only with their OK)"},
        {"type": "text", "id": "label", "label": "Label if no name", "info": "e.g. Instagram reply"},
        {"type": "text", "id": "result", "label": "Result", "info": "e.g. −13 min, Sub-3, 2:47"},
        {"type": "text", "id": "detail", "label": "Race or detail", "info": "e.g. Dublin Marathon"},
        {"type": "textarea", "id": "text", "label": "Their message, word for word",
         "info": "One line per message bubble. Leave empty to hide this block."},
    ]}


def write_static_messages(path):
    html = path.read_text()
    a, b = '<!-- messages:start -->\n', '<!-- messages:end -->'
    i, j = html.index(a) + len(a), html.index(b)
    path.write_text(html[:i] + ''.join(message_static(m) for m in MESSAGES) + html[j:])


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
    if blocks:
        schema["blocks"] = blocks
        schema["max_blocks"] = 16
    return ('{% comment %} Built by website/build_shopify.py. Edit the website/ files and rebuild. {% endcomment %}\n'
            '<style>' + style + '</style>\n' + DESIGN_MODE + body.strip() + '\n\n{% schema %}\n' +
            json.dumps(schema, indent=2) + '\n{% endschema %}\n')


def home_fix(body):
    body = re.sub(r'<img src="assets/founders\.webp"[^>]*>',
                  founders_photo('Luke and Jamie', ''), body)
    body = re.sub(r'<!-- messages:start -->\n.*?<!-- messages:end -->', lambda m: MSG_LIQUID, body, flags=re.S)
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
    write_static_messages(SRC / 'index.html')
    home = (SRC / 'index.html').read_text()
    bar = (SRC / 'bar.html').read_text()
    (OUT / 'sections' / 'ern-home.liquid').write_text(convert(home, 'ERN Home', PHOTO, home_fix, [MESSAGE_BLOCK]))
    (OUT / 'sections' / 'ern-bar.liquid').write_text(convert(bar, 'ERN Bar', PHOTO + GRAVEYARD, bar_fix))
    for name, section in (('index.json', 'ern-home'), ('page.the-bar.json', 'ern-bar')):
        main_section = {"type": section, "settings": {}}
        if section == 'ern-home':
            main_section["blocks"] = {"msg_%d" % n: {"type": "message", "settings": {k: v for k, v in m.items()}}
                                      for n, m in enumerate(MESSAGES, 1)}
            main_section["block_order"] = ["msg_%d" % n for n in range(1, len(MESSAGES) + 1)]
        tpl = {"layout": "ern", "sections": {"main": main_section}, "order": ["main"]}
        (OUT / 'templates' / name).write_text(json.dumps(tpl, indent=2) + '\n')
    for f in ('ern.css', 'ern.js', 'plan.js'):
        shutil.copy(SRC / f, OUT / 'assets' / f)
    for f in (SRC / 'assets').iterdir():
        shutil.copy(f, OUT / 'assets' / f.name)
    print('built', sorted(str(p.relative_to(OUT)) for p in OUT.rglob('*') if p.is_file()))


if __name__ == '__main__':
    main()
