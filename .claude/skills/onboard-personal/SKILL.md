---
name: onboard-personal
description: Interview the user about their personal brand (voice, pillars, audience, competitors) and write brands/personal/*.md. Run this before /ideate-personal.
argument-hint: ""
allowed-tools: Read Write Bash(date *)
---

You are onboarding the user's **personal brand** (as distinct from any
company brand). Your job: fill in `brands/personal/voice.md`,
`brands/personal/pillars.md`, `brands/personal/audience.md`, and
`brands/personal/competitors.md` with real content, replacing every
`_pending_` placeholder.

Read the current contents of those four files first so you know what's
already filled in (a re-run should only ask about what's still
`_pending_`, not redo everything).

Ask one section at a time. Don't move to the next section until the
current one is answered. If the user offers to paste in existing
research (old captions, a Reddit thread of ideas, a list of accounts
they admire), accept it directly instead of re-asking the question it
answers.

## Section 1 — Voice

Ask:

> "I want to nail your actual voice, not a generic 'confident LinkedIn
> guy' voice. Two things:
>
> 1. Paste 2-5 pieces of your own past writing, exactly as you wrote
>    them, whatever's closest to hand, old captions, a LinkedIn post,
>    a voice memo transcript, even a text to a friend that sounds like
>    you.
> 2. In a couple sentences, how would you describe your own voice to
>    someone who's never heard you talk? (e.g. 'blunt, a bit dry, no
>    fluff' or 'high energy, story-first, casual profanity')"

Write the samples verbatim into `## Voice samples`. Write their
self-description into `## Voice signature`. Pull out any recurring
words/phrases they use into `## Vocabulary / phrases you actually use`.
Ask a follow-up: "Anything you never want this to sound like, or words
you'd hate to see in your own mouth?" and write that into `## Hard
rules`.

## Section 2 — Pillars

Ask:

> "What are the 3-5 things you keep coming back to when you post or
> talk about your work? Not aspirational topics, actual recurring
> themes in what you've already made or wanted to make."

Write each as a short pillar name + one-line description into
`pillars.md`.

## Section 3 — Audience

Ask:

> "Who is this actually for? Give me: who they are (role, stage,
> whatever's relevant), what they're struggling with that you can
> speak to, and why they'd follow you specifically instead of someone
> else in the space."

Write the answer into the three subsections of `audience.md`.

## Section 4 — Competitors

If `brands/personal/competitors.md` doesn't exist yet or is empty, ask:

> "Who do you compete with or admire in your personal-brand space?
>
> 1. **YouTube channels** — 2-5 creators, handles or URLs.
> 2. **Subreddits** — 3-5 where your audience hangs out.
> 3. **Instagram accounts** — 3-5 competitor handles you respect (no @).
> 4. **TikTok accounts** — 2-5 competitor handles you respect (no @).
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

# My Competitors — Personal

## YouTube channels
- @creator1

## Subreddits
- r/subreddit1

## Instagram handles
- creator1

## TikTok handles
- creator1
```

## Wrap up

After all four files are filled in (no `_pending_` left), tell the
user: "Personal brand is set up. Run `/ideate-personal` to generate
your first batch of ideas." If `principles.md` or `hook-frameworks.md`
at the repo root are still `_pending_`, remind them those are shared
across both brands and need the actual PBA course content pasted in
before `/ideate-personal` will run.
