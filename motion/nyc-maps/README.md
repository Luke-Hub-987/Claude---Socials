# New York City Marathon course maps

Five 1080 x 960 PNGs for the top half of a reel (28 Oct): the whole route,
then miles 0-2 (the bridge), 2-13 (Brooklyn to the Pulaski Bridge), 15-20
(Queensboro and First Avenue) and 20 to the line (the Bronx, Fifth Avenue,
the park). Same framing in all five. Artifact with download buttons:
https://claude.ai/artifact/4fb7kihUqVTYc1Eo6tHy7K

How they were made (rebuild with these if the course changes):
- `tools/route.py` traces the route from US Census TIGER 2023 street
  centrelines, leg by leg, following the 2025 main-route closure list
  (CBS/NYRR, printed by ABC7 and Bleacher Report). Output: `route.json`.
  Traced length 26.47 miles (official 26.2); mile 2 lands at the end of the
  bridge and halfway at the foot of the Pulaski Bridge.
- `tools/render.py` draws land (TIGER county outlines) and water (TIGER
  AREAWATER), drops lakes, park ponds, pier slips and piers, and draws the
  route (22 px, round ends) and the start and finish dots.
- Data (not in the repo): `tl_2023_us_county`, and AREAWATER and ROADS for
  the five boroughs plus Hudson, Bergen, Essex, Union and Middlesex, NJ,
  from https://www2.census.gov/geo/tiger/TIGER2023/.

Simplified at this scale (about 29 m per pixel): the Bronx loop (Alexander,
138th, Morris, 140th, Rider) and the Queens Plaza turn read as small knots,
and the 3rd Avenue block in the Bronx is skipped (it starts and ends at the
same corner as Morris Avenue).
