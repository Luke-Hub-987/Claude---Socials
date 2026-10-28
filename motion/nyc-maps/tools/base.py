"""16:9 base maps (land and water) and the route in pixels, for the New York frames.
Usage: python3 -I base.py <TIGER data dir> <route.json> <out dir>
Writes base-<framing>.png (1920 x 1080) and geo.json: for each framing the route
(dense, with the mile of every point), mile points, landmarks, borough names and
Central Park, all in pixels. The frames themselves are drawn by frames.html.
"""
import shapefile, sys, json, math, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from shapely.geometry import LineString, Point

D, RJ, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
W, H, SS = 1920, 1080, 2
MAPW = 940                                         # the map panel; the plan panel sits to its right
LAND, WATER = (0xEE, 0xE8, 0xDC), (0xCF, 0xE0, 0xF0)
LAT0 = 40.70
KX = 111320 * math.cos(math.radians(LAT0)); KY = 110540
R = json.load(open(RJ)); legs = R['legs']

full = []
for _, cs in legs: full += cs if not full or full[-1] != cs[0] else cs[1:]
line = LineString([(p[0] * KX, p[1] * KY) for p in full])
k = line.length / (26.2188 * 1609.344)             # stretch the trace to the official distance
def at_mile(mi):
    p = line.interpolate(min(max(mi, 0) * 1609.344 * k, line.length)); return (p.x / KX, p.y / KY)
def mile_of_xy(x, y): return line.project(Point(x, y)) / k / 1609.344

def framing_whole(ox):
    xs, ys = line.xy; cx = (min(xs) + max(xs)) / 2; cy = (min(ys) + max(ys)) / 2
    return dict(cx=cx, cy=cy, ox=ox, oy=H / 2, scale=(H - 2 * 64) / (max(ys) - min(ys)))
def framing_miles(a, b, pad=120, max_scale=1 / 7.0):
    seg = [at_mile(a + (b - a) * i / 200) for i in range(201)]
    xs = [p[0] * KX for p in seg]; ys = [p[1] * KY for p in seg]
    s = min((MAPW - 2 * pad) / (max(xs) - min(xs) + 1), (H - 2 * pad) / (max(ys) - min(ys) + 1), max_scale)
    return dict(cx=(min(xs) + max(xs)) / 2, cy=(min(ys) + max(ys)) / 2, ox=MAPW / 2, oy=H / 2, scale=s)

FRAMINGS = {
    'centre': framing_whole(960),
    'left':   framing_whole(470),
    'bridge': framing_miles(-0.2, 2.9),
    'brooklyn': framing_miles(1.8, 13.4),
    'quiet': framing_miles(13.0, 20.0),
    'fifth': framing_miles(19.1, 26.2),
}

def projector(f):
    def px(lon, lat, s=1):
        return ((f['ox'] + (lon * KX - f['cx']) * f['scale']) * s, (f['oy'] - (lat * KY - f['cy']) * f['scale']) * s)
    return px

def rings(shape):
    parts = list(shape.parts) + [len(shape.points)]
    for a, b in zip(parts[:-1], parts[1:]):
        r = shape.points[a:b]
        area = sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(r, r[1:] + r[:1])) / 2
        yield r, area < 0

COUNTIES = {'36085', '36047', '36081', '36061', '36005', '36059', '36119', '34017', '34003', '34013', '34039', '34023', '34031'}
rc = shapefile.Reader(f'{D}/county/tl_2023_us_county')
county_shapes = [rc.shape(i) for i, rec in enumerate(rc.iterRecords(fields=['GEOID'])) if rec['GEOID'] in COUNTIES]
water_shapes = []
for f in sorted(os.listdir(D)):
    if f.startswith('aw_') and '.' not in f:
        water_shapes += shapefile.Reader(f'{D}/{f}/tl_2023_{f[3:]}_areawater').shapes()

def visible(bbox, f, margin=200):
    px = projector(f); x0, y0 = px(bbox[0], bbox[3]); x1, y1 = px(bbox[2], bbox[1])
    return not (x1 < -margin or x0 > W + margin or y1 < -margin or y0 > H + margin)

