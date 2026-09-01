---
name: ideate-personal
description: Generate 10 content ideas for Luke's personal brand by scanning YouTube outliers, Reddit top posts, IG competitor reels, and TikTok competitor videos, then applying Briar's frameworks + Luke's voice. Every idea cites a real source URL.
argument-hint: "[optional: pillar name or topic to focus on]"
allowed-tools: Bash(python3 *) Bash(cat *) Bash(ls *) Bash(grep *) Bash(date *) Read Write
---

You are running the personal-brand ideation pipeline. Your job:
produce 10 content ideas, each grounded in a real source from Luke's
competitor research, written in his voice, applying Briar's
frameworks.

This enforces the same hard rules as the shared ideation system: every
idea cites a reachable URL, no duplicate creators across the brief, and
a strict source-quota distribution.

## Pre-flight: load context

Read these files in order. If any of the first four are missing or
still have `_pending_` placeholders, stop and tell the user to finish
`/onboard-personal` first (or, for principles/hook-frameworks, to
paste in the PBA course content those files are waiting on).

1. `brands/personal/voice.md` — voice signature, hard rules, samples
2. `brands/personal/pillars.md` — content themes
3. `brands/personal/audience.md` — ICP
4. `principles.md` — Briar's positions (shared across brands)
5. `hook-frameworks.md` — Briar's hook patterns (shared across brands)
6. `voice-rules.md` — universal voice rules (em-dashes etc., shared)
7. `brands/personal/competitors.md` — if MISSING or empty, tell the
   user to run `/onboard-personal` first (it collects this)

If `voice.md` doesn't have at least 2 voice samples or a voice
signature yet, warn the user: "Your voice doc is light, ideas will be
generic. Consider re-running `/onboard-personal` to add more samples,
then re-run `/ideate-personal`." Continue if they want to anyway.

## Argument handling

If an argument was passed (e.g. `/ideate-personal authority`), use it
as a focus filter, all 10 ideas should serve that pillar or topic. If
no argument, spread the 10 ideas across all pillars roughly evenly
(the 4/3/2/1 mix described in "The 10 ideas" below).

## Step 1 — Scrape YouTube outliers

Read the YouTube channels from `brands/personal/competitors.md`. Run:

```bash
python3 scripts/yt_outliers.py \
  <space-separated-channel-handles> \
  --output /tmp/yt_outliers_personal.json
```

Tell the user: "Scanning YouTube, this takes 30-60 seconds." After it
finishes, read the output file to confirm. Report how many outliers
you got. If no YouTube channels are listed, skip this step.

## Step 2 — Scrape Reddit

Read the subreddits from `brands/personal/competitors.md`. Run:

```bash
python3 scripts/reddit_scan.py \
  "<comma-separated-subreddit-names>" \
  --output /tmp/reddit_posts_personal.json
```

Tell the user: "Scanning Reddit." Read the output JSON, report counts.

## Step 3 — Scrape Instagram

Read the IG handles from `brands/personal/competitors.md`. Run:

```bash
python3 scripts/ig_outliers.py \
  <space-separated-handles> \
  --output /tmp/ig_outliers_personal.json
```

Tell the user: "Scanning Instagram via Apify, this can take a few
minutes." Read the JSON, report.

## Step 4 — Scrape TikTok

Read the TikTok handles from `brands/personal/competitors.md`. Run:

```bash
python3 scripts/tiktok_outliers.py \
  <space-separated-handles> \
  --output /tmp/tiktok_outliers_personal.json
```

Tell the user: "Scanning TikTok via Apify, this can take a few
minutes too." Read the JSON, report. If no TikTok handles are listed,
skip this step.

Common errors to handle (all three Apify-backed scripts: Instagram,
Reddit, TikTok):
- `APIFY_API_TOKEN not set` (or `YOUTUBE_API_KEY`) → tell the user to
  fill in `.env` from `.env.example`. Reddit and TikTok scraping use
  the same Apify token as Instagram, no separate credential exists for
  either.
- Apify run didn't finish within its wait budget → the script aborts
  the run itself and reports the error; note it in the brief, don't
  retry more than once
- One handle/subreddit private, banned, or scrape failed → script
  continues with others; note it in the brief

## Step 5 — Generate 10 ideas

Synthesize 10 ideas using:

