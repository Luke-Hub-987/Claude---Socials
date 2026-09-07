# The Analytical Athlete (LinkedIn)

A completely separate project from the rest of this repo, per Luke's
direct instruction (2026-09-07): what works on LinkedIn doesn't
necessarily work on IG/TikTok/YouTube, and vice versa, so this project
keeps its own independent copy of every rule and craft principle it
needs rather than sharing files with the personal/ERN video system.

This covers Luke's LinkedIn presence (@luke-morrison-aca-cta). It's
text-only, no video, and its CTA funnels into Engine Room Nutrition's
real pre-launch email list — see `brand/audience.md` for the full
picture of who sees this content and why, and `brand/swipe-file.md`
for the real analytics data everything here is built from.

## Layout

```
linkedin-analytical-athlete/
  README.md              this file
  craft-reference.md      self-contained writing rules + hook craft toolkit
                          (universal style rules, the absolute AI-slop rule,
                          CCN, the specificity bar, the power-word bank,
                          the hook-shape menu, post structure)
  brand/
    audience.md           ICP, built from real LinkedIn analytics data
    voice.md               voice signature, post structure, hard rules
    pillars.md              5 content pillars + mix guidance
    competitors.md          named style references, open items
    swipe-file.md            real past-post text + performance data
  ideas/
    <date>-ideate-brief.md   generated ideation briefs land here
```

The two skills that operate on this project —
`.claude/skills/onboard-analytical-athlete/` and
`.claude/skills/ideate-analytical-athlete/` — live under `.claude/
skills/` (a harness requirement for slash-command discovery), but only
read and write inside this folder. They never read or edit `brands/`,
`principles.md`, `hook-frameworks.md`, `ost-*.md`, `voice-rules.md`,
`research/`, or `scripts/` at the repo root.

## Status

- `brand/audience.md` and `brand/swipe-file.md`: **live**, built
  directly from Luke's real LinkedIn Aggregate Analytics export and
  phone Post Analytics screenshots.
- `brand/voice.md`, `brand/pillars.md`, `brand/competitors.md`:
  **draft**, inferred from that data, pending Luke's confirmation —
  run `/onboard-analytical-athlete` to close the open items each file
  lists.
- `craft-reference.md`: **live**, this project's own copy of the
  writing rules and hook-craft toolkit (some concepts were originally
  developed for the video system and copied here once — this file is
  now the independent source of truth for LinkedIn going forward).

## Usage

1. Run `/onboard-analytical-athlete` to confirm the draft files and
   close their open items (or skip straight to ideation, it works from
   drafts).
2. Run `/ideate-analytical-athlete` to generate a batch of LinkedIn
   post ideas into `ideas/`.
