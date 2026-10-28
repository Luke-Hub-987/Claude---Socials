"""Build the NYC Marathon route from TIGER 2023 street centrelines.
Usage: python3 -I route.py <data dir> <out json>

The legs follow the 2025 main-route closure list (CBS / NYRR, as printed by
ABC7 and Bleacher Report): every street, in order, with its limits. Each leg is
the shortest path along that street's own centrelines between the junction with
the previous street and the junction with the next one.
"""
import shapefile, sys, json, math, heapq
from shapely.geometry import LineString, Point
from shapely.ops import nearest_points

D, OUT = sys.argv[1], sys.argv[2]
LAT0 = 40.70
KX = 111320 * math.cos(math.radians(LAT0)); KY = 110540
def m(p): return (p[0] * KX, p[1] * KY)
def ll(p): return (p[0] / KX, p[1] / KY)

_cache = {}
def roads(county):
    if county not in _cache:
        r = shapefile.Reader(f'{D}/rd_{county}/tl_2023_{county}_roads')
        _cache[county] = [(rec['FULLNAME'], sh.points, sh.parts) for rec, sh in zip(r.records(), r.shapes())]
    return _cache[county]

def pieces(counties, names, centre, radius):
    c0 = Point(m(centre)); out = []
    for c in counties.split(','):
        for nm, pts, parts in roads(c):
            if nm not in names: continue
            parts = list(parts) + [len(pts)]
            for a, b in zip(parts[:-1], parts[1:]):
                seg = [m(p) for p in pts[a:b]]
                if len(seg) > 1 and LineString(seg).distance(c0) < radius: out.append(seg)
    if not out: raise SystemExit(f'no pieces for {names} near {centre}')
    return out

def key(p): return (round(p[0], 1), round(p[1], 1))

def path(segs, a, b, gap=90):
    for g in (gap, 300, 900):
        try: return _path(segs, a, b, g)
        except LookupError: print('   (bridging gaps up to %d m)' % (g * 3 if g < 900 else g))
    raise SystemExit('no path at all')

def _path(segs, a, b, gap):
    """Shortest path from a to b along segs (metres), bridging gaps between pieces up to `gap`."""
    G = {}
    def edge(u, v):
        d = math.dist(u, v); G.setdefault(key(u), []).append((key(v), d, v)); G.setdefault(key(v), []).append((key(u), d, u))
    verts = []
    for s in segs:
        for u, v in zip(s[:-1], s[1:]): edge(u, v)
        verts += s
    ends = [s[0] for s in segs] + [s[-1] for s in segs]
    for e in ends:
        for v in verts:
            d = math.dist(e, v)
            if 0.5 < d < gap: edge(e, v)
    # join a and b to the network at their projections on the nearest segment
    def attach(p):
        best = None
        for s in segs:
            l = LineString(s); d = l.distance(Point(p))
            if best is None or d < best[0]: best = (d, s, l)
        d, s, l = best; q = l.interpolate(l.project(Point(p))); q = (q.x, q.y)
        # connect q to the two vertices of the segment it lies on
        u, v = min(zip(s[:-1], s[1:]), key=lambda uv: LineString(uv).distance(Point(q)))
        edge(q, u); edge(q, v)
        edge(p, q)
        return d
    da, db = attach(a), attach(b)
    coords = {key(a): a}; dist = {key(a): 0}; prev = {}; pq = [(0, key(a))]
    while pq:
        d, u = heapq.heappop(pq)
        if u == key(b): break
        if d > dist.get(u, 1e18): continue
        for v, w, vc in G.get(u, []):
            nd = d + w
            if nd < dist.get(v, 1e18): dist[v] = nd; prev[v] = u; coords[v] = vc; heapq.heappush(pq, (nd, v))
    if key(b) not in prev and key(a) != key(b): raise LookupError
    out = [b]; u = key(b)
    while u != key(a): u = prev[u]; out.append(coords.get(u, a))
    return out[::-1], da, db

def junction(s1, s2, guess):
    g = Point(m(guess)); best = None
    L1 = [LineString(s) for s in s1]; L2 = [LineString(s) for s in s2]
    for a in L1:
        for b in L2:
            x = a.intersection(b)
            for p in ([x] if x.geom_type == 'Point' else list(getattr(x, 'geoms', []))):
                if p.geom_type == 'Point' and (best is None or p.distance(g) < best[0]): best = (p.distance(g), (p.x, p.y))
    if best is not None and best[0] < 350: return best[1], 'meets %.0f m from guess' % best[0]
    a = min(L1, key=lambda l: l.distance(g)); b = min(L2, key=lambda l: l.distance(g))
    p1, p2 = nearest_points(a, b)
    return ((p1.x + p2.x) / 2, (p1.y + p2.y) / 2), 'nearest points, %.0f m apart' % p1.distance(p2)

