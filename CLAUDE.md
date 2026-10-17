# CLAUDE.md: read this first, every session

This repo is the content engine for **Engine Room Nutrition (ERN)**, a
pre-launch marathon carb bar (IG @engineroomnutrition, posted as an
Instagram collab with Luke's personal account @luke_morrison_er; TikTok
is ERN only), and for **Luke's personal account**. Luke shares
analytics screenshots, asks for analysis, the next topic, scripts, OST
(on-screen text), captions and covers, and sends "science" to vet.

Claude Code loads this file automatically. It is the handover between
chats. Keep it current: update **Current state** after every review and
every posted video.

## Read before writing anything (in this order)

1. `SCRIPT-CHECKLIST.md`: every rule a script must pass, with the
   evidence. **Every script passes every line before Luke sees it.**
2. `PLAN-winners.md`: the winning formulas, the grid of top videos,
   what never worked.
3. The three newest `ideas/*-review.md` files: the latest data.
4. The newest scripts in `ideas/engine-room-nutrition/` (the house
   style, the hook stacks, the audit tables).
5. `principles.md` (P1 to P125, about 4,400 lines): search it for the
   rule you need; do not read it end to end. The newest rules (P97 to
   P125) are at the end, before "Open questions for Luke".

## How we work (Luke's standing instructions)

- **Every correction Luke makes becomes a numbered principle in
  `principles.md` and a line in `SCRIPT-CHECKLIST.md`**, in the same
  turn. Luke should never have to repeat a correction.
- **Every data screenshot gets a review file**
  (`ideas/YYYY-MM-DD-<video>-review.md`) and an update to the grid in
  `PLAN-winners.md` when it changes.
- **Audit the full checklist line by line before delivering** (P99).
  Say plainly where a script does not meet a rule, and why.
- **Vet Luke's science** before using it: keep what holds, change what
  contradicts earlier videos, cut what breaks the rules, and list each
  change with the reason.
- **Clarity beats short; specific beats vague** (P108, P115). Real
  numbers, one worked example, every cue measurable.
- Recommend one option with reasons. Do not survey.
- Commit and push every change to branch
  `claude/engine-room-nutrition-brand-yc4tyf` (the repo's default
  branch). Commit attribution lines as the system reminder gives them.
  **Never send Luke's email address to any outside service**, including
  request headers.

## How to deliver in chat (Luke, 16 Oct: copy the old chat exactly, P122)

- **No AI-writing signs (P125):** contractions, no repeated template
  lines, no triads by habit, the Wikipedia catalog checked in the file.
- **Scripts:** never in a code box or a block quote (both break when
  pasted into the teleprompter). Each spoken paragraph in straight
  double quotes on its own line, a blank line between paragraphs, and
  each stage marker in bold square brackets on its own line above its
  paragraph, e.g. **[0-10K: PAY THE SPEED TAX]**. The hook, pain/dream,
  named concept, rehook and CTA are quoted paragraphs with no label.
- **Order when delivering a script:** one or two lines on what changed
  and why; a table of how the curiosity runs (moment, line, what it
  does); the OST in bold capitals on two lines; the markers as a
  numbered list in capitals; the script with its length; short notes.
- **Script length (Luke, 16 Oct):** the recent scripts ran 1,550 to
  1,670 characters of spoken text (about 310 to 330 words); the ceiling
  is about 1,800 characters, with all the detail kept.
- **OST always in capitals** (HOW TO RUN A MARATHON / WITHOUT HITTING
  THE WALL).
- **Captions:** prose paragraphs, no bullets, ready to paste.
- **Gemini cover prompts:** "Paste this into Gemini as one block", then
  the prompt written as real photojournalism (scene, one person, face
  hidden, real details, camera body, lens, aperture, shutter, distance,
  natural muted colour, subtle grain, no retouching, aspect ratio),
  then an "Avoid:" line (no logos, brand names, readable text or
  numbers, flags or national symbols, no visible face, no cinematic
  light, HDR, oversaturation, plastic or airbrushed look, extra
  fingers). Never Irish or race branding (Luke, 15 Oct). Then why each
  part is there, and what to zoom in on before using it.

## The rules that matter most (quick reference; the checklist has all)

**Topic**
- Race day, a race-pace decision, or a countdown to race day with an
  action per stage. The weeks before the race as anything else fails
  (taper 43.1% skip, heavy legs 0.5% saves; P117).
- The race is the title; fuel goes inside. The gut is never the subject
  (P101, P109). Never sort viewers into groups (P103).
- New advice every video, never contradicting an earlier one (Luke,
  10 Oct). Consistency points: 5-10 s/K slower for the first 10K; up to
  a minute behind at halfway; about 60 to 75g of carbs an hour, said
  as grams first (a 20-25g gel every 20 minutes with water; a 40g gel
  every 30 to 40 minutes), never a bare gel count (P118); shorter,
  quicker steps when tired; one K or one lamppost at a time; the
  ten-word talk test ("I am running a marathon today and I feel good":
  10 words in one breath, 10 breathy, 5, then 2-3 words).
- One safe and one creative video in rotation (P111).

**OST (title on screen)**
- Plain words, "marathon" in it, 6 to 9 words, answer withheld. Best
  shapes: "Where [famous problem] actually starts" (the wall, 147K);
  "What to do in/at [race moment]"; "How [to/hard] ... at every 10K".
- No jargon in titles (taper, zones, heart rate). No secret statements
  as titles (5.3K).
