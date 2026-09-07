---
name: ideate-analytical-athlete
description: Generate 10 LinkedIn post ideas for The Analytical Athlete (Luke's LinkedIn/newsletter brand), grounded in his own swipe file of real top-performing posts rather than competitor scraping, ending every idea in a newsletter CTA.
argument-hint: "[optional: pillar name or topic to focus on]"
allowed-tools: Read Write Bash(date *)
---

You are running the ideation pipeline for **The Analytical Athlete**
(Luke's LinkedIn brand). **This is a completely separate project from
the rest of this repo, per Luke's direct instruction (2026-09-07):**
what works on LinkedIn doesn't necessarily work on IG/TikTok and vice
versa, so this skill only reads and writes inside
`linkedin-analytical-athlete/`. Never read or edit `brands/`,
`ideas/personal/`, `ideas/engine-room-nutrition/`, `principles.md`,
`hook-frameworks.md`, `ost-*.md`, `voice-rules.md`, `research/`, or
`scripts/` — those belong to the personal/ERN video system and this
project keeps its own independent copy of anything it needs.

There is no video, no competitor outlier-scraping pipeline, and the
goal metric is signups to Engine Room Nutrition's real pre-launch email
list feeding a future paid offer, not reach/views for their own sake.
Every idea's fuel comes from `linkedin-analytical-athlete/brand/
swipe-file.md` — what has actually worked for this exact account — not
from scraped outliers.

## Pre-flight: load context

Read these, all inside `linkedin-analytical-athlete/`, in order. If
files are still `status: draft` with unresolved "Open" items, continue
anyway but note in the brief which inputs are unconfirmed.

1. `brand/swipe-file.md` — MANDATORY, read FIRST and read in full. The
   actual evidence base: which posts worked, their full text, the
   data-quality corrections already made, and the funnel destination
   (Engine Room Nutrition's real pre-launch product/list). Every idea
   should be traceable to a pattern in here.
2. `brand/voice.md` — the line-by-line "slippery slide" mechanic, the
   post-structure model, the "engine" metaphor, the confirmed two-panel
   image device, and the "Headline craft" section.
3. `brand/pillars.md` — the 5 pillars and mix guidance (Pillar 5,
   direct running/fueling content, is the largest single pillar as of
   2026-09-07 — don't skip it).
4. `brand/audience.md` — ICP and its "Clarified targeting logic"
   section: LinkedIn's follower demographics (finance/professional-
   services) describe who sees the content, not who it must always be
   written for — the list's real job is collecting runners, of any
   profession, for the eventual carb bar.
5. `brand/competitors.md` — named style references and any LinkedIn
   URLs Luke has given for manual reference.
6. `craft-reference.md` — MANDATORY, this project's self-contained
   copy of every writing rule and craft principle used here: universal
   style rules, the absolute AI-slop rule (checked against Wikipedia's
   "Signs of AI Writing" every time, no carve-outs), the on-screen-
   text-equivalent hook craft (CCN, the specificity bar, one-example-
   is-a-device-not-a-template, the hook-shape menu), and the
   power-word bank. Nothing outside this project needs to be read for
   any of this.

## Argument handling

If an argument was passed (e.g. `/ideate-analytical-athlete
career-capacity`), use it as a focus filter — all 10 ideas serve that
pillar. Otherwise spread across pillars per the mix guidance in
`brand/pillars.md`.

## Prefer swipe-file citations over new research

When a Pillar 1/2 idea needs an external-subject anchor (a study, a
named example), **check `brand/swipe-file.md` for a citation already
proven with this audience before reaching for new research**. The
S&P 1500 marathon-CEO study names three explanations (stress
tolerance, long-term thinking, recovery discipline) in one line each —
each unused facet of an already-proven citation is a legitimate new
idea. Only bring in genuinely new research (verified via WebSearch,
never fabricated, clearly flagged as untested with this audience) once
already-proven citations are exhausted, and say explicitly it's new
when you do.

## Step 1 — Mine the swipe file and craft-reference for patterns

For each top full-text post in `brand/swipe-file.md`, identify the
underlying **mechanism**, not the surface topic (e.g. "Same intake,
same bonus" is the pattern "two identically-positioned people, one
compounding choice, shown at a time delta" — though that specific
device is retired, see Hard rules below). Reuse mechanisms on a new
specific instance, never the exact scenario Luke already published.
For Pillar 5 ideas, draw on the real facts already inlined in
`brand/pillars.md` and `brand/swipe-file.md` (fueling physiology, real
runner pain points) rather than inventing new claims.

## Step 2 — Generate 10 ideas

Per-idea schema:

```yaml
- id: 1
  pillar: <Pillar 1-5, from brand/pillars.md>
  hook: <MANDATORY. The literal opening 1-3 lines as they'd appear before LinkedIn's "see more" cutoff — this IS the headline, treated with the same craft rigor as on-screen text per craft-reference.md. A single sharp claim or contrast, never a scene-setter>
  ccn: <MANDATORY, per craft-reference.md's CCN section. Who's Core, who's Casual, who's New for this hook, and what specific-curiosity mechanism pulls all three at once>
  device: <MANDATORY, per craft-reference.md's "one example is a device" rule. Name the structural device (scenario-question, numbered taxonomy, named-tier/borrowed-authority, ladder/progression, research-citation, first-person admission, confession, effort-to-outcome-gap, money, etc.) for the batch-level check below>
  power_word: <OPTIONAL. If used, name it and its job per craft-reference.md's power-word bank. One word, one slot>
  body_talking_points: <3-6 short bullets in the line-by-line "slippery slide" order: hook -> mechanism/citation -> reframe onto reader's own life, 2nd person -> transition to CTA. Talking points to riff on, not a verbatim script>
  research_claim: <Any specific number/study/fact the idea leans on, with its source (from this project's own files, or something Luke has explicitly told you, or a citation verified via search and flagged as new/untested). If unsourced, write "NEEDS REAL CITATION" or "NEEDS VERIFICATION" instead of inventing one>
  cta: <The newsletter close, naming "The Analytical Athlete" and the current subscriber count from brand/swipe-file.md's "Newsletter growth" section. This funnels into Engine Room Nutrition's real pre-launch product/list (see brand/audience.md) — don't invent claims about what happens after signup beyond what's already documented there>
  voice_match: <one line citing which brand/voice.md device this uses>
  visual_concept: <OPTIONAL. Only for a hook built on a real two-sided contrast, per voice.md's confirmed two-panel image device>
  swipe_file_precedent: <MANDATORY. Which real post/fact in brand/swipe-file.md or brand/pillars.md this idea is modeled on. If it can't be traced to a real precedent, say so explicitly as a stretch idea>
```

### Batch-level device check, mandatory before finalizing

Count which `device` each idea uses. No single device should account
for more than roughly a quarter of the batch (2-3 out of 10). If one
dominates, swap some ideas for a different device from
`craft-reference.md`'s hook-shape menu.

### Mix (default, no argument passed)

Per `brand/pillars.md`'s mix guidance (3 Pillar 1, 4 Pillar 5, 1 each
of Pillars 2-4 as of 2026-09-07 — check the file for the current
numbers since this may be revised). An other-person's-story idea
(Pillar 1 or 4) needs a real, specific, named research citation
underneath it, not just an anecdote about someone famous. A Pillar 4
idea built on Luke's own race/result/lived detail is always safe.

### Hard rules

- **Never build a hook around a fictional/composite "two colleagues or
  trainees at a firm diverge" comparison.** Luke is Associate Director
  at Grant Thornton, a top employer in his own follower base per
  `brand/audience.md` — even fictional coworker comparisons read as
  real commentary and carry professional risk. Use external, named,
  checkable subjects or Luke's own first-person experience instead.
- **Painkiller, not vitamin:** every hook should name something the
  reader already consciously dreads or resents before offering the
  mechanism. See `brand/audience.md`'s test and its honest caveat that
  the account's best-reach post is itself vitamin-shaped — this is a
  deliberate positioning choice, not proven by reach data, don't
  oversell it as such.
- **No fabricated research claims**, ever. Mark unsourced claims
  "NEEDS REAL CITATION" / "NEEDS VERIFICATION" and don't present them
  as fact in `body_talking_points`.
- **No AI-slop language, absolute, no exceptions** — see
  `craft-reference.md`. Negative parallelism ("not just X, but Y,"
  "it's not X, it's Y," "X isn't Y, it's Z") is banned outright, in any
  form, including a "corrected" version where the twist just moves one
  clause later. Check every hook against this before finalizing.
- **Every idea ends in a real, named CTA** with a current subscriber
  count. Never "link in bio," never omitted.
- **No two ideas share the same underlying mechanism/device** as each
  other or as an existing swipe-file post.
- **Every idea traces to a real precedent** or is explicitly flagged
  as an untested stretch idea.
- **P1-style test (TAM/unique/money):** does this idea connect to
  either the career-capacity bridge (Pillar 1) or real runner pain
  points that make someone a qualified lead for the carb bar
  (Pillar 5)? Both are valid per `brand/audience.md`.

## Step 3 — Write the brief

Get today's date (`date +%Y-%m-%d`). Write to
`linkedin-analytical-athlete/ideas/<date>-ideate-brief.md`:

```yaml
---
type: ideation-brief
project: linkedin-analytical-athlete
generated_at: <full timestamp>
focus: <argument value or "all-pillars">
pillars_covered: [list]
inputs_status: <note which brand/*.md files were still draft/had open items>
---

# Ideation Brief (The Analytical Athlete) — <date>

## Ideas

### Idea 1 — <short title>

- **Pillar:** ...
- **Hook:** "..."
- **CCN:** ...
- **Device:** ...
- **Power word (if used):** ...
- **Body talking points:** ...
- **Research claim:** ... (or "NEEDS REAL CITATION")
- **CTA:** ...
- **Voice match:** ...
- **Swipe-file precedent:** ...

[... repeat for ideas 2-10 ...]
```

Also print a clean readable summary to the terminal.

## Step 4 — Wrap up

Tell Luke: the path to the brief, how many ideas per pillar, how many
carry an unresolved citation/verification flag, and to star the 3-5
he'd actually write up. If any `brand/*.md` inputs are still draft,
remind him `/onboard-analytical-athlete` will close those gaps.