# (label, counties, street names, centre for picking the right pieces, radius m, guess for the junction with the NEXT leg)
LEGS = [
 ('SI Expressway',      '36085', ['Staten Island Expy', 'I- 278'], (-74.060, 40.6035), 1500, (-74.0536, 40.6038)),
 ('Verrazzano Bridge',  '36085,36047', ['Verrazano Brg', 'I- 278'], (-74.040, 40.609), 1800, (-74.0275, 40.6129)),
 ('Dahlgren Pl',        '36047', ['Dahlgren Pl'],     (-74.028, 40.615), 1200, (-74.0270, 40.6170)),
 ('92nd St',            '36047', ['92nd St'],         (-74.028, 40.617), 1000, (-74.0302, 40.6183)),
 ('4th Ave',            '36047', ['4th Ave'],         (-74.000, 40.650), 6000, (-73.9781, 40.6845)),
 ('Flatbush Ave',       '36047', ['Flatbush Ave'],    (-73.979, 40.686),  600, (-73.9794, 40.6867)),
 ('Lafayette Ave',      '36047', ['Lafayette Ave'],   (-73.967, 40.688), 2000, (-73.9551, 40.6894)),
 ('Bedford Ave',        '36047', ['Bedford Ave'],     (-73.957, 40.707), 3000, (-73.9535, 40.7235)),
 ('Nassau Ave',         '36047', ['Nassau Ave'],      (-73.952, 40.724),  900, (-73.9510, 40.7240)),
 ('Manhattan Ave',      '36047', ['Manhattan Ave'],   (-73.952, 40.727), 1200, (-73.9543, 40.7302)),
 ('Greenpoint Ave',     '36047', ['Greenpoint Ave'],  (-73.952, 40.730),  800, (-73.9514, 40.7305)),
 ('McGuinness Blvd',    '36047', ['McGuinness Blvd'], (-73.952, 40.734), 1000, (-73.9526, 40.7354)),
 ('Pulaski Bridge',     '36047,36081', ['Pulaski Brg'], (-73.952, 40.741), 900, (-73.9505, 40.7440)),
 ('11th St',            '36081', ['11th St'],         (-73.950, 40.745),  700, (-73.9497, 40.7450)),
 ('48th Ave',           '36081', ['48th Ave'],        (-73.952, 40.745),  700, (-73.9540, 40.7438)),
 ('Vernon Blvd',        '36081', ['Vernon Blvd'],     (-73.953, 40.746),  900, (-73.9530, 40.7465)),
 ('10th St',            '36081', ['10th St'],         (-73.952, 40.748),  700, (-73.9505, 40.7495)),
 ('44th Dr',            '36081', ['44th Dr'],         (-73.946, 40.749), 1200, (-73.9435, 40.7488)),
 ('Hunter St',          '36081', ['Hunter St'],       (-73.942, 40.749),  800, (-73.9410, 40.7500)),
 ('Crescent St',        '36081', ['Crescent St'],     (-73.940, 40.751),  800, (-73.9400, 40.7508)),
 ('Queens Plaza S',     '36081', ['Queens Plz S'],    (-73.939, 40.750),  900, (-73.9380, 40.7505)),
 ('Queensboro Bridge',  '36081,36061', ['Queensboro Brg', 'Ed Koch Queensboro Brg'], (-73.952, 40.756), 2200, (-73.9640, 40.7605)),
 ('E 59th St',          '36061', ['E 59th St'],       (-73.963, 40.760),  600, (-73.9614, 40.7595)),
 ('1st Ave',            '36061', ['1st Ave'],         (-73.945, 40.780), 5000, (-73.9330, 40.8020)),
 ('Willis Ave Bridge',  '36061,36005', ['Willis Avenue Brg'], (-73.929, 40.805), 900, (-73.9260, 40.8055)),
 ('E 135th St (Bx)',    '36005', ['E 135th St'],      (-73.926, 40.806),  500, (-73.9272, 40.8060)),
 ('Alexander Ave',      '36005', ['Alexander Ave'],   (-73.927, 40.808),  700, (-73.9255, 40.8100)),
 ('E 138th St (Bx)',    '36005', ['E 138th St'],      (-73.928, 40.811), 1000, (-73.9285, 40.8115)),
 ('3rd Ave (Bx)',       '36005', ['3rd Ave'],         (-73.929, 40.812),  500, (-73.9295, 40.8125)),
 ('Morris Ave',         '36005', ['Morris Ave'],      (-73.929, 40.813),  500, (-73.9300, 40.8135)),
 ('E 140th St',         '36005', ['E 140th St'],      (-73.927, 40.8135),  300, (-73.9271, 40.8134)),
 ('Rider Ave',          '36005', ['Rider Ave'],       (-73.930, 40.812),  500, (-73.9305, 40.8120)),
 ('E 138th St (Bx) 2',  '36005', ['E 138th St'],      (-73.931, 40.813),  700, (-73.9324, 40.8141)),
 ('Madison Ave Bridge', '36005,36061', ['Madison Avenue Brg'], (-73.934, 40.814), 600, (-73.9348, 40.8140)),
 ('E 138th St (Mn)',    '36061', ['E 138th St'],      (-73.936, 40.8145), 500, (-73.9370, 40.8150)),
 ('5th Ave (Harlem)',   '36061', ['5th Ave'],         (-73.940, 40.810), 1000, (-73.9429, 40.8065)),
 ('W 124th St',         '36061', ['W 124th St', 'E 124th St'], (-73.944, 40.807), 400, (-73.9440, 40.8060)),
 ('Mt Morris Park W',   '36061', ['Mount Morris Park W'], (-73.945, 40.805), 400, (-73.9461, 40.8039)),
 ('W 120th St',         '36061', ['W 120th St', 'E 120th St'], (-73.945, 40.804), 400, (-73.9447, 40.8033)),
 ('5th Ave',            '36061', ['5th Ave'],         (-73.952, 40.793), 1800, (-73.9587, 40.7843)),
 ('E 90th St',          '36061', ['E 90th St'],       (-73.959, 40.784),  400, (-73.9592, 40.7848)),
 ('East Dr',            '36061', ['East Dr'],         (-73.967, 40.774), 2500, (-73.9725, 40.7655)),
 ('Grand Army Plaza',   '36061', ['Grand Army Plz'],  (-73.973, 40.765),  400, (-73.9735, 40.7647)),
 ('Central Park S',     '36061', ['Central Park S'],  (-73.977, 40.766),  800, (-73.9805, 40.7676)),
 ('Columbus Circle',    '36061', ['Columbus Cir'],    (-73.982, 40.768),  300, (-73.9815, 40.7685)),
 ('CP Driveway',        '36061', ['Central Park Driveway'], (-73.981, 40.769), 400, (-73.9805, 40.7690)),
 ('West Dr',            '36061', ['West Dr'],         (-73.977, 40.772),  800, None),
]
FINISH_NEAR = (-73.9772, 40.7726)   # West Drive at the 67th Street approach