def base(f):
    px = projector(f)
    mask = Image.new('L', (W * SS, H * SS), 0); md = ImageDraw.Draw(mask)
    for sh in county_shapes:
        if not visible(sh.bbox, f): continue
        for r, outer in rings(sh): md.polygon([px(*p, SS) for p in r], fill=255 if outer else 0)
    for sh in water_shapes:
        if not visible(sh.bbox, f): continue
        rs = list(rings(sh))
        for r, outer in rs:
            if outer: md.polygon([px(*p, SS) for p in r], fill=0, outline=0)
        for r, outer in rs:
            if not outer: md.polygon([px(*p, SS) for p in r], fill=255)
    # simplify: no pier slips, no piers (scaled to the zoom: about 70 m)
    n = max(3, min(15, int(round(70 * f['scale'] * SS))) | 1)
    mask = mask.filter(ImageFilter.MaxFilter(n)).filter(ImageFilter.MinFilter(n))
    mask = mask.filter(ImageFilter.MinFilter(n)).filter(ImageFilter.MaxFilter(n))
    # keep water joined to the harbour, the ocean or the frame edge; lakes become land
    wide = mask.filter(ImageFilter.MinFilter(5))
    seeds = [px(-74.045, 40.672, SS), px(-74.02, 40.585, SS), px(-73.958, 40.762, SS)]
    seeds += [(x, y) for x in range(0, W * SS, 3) for y in (0, H * SS - 1)] + [(x, y) for y in range(0, H * SS, 3) for x in (0, W * SS - 1)]
    for x, y in seeds:
        x, y = int(x), int(y)
        if 0 <= x < W * SS and 0 <= y < H * SS and wide.getpixel((x, y)) == 0: ImageDraw.floodfill(wide, (x, y), 128)
    water = (np.array(wide) == 128) & (np.array(mask) == 0)
    img = np.where(water[..., None], np.array(WATER, 'uint8'), np.array(LAND, 'uint8')).astype('uint8')
    return Image.fromarray(img).resize((W, H), Image.LANCZOS)

marks = {
    'start': R['start'], 'finish': R['finish'],
    'verrazzano': at_mile(1.0), 'bridge_end': at_mile(1.98), 'fourth': at_mile(5.5), 'lafayette': at_mile(8.9), 'bedford': at_mile(10.8),
    'pulaski': at_mile(13.15), 'queensboro': at_mile(15.4), 'first': at_mile(17.6),
    'willis': at_mile(19.5), 'bronx': at_mile(20.5), 'madison': at_mile(21.0), 'fifth': at_mile(22.9), 'park': at_mile(24.6),
}
PLACES = {
    'STATEN ISLAND': (-74.085, 40.600), 'BROOKLYN': (-73.950, 40.655), 'QUEENS': (-73.905, 40.735),
    'MANHATTAN': (-73.985, 40.752), 'THE BRONX': (-73.905, 40.828), 'NEW JERSEY': (-74.085, 40.700),
    'EAST RIVER': (-73.966, 40.748), 'THE NARROWS': (-74.047, 40.598),
    'MANHATTAN ': (-73.972, 40.741), 'THE BRONX ': (-73.915, 40.819), 'MANHATTAN  ': (-73.956, 40.818), 'HARLEM RIVER': (-73.937, 40.823),
}
# Central Park: 59th to 110th Street, Fifth Avenue to Central Park West
PARK = [(-73.9730, 40.7644), (-73.9819, 40.7681), (-73.9581, 40.8006), (-73.9493, 40.7968)]

dense = line.simplify(2).segmentize(30)
geo = {'framings': {}}
os.makedirs(OUT, exist_ok=True)
for name, f in FRAMINGS.items():
    px = projector(f)
    route = [px(x / KX, y / KY) for x, y in dense.coords]
    geo['framings'][name] = {
        'scale_m_per_px': round(1 / f['scale'], 2),
        'route': [[round(a, 1), round(b, 1)] for a, b in route],
        'route_miles': [round(mile_of_xy(x, y), 3) for x, y in dense.coords],
        'miles': {str(i): [round(v, 1) for v in px(*at_mile(i))] for i in range(1, 27)},
        'marks': {kk: [round(v, 1) for v in px(*v2)] for kk, v2 in marks.items()},
        'places': {kk: [round(v, 1) for v in px(*v2)] for kk, v2 in PLACES.items()},
        'park': [[round(v, 1) for v in px(*p)] for p in PARK],
    }
    base(f).save(f'{OUT}/base-{name}.png', optimize=True); print('base', name, '%.1f m/px' % (1 / f['scale']))
json.dump(geo, open(f'{OUT}/geo.json', 'w'))