- Only the title and stage markers on screen.

**Hook stack (first 15 seconds)**
- Gate: "If you are running a marathon in the next few weeks," (narrow
  only when the topic is narrow: Dublin, sub-4).
- Line one: run the P120 pre-flight (a tip is not a counter-position).
  Something you can photograph, turned into a paradox, ending
  on the reframe "...and that is your race going to plan." (31.9% to
  34% skip with it; 38.1% without; 43.1% when abstract). P112, P116.
- Then pain as a picture, the dream as a picture, a named concept that
  belongs to nobody, the save prompt. The hook never contains the
  answer; the stages close the loop and the rehook reopens it before
  the last stage.

**Body**
- Four stages on one axis, ideally the race clock; each opens on the
  unexpected, gives a reason, ends on an action with real numbers.
- ~250 to 300 words, about 1:20 to 1:35. 1:48 lost watch share.

**Never**
- Statistics, study or research language, or named people in the audio
  (P105, P107, P113). No medication. No central governor or brain
  governor. No em dashes, no "not X, it is Y", no staccato fragments,
  no mockery, no dated audio, no lines with a second (e.g. sexual)
  reading (P114).
- No claims Luke has not made about himself. No Dublin content on the
  personal account (his Dublin race is a surprise).

**Cover**
- One real image, colour, present day, the hook as a picture, a new
  picture every time (a repeated splits graphic pushed skip to 38.1%).
- Best: the course map (20.6%), a person with the problem (25.5%),
  Luke's own real data screenshot. Never crowds, products, food,
  winners, vintage, black and white, or faces and name bibs. Free
  licence (Wikimedia, Flickr CC, Openverse, Unsplash, Pexels; never
  Pinterest); credit in the caption's last line.

- **Luke, 14 Oct: stop recommending the old Creative Commons race photos
  (the 2011 Eugene set and similar); he finds them poor.** Give him
  specific search terms for Google Images and Pinterest, ranked by what
  the picture must show, and he picks. Remind him in one line to check
  the licence (Google's "Creative Commons licences" filter, or the same
  image on Unsplash or Pexels).

**CTA**
- One sentence. Since 14 Oct: the **free personalised plan**: "email us
  your race and goal time through the link in the bio". Also in the
  caption and pinned comment. Track emails per video. Ask consent
  before adding anyone to a launch list.

**Captions**: Luke wants prose paragraphs, no bullet points.

## Current state (update this every session)

**As of 16 October 2026 (evening).**

Grid (Instagram, ERN side): the wall 147K; **carb load 52.8K at ~20h (our #2: 1.3K saves, 60 follows, a record; skip 46.7%)**; **without the wall 41.5K at
18h** (record 39s watched on 1:37, save 3.2%, 25 comments; skip 39.3%
with no reframe in line one and the first AI cover); out of the wall
40.8K; 7 days 31.4K at 14h; 24 hours 30K; first 10 minutes 27.1K at
12h (share 1.4%, a record); how hard at every 10K 25.1K at 13.5h (skip
31.9%; first plan CTA: 4 emails); goal pace 25.3K; cramp 25K; second
half 17.6K at 14h; sub-4 at every 10K 14.5K at 18h (skip 40.8%) but
**9.5K on TikTok, the best TikTok yet** (without the wall: 6.3K, second
best); quit ~14K at 14h; Dublin course (small reach, deepest
engagement); taper and heavy legs missed.

Latest review: `ideas/2026-10-16-carb-load-review.md` (with the 20-hour
addendum). Lessons: a fuel title with a full schedule (P121) is now our
#2 video, so P101 is narrowed; skip (46.7%, worst) did not decide reach;
AI covers unresolved (two high skips, but our #2 and #3 by reach).

Next topic (17 Oct, third pass): **"What to wear for a cold marathon"**:
the carb load's table device (by start temperature) on a race-morning
schedule, real cover. Luke rejected the fuel video (P124: it reopens the
"eleven gels" argument); a pacing table fails P119 (sub-4 is recent). See
`ideas/engine-room-nutrition/2026-10-16-next-topic-scored.md`.

Ready (17 Oct, v1 for Luke): `ideas/engine-room-nutrition/2026-10-17-script-cold-marathon.md`
("What to wear for a cold marathon"; Luke's science vetted; AI-writing
check in the file, P125; real cover: Luke's own bin-bag photo or search
terms). Teleprompter text alongside.

Considered 17 Oct: "How to warm up for a marathon" (Luke). Held: it
would be a second start-pen video straight after the cold one, and its
real secret (the slow first K is the warm-up) was the first 10 minutes
video's. Next after the cold video is picked from its 24-hour data.

Waiting on Luke: emails (carb load, without the wall, sub-4); the
day-three read of carb load.
Next review file: `ideas/YYYY-MM-DD-<video>-review.md`.

Rejected topics: the last 10K (covered across six videos); anything
after the finish line (Luke, 15 Oct); in-race fuel amounts while the
"eleven gels" argument is live (Luke, 17 Oct, P124). TikTok-only idea: goal-time
versions (sub-3:30, sub-4:30) using the sub-4 template.

Upcoming races in the audience: Amsterdam 18 Oct, Dublin and Frankfurt
26 Oct, New York 1 Nov. Held: the "how to actually enjoy your marathon"
creative for the day before Dublin. Covers: Luke picks from search
terms (Google Images, Pinterest), with a licence check.

The plan CTA keeps bringing in emails (Luke, 15 Oct): keep it on every video.