segs = [pieces(c, n, ctr, r) for _, c, n, ctr, r, _ in LEGS]

# start: 1 mile back from the middle of the bridge (the county line), along the expressway
mid = m((-74.04389, 40.60691))
si = segs[0] + [s for s in segs[1] if LineString(s).distance(Point(mid)) < 50]
toll, _, _ = path(si, m((-74.0750, 40.6010)), mid)
acc = 0; START = None
for u, v in zip(toll[::-1][:-1], toll[::-1][1:]):
    d = math.dist(u, v)
    if acc + d >= 1609.34:
        t = (1609.34 - acc) / d; START = (u[0] + (v[0] - u[0]) * t, u[1] + (v[1] - u[1]) * t); break
    acc += d

# The bridge ramp onto Dahlgren Place has no name in TIGER: join at Dahlgren's south end.
FIXED = {1: (-74.02755, 40.61292)}
pts = [START]
for i in range(len(LEGS) - 1):
    if i in FIXED: p, note = m(FIXED[i]), 'fixed: the south end of Dahlgren Pl'
    else: p, note = junction(segs[i], segs[i + 1], LEGS[i][5])
    pts.append(p)
    print(f'{LEGS[i][0]:>18} -> {LEGS[i+1][0]:<18} {ll(p)[1]:.5f},{ll(p)[0]:.5f}  {note}')
wd = LineString(max(segs[-1], key=lambda s: -LineString(s).distance(Point(m(FINISH_NEAR)))))
f = wd.interpolate(wd.project(Point(m(FINISH_NEAR)))); pts.append((f.x, f.y))

legs = []; total = 0
for i, (label, *_ ) in enumerate(LEGS):
    if math.dist(pts[i], pts[i + 1]) < 1: print(f'{label:>18}: skipped (it starts and ends at the same corner)'); continue
    cs, da, db = path(segs[i], pts[i], pts[i + 1])
    L = LineString(cs).length; total += L
    print(f'{label:>18}: {L/1609.34:5.2f} mi   (ends {da:.0f} m / {db:.0f} m from the street)   mile {total/1609.34:5.2f}')
    legs.append((label, [ll(p) for p in cs]))
print('TOTAL %.2f miles' % (total / 1609.34))
json.dump({'legs': legs, 'start': ll(START), 'finish': ll(pts[-1])}, open(OUT, 'w'))
