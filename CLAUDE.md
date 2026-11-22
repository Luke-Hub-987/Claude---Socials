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

## FIRST: one chat, title first (P219, Luke 18 Nov)
**Every reel starts with the `title-producer` skill** (`.claude/skills/title-producer/`): the five levers, 20 titles over 8+ devices, `python3 gate/ost_check.py --file <titles>` (counts, of what / in what / who, hedges, repeats, phone size 7.0vw+), the cold `ost-reviewer` agent, then the top 3 with their hooks (40 to 45 words, the title's keywords in the first 20). Then the script and the gate below, in this same chat (the two-chat split, P191, is retired). Graphics: `node motion/title-cards/make_title.js <prefix> "L1 / L2 / (L3)" --red WORD`. Weekly results loop: **scheduled 18 Nov** (every Monday 7:41am Irish time, first run 23 Nov; instructions `ideas/weekly-loop-prompt.md`). It was created without connectors, so until the Windsor connector is added to the routine in claude.ai it will ask Luke for screenshots. **Title library: `ideas/engine-room-nutrition/TITLE-EXAMPLES.md`** (Luke's examples, transcribed, with what we take; screenshots in `research/title-examples/`): read on every title run; new examples get added there the same turn. **P220 (Luke 18 Nov): titles wide open** (Briar's grid added to the library): any route, not only a belief broken; the new must-pass is "they already know it's their problem"; every title promises something we send (comment word -> email). Open shortlist: `ideas/engine-room-nutrition/2026-11-18-titles-open.md`.

## FIRST: where the bar is, and the true-fans lens (P238, P239, Luke 22 Nov: "record this and not to ask me again")
**The bar is not available and has no date. Never ask Luke about launch, batch size, samples or packaging again; he'll say when it changes.** As of 22 Nov: still with the food scientist; no packaging; nothing confirmed. The hope is to hand bars out from a table at the Art O'Neill Challenge (Fri 15 Jan), but nobody has asked the organisers yet, so it's a hope, not a plan. So: no founding-list numbers, no "first batch" scarcity, no pre-orders, no copy that implies it exists. The job until then is **emails**: every piece of content earns an address (the comment word -> email, P220), so the list is there to email when the bar lands. **Seth Godin's three wants, in Luke's words** (`ideas/2026-11-22-seth-godin-true-fans-plan.md`): **status** = run fast, win something, and tell everyone; **freedom from fear** = not looking bad or unfit in front of people they respect; **affiliation** = being part of a team or group. **Many runners train alone (P239):** never assume a run club or training partner; belonging comes from "people like us" (other restarters, other 4-hour runners, the list, the podcast). Year-round demand comes from the **"again" series** (P236, rory.bingethinking's shape): people in their 30s and 40s who let themselves go, see everyone running halves and marathons and want to start; the list is the easy save and the first-step feeling. North star: true fans (replied, came on a call, sent a result), target 100 by 31 Jan; Luke does 10 fan calls, which double as a podcast segment.

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
- **OST scorecard (P210, Luke 13 Nov):** every OST 9+ of 10 on `ideas/engine-room-nutrition/OST-SCORECARD.md`, the score next to it in chat; the most aggressive true version first (G10 checks the `OST score:` field).
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

