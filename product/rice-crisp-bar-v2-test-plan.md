# Rice Crisp Carb Bar: v2 Test Plan (fixing the next-day staleness)

## Problem
Bars are great on day 1. By day 2 the outside is still crunchy but the inside
tastes stale.

## Diagnosis (hypothesis, to be confirmed by measurement)
Moisture moves from the marshmallow binder into the rice, and the rice goes
leathery.
- Binder: estimated water activity (aw) ~0.6–0.7, a typical marshmallow
  (not yet measured).
- Crisped rice: ~0.2–0.3.
- Water always moves toward the lower aw until the two are equal. The rice
  can't stay crisp inside a wet binder. In food-science terms this is moisture
  migration, and it shows up as staleness.
- The outside stays crunchy because the surface dries into the air, which also
  suggests the bars aren't sealed straight after cooling.

aw (water activity) measures how much free water is in a food. The fix is to
bring binder aw closer to the rice's and seal the bars properly. Six months also
*requires* this: a gelatin marshmallow at ~0.65+ aw is a mould risk over that
time.

## v2 formula (5 bars, ~39g each, ~29.5g carbs per bar before glycerol)

| Ingredient | v1 (g) | v2 (g) | Why |
|---|---|---|---|
| Crisped rice | 50.0 | 50.0 | |
| Coconut oil (rice pre-coat) | 5.0 | 5.0 | Keep the fat barrier |
| Glucose syrup 42 DE | 48.0 | 48.0 | |
| Maple syrup | 25.0 | 25.0 | Flavour (golden syrup is a cheaper option) |
| Sugar | 33.0 | 33.0 | |
| Maltodextrin | 19.5 | **0** | Large molecules barely lower aw |
| Dextrose | – | **10.0** | Small molecule, lowers aw |
| Crystalline fructose | – | **8.0** | Lowers aw strongly, less start-line sugar dip |
| Vegetable glycerine | – | **0 / 5 / 10** | The main variable (see below) |
| Salt | 1.0 | **2.0** | ~160mg sodium per bar |
| Gelatine (Dr. Oetker) | 1.5 | 1.5 | |
| Water (bloom) | 7.5 | 7.5 | |
| Vanilla | 0.5 | 0.5 | |

Glycerine (the "humectant" in commercial bars) holds water so the rice can't
take it. Don't count it toward the 30g carb claim. Check how it has to be
labelled before any packaging goes to print.

## Experiment 1: glycerine × packaging (the one that matters)

Make three batches with glycerine at 0g, 5g and 10g. Keep everything else
identical, including the cook temperature (probe thermometer) and how hard you
press the tin.

- Press lightly. Crushed rice has more surface area and goes stale faster.
- Split each batch in two:
  - **A:** sealed into foil or metallised pouches within 30 minutes of setting.
  - **B:** cling film (what we do now).

| Batch | Pack | D1 | D3 | D7 | D14 | D28 | Notes |
|---|---|---|---|---|---|---|---|
| G0 | A | | | | | | |
| G0 | B | | | | | | |
| G5 | A | | | | | | |
| G5 | B | | | | | | |
| G10 | A | | | | | | |
| G10 | B | | | | | | |

Score inside crispness and "stale" flavour from 1 to 10, blind (someone else
labels the bars). Also note stickiness and any glycerine aftertaste (bitter or
warming).

## Experiment 2: measure aw
Send the G0 and best-scoring binder, plus the plain rice, to a food lab for aw
(e.g. Campden BRI or any UKAS-accredited lab).
- Target: finished bar aw ≤ ~0.55. That's needed for a 6-month claim and
  narrows the gap to the rice.
- A formal shelf-life study (with micro testing) is still needed before
  printing a best-before date.

## Benchmark
Kellogg's Rice Krispies Squares. Buy a pack, check the ingredients list for
humectants and sugar types, and taste one side by side at D7. Their rice is
*not* crisp: it's a soft chew that equilibrated in the factory. Decide if that's
the target texture, because a truly crisp rice bar at 6 months is much harder.
