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

0. **`FACTS.md`: the fixed facts (who they are, what they carry, the gel
   and pace numbers, what we've already said, the email answers). Every
   number and every practical detail in a script comes from here. Do the
   maths (grams an hour) before writing.**
1. `SCRIPT-CHECKLIST.md`: every rule a script must pass, with the
   evidence. **Every script passes every line before Luke sees it.**
2. `PLAN-winners.md`: the winning formulas, the grid of top videos,
   what never worked.
3. The three newest `ideas/*-review.md` files: the latest data.
4. The newest scripts in `ideas/engine-room-nutrition/` (the house
   style, the hook stacks, the audit tables).
5. `principles.md` (P1 to P142, about 4,400 lines): search it for the
   rule you need; do not read it end to end. The newest rules (P97 to
   P142) are at the end, before "Open questions for Luke".

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
- **Every video hands over a method they use today (P127):** numbers,
  a framework, a table in the caption.
- **Advise only what this audience actually does (P126):** amateur
  runners in Ireland, the UK and Europe; no niche kit (arm sleeves).
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
- **Before a full script on a new topic (P138):** send a short brief first
  (the method in numbers, line one, pain and dream in one line each, and
  every fact used with where it comes from in FACTS.md) and get Luke's yes.
  Then write the script.
- **Facts check before delivering (P138):** a table in the notes of every
  number and practical claim in the script, each traced to FACTS.md or an
  earlier script. Anything that can't be traced gets cut or flagged.
- **Order when delivering a script:** one or two lines on what changed
  and why; a table of how the curiosity runs (moment, line, what it
  does); the OST in bold capitals on two lines; the markers as a
  numbered list in capitals; the script with its length; short notes.
- **Numbers as numerals in scripts (P131):** 3:30, 20K. **Paces as 5-second watch bands (P132):** "between 4:50 and 4:55".

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
  on a reframe (31.9% to 34% skip with it; 38.1% without; 43.1% when
  abstract). P112, P116. **New wording every video (P136): "that's your
  race going to plan" is retired** ("and that's exactly how it should feel").
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
- **A third of the way in, then back to the video (P128).**
- One sentence. Since 14 Oct: the **free personalised plan**: "email us
  your race and goal time through the link in the bio". Also in the
  caption and pinned comment. Track emails per video. Ask consent
  before adding anyone to a launch list.

**Captions**: Luke wants prose paragraphs, no bullet points.

## Current state (update this every session)

**As of 20 October 2026.**

Grid (Instagram, ERN side): the wall 147K; **3:45 pacing 29.1K at ~17h, TikTok 10.9K (record), emails up with the CTA a third of the way in (P128)**; **carb load 52.8K at ~20h (our #2: 1.3K saves, 60 follows, a record; skip 46.7%)**; **without the wall 41.5K at
18h** (record 39s watched on 1:37, save 3.2%, 25 comments; skip 39.3%
with no reframe in line one and the first AI cover); out of the wall
40.8K; 7 days 31.4K at 14h; 24 hours 30K; first 10 minutes 27.1K at
12h (share 1.4%, a record); how hard at every 10K 25.1K at 13.5h (skip
31.9%; first plan CTA: 4 emails); goal pace 25.3K; cramp 25K; second
half 17.6K at 14h; sub-4 at every 10K 14.5K at 18h (skip 40.8%) but
**9.5K on TikTok, the best TikTok yet** (without the wall: 6.3K, second
best); quit ~14K at 14h; Dublin course (small reach, deepest
engagement); taper and heavy legs missed.

Latest review: `ideas/2026-10-20-430-review.md` (4:30 at ~10.5h, lunchtime
post: 14.6K IG, TikTok 8.5K, **skip 37.0%, best of the goal-time series**:
slower goal = bigger group; cover of one runner at a drink station, no
crowd; CTA step at ~0:40; "lots of emails this week"). Before it: 3:30
(8.9K at 12.5h, skip 48.9%, crowd frame, 6pm post); 3:45 (29.1K).
Earlier: cold marathon (real cover 35.1% skip, 0.9% saves; AI covers
retired), carb load (52.8K, our #2).

**Week plan (demand-led, 19 Oct):** `ideas/engine-room-nutrition/2026-10-19-demand-led-week.md`
(from Luke's inbox themes and TikTok search). Tue 20: 3:30 pacing. Wed 21
(views): what to do when you can't face another gel. Thu 22: how to turn
your half marathon time into a marathon goal (incl. after illness). Fri 23
(views): how to run the New York marathon. Sat 24: how to actually enjoy
your marathon. 4:30 goes TikTok-only. Luke's goal: 1M lifetime IG views
(840K on 19 Oct; 865K on 21 Oct). Every pace in km and miles in captions (P129).

Waiting on Luke: gel script FINAL v11 delivered (hook invites, P141; pain at 20K into a long run, P142; jellies and flavours in the caption) (`ideas/engine-room-nutrition/2026-10-21-script-gel.md`: drink your gel, squeezed into the 250ml station bottle; P140 one aha); emails per video (3:30, 4:30).
Website v4 (21 Oct): `website/` (home = free pace plan, shown on screen after the email via `plan.js`, the video method as code; /pages/the-bar = waitlist with the kit-bag comparison; README has install, Klaviyo, the plan table for Luke to check). Proof (22 Oct): named results wall (Dave -45 min Dublin, Caroline -13 min Dublin, Tom 3:19 Chicago aiming sub-3:30, Ellie sub-3 Frankfurt, Conor 2:47 Malaga) plus the anonymous 12-minute PB (P143). DNS host: Shopify (domain bought through Shopify; Shopify DNS runs on Google Cloud nameservers, ns-cloud-c*.googledomains.com, registrar Tucows). Edit in Shopify > Settings > Domains. Klaviyo list 468, 270 since 14 Oct; 62% Gmail. Instagram export: 915K views on ERN reels since 1 Sep, 18,721 saves. DNS (22 Oct): SPF and Google DKIM (1024-bit; Shopify caps TXT at 255 chars) live; mail-tester 10/10. Website v5 (22 Oct, `website/BRIEF-v5.md`): goal slider in the phone first screen, the bar inside the plan's race-morning step, founders video slot and honest race CV, "tell us your time" results form, events at every step (Clarity/GA4/Klaviyo), WebP images. Waiting on Luke: DMARC report address, founders clip (MP4), Clarity install, Tom's message and permission, bar eating time and price, lab figures, FSAI.
Next review file: `ideas/YYYY-MM-DD-<video>-review.md`.

Rejected topics: the last 10K (covered across six videos); anything
after the finish line (Luke, 15 Oct); in-race fuel amounts while the
"eleven gels" argument is live (Luke, 17 Oct, P124). TikTok-only idea: goal-time
versions (sub-3:30, sub-4:30) using the sub-4 template.

Upcoming races in the audience: Amsterdam 18 Oct, Dublin and Frankfurt
Sunday 25 Oct (not 26: that's a Monday), New York 1 Nov. Held: the "how to actually enjoy your marathon"
creative for the day before Dublin. Covers: Luke picks from search
terms (Google Images, Pinterest), with a licence check.

The plan CTA keeps bringing in emails (Luke, 15 Oct): keep it on every video.
