---
type: system
section: voice-rules
status: draft
updated_at: 2026-08-31
---

# Universal Voice Rules

These apply to every brand and every piece of content the ideate/draft
pipeline generates, regardless of pillar, format, or which brand's
`voice.md` is in play. Per-brand `voice.md` files add on top of this;
they never override the "never" rules below.

This is a starter draft, not course material. If your PBA program has
its own universal style guide from Briar, replace this file with that
content (or merge it in) so `/ideate-*` is enforcing the real rules.

## Never

- No em-dashes anywhere, in hooks, body angles, or captions. Use a
  period, comma, or parentheses instead.
- No corporate/LinkedIn-speak filler: "in today's world," "let's dive
  in," "unlock your potential," "game-changer."
- No hedging language in hooks: "I think," "maybe," "just my opinion."
  State the position.
- No hashtag walls. If hashtags are used, 3-5 max, relevant only.
- **No AI slop language (2026-09-07, Luke direct).** Before finalizing
  any headline/hook, check it against
  [Wikipedia: Signs of AI Writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
  every time, not just once. The parts of that checklist that actually
  apply to short-form hooks and posts (the Wikipedia-specific markup/
  citation items don't):
  - **Negative parallelism, banned outright, no exceptions:** "not
    just X, but Y," "it's not X, it's Y," "X rather than Y" as the
    entire mechanism of a line. This is the single most-flagged
    pattern and the one most likely to show up in a hook.
  - **Avoidance of plain "is/are":** don't reach for "serves as,"
    "stands as," "marks," "functions as," "represents" where "is"
    would do the job.
  - **Marketing verbs standing in for "has":** "features," "boasts,"
    "offers," "maintains" used unnaturally.
  - **Overused AI vocabulary:** "delve," "intricate/intricacies,"
    "meticulous," "tapestry," "underscore," "garner," "bolstered,"
    "align with," "enhance," "fostering," "showcasing," "emphasizing,"
    "deep dive," "additionally" as a transition crutch.
  - **Promotional/inflated tone:** "boasts," "vibrant," "profound,"
    "groundbreaking," "renowned," "game-changing," "pivotal moment,"
    "testament to," "stands as a reminder."
  - **Rule-of-three padding:** three parallel items listed purely for
    rhythm, not because there are actually three things worth saying.
  - **Present-participle padding:** trailing "-ing" clauses added for
    vague superficial analysis ("highlighting their significance").
  - **Vague attribution:** "industry reports show," "experts argue,"
    "observers have noted" without a real, named, checkable source.
  - **Excessive boldface, title-case abuse, emoji-as-formatting.**
  - **The "challenges" formula:** "Despite its [positive], [subject]
    faces challenges..." as a rigid, formulaic structure.

## Fabrication and sourcing

- Never fabricate a research claim, statistic, or study, in any brand.
  If a claim can't be traced to something real (a source in
  `research/`, something the user has explicitly confirmed, or a
  citation genuinely verified via search and clearly flagged as such),
  don't state it as fact.

## Always

- Write at a spoken register: short sentences, contractions, the way
  you'd actually say it out loud to one person.
- Lead with the claim or the tension, not the setup.
- One idea per hook. If a hook needs "and" to hold two claims, split it.
- For IG/TikTok/YT_short formats, the `hook` field is the on-screen
  text overlay, not spoken audio and not the caption. Captions don't
  drive reach on these platforms (P15, principles.md) — the on-screen
  text does all the work a headline does. Don't waste effort polishing
  a caption; put it into the on-screen text instead.

## Per-brand overrides

A brand's own `voice.md` can add vocabulary, banned words, or stylistic
quirks specific to that voice, but cannot re-permit anything banned
here.
