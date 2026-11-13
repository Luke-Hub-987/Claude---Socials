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

## FIRST: the gate (P190, built 4 Nov)
**Every script passes `GATE.md` before Luke sees it. No exceptions, no self-grading.**
1. `python3 gate/check.py <script file>`: the AUTO tests. Hooks run it on every
   edit, on every commit (`.githooks/pre-commit`, set by the SessionStart hook)
   and when a turn ends, so a failing script can't be committed or slip out.
2. **One review (P196, Luke 10 Nov):** settle the idea on the brief (repeats,
   premises, the gap, the turn: `brief_ok:` in the front matter), then build the
   packet (`python3 gate/check.py --packet <script>`) and run the `gate-reviewer`
   agent **once** on the words (G2, G12, G21, G22, G23, G29). Fix every FAIL and
   list it in `fixed_after_review:`; no second round. Luke's `luke_override:` ends
   it; a FAIL that needs his fact goes to him as "blocked on X" with the exact
   question. Judgement tests go in the Known risks box, ungraded.
3. Frame one mocked up at phone size: `node gate/shoot_frame.js <out.png> "<query>"`.
4. Forecasts are ranges from the last 3 to 5 comparable reels, never "confident".
**GATE.md is v0.9 until Luke settles the 24 contradictions in
`gate/contradictions.md`; the [C#] lines use the recommendation till then.**
A new script file copies the layout of
`ideas/engine-room-nutrition/2026-11-06-script-sub-430-secretly.md`.

## Read before writing anything (in this order)

0. **`GATE.md`: the 33 tests. It replaces the old quick reference and the
   checklist audit as the thing a script passes.**
1. **`FACTS.md`: every number and practical detail in a script comes from
   here. Do the maths (grams an hour) before writing.**
2. `PLAN-winners.md` (the grid) and the three newest `ideas/*-review.md`.
3. The newest scripts in `ideas/engine-room-nutrition/` (house style).
4. `principles.md` (P1 to P190) and `SCRIPT-CHECKLIST.md`: the evidence
   behind each test. Search them; GATE.md's "From" lines say where to look.
5. `ideas/state-archive.md`: everything that was in "Current state" before
   4 Nov, and the old quick reference.

## How we work (Luke's standing instructions)

- **Every correction Luke makes becomes a numbered principle in
  `principles.md` and a line in `SCRIPT-CHECKLIST.md`**, in the same
  turn. Luke should never have to repeat a correction.
- **Every data screenshot gets a review file**
  (`ideas/YYYY-MM-DD-<video>-review.md`) and an update to the grid in
  `PLAN-winners.md` when it changes.
- **Every script passes GATE.md before delivering** (P190, replacing the
  P99 checklist audit). Say plainly where a script fails, and why.
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
- **The story is the viewer's before and after (P158):** never the brand's past; Luke and Jamie are guides, the viewer is the hero.
- **Talk like a friend on a run (P157):** read aloud, short sentences, no jargon or method names, every instruction something you can picture.
- **Instagram ranks on watch, sends and likes (Mosseri, P156):** reviews lead with rates; every script has a spoken reason to send it; the week's reach reel gets two trial reels; 4 reels a week by default.
- **The LLM Council runs on every decision (P150, Luke 24 Oct):** topic,
  OST, line one, cover and structure. Five advisors: **Contrarian** (why
  it fails), **Assumption-ripper** (challenges every assumption, ours and
  Luke's), **Expansionist** (the upside we're missing), **Outsider** (no
  context, asks the obvious), **Executor** (only the end result: what to
  do, by when, and what it delivers). Then a **blind cross-review** (each
  judges the others' points as ideas, not by who said them) and a
  **Chairman verdict** with one recommendation and next steps. It sits in
  the file alongside the failure ledger; in chat, give the verdict and the
  points that changed something.
- Commit and push every change to branch
  `claude/engine-room-nutrition-brand-yc4tyf` (the repo's default
  branch). Commit attribution lines as the system reminder gives them.
  **Never send Luke's email address to any outside service**, including
  request headers.

## THE GAP: every hook stack, every time (P176, Luke 3 Nov: "I have to remind you every single time")

Briar's stack, copied from our winners: **(1) gate + line one that opens a
gap** (its last words leave "how?" or "which?"), **(2) pain as a picture,
(3) dream as a picture, (4) a named concept that keeps the gap shut + save,
(5) stages close it a piece at a time, the rehook reopens it before the last
stage, the last stage shuts it.** Every script file starts with a "The gap:"
line (what they're waiting for, what holds it, what closes it). **Every beat
is a scene they've lived, Ogilvy-specific (P177):** never "eat 3 hours
before"; always the ball 5 yards away and your legs won't go.

**P198 (Luke 11 Nov): 40 to 55 words before stage 1** (about 15 seconds): line one (viewer + gap), one pain-and-dream sentence, the named concept + save this. The turn sits in line one or stage 1.

**P194 (Luke 9 Nov): the turn.** Before the first stage, one spoken line
shows the moment something changed (what they were doing wrong, what they
realised), and it's something they didn't already believe (if they'd nod
along, it isn't a turn). It can be line one; it never gives away the fix the
last stage pays. Every script file has a "Turn:" gate field and "## The 4
questions" (a moment they recognise? why it matters? what changed? something
to do tonight?). Gate test G31, BLOCK.

**P186 (Luke 4 Nov, "every single time", a repeat): two checks in every
script file before Luke sees it.** (a) **The line-one gap test:** read line
one alone, write the one question a stranger would ask ("what 10 words?"):
one specific question, not guessable, answered by a named stage, nothing
earlier gives it away, and never about a stranger's result. (b) **Pain and
dream built new:** never "Get it wrong / Get it right" or "you're the one
who" (check.py flags them). Pain = the cost with the feeling or the cruel
timing (Briar: "...and hate throwing that money away"); dream = what they'll
see (Briar: "you will end up with..."; Luke: "after watching this you'll be
passing people at 32K"). A shape the last 3 scripts didn't use; the stack
table shows it.

## How to deliver in chat (Luke, 16 Oct: copy the old chat exactly, P122)

- **No AI-writing signs (P125, P169): run the humanizer skill
  (`.claude/skills/humanizer/`) on every script, caption, pinned comment,
  OST and story line before Luke sees it, without being asked.** The
  checker, then a full read against the Wikipedia catalog, then the
  rewrites, then the Humanizer table in the file. Words only: the hook
  stack, Briar's frameworks, the numbers and the length stay as they are.
- **Every beat turns (P199, Luke 11 Nov, Ogilvy):** but or so, never and then; every word counts; figures, not atmosphere; facts, not clichés. The humanizer checker flags them.
- **Even sentences (P202, Luke 11 Nov):** no 3- or 4-word sentence, and no short one straight after a long one (the AI tell); join it on with but, so or because. A study reel walks one runner through the study's numbers. The humanizer checker flags it.
- **Captivating (P206 to P208, Luke 12 Nov):** open on the myth killed or a goal-time call-out; one `Repeat line:` contrast pair (G33); the runner's own words aloud; the honest cost; the identity follow last; on screen, a count + escalation tag, the feeling word in red, the myth struck through per stage. The 60-second 3-item format is a trial reel only (`trial_format: 60s`).
- **Urgent, opinionated, memorable (P200, Luke 11 Nov):** a real date to act on, a plain opinion backed by a fact, one line they'd repeat; nothing that could be in any running video.
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
- **[C12, pending Luke: AI covers were retired on 18 Oct, so I recommend
  deleting this item and giving search terms instead.]** **Gemini cover prompts:** "Paste this into Gemini as one block", then
  the prompt written as real photojournalism (scene, one person, face
  hidden, real details, camera body, lens, aperture, shutter, distance,
  natural muted colour, subtle grain, no retouching, aspect ratio),
  then an "Avoid:" line (no logos, brand names, readable text or
  numbers, flags or national symbols, no visible face, no cinematic
  light, HDR, oversaturation, plastic or airbrushed look, extra
  fingers). Never Irish or race branding (Luke, 15 Oct). Then why each
  part is there, and what to zoom in on before using it.

## The failure ledger (P148): the record of what failed

**Since 4 Nov every row is caught by a GATE.md test (the map is at the end of
GATE.md). A script file carries the gate table and the reviewer's verdicts in
place of this table [C16, pending Luke]. Reviews still check this list first:
a repeat is named as a repeat, and the gate test that missed it gets fixed.**

Luke, 24 Oct: "I have asked you to update this before and you clearly
haven't." The sleep video repeated three failures already on record. Rules
existed; nothing forced the check. **Every script file carries this table
with a pass/fail per row before Luke sees it. Every review that finds a
cause checks this list first: a repeat is named as a repeat (my miss), and
a new cause becomes a new row in the same turn.**

| # | Failure | Where it happened | The check |
|---|---|---|---|
| 1 | **The answer up front** (OST, line one, opening frame, named concept) | Gels count 42.9% ("the OST answered its own question", 20 Sep); taper v2, wall v1 (Luke caught); sleep 41.4% (the reassurance as a sentence on screen) | After the opening frame, line one and the named concept, what is the viewer still waiting to find out? |
| 2 | **Reassurance in place of instructions** | Heavy legs (0.5% saves); sleep (1.0%) | Every stage ends on an action with a number |
| 3 | **Off the race clock** (the gut, taper, training weeks, kit, sleep) | Stomach 4.1K; taper 43.1%; training 4.4-5.3K; cold 0.9% saves; sleep 1.0% saves | Race day, a race-pace decision, or a countdown with an action per stage (P117) |
| 4 | **A crowd, start or finish** in the cover or opening frame | 3:30 48.9%; out of the wall's first frame; last 24 hours 38.1%; sub-4 40.8% | One person, one object, or one number |
| 5 | **Collage, AI or repeated cover** | Cramp, taper, stomach collages; AI 39.3%, 46.7%; repeated splits 38.1% | One new real image (or a motion graphic of the hook) |
| 6 | **Abstract line one, or no reframe** | Taper 43.1%; without the wall 39.3% | Photograph test plus a reframe in new words (P116, P136) |
| 7 | **Too long** | How hard 1:48; cramp 1:31 on 300 words | About 300 to 320 words, 1,550 to 1,670 characters |
| 8 | **A "why" stage after the method** | Goal gone, half gone at 1:13 | The why is one line inside the payoff stage |
| 9 | **CTA late or long** (hook now 40 to 55 words, P198) | Sleep 0:49 (116-word hook); 4:30 0:40; enjoy 0:42 (38% to 26%); thread line plus CTA cliff (out of the wall); **10% rule, 12 Nov: the ask after stage 1 lost half the viewers left at 0:38 to 0:45 (a repeat)** | Hook 40 to 55 words; **no email ask in the body: last line or pinned only; save after stage 1, send after stage 2 (P204, G19)**. **Count the emails per video** so the step can be judged against what it brings in |
| 10 | **Sorting viewers** | Who hits the wall ~7.5K | Every viewer is the subject of every stage (P103) |
| 11 | **A problem few viewers have** | Gel 5.8K; narrow gates on IG (sub-4, Dublin) | What share of viewers have this problem? |
| 12 | **Mixed timelines in the stages** | Stomach | One clock |
| 13 | **A list of symptoms, not a sequence** | Heavy legs | Stages in time order, each an action |
| 14 | **Cover number not in the title** | Sub-4 (a 3:45 flag) | Every number on screen is in the title or line one |
| 15 | **A tip as line one** | Carb load v1 to v6 (Luke caught) | P120 pre-flight: would runners argue, and can't they guess why? |
| 16 | **Template lines repeated** | "That's your race going to plan" (P136); a viewer called a script AI (P125); **"Get it wrong / Get it right" in match v2, long run v2-v4, Valencia, 200 plans (Luke caught, 4 Nov, a repeat of 17 Oct)** | No line **or pain/dream shape** from the last three scripts; check.py 0 flags (P186) |
| 17 | **A reframe that answers line one, or no gap** | Enjoy v1, "that's how it's meant to go" (Luke caught, 24 Oct); 200 plans v1, a stranger's result with a guessable answer that no stage came back to (Luke caught, 4 Nov) | The line-one gap test table (P186): the stranger's one question, not guessable, the stage that answers it. A promise ends on the open loop, not a reframe (P149) |
| 18 | **Nothing too long to remember** | Cold 0.9% saves, sleep 1.0%, enjoy 1.2%, surprise 0.0% | A schedule, table or K-by-K plan they'd come back to on race morning (P152) |
| 19 | **Dated words in the gate or audio** | Enjoy ("this weekend": flat after day one) | No "this weekend", "tomorrow", "tonight" (P82, P153) |
| 20 | **A story with no stake for strangers** | Surprise 44.1% skip, 0 saves (opening frame: Luke talking, not the bib) | The stake as a picture in frame one; a story opens an advice video, not alone (P151) |
| 21 | **Maths in the audio** | Goal gone ("your A goal times 0.59"), 3:45 (the GPS explanation): viewers called it complicated (Luke, 27 Oct) | The answer as one number, never the sum; one worked example; the rest in the caption (P155) |
| 22 | **A busy first second** | Last marathon 52.4% (a splits list, tiles, labels and a strip in the top band; a repeat of P147) | One big element, or Luke alone with the title, for the first 3 seconds; graphics from stage 1; checked at phone size (P159) |
| 23 | **Someone else's numbers** | Email wall: a 3:23 plan, saves 0.4%, shares 0.1% (30 Oct) | The worked example is a goal most viewers have (3:45 to 4:00, sub-4), or the plan for every common goal is in the caption and the last frame |
| 26 | **Advice they already know** | Match reel v1: our race-morning clock ported to football (Luke caught, 3 Nov, before filming); the carousel stopped at 1.6 of 5 photos (consistent, not proof) | Name the belief we overturn and what they learn that they didn't know; known advice is one short stage at most (P175). Rows 24 and 25 were withdrawn on 1 Nov |
| 27 | **A general title: no number, no deadline, nothing new** | Long run 55.5% skip (4 Nov); where it goes wrong 52.1%; last marathon 52.4%; taper 43.1%; heavy legs 0.5% saves | Two of five in the title: number or race, deadline, constraint, proof, our own method (P178) |
| 28 | **Numbers that read as failure** | 200 plans / 10 PBs read as 5% (Luke caught, 4 Nov, before filming) | Divide each number on screen by the biggest one next to it; the true base, said aloud (P187) |
| 29 | **A picture that repeats the title** | 200 plans cover: the 16 / 10 / 2 scoreboard under the same numbers in the title (Luke caught, 4 Nov, before posting) | One line per layer (title, picture, line one); each says something new (P188) |
| 30 | **Line one about us, not them** | 16 results trial: "We've sent over 200 free marathon plans" first, gate second, title = our result; 44.4% skip, 80% gone by 0:05 (4 Nov) | The first-3-seconds gate (P189): first words the viewer, one thing on screen, the question inside 10 words, the title their goal |
| 31 | **A sequel to the same followers within days** | Sub-4:30 (secretly), 9 Nov: the parent's title twist, line one and method with the goal changed, posted to the profile 3 days after the parent: skip 51.3% (Higher), 10s watched against 23s, reach stopped at followers (Feed the top source). A repeat in part: the known risks G17 and the one-change sequel were in its box, and ledger row 16 | On the profile, a sequel gets a new twist, a new line-one shape and a new frame-one picture, and posts at least 7 days after the parent; a one-change test only as a trial reel (G32, P195) |
| 32 | **A payoff that contradicts the title** | 10% rule, 11 Nov: title STOP USING THE 10% RULE, method "add 10% to your longest run" (Luke caught, before filming) | Title, line one and last stage read together: the fix never does what the title says to stop (P201; reviewer, under G22) |
| 33 | **A title you can't read in one second** | 10% rule, 12 Nov: small, mid-frame, mid-blue box on a blue T-shirt; the third post running where frame one wasn't the brief's (row 22) | Top band, full width, black bold on white, shot at phone size with `spec=white` (P205; G15 mockup) |

## Current state (update this every session; older entries in `ideas/state-archive.md`)

**As of 4 November 2026.**

**Posted 11 Nov 8:47pm: THE 10% MILEAGE RULE / FAILED ITS ONLY TRIAL.** ERN TikTok at ~14h: 489 views, **13.6s, 3.05% full, 3 follows** (the body beat our last four), 2 saves, 0 shares, **most left at 0:01**. Frame one: a small mid-blue title on Luke's chest plus a cartoon runner from 0:00 (row 22, third post running); the title had no "you" and no feeling word. IG + FB at ~13.5h: **7,238 views (2,260 IG, 4,978 FB), skip 41.1% Lower (best of the last four), 16s, saves 0.4%, shares 0.1%, 0 follows, Reels tab top source**; flat overnight after 2h (evening posts 2 for 2); a step down at 0:38 to 0:45 at the CTA (row 9 repeat); the send line at 1:26 reached ~3%. Forecast 9K to 12K. Fixes: CTA to the end or the pinned comment, send line after the worked example, save after the first keepable number, 7am (`ideas/2026-11-12-10-percent-rule-review.md`). New title spec and feeling devices: `ideas/engine-room-nutrition/2026-11-12-feel-something-osts.md`. Fri: THE 5 STAGES OF THE / MARATHON WALL / (EACH ONE MORE BRUTAL). New ledger cause for the gate chat: a title you can't read in one second.

**12 Nov: THE MARATHON WALL / HITS YOU IN 5 STAGES / (EACH ONE MORE BRUTAL) ready to film** (13 Nov: BRUTAL in red on the title card; cover `motion/covers/wall-cover.png`, a runner face-first into a brick wall under the title; web image links given in chat) (OST changed by Luke the same day; text cards in the style Luke sent, `motion/wall-cards/wall-card-*.png`, and an illustrated scene per stage, `motion/wall-cards/wall-[1-5]-*.png`, page `motion/wall-scenes.html`) (`ideas/engine-room-nutrition/2026-11-12-script-5-stages-wall.md`, post Fri 14 Nov 7am). 0 FAIL after the one review (G21, G22, G23 fixed; G29 Luke's rehook). New from the 10% data: P204 (save after stage 1, send after stage 2, email ask pinned only; G19), P205 (title in the top band, black on white: `shoot_frame.js "spec=white&fit=line..."`), ledger row 33. Frames `motion/plan-frames/wall-*.png`.

**Posted 10 Nov ~1:16pm: 8 SPRING MARATHONS: / 1 CHANGE FOR YOUR PB** (profile collab + FB + ERN TikTok). At ~5h: 1,406 views (1,065 IG, 341 FB), **skip 48.0% Lower, 17s, shares 0.2% Higher, saves 0.5% Lower, 0 follows**; TikTok 700, 9.7s, most left at 0:02 (`ideas/2026-11-10-spring-ranking-review.md`). Frame one was the busy tier board, not the planned title-only frame (row 22 repeat; second post running). Next: THE 5 STAGES OF THE / MARATHON WALL, Fri 7am (brief `ideas/engine-room-nutrition/2026-11-10-brief-5-stages-wall.md`, needs Luke's stage names); frame one screenshot checked before posting.

**Posted 9 Nov 8:30pm: HOW TO RUN A SUB-4:30 / MARATHON (SECRETLY)** (profile collab + FB + ERN TikTok). At ~10h: 3,616 views (793 IG, 2,823 FB), **skip 51.3% Higher, 10s, saves 1.0%, shares 0, 0 follows**; Feed top source (it stopped at followers); TikTok 787, 10.1s, 1.5% full (`ideas/2026-11-10-sub-430-secretly-review.md`). The one-change test answer: the same title, line one and method don't carry a second goal 3 days later on the profile. No third (SECRETLY) reel; the 3:45 row goes in a caption or story. New ledger cause for the gate chat: a sequel to the same followers within days.

**9 Nov:** SUB-4:30 (SECRETLY) v2 ready to film (0 BLOCK; known risks G5, G13, G17; Luke allowed the 20 Oct repeat; frames `motion/plan-frames/s430-*.png`); its follow line promises sub-3:45 next. P194 the turn (G31) added. Spring ranking v2 blocked after 2 rounds (`gate/runs/2026-11-09-spring-ranking.md`): G8 needs Luke (the start-slow payoff repeats 1 Nov), G16 and G31 follow from it. Spring 2027 dates, entry routes and course facts in FACTS.

**Parkrun posted 7 Nov (blocked on G8 in the gate): 8,267 views, skip 44.9%, 14s, saves 0.2%, shares 0.1%, 0 follows (`ideas/2026-11-08-parkrun-25-review.md`); front held, body didn't (known advice). Sub-4 (secretly) at 3 days: 10.4K, 15 shares. Next: Monday the gated 4:30 sequel; this week IF YOUR SPLITS LOOK / LIKE THIS, DO THIS (needs Luke's 3 shapes); `ideas/engine-room-nutrition/2026-11-08-ideas-watch-time.md`.**

**14h read (6 Nov 21:10): 7,199 views (3,818 IG), skip 44.5% (Lower; the 1h 18.5% was mostly followers), 23s, saves 2.3% and shares 0.4% Higher, 0 follows. Next: HOW TO RUN A SUB-4:30 / MARATHON (SECRETLY); Valencia from 15 Nov as VALENCIA MARATHON / SUB-4 (THE 31K TRAP); parkrun blocked on Luke.**

**Posted 6 Nov 7:13am: HOW TO RUN A SUB-4 / MARATHON (SECRETLY)** (the just-to-finish script, profile collab + FB, not a trial; `ideas/2026-11-06-sub-4-secretly-review.md`). At ~1h: IG 1,034 views (731 IG), **skip 18.5% (our best ever), 21s, saves 2.3% Higher**, shares 0, follows 0; TikTok 293, 18.2s, 5.5% full. Formula: HOW TO [outcome + number] / [EVENT] ([TWIST]). Next topics: `ideas/engine-room-nutrition/2026-11-06-ideas-formula.md` (parkrun #1 for Saturday, needs Luke's 5K numbers).

**GATE.md built (4 Nov, P190).** 30 tests, the 4-line first-3-seconds gate
(P189) on top, every principle mapped (end of GATE.md). Checker
`gate/check.py`, hooks in `.claude/settings.json` and `.githooks/`, reviewer
`.claude/agents/gate-reviewer.md`, phone-size frame tool `gate/shoot_frame.js`.
**Waiting on Luke: the 24 contradictions (`gate/contradictions.md`).** Then
GATE.md goes to v1 and the [C#] lines change to his answers.

**First gate run: the 16 results refilm. Verdict: don't film it**
(`gate/runs/2026-11-04-16-results-refilm.md`, reviews in `gate/reviews/`).
v1 (the review's plan: refilm 15 seconds, keep the body) failed 17 tests; v2
(a full rebuild) failed 10. What's left is the topic: the 10-word test was the
payoff of 3 reels (G8, C21), no race inside 4 weeks (G5), the title names no
event (G11), and "every good result with splits" isn't a real count (G22).
The hook wouldn't commit the failing script, so it's kept as a record and its
teleprompter was removed. Recommendation: put the filming time into Valencia.

**Gate run 2: Valencia (5 Nov). Not ready to film** (`gate/runs/2026-11-05-valencia.md`).
v1 to v3 failed the reviewer on 11, 9 and 10 tests. Blocked on Luke's C22 (gels:
the clock vs 100m before a station, which never line up on this course), C23
(is a map fact enough for a course video's line one) and C24 (watch pace vs
clock time). The official 2026 map is in `research/`; Valencia facts in FACTS.md.
Post window stays 15 to 22 Nov. Today's post: the weekly winner repost (no filming).

**Gate run 3: "Just to finish". Ready to film** (`ideas/engine-room-nutrition/2026-11-05-script-just-to-finish.md`).
SAID JUST TO FINISH. / WANT SUB-4 MARATHON? Luke's "just write the script" covered
the repeat (C21), the premise and no deadline. Under P192's two tiers: 0 BLOCK
fails; known risks G17 (guessable for anyone who saw 14 Oct) and G18 (dream shape
near long run v4), in the file's box. IG trial from ERN + ERN TikTok. **Top-band frames (5 Nov):** `motion/plan-frames/jtf-*.png` (5 frames, 16:9, the hand plan fills in per stage). **Covers (5 Nov):** `motion/covers/just-to-finish-cover-watch.png` (FINISH 4:02 on a watch, recommended) and `-cover-hand.png` (the hand plan, 4 blanks).

**10% rule character motion (11 Nov, Luke: "actual characters... start to finish"):** `motion/ten-percent-characters.html`, one 1:33 cut (6 scenes), sent in chat.  `motion/ten-percent/` (3 MP4 scenes, one per stage, 16:9, plus stills of each last frame; page `motion/ten-percent.html`).

**Spring ranking top-band frames (9 Nov):** `motion/plan-frames/spring-*.png` (6 frames, 16:9; the tier board fills in D to S, unranked courses face down). The script is still blocked (`gate/runs/2026-11-09-spring-ranking.md`).

**Parkrun 25 top-band frames (6 Nov):** `motion/plan-frames/pr25-*.png` (5 frames, 16:9; the 3 ranges card fills in per stage). The script is still blocked on Luke (G8, G9, G16; `gate/runs/2026-11-06-parkrun-25-v3-full-file.txt`).

**P192 (Luke 5 Nov, "too strict"):** BLOCK tests must pass; RISK fails get one round,
then a Known risks box Luke sees before filming; 2 reviewer rounds at most;
reviews check the box before naming a cause. Reviews use one packet (~2 min).

**Two chats (Luke, 5 Nov, P191):** this chat writes scripts and owns GATE.md
and gate/; a second chat does ideas, topics and OST from `gate/prompts/ideas-chat.md`
and touches only ideas/. C22 to C24 settled (gels on the clock, grab water when
passing a station; the clock at every 10K sign).

**Live and waiting on Luke:**
- 16 results: is Luke's own 3:44:13 one of the 16? How many results came
  with splits, and how many held the second half? Read the first trial
  (459 views, 44.4% skip at 1h) at 24h.
- Cover v2 for the results video: one real runner's line ("about 10 minutes
  quicker than planned"), needs her OK; under C9 it's the grid cover or a
  0:03+ frame, never frame one. Fallback: a licensed photo of one runner
  checking their watch late in a race.
- **Valencia** (6 Dec): brief `ideas/engine-room-nutrition/2026-11-04-brief-valencia.md`;
  WHERE THE VALENCIA / MARATHON IS LOST; check the official 2026 map full size
  before scripting; post 15 to 22 Nov as a trial reel; race-week reposts
  (7 days, carb load, 24 hours) from 26 Nov.
- **Black Friday (27 Nov):** £250 SHOES FOR A / 4-HOUR MARATHON? vs DO YOU
  ACTUALLY NEED / SUPER SHOES? as a trial A/B; Luke's 3:44:13 and passing
  people in super shoes is line one; price to check; post by 25 Nov.
- **The 4:20:51 runner** (SHE PLANNED 4:30. / SHE RAN 4:20:51): only with
  her OK, name hidden.
- **Team sport:** the match trial's 24h read (242 views, 26.2% skip at 2h);
  if under 2K, rerun as one sport (Sunday league soccer, 90-minute clock).
  In or out is C8.
- **Weekly winner repost** as a trial (next: how hard at every 10K, cramp,
  what marathon time you're in shape for).
- Sign-ups per day since 1 Nov (Klaviyo counts only, P154).

**Base rates for forecasts (P171):** IG trial reels since 2 Nov: the wall
repost 3,537 views, 33.3% skip (about a day); the long run 290, 55.5% (10h);
the match 242, 26.2% (2h); 16 results 459, 44.4% (1h). November profile
reels: 2K to 6K at 5h (11 in a row). The calendar sets the ceiling until the
spring blocks start (late Dec, Jan).

**Rules added this month that live in the gate now:** P174 (trial first),
P175 (novelty), P176 to P189 (the gap, visceral, two of five, the
4-week deadline, "in what?", evergreen stake, gate table, premises, CCN,
exact numbers, the stack built new, the denominator, layers, first 3
seconds).

**Tools:** `motion/scoreboard/` (16 / 10 / 2 frames), `motion/plan-frames/`
(per-goal pace frames), `motion/nyc-maps/tools/` (course breakdowns),
`gate/shoot_frame.js` (frame one at phone size).