**22 Nov, life-calendar training app (Luke's idea; `ideas/2026-11-22-life-calendar-training-app.md`):** council verdict: don't build; run it by hand by email to 18 Dec, runners only ('send us your week, we'll slot your runs and when to eat'); pass = 50 requests + 20 week-2 returns, then a web form with no integrations; calendar/Garmin sync last (work Outlook admin consent, Garmin approval, GDPR health data). Waiting on Luke's yes.

**22 Nov, Seth Godin / 1,000 true fans plan (Luke pasted the transcript):** `ideas/2026-11-22-seth-godin-true-fans-plan.md`. Klaviyo: 590 on the list; sign-ups about 7 a day (26 to 31 Oct) down to about 2.6 a day (1 to 21 Nov); the 18K fourth-hour reel didn't move them; 0 to 8 clicks per email, so under 10 true fans. Council verdict: now, the one-sentence audience (3:30 to 4:30 spring marathoners who hit the wall or hate gels), 20 founder fan calls by 13 Dec (the next email asks what they ate before their last long run), and the weekly loop counting true fans (target 100 by 31 Jan); test the email ask back in one reel's body (the CTA move on 12 Nov may explain the drop). Luke's answers the same day: audience yes; the bar is a training bar, before, during slower runs and after, never a gel at race pace (P237); the non-marathon slot stays if it's the same runner on a training run (Sunday league and the broad 'fit again' fail that test); Luke does 10 calls, which double as a podcast segment. Bar status settled 22 Nov (P238): not available, no date, don't ask again.

**20 Nov, TED-Ed cutaway plan for the 3:59 reel (Luke: plan first, no visuals yet):** `ideas/engine-room-nutrition/2026-11-20-teded-visual-plan-3-59.md`. A/B of one take as two IG trial reels: A cuts to full-screen (9:16) cream-paper animation for the bunching, the last 2.2K and your next run (about 48 s, 5 or 6 shots each); B is the gated band-only version. Luke stays on camera for the hook, every ask and the 40K instruction (the clock card animated in the band). Keep A if watch time is 3 s+ longer and retention at 0:45 higher with saves no lower. Waiting on Luke: yes to the A/B, full screen vs band, the recorded audio. Storyboard stills come before any animation. **Luke chose full screen with his audio underneath and killed the stick figures (P229): new rig and 4 style stills in `motion/three-59/teded/` (cast, the 2:59 vs 3:00 columns, the 3:57:40 gantry, the 14:52 watch); later: main runner fair-skinned, ERN logo on every frame, and **4 full-screen cutaways rendered** (`motion/three-59/teded/out/cutaway-[1-4]-*.mp4`, 16 to 21 s each, timed to the script; where each goes: `motion/three-59/teded/README.md`).**

**22 Nov, the again series, two reels gated (Luke: "These are super fucking good!"):** (1) **'I LET MYSELF GO' / 10/10 HABITS TO / GET FIT AGAIN** (9/9), `2026-11-22-script-let-myself-go.md`, hook 41, script 325; (2) **STOP DREADING YOUR / FIRST RUN BACK / (10/10 NICHE HABITS)**, `2026-11-22-script-first-run-back.md`, hook 40, script 319; both ERN trial reels, Rory's shape (a marker per item, P240), one review each, fixes listed; FACTS "The restart"; cards `motion/again/`; comment START -> full list + first run by email. Luke to OK: the kitchen strength line (coaching). P240; check.py: 10/10 lists, `series: again` (up to 10 markers), `moment: training` (food allowed).

**21 Nov, two reels gated (Luke: "Yes write both scripts"):** (1) **'I DON'T NEED GELS' / KILLS 4-HOUR MARATHONS / (THE FIRST 2 HOURS LIE)** (KILLS red, 8/9), ERN trial reel (G32), `2026-11-21-script-no-gel.md`, hook 44, script 296, one review, G22 G29 fixed; card `motion/no-gel/no-gel-clock-16x9.png`. (2) The non-marathon slot (P234): **YOU'RE WASTING YOUR / PRE-RUN COFFEE / (ONE INSTANT? HALF A DOSE)** (WASTING red, 8/9), ERN trial, `2026-11-21-script-coffee.md`, hook 41, script 283, one review, G22 G23 G29 fixed; card `motion/coffee/coffee-dose-card-16x9.png`; FACTS "Caffeine before a run". P233 (no "only we could post it" test, scorecard out of 9, bar 8), P234 (one non-marathon topic in every set), P235 (send line at the end, card by 0:30; G19).

**21 Nov, 3:59 at ~15h + polls (`ideas/2026-11-21-3-59-review.md`):** 6,186 views (3,947 IG, 2,239 FB), skip 37.9% Higher, **24s**, saves 0.5%, shares 0.2%, 1 follow, 0 comments; above the typical line. The send line at ~0:44 lost almost half of who was left (32% to 18%; second time an ask in the body made a step) and the clock card came after it. Proposal for Luke: send line to the end (P204 change). Polls: ERN no gel 82% (9 of 11), personal peak at 30+ 56%. **Today: the no-gel reel as an ERN trial** (G32: the fourth hour was 6 days ago); titles `2026-11-21-titles-no-gel.md`. **Topic bank (P232):** `2026-11-20-titles-30-from-the-greats.md`, read first on every title request, TED-Ed shapes at the front.

**21 Nov reel gated (Lane A, first evergreen trial): WHY SO MANY / MARATHONERS FINISH / AT 3:59** (3:59 red, title only on screen; Luke chose it over the cold reviewer's 3/10, `luke_override: G12`), IG trial from ERN + TikTok, `ideas/engine-room-nutrition/2026-11-21-script-3-59.md`; Allen, Dechow, Pope and Wu 2017 (9.5M finishes, 51.4% more in the minute under 3:00, the speed-up from 40K); hook 44, script 286; one review, G21 G22 G29 fixed (no "felt empty" claims: the study measured times, not feelings); check.py PASS. Keep: the last 4K clock card (`motion/three-59/three-59-clock-card-16x9.png`, 38 to 41K for sub-3 to sub-4:30). **Hook rewritten to Luke's shape (P228, interest beats need off season):** "You'd think so many marathoners finish at 3:59 because they want sub-4, but there's a deeper reason", then 4:00 as the line between winning and losing (the paper's reference point, never "loss aversion"), stage 1 opens on the 50% fact and busts the pacer myth. The YOU WEREN'T EMPTY test is dropped (a race-moment title with no race coming); P227 (a title test changes the title only) stays as the rule for future tests.

**20 Nov, P225 (Luke): most viewers have no race, so evergreen first, specific close to the event.** Two lanes (`ideas/engine-room-nutrition/2026-11-20-evergreen-lane.md`): Lane A evergreen (identity like nerves of steel, or TED-Ed why / how that ends in something they use; trial first), Lane B events close to the date. G5 amended for Lane A; C8 partly settled. **Valencia moves to race week** (from about 30 Nov; the gated script and its 3 titles stay banked). Trial slate: `2026-11-20-titles-evergreen.md`.

**20 Nov reel gated: VALENCIA MARATHON / GELS START AT 16.2K / (AN HOUR TOO LATE)** (TOO LATE red, 7/10 cold review, Luke's yes 19 Nov in `ost_score_ok_by_luke:`), IG trial from ERN + TikTok, `ideas/engine-room-nutrition/2026-11-20-script-valencia-gels.md`; hook 42, script 314; one review, G21 G22 G29 fixed; check.py PASS. Cards `motion/valencia/` (title card, 9:16 overlay, the Valencia clock card from the stage 1 save line). check.py G10 now takes `ost_score_ok_by_luke:` for a title under 9 that Luke said yes to.

**Gut carousel posted 19 Nov 9:41am, first read (Windsor):** 429 views, reach 158, 1 like, 2 saves, 0 shares, 2.7 views a person; reach stalled (heavier carousel 1,380); 8.7h screenshots: 633 views (455 IG), 171 viewers, Feed 99.8% (never left followers), collab confirmed, 3.7 views a viewer; causes: it reads as an ad, a repeat topic; next carousel back to the plain white look (`ideas/2026-11-20-gut-carousel-review.md`).

**19 Nov, carousel drawn, waiting on Luke's OK for the repeat:** 'GELS MAKE ME SICK'? / 2 WEEKS CUT IT 60% / (YOUR MARATHON GUT PLAN) (SICK red, 8/10 cold review), 9 slides in ERN colours, `motion/carousel-gut/` (`ideas/engine-room-nutrition/2026-11-19-carousel-gut.md`); Costa 2017 and Miall 2018 in FACTS (Gut training). The watch carousel was killed by the reviewer (posted 5 times since 14 Oct). Last carousel (heavier): reach 1,362, saves 0.6%, about 2 views a person (aha at slide 6, the numbers only in the caption, 19 slides). ost_check: % now counts as a unit.

**19 Nov, saves deep dive (Luke: "look deeper on the saves"; `ideas/2026-11-19-saves-deep-dive.md`):** across 22 reels every one at 1.6%+ saves handed over numbers per goal time to carry into the race (hand plan 2.7%, wrist numbers 2.6%, NYC 2.6%, gel clock 2.0%); rules, rankings and stories 0.3% to 0.8%. **P224 / G34:** a `Keep:` field with 4+ numbers on screen per goal time, the save line names the act. **P223:** no medical-tent lines (G18 flags them).

**19 Nov, 30K reel at 16h (profile collab + FB, not a trial; Luke's screenshots):** 7,239 views (4,678 IG, 2,561 FB), **skip 29.5% Lower, 23s, 4 follows**, saves 0.6% and shares 0.1% Lower; second-best profile reel of November; half gone by 0:08, body held (no 0:45 step); saves low because the takeaway is short enough to remember (row 18), shares because the send line pointed at a friend's weakness. Next script: a clock or table to keep on screen, a send line that flatters the friend, a myth killed in line one. P222 (Luke): captions are barely read, never the diagnosis; read the post type off the insights before comparing (`ideas/2026-11-19-brain-30k-trial-review.md`). Oranges at ~40h: 2,468, skip 33.4%, 17.1s (missed the 2.8K to 3.6K forecast).

**18 Nov: YOUR BRAIN QUITS AT / 30K OF A MARATHON / (IT'S NOT WEAKNESS) gated** (`ideas/engine-room-nutrition/2026-11-18-script-brain-30k.md`, posted 18 Nov as a profile collab + FB, not a trial). Nybo 2003 read into FACTS ("The brain at 30K": 6 men, 5.2 to 2.9 mmol/L, effort felt harder; no "apathy" in the abstract); the 10 minutes is a decision rule, not a lab number. check.py: hook 40 to 45 words (P218) and captions 2,200 characters or fewer from 18 Nov. Graphics `motion/brain-30k/` (white card, 9:16 overlay, text-only cover). **Retitled before posting (Luke, 18 Nov, P220/P221): NEVER DECIDE TO WALK / AT 30K OF A MARATHON / (WAIT 10 MINUTES)**, NEVER red, the ost-reviewer's first pick of 14 (`2026-11-18-titles-brain-30k-v2*.md`); cards `motion/brain-30k/brain-30k-v2-*`; then rewritten for it (Luke: "go ahead and produce the script", his own 30K voice lines): line one says the title back, the turn by ~0:10, Cian's "3 things, each harder" from ~0:15 (1 OF 3 to 3 OF 3 (THE HARDEST) on screen); hook 43 words, script 302; one gate review, G22 (pace now matches the wall reel: 15 to 20 s/K slower) and G23 (no decision before 3:00 off the race time) fixed; check.py PASS. **Body pictures (18 Nov):** `motion/brain-30k/brain-30k-scene-[0-4]-*-16x9.png` (page `motion/brain-30k/scenes.html`, `?s=0..4`): the hill at the 30K sign, the 3 voice lines + fuel gauge (1 OF 3), the 2:50 gel (2 OF 3), 10 MIN no decision before 3:00 (3 OF 3 (THE HARDEST)), passing a walker at 38K with the 3:20 gel; cover `brain-30k-v2-cover-16x9.png` (text only).

**Tue 17 Nov, two reels gated (ideas chat, Luke: "the two posts for today and the scripts"):** (1) The walk reel is **killed** (Luke: "walk at 2.5K of what?"; he runs from the start, he doesn't walk). (2) Match reel repackaged after Luke's "last 15 of what? pros in what sport?": **SUNDAY LEAGUE LEGS DIE / AT 75 MINUTES / (EVEN IN THE PREMIER LEAGUE)** (10/10, DIE red; the bracket needs Luke's yes; Bradley 2009 Premier League fade in FACTS; new must-pass on the scorecard: every of what / in what / who answered on screen), IG trial reel from ERN only, `ideas/engine-room-nutrition/2026-11-17-script-match-last-15.md`, one review, 4 fixed; FACTS "Match day fuel, soccer" added (UEFA 2021 read from the full text; the Premier League under-eating line cut). Mockups `ideas/engine-room-nutrition/mockups/2026-11-17-*-frame-one.png`. Later 17 Nov (Luke: "the exact leagues"): the audio names the Danish fourth division (Krustrup) and the Premier League (Bradley 2009: about 20% less in every one of 5 positions, read from the abstract); only the fade was measured in the Premier League, not the empty fibres or the fixes; per-stage source tags on screen; frame one = the fourth-hour title card (no photo row); the graphics prompt for the gate chat is in chat. Then Luke picked the titles: **ORANGES WON'T SAVE / YOUR LEGS AT 75 MINS / (SUNDAY LEAGUE)** (WON'T red, 9/10) with **SUNDAY LEAGUE LEGS, / PREMIER LEAGUE FUEL / (STILL FLYING AT 85)** (FUEL red) as the second trial reel; white covers asked of the gate chat; stage cards unchanged. Final (Luke: no second opening, pick one): **A**, after the pre-mortem and council; send line 'whoever brings the oranges at half-time', pinned 'What does your team eat at half-time?'; B banked as a series name. Stage pictures (17 Nov, ideas chat, Luke asked): motion/match/match-scene-[0-4]-*-16x9.png (page motion/match/scenes.html): the empty 15, half the plate, 3-4H before kick-off, oranges crossed out for 30G, first to the ball at 85'; the text-only cover is match-a-title-16x9.png. **Posted as an IG trial 17 Nov 6:04pm; at ~2h 613 views, skip 27.8%, 14.2s, 3 shares, 1 save; the caption was cut at Instagram's 2,200 characters (the plan missing), rewritten at 1,774 for Luke to edit in; gate chat: add a caption-length check.** **At 12.5h (18 Nov): 2,308 views, skip 31.3%, 16s, 10 saves, 4 follows; half gone by 0:05, a step at ~0:45; Luke wrote his own opening; forecast 2.8K to 3.6K at 24h (`ideas/2026-11-18-oranges-trial-review.md`). Next: the 30K brain reel as a trial today, script prompt for the gate chat given in chat.** **18 Nov, P219 (Luke): one chat end to end; built `gate/ost_check.py` (fails every title Luke killed this week, passes the oranges and the fourth hour), the `ost-reviewer` agent, the `title-producer` skill and `motion/title-cards/make_title.js` (30K cards in `motion/brain-30k/`); the weekly loop needs Luke's OK to schedule.**

**17 Nov, YouTube long-form chat set up:** `youtube/README.md` (monthly calendar, links to podcast and emails); brief `youtube/2027-framework-brief.md`: OUR 2027 FRAMEWORK, Sun 3 Jan, 18 min, built on the tank (about 500 g runs short at about 3 hours): fill it (8 to 10 g/kg), spend it slower (first 10K), top it up (30 g every 30), check it (10K signs); cold open the 4:02 sub-4 finish; email reason a race page with their four numbers; waiting on Luke's 6 answers. Later 17 Nov: the Art O'Neill documentary (race Fri 15 Jan) takes February's slot, out Sun 31 Jan; shot list in the README; title rewritten without the job line (voice.md); Seville guide moved to reels. Then (P214, P215): documentary title 8 WEEKS TO BEAT 10:35 (A 62KM NIGHT RACE, WITH A FULL-TIME JOB): the goal is top 10 in his class (10:35:37 last year), never "top 10" alone; chapter 1 is the bet from podcast ep 1 (Fri 20 Nov) plus the Sat 21 Nov benchmark. P216: no crew, phone only and optional; the documentary is 10 to 12 min, mostly the podcast's bet and result episodes plus 4 phone clips; Jamie an equal co-host (framework: two parts each); Luke's questions cut to 3. Podcast every Sunday from 22 Nov, so long-form moves to Saturdays: framework Sat 2 Jan, documentary Sat 30 Jan, built on the episode 1 predictions replayed against the result episode (Sun 17 Jan). Podcast name: see the podcast plan (DEAD LEGS, poll vs ON FUMES, locked Fri 20 Nov); the bar is out of the framework video (an implied claim next to "faster than you deserve").

**Podcast name (18 Nov, council, plan 0.12): DEAD LEGS, running, sport and fuel, by Engine Room; story poll vs ON FUMES Wed to Thu (On Fumes only at 6 in 10+), lock Fri; segment Dead Leg of the Week** (earlier: On Fumes; The Race Plan rejected by Luke as generic, P217; FTYD kept as the Jan video title; "The Engine Room" is an existing endurance podcast). **Master podcast plan + episode template: Claude doc https://claude.ai/artifact/6LftEYohSrQKg6iTE96QpG.** **Fri 20 Nov: record podcast episode 1, THE BETS (v2, P216: equal co-hosts, both bets in the open, a one-page cue card, no crew; Luke Art O'Neill top 10 in class 10:35, Jamie Western Yards top 10; title 8 WEEKS OR 28; v3: four rounds (on the record, why you won't make it, 8 weeks or 28, myth or fact for points), listener-picked forfeit, season scoreboard)** (`podcast/2026-11-20-episode-1-run-of-show.md`); **out Sunday 22 Nov, then weekly on Sundays; the result episode Sun 17 Jan.** Art O'Neill 62km, Fri 15 Jan, target settled: top 10 in the Ultra - Male class, 10:35:37 last year (say "in my class"); Jamie's copy of the run of show is a Claude doc (https://claude.ai/artifact/EW9WBoUzRLxujMCSU7U9a4); Norn Iron 100 29 to 30 May (~106 miles); Western Yards listed 5 June (to confirm). P214 look it up yourself; P215 jobs fine, no "better at work". **17 Nov, podcast challenge (dates, plan 0.8):** season 1 TOP 10 BY 15 JANUARY, Luke's Art O'Neill (Fri 15 Jan 2027, ranked), 8 episodes 9 Dec to the result 20 Jan; season 2 MAY HEAD TO HEAD, Luke's Norn Iron 100 and Jamie's Western Yards Backyard; record Luke's bet + a benchmark run this week; need last year's 10th-place time; your race is the story, their marathon the lesson (plan 0.7; race facts unconfirmed in FACTS). Chats (Luke, 17 Nov): "Podcast - Riverside" does `podcast/`; a new "YouTube long-form" chat does `youtube/` (monthly videos, first the 2027 framework); reels chats unchanged (`podcast/README.md`). P213: do it, don't tell Luke how. **17 Nov, podcast v2 (P212, Luke: a show we enjoy; long-form separate):** plan section 0: 25 to 30 minutes, fixed first minute, loose chat under chapters, quick-fire clip section, Luke vs Jamie spring rivalry; long-form monthly from early Jan, first the 2027 FRAMEWORK video, uncut, own email reason. v1: `podcast/2026-11-17-podcast-plan.md`. 20 to 25 minutes, one searchable question, 7 fixed parts starting from a real runner in the inbox (the ~200 plans are the authority, not our times); Luke the numbers, Jamie the listener's voice; season 1 ROAD TO SPRING, 10 episodes from Wed 9 Dec (3 at once) to Seville; it is the long-form YouTube for season 1; clips to TikTok, Shorts and IG trial reels, the best rewritten as a gated profile reel; the bar from January via the Lab, within UK/EU claims rules; episode 0 unpublished the week of 23 Nov. Waiting on Luke's 6 answers (rooms, spring races, Jamie, samples, email day, was the Dublin episode recorded).

**16 Nov, match reel brief: SUNDAY LEAGUE LEGS DIE / IN THE LAST 15 / (SO DO THE PROS)** (10/10, DIE in red; soccer only; A/B YOUR LEGS AREN'T GONE / IN THE LAST 15. / THEY'RE EMPTY., 9/10; Mohr 2003, Krustrup 2006, Balsom 1999, Harper 2017, Anderson 2017, Wenger's Mars bars; IG trial Sat 21 Nov 7am; needs Luke's yes and the grams in FACTS; `ideas/engine-room-nutrition/2026-11-16-brief-match-last-15.md`). **17 Nov: match reel graphics** (SUNDAY LEAGUE LEGS DIE / AT 75 MINUTES / (EVEN IN THE PREMIER LEAGUE)): title cards white and navy, 2 and 3 lines, 9:16 overlays, cover (drawn pitch scene), stage cards with source lines, all in `motion/match/`.

**16 Nov: the heavier carousel posted.** **Tue 17 Nov: ULTRARUNNERS WALK / ON PURPOSE. / MARATHONERS WALK AT 32K** (10/10, AT 32K in red; Hottenrott 2016 run/walk study; `ideas/engine-room-nutrition/2026-11-16-brief-walk-on-purpose.md`). Luke: post something tomorrow; the shoes script stays unposted. Three ideas killed on 16 Nov: the water reel (contradicts our gel-with-water advice), FINISHER → RACER → HUNTER (sorts and blames the viewer), £250 SHOES MAKE SOME... (a known debate; SOME lets everyone out; the study measured economy, not race times; the payoff blames pacing, not shoes). The five levers under every winner and the tightened scorecard: `ideas/engine-room-nutrition/2026-11-16-premortem-psychology.md`. Next filmed reel Wed or Thu, built from the levers first. 5 TACTICS to April.

**Posted 15 Nov 7:43pm: 4-HOUR MARATHONS DIE / IN HOUR 4 / (EVEN THE FIT ONES).** **Day 2 via Windsor (17 Nov, IG only): 18,023 views, skip 26.9%, 31.6s, 277 saves, 75 shares.** Windsor.ai for Social Media is connected (ERN Instagram only; TikTok not being added for now, Luke 17 Nov, so TikTok numbers stay as screenshots): Claude pulls per-reel views, reach, skip, watch time, saves, shares; the curve, sources and follows still need screenshots. At ~12h: IG + FB **14,995 (8,724 IG, 6,271 FB), skip 27.0%, 29s, saves 1.7%, shares 0.4%, likes 1.5%**, still climbing; TikTok 3,812, 14.9s, **8 follows**. Our best since September. Frame one on the brief for the first time in five posts (white title card full width, DIE in red, Luke alone, eyes on the lens): skip 60.5% (wall) to 27.0% in the same week. Luke's line one killed the 90-minute myth with proof. The evening rule was wrong (P144 already said time doesn't predict views). Template: this frame one; the myth killed first; the fuel lane with new twists. `ideas/2026-11-16-fourth-hour-review.md`.

**Posted 13 Nov 6:20pm (not Fri 7am): THE MARATHON WALL / HITS YOU IN 5 STAGES / (EACH ONE MORE BRUTAL).** At ~43h: IG + FB **2,002 (1,278 IG, 724 FB), skip 60.5% (our worst ever), 15s, saves 1.1% (best since 6 Nov), shares 0, 0 follows**; body flat at ~20% from 0:10 to 1:20; TikTok 954, 11.9s, 2 follows. Frame one: the title squeezed into the left half of a dark 16:9 card beside a finish-line photo (rows 33, 22, 4 repeated two days after row 33; fourth post running off the brief). Fixes: frame one delivered as a finished 9:16 overlay PNG; no post without the 0:00 screenshot matched; 7am; the wall off the profile until January (trial reels only). `ideas/2026-11-15-wall-5-stages-review.md`.

**Posted 11 Nov 8:47pm: THE 10% MILEAGE RULE / FAILED ITS ONLY TRIAL.** ERN TikTok at ~14h: 489 views, **13.6s, 3.05% full, 3 follows** (the body beat our last four), 2 saves, 0 shares, **most left at 0:01**. Frame one: a small mid-blue title on Luke's chest plus a cartoon runner from 0:00 (row 22, third post running); the title had no "you" and no feeling word. IG + FB at ~13.5h: **7,238 views (2,260 IG, 4,978 FB), skip 41.1% Lower (best of the last four), 16s, saves 0.4%, shares 0.1%, 0 follows, Reels tab top source**; flat overnight after 2h (evening posts 2 for 2); a step down at 0:38 to 0:45 at the CTA (row 9 repeat); the send line at 1:26 reached ~3%. Forecast 9K to 12K. Fixes: CTA to the end or the pinned comment, send line after the worked example, save after the first keepable number, 7am (`ideas/2026-11-12-10-percent-rule-review.md`). New title spec and feeling devices: `ideas/engine-room-nutrition/2026-11-12-feel-something-osts.md`. Fri: THE 5 STAGES OF THE / MARATHON WALL / (EACH ONE MORE BRUTAL). New ledger cause for the gate chat: a title you can't read in one second.

**16 Nov: £250 SHOES MAKE SOME / 4-HOUR RUNNERS SLOWER / (I PASSED THEM IN DUBLIN) ready to film** (`ideas/engine-room-nutrition/2026-11-16-script-super-shoes.md`, Tue 17 Nov 7am). One review: G21, G22, G23, G29 fixed. Joubert 2023 confirmed (a third used more energy at 10 km/h); a newer study the brief didn't have (Bolliger 2026) found about 2.4% saved at 10.5 km/h, so the audio says both. Luke to OK: what he wore in Dublin, £250, the returns line. Title card `ideas/engine-room-nutrition/overlays/2026-11-17-super-shoes-title-16x9.jpg` (template page `motion/title-cards/title-16x9.html`). FINISHER → RACER → HUNTER is dead.

**16 Nov: heavier carousel drawn** (`ideas/engine-room-nutrition/2026-11-16-carousel-heavier.md`): GAIN 1.5KG BEFORE / YOUR MARATHON / (OR RUN SLOWER) (cover v3, 10/10; v1 answered the quiz, v2 scored 7), weights 70kg to 71.5kg, 19 slides, waist-up close-ups, `motion/carousel-heavier/tiktok-3x4/` (TikTok tonight) and `instagram-4x5/` (Wed or Thu if over half the photos are viewed); caption, pinned comment, FACTS "Carb loading and the scales"; P211 (carousels: one beat a slide, the look). Fourth hour at 12h: 15K, skip 27.0%, 29s; its frame one is the template.

**16:9 rule for graphics (Luke 13 Nov):** every cover, card and picture Luke pastes above the video is 1920 x 1080 (YouTube thumbnail shape): `motion/covers/*-cover-16x9.png`, `motion/wall-cards/16x9/`, `motion/hour4-cards/16x9/`; scenes are already 16:9.

**Fourth hour graphics (13 Nov):** text cards `motion/hour4-cards/hour4-card-*.png` (DIE in red), scenes `motion/hour4-cards/hour4-[0-5]-*.png` (page `motion/hour4-scenes.html`), cover `motion/covers/hour4-cover.png` (empty fuel gauge over a runner); web image links in chat.

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

**Two chats (Luke, 5 Nov, P191; RETIRED 18 Nov by P219: one chat does everything):** this chat writes scripts and owns GATE.md
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