- Luke's voice samples + signature (`brands/personal/voice.md`)
- His pillars (`brands/personal/pillars.md`)
- His audience (`brands/personal/audience.md`)
- Briar's principles (`principles.md`)
- Briar's hook frameworks (`hook-frameworks.md`)
- Universal voice rules (`voice-rules.md`)
- The actual outlier content from `/tmp/*_personal.json`
- **`research/reddit-running-research-manual.txt`** — Luke's own
  manual research (~7,264 lines of real ICP posts/questions). Per his
  direct instruction, this is the default *topic* source: filter it
  for a real, specific, already-asked question first, then apply the
  hook-craft toolkit (P21, P29, P32, HF6, HF10) to the packaging. The
  outlier scrapes (`/tmp/*_personal.json`) are a hook-craft/format
  reference (P17), not the first place a topic should come from.

Per P16 (principles.md): spend the real effort on topic/idea
selection first (P1 TAM+unique+psychology, P6 idea funnel) — hooks are
a later, smaller lever, not the primary one. Write `body_angle` as
talking points to riff on (P19), not a verbatim script.

Two more levers once a topic is chosen: P24 (raise the stakes — frame
a real moment with real intensity instead of a plain listicle, bounded
by P23, never an invented moment) and HF10 in `hook-frameworks.md` (a
library of real on-screen-text shapes — use for the *pattern*, never
copy the actual wording onto Luke's topic).

Two final filters, both catching things P21 lets through — run every
idea through both before finalizing: **P29** (Purple Cow test — a
hook can be fully specific and still be unremarkable; would someone
actually be desperate for the answer, or just able to follow it once
told) and **P30** (StoryBrand — the hook and verbal hook must be
framed around what the viewer gets, not what Luke did; a day-in-the-
life or proof-by-doing idea needs a viewer-facing transformation
wrapped around it, not the creator's day as the subject itself).

### Hard quotas (non-negotiable)

- **Max 3 from YouTube**
- **Max 2 from Reddit**
- **Max 3 from TikTok**
- **Min 5 from Instagram** (primary source — this is where Luke
  actually publishes; the other three are discovery/research sources)

These are independent caps, not required allocations — they won't all
hit their max in the same 10-idea batch (5+3+2+3 = 13 > 10). Fill
toward the Instagram floor first, then round out with the others.

### Mix across pillars

If no focus argument was passed:
- 4 ideas serving established pillars (depth)
- 3 ideas testing adjacent angles (range)
- 2 ideas applying a Briar framework Luke likely hasn't tried (stretch)
- 1 contrarian take on something in his pillar (provocation)

### Per-idea schema

```yaml
- id: 1
  pillar: <which pillar this serves>
  format: <IG_carousel | IG_reel | IG_post | X_thread | LinkedIn_post | YT_short | YT_long>
  on_screen_text_hook: <MANDATORY. The literal on-screen text overlay, per HF6/P15/P21. Specific, numbered/taxonomy-shaped where possible, NO em-dashes, NO bare reversal clichés ("it's not what you think" etc unless paired with real specificity)>
  verbal_hook: <OPTIONAL. The spoken opening line per HF9, only if distinct from the on-screen text hook, NO em-dashes>
  body_angle: <2-3 sentences describing what the post argues or shows>
  voice_match: <one short line citing a specific element of voice.md it adheres to>
  briar_principle: <name + citation from principles.md>
  hook_framework: <name from hook-frameworks.md>
  source:
    creator: <handle or name>
    platform: <youtube | reddit | instagram | tiktok>
    url: <FULL real URL from the scraped JSON, must be reachable>
```

### Hard rules for the ideas themselves

- Every `source.url` must be copied verbatim from the scraped JSON.
- Every `on_screen_text_hook` is mandatory and must follow a framework
  you can name from `hook-frameworks.md`.
- No em-dashes anywhere, per `voice-rules.md`.
- No two ideas cite the same creator.
- Each idea must serve one of the pillars in `pillars.md`.
- **P20 test (principles.md): every idea must be filmable inside
  Luke's existing normal week** — no new race signup, no new event,
  no new purchase required, unless it's something he already does
  regularly (his adventure pillar is fine because he climbs mountains
  often, a specific record-attempt framing is not). When an outlier
  source is a big physical feat, translate the *curiosity angle*
  (what made it intriguing), never the *scale* (do a comparable feat).
- **P21 test (principles.md): every `on_screen_text_hook` must clear
  the newspaper-headline bar** — a specific number, a named
  taxonomy/system, or a concrete claim, not a generic curiosity-gap
  phrase. "It's not what you think" / "the real reason X" / "everyone
  thinks X but actually Y" is banned as the *entire* mechanism of a
  hook; a reversal framing is only allowed paired with real
  specificity underneath it. Model: "The 3 types of hills near me (and
  what each one is actually training)."
- **P22 test (principles.md): before citing a source, weigh
  confounds.** Would this packaging plausibly have worked from a
  smaller or unrelated account too, or is the source's channel
  size/topicality (mega-channel reach, breaking-news timing) doing the
  actual work? Drop or flag sources where the multiplier likely
  reflects reach/timing rather than genuine hook quality.
- **P23 test (principles.md): never fabricate a personal fact.** Don't
  assert a habit, routine, or claim about Luke as autobiographical fact
  unless it's actually confirmed true. If a source's angle depends on
  an unconfirmed personal claim, reframe it as a question/hypothetical
  or drop it for a different confirmed angle, never assert it anyway.

## Step 6 — Validate

Write the 10 ideas to `/tmp/ideate-draft-personal.json`:

```json
{ "ideas": [ { ... }, { ... } ] }
```

Run:

```bash
python3 scripts/validator.py /tmp/ideate-draft-personal.json
```

It checks every cited URL resolves and no two ideas cite the same
creator.

If validation FAILS: print the errors, fix the offending idea(s) with
different sources from the scraped pool, re-run the validator, retry
up to 2 times. If still failing, write what you have to
`ideas/personal/<date>-brief.md` but flag the unvalidated ideas
clearly.

If validation PASSES, continue to step 7.

## Step 7 — Write the brief

Get today's date with `date +%Y-%m-%d`. Write to
`ideas/personal/<date>-ideate-brief.md`:

```yaml
---
type: ideation-brief
brand: personal
generated_at: <full timestamp>
focus: <argument value or "all-pillars">
pillars_covered: [list]
sources_scraped:
  youtube: <N outliers>
  reddit: <N posts>
  instagram: <N reels>
  tiktok: <N videos>
validation: passed | failed-after-retries
---

# Ideation Brief (Personal) — <date>

## How to use this brief

Each idea below is grounded in a real outlier from your competitive
research. Pick the ones that excite you. Star or comment in the file.

## Ideas

### Idea 1 — <short title>

- **Pillar:** ...
- **Format:** ...
- **On-screen text hook:** "..."
- **Verbal hook (if distinct):** "..."
- **Body angle:** ...
- **Why it matches your voice:** ...
- **Briar principle applied:** ...
- **Hook framework:** ...
- **Source:** <creator>, [<platform>](<url>)

[... repeat for ideas 2-10 ...]

## Source pool reference

YouTube outliers analyzed: <N>. Top creators: ...
Reddit top posts analyzed: <N>. Top subreddits: ...
Instagram reels analyzed: <N>. Top accounts: ...
TikTok videos analyzed: <N>. Top accounts: ...
```

Also print a clean readable summary to the terminal.

## Step 8 — Wrap up

Tell the user:

1. The path to the brief (`ideas/personal/<date>-ideate-brief.md`)
2. How many ideas across each pillar
3. "Open the file, star the 3-5 you'd actually make."

If validation failed after retries, name which ideas were flagged and
why.

## Hard rules (repeated, because these matter most)

- **No fabricated sources.** Every cited URL comes from a scraped JSON
  file in /tmp. If you can't find a real source, drop the idea.
- **No fabricated personal facts** (P23). Never assert an unconfirmed
  habit/routine/claim about Luke as if it's true.
- **No em-dashes** anywhere in the brief.
- **No two ideas cite the same creator.**
- **Every idea has a mandatory `on_screen_text_hook`** that clears the
  P21 specificity bar — no bare reversal clichés.
- **Weigh outlier confounds (P22)** before trusting a source's
  multiplier as evidence a hook pattern works.
- **Quotas: ≤3 YouTube, ≤2 Reddit, ≤3 TikTok, ≥5 Instagram.** If you
  can't hit the IG minimum, reduce the total (e.g. output 7) rather
  than padding with extra YT/TikTok.
- **If voice doc is thin** (under 2 voice samples), flag it at the top
  of the brief.
