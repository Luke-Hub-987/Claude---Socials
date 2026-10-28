"""Render the 5 NYC Marathon map images (1080 x 960) from route.json and TIGER land/water.
Usage: python3 -I render.py <data dir> <route.json> <out dir> [debug]
"""
import shapefile, sys, json, math, os
from PIL import Image, ImageDraw
from shapely.geometry import LineString

D, RJ, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
DEBUG = len(sys.argv) > 4
W, H, SS = 1080, 960, 3                      # final size, supersampling
LAND, WATER = (0xE9, 0xE6, 0xDF), (0xD6, 0xE6, 0xEF)
BLUE, GREY, DOT = (0x1F, 0x7A, 0xE0), (0xC9, 0xC9, 0xC9), (0x0D, 0x17, 0x26)
LINE, DOT_R = 22, 13                         # px at final size

LAT0 = 40.70
KX = 111320 * math.cos(math.radians(LAT0)); KY = 110540
R = json.load(open(RJ))
legs = R['legs']

# frame: the route's box, centred, with the same margin top and bottom
allpts = [p for _, cs in legs for p in cs]
xs = [p[0] * KX for p in allpts]; ys = [p[1] * KY for p in allpts]
cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
MARGIN = 78
scale = min((W - 2 * MARGIN) / (max(xs) - min(xs)), (H - 2 * MARGIN) / (max(ys) - min(ys)))
def px(lon, lat, s=SS):
    return ((W / 2 + (lon * KX - cx) * scale) * s, (H / 2 - (lat * KY - cy) * scale) * s)
lon_min = (cx - W / 2 / scale) / KX; lon_max = (cx + W / 2 / scale) / KX
lat_min = (cy - H / 2 / scale) / KY; lat_max = (cy + H / 2 / scale) / KY
print(f'frame: lon {lon_min:.4f} to {lon_max:.4f}, lat {lat_min:.4f} to {lat_max:.4f}; {1/scale:.1f} m per px')

def inframe(bbox, pad=0.05):
    x0, y0, x1, y1 = bbox
    return not (x1 < lon_min - pad or x0 > lon_max + pad or y1 < lat_min - pad or y0 > lat_max + pad)

def rings(shape):
    parts = list(shape.parts) + [len(shape.points)]
    for a, b in zip(parts[:-1], parts[1:]):
        r = shape.points[a:b]
        area = sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(r, r[1:] + r[:1])) / 2
        yield r, area < 0          # shapefile outer rings run clockwise

# ---- land and water mask ----
mask = Image.new('L', (W * SS, H * SS), 0)
md = ImageDraw.Draw(mask)
COUNTIES = {'36085', '36047', '36081', '36061', '36005', '36059', '36119', '34017', '34003', '34013', '34039', '34023', '34031'}
rc = shapefile.Reader(f'{D}/county/tl_2023_us_county')
for i, rec in enumerate(rc.iterRecords(fields=['GEOID'])):
    if rec['GEOID'] not in COUNTIES: continue
    sh = rc.shape(i)
    if not inframe(sh.bbox): continue
    for r, outer in rings(sh):
        md.polygon([px(*p) for p in r], fill=255 if outer else 0)
n = 0
for f in sorted(os.listdir(D)):
    if not f.startswith('aw_') or '.' in f: continue
    rw = shapefile.Reader(f'{D}/{f}/tl_2023_{f[3:]}_areawater')
    for sh in rw.shapes():
        if not inframe(sh.bbox, 0): continue
        rs = list(rings(sh))
        for r, outer in rs:
            if outer: md.polygon([px(*p) for p in r], fill=0, outline=0); n += 1
        for r, outer in rs:
            if not outer: md.polygon([px(*p) for p in r], fill=255)
print('water polygons drawn:', n)
if DEBUG: mask.resize((W, H)).save(f'{OUT}/debug-rawmask.png')
# simplify: drop water narrower than about 70 m (pier slips), keep rivers
from PIL import ImageFilter
import numpy as np
mask = mask.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.MinFilter(9))   # slips between piers
mask = mask.filter(ImageFilter.MinFilter(9)).filter(ImageFilter.MaxFilter(9))   # the piers themselves
# keep only the water that joins the harbour and the ocean; lakes and park ponds become land.
# Flood on a slightly widened copy so seams between water bodies on county lines don't block it.
wide = mask.filter(ImageFilter.MinFilter(5))
seeds = [(-74.045, 40.672), (-74.02, 40.585), (-73.975, 40.705), (-73.955, 40.745)]
for lon, lat in seeds:
    x, y = px(lon, lat)
    if 0 <= x < W * SS and 0 <= y < H * SS and wide.getpixel((int(x), int(y))) == 0:
        ImageDraw.floodfill(wide, (int(x), int(y)), 128)
