---
name: ideate-analytical-athlete
description: Generate 10 LinkedIn post ideas for The Analytical Athlete (Luke's LinkedIn/newsletter brand), grounded in his own swipe file of real top-performing posts rather than competitor scraping, ending every idea in a newsletter CTA.
argument-hint: "[optional: pillar name or topic to focus on]"
allowed-tools: Read Write Bash(date *)
---

You are running the ideation pipeline for **The Analytical Athlete**
(Luke's LinkedIn brand). This is structurally different from
`/ideate-personal` and `/ideate-ern`: there is no video, no competitor
outlier-scraping pipeline for LinkedIn in this repo, and the goal
metric is newsletter signups feeding a future paid offer, not
reach/views for their own sake. Every idea's fuel comes from Luke's own
`swipe-file.md` — what has actually worked for this exact account — not
from scraped outliers.

## Pre-flight: load context

Read these in order. If `brands/analytical-athlete/*.md` files are
still `status: draft` with unresolved "Open" items, continue anyway but
note in the brief which inputs are unconfirmed — don't block on it the
way `/ideate-personal` blocks on missing `_pending_` files, since this
brand's docs start populated from real data rather than empty.

1. `brands/analytical-athlete/swipe-file.md` — MANDATORY, read FIRST
   and read in full. This is the actual evidence base: which posts
   worked, their full text, the pre/post-pivot contrast, and the
   flagged underperforming pattern (celebrity namedrops without Luke's
   own angle). Every idea should be traceable to a pattern in here.
2. `brands/analytical-athlete/voice.md` — the line-by-line "slippery
   slide" mechanic, the Justin Welsh post structure, the "engine"
   metaphor, hard rules.
3. `brands/analytical-athlete/pillars.md` — the 5 pillars (Pillar 5,
   direct running/fueling content, added 2026-09-07 — don't skip it,
   it's now the largest pillar by mix guidance) and mix guidance.
4. `brands/analytical-athlete/audience.md` — ICP (finance/professional-
   services, senior/director-level, Dublin/London) **and** its
   "Clarified targeting logic" section: the follower demographics
   describe who sees the content, not who it must always be written
   for — the list's real job is collecting runners, of any profession,
   for the eventual carb bar.
5. `brands/analytical-athlete/competitors.md` — named style references
   (Justin Welsh, Ogilvy/Caples) and any LinkedIn URLs Luke has since
   given for manual reference.
6. `brands/engine-room-nutrition/pillars.md` (its "Product context"
   section) — confirmed 2026-09-07: this brand funnels into ERN, not a
   separate product. Read this so CTAs and any product claims stay
   accurate to ERN's real, pre-manufacturing stage rather than
   inventing an "Analytical Athlete" offer.
7. For Pillar 5 ideas specifically, also read:
   `research/reddit-running-themes-summary.md` (real runner pain
   points), `ost-10-10-teardown.md` (the "10/10 X of Y" scored-list
   device, and ERN's owned RPE-scoring variant), and
   `ideas/engine-room-nutrition/2026-09-05-script-fuelling-ladder.md`
   (real, already-source-checked fueling physiology and the ladder
   device) — reuse this material directly, don't re-derive physiology
   claims from scratch or invent new ones.
8. `voice-rules.md` — universal rules (no em-dashes, no hedging, no
   corporate filler, and the **AI-slop checklist** — read this in full
   and check every hook against it before finalizing, every single
   run, not just once).
9. `principles.md` — P1 (TAM/unique angle/money) and P2
   (counter-positioning) apply directly and are worth citing. Treat
   the rest of that file with judgment: it was built for short-form
   video (on-screen text, watch-time, skip-rate) and much of it
   (HF-series in `hook-frameworks.md` especially) doesn't translate to
   a LinkedIn text post's mechanics. Don't force a video-specific
   framework citation onto a LinkedIn idea just to fill the field.

## Argument handling

If an argument was passed (e.g. `/ideate-analytical-athlete
career-capacity`), use it as a focus filter — all 10 ideas serve that
pillar. Otherwise spread across pillars per the mix guidance in
`pillars.md` (currently 4/2/2/2 favoring Pillar 1, career-capacity
narrative).

## Prefer swipe-file citations over new research (2026-09-07, Luke direct)

When a Pillar 1/2 idea needs an external-subject anchor (a study, a
named example), **check `swipe-file.md` for a citation already proven
with this audience before reaching for new research**. The S&P 1500
marathon-CEO study in "Companies led by marathon-running CEOs" names
three explanations (stress tolerance, long-term thinking, recovery
discipline) in one line each — each unused facet of an already-proven
citation is a legitimate, un-fabricated new idea. Only bring in
genuinely new research (verified via WebSearch, never fabricated, and
clearly flagged as untested with this audience) once the already-
proven citations are exhausted, and say explicitly that it's new/
untested when you do — don't present it as equivalent to proven
material.

## Step 1 — Mine the swipe file for patterns, not just topics

Per P16-style discipline (spend real effort on topic/angle selection
before wording): for each of the 10 top full-text posts in
`swipe-file.md`, identify the underlying **mechanism**, not the
surface topic. E.g. "Same intake, same bonus" isn't a post about
running, it's the pattern "two identically-positioned people, one
small compounding choice, shown at a 3-year time delta." Reuse the
*mechanism* on a new specific instance, never reuse the exact same
scenario Luke already published.

## Step 2 — Generate 10 ideas

Per-idea schema:

```yaml
- id: 1
  pillar: <Pillar 1-4, from pillars.md>
  hook: <MANDATORY. The literal opening 1-3 lines as they'd appear before LinkedIn's "see more" cutoff. This is the equivalent of the on-screen-text hook in the other brands' schemas — it IS the headline here, there's no separate visual layer. Must be a single sharp claim or contrast, per voice.md's post-structure model, never a scene-setter or a question that needs the reader to already care>
  body_talking_points: <3-6 short bullets in the line-by-line "slippery slide" order: hook -> mechanism/research citation -> reframe onto reader's own life, 2nd person -> transition to CTA. Talking points to riff on when actually writing the post (P19-style), not a verbatim script>
  research_claim: <Any specific number/study the idea leans on, with its source. If genuinely sourced (from research/ files in this repo, or something Luke has explicitly told you), cite it. If no real source exists yet, write "NEEDS REAL CITATION — do not publish until sourced" instead of inventing one. Never fabricate a study or statistic, this is a hard rule, see below>
  cta: <The newsletter close, naming "The Analytical Athlete" and the current subscriber count from swipe-file.md's "Newsletter growth" section (use the latest figure, note it'll be stale by publish time and Luke should update it). Confirmed: this funnels into Engine Room Nutrition's own list (engineroomnutrition.com/pages/fuel-1), not a separate product — see audience.md. Don't invent Analytical-Athlete-specific offers or claims about what happens after signup beyond what brands/engine-room-nutrition/pillars.md's product context actually supports>
  voice_match: <one line citing which voice.md device this uses: the engine metaphor, direct 2nd-person address, a PS-line secondary hook, etc.>
  visual_concept: <OPTIONAL. Only if the hook is built on a two-sided contrast (per voice.md's confirmed two-panel image device) — a one-line description of a two-panel image mirroring the contrast, e.g. "left: at desk late, right: lacing up shoes at dawn." Omit entirely for ideas without a real contrast to mirror, don't force it>
  swipe_file_precedent: <MANDATORY. For Pillars 1-4, which real post in swipe-file.md this idea's mechanism is modeled on, by date/title. For Pillar 5, which real source this draws from instead (research/reddit-running-themes-summary.md's named pain point, ost-10-10-teardown.md's device, or the fuelling-ladder script) — cite it the same way. If it can't be traced to a real precedent/source, it's a stretch idea — say so explicitly rather than pretending it's proven>
  briar_principle: <P1 or P2 from principles.md if genuinely applicable, otherwise omit the field rather than forcing a citation>
```

### Mix (default, no argument passed)

Per `pillars.md`'s revised mix: 3 Pillar 1 (career-capacity narrative),
4 Pillar 5 (direct running/fueling — now the largest single pillar,
per Luke's 2026-09-07 instruction not to fixate on the career-bridge
angle), 1 Pillar 2, 1 Pillar 3, 1 Pillar 4. An earlier version
of this rule banned other-people's-story ideas (Bezos/Branson/Ramsay-
style) from Pillar 4 outright — that was based on xlsx numbers later
found to be unreliable for pre-6/10/2026 posts, and the best-verified
post in the account's history ("Companies led by marathon-running
CEOs") is exactly that shape. The real rule per `pillars.md`: an
other-person's-story idea needs a **real, specific, named research
citation** underneath it (a named study, a real data point), not just
an anecdote about someone famous — that's what separated the verified
winner from the still-unverified mid-tier posts in that shape. A
Pillar 4 idea built on Luke's own race/result/lived detail is always
safe; a Pillar 4 idea built on someone else's story needs the citation
test to pass.

### Hard rules

- **Never build a hook around a fictional/composite "two colleagues or
  trainees at a firm diverge" comparison** (retired 2026-09-07, Luke
  direct — he's Associate Director at Grant Thornton, a top employer
  in his own follower base per `audience.md`; even fictional coworker
  comparisons read as real commentary and carry professional risk).
  Use external, named, checkable subjects (companies, executives,
  research) or Luke's own first-person experience instead.
- **Painkiller, not vitamin** (2026-09-07, Luke direct): every hook
  should name something the reader already consciously dreads or
  resents before offering the mechanism, not just a nice hypothetical
  upside. See `audience.md`'s test and its honest caveat that the
  account's best-reach post is itself vitamin-shaped — this is a
  deliberate positioning choice, not something reach data already
  proved, so don't oversell it as "what the data says" when pitching
  ideas back to Luke.
- **No fabricated research claims.** If `research_claim` can't be
  traced to something real, mark it "NEEDS REAL CITATION" per the
  schema above and do not present it as an established fact in
  `body_talking_points`. This matters more here than in the other
  brands: the entire voice is built on citing real numbers as the
  credibility mechanism (see `voice.md`), so a fabricated stat isn't
  just risky, it breaks the actual thing that makes this voice work.
- **No em-dashes**, no corporate filler ("unlock your potential,"
  "let's dive in") per `voice-rules.md` — LinkedIn is exactly the
  platform this rule exists to guard against.
- **Every idea ends in a real, named CTA** to The Analytical Athlete
  newsletter with a subscriber count. Never "link in bio," never
  omitted.
- **No two ideas share the same underlying mechanism** as each other
  or as an existing swipe-file post — riff on the pattern, don't repeat
  the scenario.
- **Every idea traces to a `swipe_file_precedent`** or is explicitly
  flagged as an untested stretch idea.
- **P1 test (TAM/unique/money), REVISED 2026-09-07:** does this idea's
  angle connect back to either the career-capacity bridge (Pillar 1)
  *or* directly to real runner pain points that make someone a
  qualified lead for the eventual carb bar (Pillar 5)? Both are valid
  per `audience.md`'s "Clarified targeting logic" — a Pillar 5 idea
  overlapping with `brands/personal/` content is fine and expected
  (both draw on the same real running-audience research), the LinkedIn
  version should still be adapted to this platform's text format and
  voice, not copy-pasted.
- **AI-slop check, mandatory, every idea, every run** (see
  `voice-rules.md`): before finalizing, check every `hook` against the
  checklist there. Negative parallelism ("not just X, but Y," "it's
  not X, it's Y") is banned outright with no exceptions — it's the
  single most likely pattern to slip in unnoticed.

## Step 3 — Write the brief

Get today's date (`date +%Y-%m-%d`). Write to
`ideas/analytical-athlete/<date>-ideate-brief.md`:

```yaml
---
type: ideation-brief
brand: analytical-athlete
generated_at: <full timestamp>
focus: <argument value or "all-pillars">
pillars_covered: [list]
inputs_status: <note which brands/analytical-athlete/*.md files were still draft/had open items>
---

# Ideation Brief (The Analytical Athlete) — <date>

## Ideas

### Idea 1 — <short title>

- **Pillar:** ...
- **Hook:** "..."
- **Body talking points:** ...
- **Research claim:** ... (or "NEEDS REAL CITATION")
- **CTA:** ...
- **Voice match:** ...
- **Swipe-file precedent:** ...
- **Briar principle (if applicable):** ...

[... repeat for ideas 2-10 ...]
```

Also print a clean readable summary to the terminal.

## Step 4 — Wrap up

Tell Luke: the path to the brief, how many ideas per pillar, how many
carry an unresolved "NEEDS REAL CITATION" flag (these need his input
before they're publishable, not just a rewrite), and to star the 3-5
he'd actually write up. If any `brands/analytical-athlete/*.md` inputs
are still draft, remind him `/onboard-analytical-athlete` will close
those gaps for a stronger next batch.
