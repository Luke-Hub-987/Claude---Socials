---
name: onboard-ern
description: Interview the user about the Engine Room Nutrition company brand (voice, pillars, audience, competitors) and write brands/engine-room-nutrition/*.md. Run this before /ideate-ern.
argument-hint: ""
allowed-tools: Read Write Bash(date *)
---

You are onboarding the **Engine Room Nutrition company brand**, as
distinct from the user's personal brand. Your job: fill in
`brands/engine-room-nutrition/voice.md`,
`brands/engine-room-nutrition/pillars.md`,
`brands/engine-room-nutrition/audience.md`, and
`brands/engine-room-nutrition/competitors.md` with real content,
replacing every `_pending_` placeholder.

Read the current contents of those four files first so a re-run only
asks about what's still `_pending_`.

Ask one section at a time. If the user offers existing material (past
IG captions, product copy, brand guidelines, competitor research
they've already done), accept it directly instead of re-asking.

## Section 1 — Voice

Ask:

> "For Engine Room Nutrition's own voice, distinct from your personal
> voice: paste 2-5 pieces of ERN's actual past content, IG captions,
> emails, product page copy, whatever's on hand. Then describe the
> brand's voice in a couple sentences, e.g. 'science-forward but not
> preachy, direct about what works,' or however you'd actually put it."

Write samples verbatim into `## Voice samples`, the description into
`## Voice signature`, recurring brand vocabulary into `## Vocabulary /
phrases ERN actually uses`. Ask: "Anything ERN should never sound
like, claims it should never make, words it avoids?" and write that
into `## Hard rules`.

## Section 2 — Pillars

Ask:

> "What are the 3-5 recurring content themes for ERN? Think product
> categories, use cases, brand positioning angles, whatever ERN's
> content actually keeps coming back to."

Write each as a pillar name + one-line description into `pillars.md`.

## Section 3 — Audience

Ask:

> "Who is ERN's customer? Who they are, what problem they're solving
> when they find ERN, and why they'd buy from ERN over a competitor."

Write the answer into the three subsections of `audience.md`.

## Section 4 — Competitors

If `brands/engine-room-nutrition/competitors.md` doesn't exist yet or
is empty, ask:

> "Who does ERN compete with or take inspiration from?
>
> 1. **YouTube channels** — 2-5 creators/brands in nutrition/fitness.
> 2. **Subreddits** — 3-5 where ERN's customers hang out.
> 3. **Instagram accounts** — 3-5 competitor brand handles (no @).
>
> Skip any that don't apply."

Write it using this schema:

```yaml
---
type: my-brand
section: competitors
status: live
updated_at: <today, via `date +%Y-%m-%d`>
---

# ERN Competitors

## YouTube channels
- @creator1

## Subreddits
- r/subreddit1

## Instagram handles
- creator1
```

## Wrap up

After all four files are filled in, tell the user: "Engine Room
Nutrition brand is set up. Run `/ideate-ern` to generate your first
batch of ideas." If `principles.md` or `hook-frameworks.md` at the
repo root are still `_pending_`, remind them those are shared across
both brands and need the actual PBA course content pasted in before
`/ideate-ern` will run.
