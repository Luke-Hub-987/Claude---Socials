---
name: onboard-analytical-athlete
description: Fill remaining gaps in linkedin-analytical-athlete/brand/*.md (Luke's LinkedIn/newsletter brand) — draft docs already exist from real analytics data, this closes what's still open. Run before /ideate-analytical-athlete for best results, though ideate can run on the drafts as-is.
argument-hint: ""
allowed-tools: Read Write Edit Bash(date *)
---

You are onboarding **The Analytical Athlete** — Luke's LinkedIn/
newsletter brand. **This is a completely separate project from the
rest of this repo, per Luke's direct instruction (2026-09-07):** only
read and write inside `linkedin-analytical-athlete/`. Never read or
edit `brands/`, `principles.md`, `hook-frameworks.md`, `ost-*.md`,
`voice-rules.md`, or anything else at the repo root — this project
keeps its own independent copy of everything it needs
(`linkedin-analytical-athlete/craft-reference.md` holds the writing
rules and craft toolkit).

Unlike a from-scratch onboarding, this one didn't start from an
interview — it started from Luke's real LinkedIn Aggregate Analytics
export, turned into `brand/swipe-file.md`, `brand/voice.md`,
`brand/pillars.md`, `brand/audience.md`, and `brand/competitors.md`.
Read all five before asking anything — most of what a normal
onboarding interview would ask is already answered from real data,
marked `status: draft` where it's inferred rather than confirmed.

Your job is narrower than a full interview: **confirm the drafts and
close the specific open items each file already lists**, not re-run a
full interview from scratch. Each file's "Open question(s)" or "Open
items" or "Gaps in this file" section names exactly what's missing —
treat those as your question list, don't invent new ones.

## Step 1 — Read everything first

Read in order: `brand/audience.md`, `brand/voice.md`, `brand/
pillars.md`, `brand/competitors.md`, `brand/swipe-file.md`. Note every
file's `status` field — `live` means built directly from Luke's own
data and shouldn't be re-litigated from a casual answer, only corrected
with new data. `draft` means inferred and should be checked with Luke
directly.

## Step 2 — Ask about the open items, one file at a time

For each `draft`-status file, read its "Open question" section aloud
to Luke in your own words and ask directly. Suggested order:

1. **voice.md**: "Does the voice doc match how you actually want to
   sound? Is the 'engine' metaphor and the PS-line device something
   you want to keep using? Also — do you have the Claude Project
   summary of 'what works well' you mentioned? Paste it in."
2. **pillars.md**: "Does the current pillar split and mix guidance
   match how you think about this content, or does your Claude
   Project summary suggest something different?"
3. **competitors.md**: "Give me 2-5 LinkedIn accounts or specific post
   URLs you actually want studied — I can pull them manually."
4. **audience.md**: "Can you pull click-through or signup numbers on
   your CTA link per post? Impressions/engagements are a proxy for
   what you actually care about (signups)."
5. **swipe-file.md**: "Any images or document-carousels on these posts
   I should know about, beyond the two-panel one already confirmed?"

Accept partial answers. If Luke doesn't have something, write that
into the file's "Open"/"Gaps" section as "confirmed unavailable"
rather than leaving it looking unresolved, and move on.

## Step 3 — Update the files

For each answer, edit the relevant file directly, inside
`linkedin-analytical-athlete/brand/` only:
- Update `status: draft` to `status: live` once Luke has confirmed a
  file's core content, even if minor open items remain.
- Append new competitor handles/URLs to `competitors.md`.
- If Luke pastes a Claude Project summary, add its key points as a new
  section, citing it as the source, and flag anywhere it contradicts
  the swipe-file-derived draft — don't silently overwrite, note the
  conflict and ask which should win.
- Update the `updated_at` field (via `date +%Y-%m-%d`) on any file you
  touch.

## Step 4 — Wrap up

Tell Luke which files are now `live`, which still have open items and
what they are, and that `/ideate-analytical-athlete` is ready to run
regardless (it can work from drafts, it just flags them as such in the
brief).
