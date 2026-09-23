# Rice Crisp Carb Bar: v2 Test Plan

## Constraints (set by the team)
- 5 bars per batch, 30g carbs per bar.
- Minimal, clean ingredient list. No glycerine and no added humectants.
- Beef gelatine (Dr. Oetker).
- Target glucose:fructose ratio of 1:0.8.
- 6-month shelf life, to be confirmed by lab testing (water activity and a
  shelf-life study).

## The ratio problem
- The v1 (Gemini) recipe is **1:0.2**, not 1:0.8. Gemini's own "4.5:1" figure
  says the same thing (1:0.22).
- Rice starch counts as glucose: 50g of rice is about 42g of glucose that has
  to be balanced.
- Sugar, maple and honey are all roughly 1:1. However much of them you use,
  they can't pull the whole bar past about **1:0.6**.
- Reaching 1:0.8 needs something that is mostly fructose: crystalline fructose
  or agave syrup.
- Maltodextrin and glucose syrup are pure glucose. Both work against the
  target, so both are removed in v2.

## Options (5-bar batch; per-bar figures)

All options also include: coconut oil 5g, gelatine 1.5g, water 7.5g, salt 2g,
vanilla 0.5g.

| | A: honey | A': acacia honey | B: + fructose | B': agave |
|---|---|---|---|---|
| Crisped rice | 50 | 50 | 50 | 50 |
| Honey | 60 | 60 (acacia) | 45 | – |
| Agave syrup | – | – | – | 75 |
| Maple syrup | 25 | 25 | 25 | 25 |
| Sugar | 48 | 48 | 33 | 38 |
| Crystalline fructose | – | – | 24 | – |
| **Carbs / bar** | 30.4g | 30.0g | 29.9g | 30.6g |
| **G:F** | 1:0.56 | 1:0.61 | **1:0.78** | **1:0.82** |
| Bar weight | ~40g | ~40g | ~39g | ~41g |

These estimates use typical label compositions. Agave and honey vary by brand
(acacia honey is naturally higher in fructose). B is the most precise because
crystalline fructose is 100% fructose.

For comparison, cutting the rice to 35g with only honey, maple and sugar only
reaches 1:0.68. It also costs you the rice krispie identity, so it isn't
recommended.

## Staleness (clean-label levers)
The inside goes stale because moisture moves from the marshmallow binder into
the rice. With no humectants allowed, these are the levers:
1. **Remove maltodextrin and glucose syrup** (done in v2). Fructose and honey
   hold water more tightly (lower water activity, aw) than long-chain
   maltodextrin, so less of it moves into the rice. The ratio goal and the
   staleness fix point the same way.
2. **Cook the binder hotter so less water goes in.** Test 108, 112 and 116°C,
   measured with a **probe** thermometer, not an IR gun. Fructose-rich syrups
   brown faster, so watch the colour.
3. **Keep the coconut oil coat on the rice.**
4. **Press lightly into the tin.** Crushed rice goes stale faster.
5. **Seal in foil or metallised pouches within 30 minutes of cutting.**
   Fructose is hygroscopic (pulls moisture from the air), so unsealed bars get
   sticky.

## Method (v2)
1. Toast the rice at 100°C for 8 minutes. Cool it, then toss it in the melted
   coconut oil.
2. Bloom the gelatine in the water for 5 minutes.
3. Put the sugar, honey/agave, maple, fructose (option B) and salt in a pan.
   Heat on low, stirring, until the sugar has fully dissolved.
4. Cook to the test temperature on a probe thermometer. Take it off the heat
   and let it cool to about 90°C.
5. Stir in the gelatine, then whip for 60–90 seconds until it turns opaque.
   Stir in the vanilla.
6. Fold the binder into the rice. Press lightly into a lined tin.
7. Leave to set for 1–2 hours, cut into 5 bars and seal them straight away.

## Test grid (score inside crispness and "stale" flavour 1–10, blind)

| Recipe | Cook °C | D1 | D3 | D7 | D14 | D28 | Notes (sweetness, stickiness) |
|---|---|---|---|---|---|---|---|
| v1 (control) | as made | | | | | | |
| A' | 112 | | | | | | |
| B | 108 | | | | | | |
| B | 112 | | | | | | |
| B | 116 | | | | | | |

Send the best two, plus plain rice, to the lab for aw.
- Target: finished bar aw ≤ ~0.55.
- Benchmark: Kellogg's Rice Krispies Squares at D7. Their rice is a soft chew,
  not crisp.
