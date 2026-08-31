---
type: research-summary
source: reddit-running-research-manual.txt (Luke's own manual Reddit research)
covers: engine-room-nutrition (assumed — running/endurance nutrition content, flag if wrong)
updated_at: 2026-08-31
---

# Reddit Running Research — Theme Summary

A quick pass over `reddit-running-research-manual.txt` (Luke's own
manually-collected running-subreddit posts, ~7,200 lines, no explicit
subreddit headers in the doc). Assumed relevant to **Engine Room
Nutrition** given the heavy fueling/nutrition content and ERN selling
carbohydrate bars — flag if this was meant for the personal brand
instead.

## What it is

Real post/comment text from running-focused subreddits (reads like
r/running, r/AdvancedRunning, r/marathon-adjacent communities): race
reports, training questions, gear reviews, nutrition strategy,
injury/burnout discussion. Not tagged by subreddit or date in the doc
itself.

## Theme frequency (rough keyword counts, not exhaustive)

- marathon: 506 mentions — dominant context for everything else
- PB/PR (personal best/record): 101 — performance-chasing is core to
  this audience's identity
- injury: 116 — a constant undercurrent, often tied to overtraining
- zone 2 (training): 90 — active, informed debate about training
  methodology, this audience reads primary sources/studies
- fatigue: 49
- gel: 46 — gels are the default fueling format people already use
  and complain about
- carb load: 22 (as a phrase; broader carb-related content is much
  higher — see the competitor grep below)
- hydration: 24
- stomach / GI issues: ~29 combined — a specific, recurring pain point
  around fueling during long runs/races
- half marathon: 79 / ultra: 40 — audience spans half marathon through
  ultra distance, not just marathon
- burnout / plateau: ~11 combined — a smaller but real thread about
  identity and obsession with the sport

## Competitor / adjacent product brands mentioned organically

Pulled from real posts, not a curated list — these are brands this
audience already uses and talks about:

- **Maurten** — most-mentioned by a clear margin (gels/drink mix)
- **Skratch Labs** — hydration/fueling
- **Gatorade** — baseline hydration reference point
- **Nuun** — electrolytes
- **SIS (Science in Sport)** — gels
- **Tailwind** — endurance fuel
- **Huma** — gels

Worth carrying into `brands/engine-room-nutrition/competitors.md` as
candidates when we run `/onboard-ern` — these are real, audience-named
competitors, not a guess.

## What this suggests for ERN's audience (draft signal, not final)

- The core customer is a **performance-motivated runner** (obsesses
  over PBs, reads primary research on training methodology) more than
  a casual jogger — though half-marathon/ultra range means fueling
  needs vary by distance and duration.
- **GI distress during fueling** is a specific, recurring, named pain
  point. A carb bar that solves or reduces this could be a real
  differentiator and content angle (P9/P2 from `principles.md`:
  content for customers' actual painful problem, and a possible
  counter-position against the gel-dominant category).
- **Carb-loading precision** (grams per kg, timing in the 72 hours
  pre-race, grams per hour during) is something this audience already
  thinks about quantitatively, not vague "eat some carbs before"
  advice, useful for ERN's voice and content depth.
- Injury and burnout threads suggest content that only talks about
  performance/PBs risks missing a real part of this audience's
  experience with the sport.

This is a starting point for `/onboard-ern`'s audience question, not a
replacement for it, Luke should confirm/correct against what he
actually knows about ERN's target customer.