# and any water running off the edge of the frame (Jamaica Bay reaches the ocean off-frame)
for x in range(0, W * SS, 3):
    for y in (0, H * SS - 1):
        if wide.getpixel((x, y)) == 0: ImageDraw.floodfill(wide, (x, y), 128)
for y in range(0, H * SS, 3):
    for x in (0, W * SS - 1):
        if wide.getpixel((x, y)) == 0: ImageDraw.floodfill(wide, (x, y), 128)
water = (np.array(wide) == 128) & (np.array(mask) == 0)
mask = Image.fromarray(np.where(water, 128, 255).astype('uint8'))

base = Image.new('RGB', (W * SS, H * SS), LAND)
base.paste(Image.new('RGB', base.size, WATER), mask=mask.point(lambda v: 255 if v == 128 else 0))

# ---- the route ----
def cut_at_lat(cs, lat):
    for i, (a, b) in enumerate(zip(cs[:-1], cs[1:])):
        if (a[1] - lat) * (b[1] - lat) <= 0 and a[1] != b[1]:
            t = (lat - a[1]) / (b[1] - a[1]); p = (a[0] + (b[0] - a[0]) * t, lat)
            return cs[:i + 1] + [p], [p] + cs[i + 1:]
    return cs, []

names = [l for l, _ in legs]
idx = {l: i for i, l in enumerate(names)}
# McGuinness runs onto the Pulaski Bridge in TIGER: split it where the bridge starts (40.7354)
mg = idx['McGuinness Blvd']
before, after = cut_at_lat(legs[mg][1], 40.7354)
legs = legs[:mg] + [('McGuinness Blvd', before), ('Pulaski Bridge (south)', after)] + legs[mg + 1:]
names = [l for l, _ in legs]; idx = {l: i for i, l in enumerate(names)}

def span(a, b):   # legs a..b inclusive, as one line
    out = []
    for _, cs in legs[idx[a]:idx[b] + 1]:
        out += cs if not out else cs[1:] if cs and out[-1] == cs[0] else cs
    return out

FULL = span(names[0], names[-1])
STAGES = [
    ('1-whole-route',      None),
    ('2-miles-0-2',        span('SI Expressway', 'Verrazzano Bridge')),
    ('3-miles-2-13',       span('Dahlgren Pl', 'McGuinness Blvd')),
    ('4-miles-15-20',      span('Queensboro Bridge', '1st Ave')),
    ('5-mile-20-to-line',  span('Willis Ave Bridge', names[-1])),
]

def draw_line(d, cs, col):
    s = LineString([(p[0] * KX, p[1] * KY) for p in cs]).simplify(4)
    pts = [px(x / KX, y / KY) for x, y in s.coords]
    w = LINE * SS; r = w / 2
    d.line(pts, fill=col, width=w)
    for x, y in pts: d.ellipse((x - r, y - r, x + r, y + r), fill=col)

os.makedirs(OUT, exist_ok=True)
for name, hi in STAGES:
    img = base.copy(); d = ImageDraw.Draw(img)
    draw_line(d, FULL, BLUE if hi is None else GREY)
    if hi: draw_line(d, hi, BLUE)
    for lon, lat in (R['start'], R['finish']):
        x, y = px(lon, lat); r = DOT_R * SS; d.ellipse((x - r, y - r, x + r, y + r), fill=DOT)
    img.resize((W, H), Image.LANCZOS).save(f'{OUT}/nyc-marathon-{name}.png', optimize=True)
    print('saved', name)

if DEBUG:   # close-ups at 3x for checking the trace
    full = base.copy(); d = ImageDraw.Draw(full)
    s = LineString([(p[0] * KX, p[1] * KY) for p in FULL])
    d.line([px(x / KX, y / KY) for x, y in s.coords], fill=(220, 30, 30), width=4)
    for label, (lon, lat) in [('greenpoint', (-73.952, 40.733)), ('lic', (-73.946, 40.748)), ('bronx', (-73.932, 40.810)),
                              ('park', (-73.968, 40.774)), ('bridge', (-74.040, 40.610)), ('qbb', (-73.955, 40.757))]:
        x, y = px(lon, lat); h = 330
        full.crop((int(x - h), int(y - h), int(x + h), int(y + h))).save(f'{OUT}/debug-{label}.png')
