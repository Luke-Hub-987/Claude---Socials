---
name: onboard-analytical-athlete
description: Fill remaining gaps in brands/analytical-athlete/*.md (Luke's LinkedIn/newsletter brand) — draft docs already exist from real analytics data, this closes what's still open. Run before /ideate-analytical-athlete for best results, though ideate can run on the drafts as-is.
argument-hint: ""
allowed-tools: Read Write Edit Bash(date *)
---

You are onboarding **The Analytical Athlete** — Luke's LinkedIn/
newsletter brand, distinct from `brands/personal/` (his IG/TikTok
running brand) and `brands/engine-room-nutrition/` (the company brand).
Unlike those two brands, this one didn't start from an interview — it
started from Luke's real LinkedIn Aggregate Analytics export, which was
scraped post-by-post and turned into `swipe-file.md`, `voice.md`,
`pillars.md`, `audience.md`, and `competitors.md`. Read all five before
asking anything — most of what a normal onboarding interview would ask
is already answered from real data, marked `status: draft` where it's
inferred rather than confirmed.

Your job is narrower than `onboard-personal`'s: **confirm the drafts
and close the specific open items each file already lists**, not
re-run a full interview from scratch. Each file's "Open question(s)"
or "Open items" or "Gaps in this file" section at the bottom names
exactly what's missing — treat those as your question list, don't
invent new ones.

## Step 1 — Read everything first

Read in order: `audience.md`, `voice.md`, `pillars.md`,
`competitors.md`, `swipe-file.md`. Note every file's `status` field —
`live` (audience.md, swipe-file.md) means built directly from Luke's
own data and shouldn't be re-litigated from a casual answer, only
corrected with new data. `draft` (voice.md, pillars.md, competitors.md)
means inferred from the swipe file and should be checked with Luke
directly.

## Step 2 — Ask about the open items, one file at a time

For each `draft`-status file, read its "Open question" section aloud
to Luke in your own words and ask directly. Suggested order:

1. **voice.md**: "Does the voice doc match how you actually want to
   sound? Specifically: is the 'engine' metaphor and the PS-line device
   something you want to keep using, or was that incidental? Also —
   do you have the Claude Project summary of 'what works well' you
   mentioned? Paste it in, it covers more history than the 13-week
   export this was built from."
2. **pillars.md**: "Does the 4-pillar split (career-capacity narrative,
   research citations, practical training protocols, personal
   proof-of-concept) match how you think about this content, or does
   your Claude Project summary suggest different pillars? And does the
   4/2/2/2 mix guidance seem right, or should career-capacity dominate
   even more?"
3. **competitors.md**: "Give me 2-5 LinkedIn accounts or specific post
   URLs you actually want studied, even without an automated scraper —
   I can pull them manually the same way the swipe file was built."
4. **audience.md** (only the one open item, not the whole file since
   it's `live`): "Can you pull click-through or signup numbers on your
   `lnkd.in/epPvBWP4` link per post — from Bitly, LinkedIn's campaign
   manager, or your newsletter platform? Impressions/engagements are a
   proxy for what you actually care about (signups), and right now we
   can't tell which post really converted best."
5. **swipe-file.md**: "Any images or document-carousels on these posts
   I should know about? Every post fetched showed only a generic
   LinkedIn link-preview thumbnail, no custom image or carousel came
   through — is that accurate, or did some of these actually have a
   real graphic attached that didn't surface?"

Accept partial answers. If Luke doesn't have something (e.g. no
click-data available), write that into the file's "Open"/"Gaps"
section as "confirmed unavailable" rather than leaving it looking
unresolved, and move on.

## Step 3 — Update the files

For each answer, edit the relevant file directly:
- Update `status: draft` to `status: live` once Luke has confirmed a
  file's core content, even if minor open items remain.
- Append new competitor handles/URLs to `competitors.md` under "Named
  references" or a new "Confirmed by Luke" section.
- If Luke pastes a Claude Project summary, add its key points as a new
  section in `voice.md` and/or `pillars.md`, citing it as the source,
  and flag anywhere it contradicts the swipe-file-derived draft —
  don't silently overwrite, note the conflict and ask which should
  win.
- Update the `updated_at` field (via `date +%Y-%m-%d`) on any file you
  touch.

## Step 4 — Wrap up

Tell Luke which files are now `live`, which still have open items and
what they are, and that `/ideate-analytical-athlete` is ready to run
regardless (it can work from drafts, it just flags them as such in the
brief).
