---
type: system
section: the gate (P190)
status: v0.9, PROVISIONAL. Every [C#] line uses my recommendation on a contradiction Luke hasn't settled yet. When he answers, those lines change and this becomes v1.
updated_at: 2026-11-04
checker: gate/check.py (the AUTO tests)
reviewer: .claude/agents/gate-reviewer.md (the REVIEWER tests)
mockup: gate/frame.html + gate/shoot_frame.js (G15)
---

# GATE.md: 33 tests every script passes before Luke sees it

Luke, 4 Nov: "Every video has to pass every principle we've learnt BEFORE I
see it." This file replaces the self-graded ledger table, the 151-line
checklist audit and the five-line topic gate as the thing a script has to
pass (P190). They stay as the evidence; this is the test.

**How it runs, in this order. One FAIL anywhere and the script doesn't go to Luke.**
1. `python3 gate/check.py <script file>` runs every AUTO test. The git
   pre-commit hook and the Claude Code hooks run it too, so a failing script
   can't be committed, and the session can't end quietly on one.
2. `python3 gate/check.py --packet <script>` builds one review packet (the
   tests to grade, Luke's decisions, the script, the last 3 hook stacks, every
   script's title and line one, the ledger, FACTS: about 11K tokens). Then an
   independent reviewer agent (`.claude/agents/gate-reviewer.md`, run
   cold, no access to my reasoning) reads only that packet and the phone frame,
   grades every REVIEWER test (on a re-review: every FAIL, every PASS whose
   quoted line changed, and G13, G16, G18 always; the rest carry over), quotes the
   line for each verdict, and writes `gate/reviews/<script>.md` stamped with
   a hash of the script. Edit the script after the review and the hash
   breaks: the review has to run again.
3. I fix every FAIL. I don't overrule the reviewer. If a FAIL needs a fact
   or a decision only Luke has, the script goes to him as "blocked on X",
   never as ready. In the file: `gate: blocked` and `blocked_on: G8 (why)`.
   The checker accepts that only for a REVIEWER test whose row in the
   independent review says it needs Luke; an AUTO fail can never be held.
   A blocked script can be committed (so the work isn't lost) but always
   reports "NOT ready to film".
4. The opening frame is mocked up at phone size (G15) and Luke sees it
   before filming.

## One review (Luke, 10 Nov: "too many turns and levels of review")

Six reviewer runs on one ranking (50,000 to 70,000 tokens each) cost more than
the problems they caught. So:

1. **The idea is checked once, on the brief.** Repeats (G8), premises (G9),
   the gap (G16) and the turn (G31) are settled when Luke says yes to the
   brief; the script's front matter says `brief_ok: Luke <date>` and the
   reviewer doesn't grade them again. No brief OK'd: they're graded with the
   rest, in the same pass.
2. **One reviewer pass per script, on the words:** G2 (frame one), G12
   (actions with numbers), G21 (the caption plan), G22 (facts), G23 (safety
   mid-race), G29 (repeats and AI tells), plus G32 for a sequel. About a
   minute and 25,000 tokens.
3. **No second round.** The author fixes every FAIL and lists them in the
   front matter (`fixed_after_review: G22, G29`); check.py re-runs the AUTO
   tests. The review stays valid for that version.
4. **Luke's call ends it.** `luke_override: <date> "<his words>"` accepts what's
   left, shown as such; a FAIL that needs his fact or decision is "blocked on X"
   with the exact question.
5. **The judgement tests (G4, G5, G7, G11, G13, G14, G17, G18, G20, G24)** are
   the author's checklist, not graded: anything that fails goes in one line in
   the script's "Known risks" box.
Every AUTO test still blocks. Posted reels are reviewed against the box first.

**Order of tests:** the first 3 seconds (P189) first, because that's where
80% of the 16 results viewers went. Then topic, title, frame, hook, body,
words, proof.

Tags: **AUTO** = the checker decides. **REVIEWER** = the independent agent
decides, quoting the line. **BOTH** = the checker catches the mechanical
part, the reviewer the rest.

---

## 0. The first 3 seconds (P189): checked on the real frame before filming

### G1 · The first words are the viewer · AUTO
**Test:** The first spoken word isn't "we", "I", "our" or "my", and "you"
or "your" is in the first 8 words. Or line one opens with a short question naming the viewer in their own words ("Full-time job, a family, and a spring marathon booked?", P197). The gate names the viewer's event and is
true for them now. [C1] Default for a marathon video: "If you've got a
marathon coming up,"; a named race when the title names it ("If you're
running Valencia,"); another sport names theirs.
**Evidence:** 16 results opened "We've sent over 200 free marathon plans":
44.4% skip, 80% gone by 0:05. The email reel opened on the viewer ("If you
have a marathon or any race coming up"): 33.3%.
**Passes:** "If you've got a marathon coming up, there are 10 words to say to yourself from the start line to 40K."
**From:** P189, P158, P30, P153, P103, P141, P38

### G2 · One thing to read for 3 seconds · BOTH
**Test:** From 0:00 to 0:03 the only words on screen are the title. Luke
and the title, plus at most one picture with no words in it (a runner, an
unlabelled map, a watch face). No subtitles, message bubbles, labels,
lists, tiles or strips before 0:03. [C9]
**Evidence:** Frame-one clutter tracks skip: one number (goal gone) 31.9%;
a sentence and a clock (sleep) 41.4%; a bubble, title and subtitles (16
results) 44.4%; a dashboard (last marathon) 52.4%.
**Passes:** Luke in the car, the blue title boxes, nothing else; subtitles start at 0:03.
**From:** P189, P159, P147, P151, P89

### G3 · The question lands inside about 10 words · AUTO
**Test:** The file declares the gap phrase (the thing they'll wait for).
It appears in the first 12 spoken words.
**Evidence:** 16 results said "10 words" at word 20 (about 0:06), after most
had gone; the match reel's 21-word line one lost them between 0:03 and 0:15.
**Passes:** "If you've got a marathon coming up, there are **10 words**..." (words 10 and 11).
**From:** P189, P62, P38

### G4 · The title is their goal, with a number · BOTH
**Test:** The title has a numeral (AUTO) and reads as something the viewer
wants for their own race, not our result. Our proof goes inside the video
(REVIEWER).
**Evidence:** 16 MARATHON RESULTS (our score) 44.4% skip. Luke on the
first-timer: "How a first-timer broke 3:30" becomes "How to break 4 hours
in your first marathon".
**Passes:** HOW TO BREAK 4 HOURS / IN YOUR FIRST MARATHON
**From:** P189, P181, P158, P30, P92, P185

---

## A. Topic: would they stop?

### G5 · A stake they have now · REVIEWER
**Test:** The viewer faces it within about 4 weeks (their race, their
match, Saturday's 5K, Black Friday), or the video shows a Briar-sized
result only we have (real numbers from our inbox or Luke's and Jamie's
races, with consent). And it passes "who cares": a fear they carry, a
picture of race day they want, or a number they'll use. Trivia and admin
fail whatever the date. [C8]
**Evidence:** Long run (no deadline) 55.5% skip, our worst; every top-5 reel
went up 1 to 4 weeks before the viewers' races and grew for weeks (7 days
31K to 151K); Luke stopped only for Valencia ("studying for an exam 4
months away").
**Passes:** WHERE THE VALENCIA / MARATHON IS LOST, posted 15 to 22 Nov.
**From:** P179, P181, P165, P178, P174, P166, P173, P70, P74, P92, P16, P1, P7, P9, P54, P29

### G6 · The event is the title; the body worry goes inside · REVIEWER
**Test:** The subject is a race or match moment, a race fear, a race-pace
decision, or a countdown with an action per stage. Fuel is a title only
when the body is a full schedule. Never the gut, sleep, kit or pre-race
feelings as the subject; nothing after the finish line.
**Evidence:** Fuel titles without a schedule 1.6K to 6.5K; stomach 4.1K;
sleep 1.0% saves; cold kit 0.9%; taper 43.1% skip; heavy legs 0.5% saves.
Carb load with a meal schedule: 95K, our #3.
**Passes:** HOW TO ACTUALLY CARB-LOAD / FOR A MARATHON with every meal, time and gram.
**From:** P101, P109, P117, P78, P80, P121, P57, P44, P46, P34

### G7 · Every viewer is in every stage, as the hero · REVIEWER
**Test:** Most of the audience has this problem (Family Feud: out of 100,
how many?). The stages are a sequence every viewer lives through, never
groups of runners. The viewer's before (pain) and after (dream) carry it;
Luke and Jamie are guides. A narrow topic says who it's for in the gate.
**Evidence:** Who hits the wall sorted runners into 4 groups: saves 2.8% to
0.7%. Gel struggles: "most don't have this problem", 5.8K. The founder
story: 44.1% skip, 0 saves.
**Passes:** 0-10K / 10-20K / 20-30K / 30K-FINISH (the wall, 184K).
**From:** P103, P158, P30, P141, P76, P3, P45, P48

### G8 · New, and not a repeat · REVIEWER
**Test:** Name the belief the viewer holds now and what they'll learn that a
PE teacher, physio or club coach wouldn't say. It isn't a reel we've
already posted, renamed: search every script in ideas/engine-room-nutrition/
for the same method and numbers, not just the last 3 (gate run 3: idea #9
was the 14 Oct sub-4 reel with a new hook). It doesn't reopen a number the comments argued with. It has
one aha that solves their actual complaint.
**Evidence:** Match v1 ported our race-morning clock (Luke: "nothing new or
novel"); the long run told them "run easy" (55.5%); "eleven gels" drew 25
comments, nearly all against it.
**Passes:** "The wall starts in the first 10K" (the cause somewhere they'd never look).
**From:** P175, P94, P119, P124, P140, P81, P31, P10, P2, P67, P72, P75

### G9 · Every premise checked, nobody exposed · REVIEWER
**Test:** Every habit the script assumes of the viewer comes from our data
(inbox, comments, stories, `research/`) or Luke. Every fact about Luke or
Jamie is one they've said. No viewer is identifiable unless they asked to
be, with a story they're proud of.
**Evidence:** Orange slices (most teams don't have them), 6am runs (most run
in the evening), "60K in Connemara" (Luke didn't run it), all caught by
Luke on 4 Nov. The email reel was anonymised at Luke's call.
**Passes:** "One runner we wrote a plan for" (no name, no time, consent asked).
**From:** P183, P23, P49, P40, P24, P172, P39, P59, P20

---

## B. The title (OST)

### G10 · Two short lines, plain words · AUTO
**Test:** Two lines, each 22 characters or fewer, 40 at most in total.
No jargon (taper, zone, heart rate, threshold, tempo, cadence), no gimmick
words (hacks, cheat code, maxxing, like you're 10), no dated words. Markers
22 characters or fewer, one line each. [C5] [C6]
**Evidence:** A MARATHON RUNNER EMAILED US / AFTER HITTING THE WALL AT 30K
(28 + 29) ran to nearly 4 lines; the wall is 23 + 15. "Taper" in a title:
43.1%. HEEL LOCK's hack views didn't turn into followers (1.1M on 1,684).
**Passes:** WHERE THE MARATHON / WALL ACTUALLY STARTS (18 + 22)
**From:** P170, P89, P116, P167, P47, P61, P58, P15

**From 13 Nov (P210, Luke):** the Gate fields carry `OST score: N/10` from `ideas/engine-room-nutrition/OST-SCORECARD.md`; under 9 fails.

### G11 · "In what?", and two of five · REVIEWER
**Test:** Read cold, the title names the race, event or object in words
people already say, and a non-runner gets it in one read. It carries at
least two of: a specific number or named race; a deadline they have now; a
constraint on their life; proof from our own work; a method that's ours,
named. Exact numbers, not rounded. [C7]
**Evidence:** WHY YOU'RE GONE / AT 70 MINUTES: "in what? A concert, a
park?" HOW HARD YOUR LONG RUN / SHOULD FEEL (no number, no deadline):
55.5%.
**Passes:** WHERE THE VALENCIA / MARATHON IS LOST (named race + deadline + the wall's shape)
**From:** P180, P178, P185, P184, P92, P37, P58, P21, P32, P73, P5, P25

### G12 · It never answers itself, and its numbers don't read as failure · REVIEWER
**Test:** Screenshot the title and frame one: could someone skip the video
and lose nothing? If yes, fail. Divide every number on screen by the
biggest number next to it: if that rate reads as failure, change the base.
**Evidence:** HOW MANY GELS... (IT'S ABOUT 10): 42.9% skip, our worst then.
"200 plans, 10 PBs" reads as 5% (Luke caught it before filming).
**Passes:** WHERE THE MARATHON / WALL ACTUALLY STARTS (asks, withholds)
**From:** P80, P187, P77, P97, P63

---

## C. Frame one and the cover

### G13 · Each layer says something new · BOTH
**Test:** The file has one line each for the title, the picture and line
one, and what each adds. No layer repeats another's words or numbers
(AUTO for numbers); together they don't hand over the answer (REVIEWER).
**Evidence:** The 16 / 10 / 2 scoreboard sat under 16 MARATHON RESULTS / 10
PBs, 2 MISSES: "the exact same thing... we're wasting space" (Luke).
**Passes:** Title = the claim; picture = a runner in trouble at 30K; line one = the gap.
**From:** P188, P91

### G14 · The picture shows their problem, place or moment · REVIEWER
**Test:** One real image (or none), colour, present day: the viewer's
problem, place or moment. Never a crowd, a start or finish, a product, food,
someone else's win, AI, vintage, a collage, a face or a name bib. A new
picture every video. Any number on it is in the title or line one. Free
licence, credited. [C12]
**Evidence:** Runner in trouble 25.5%; one runner at a drink station 37.0%
against a start crowd 48.9% (same series); AI covers 39.3% and 46.7%, the
first real cover after them 35.1%; a reused splits graphic 38.1%.
**Passes:** One runner bent double on a road, face turned away.
**From:** P93, P104, P116, P151, P160, P161, P84, P80, P79, P28

### G15 · The opening frame is mocked up at phone size · AUTO
**Test:** The file points to a 1080 x 1920 PNG of frame one, with
Instagram's caption and button zones marked, and a phone-size preview next
to it. Luke sees it before he films.
**Evidence:** The last-marathon frame was never looked at on a phone: 52.4%.
The 16 results frame passed a 29-row self-check and broke 3 rules in its
first second.
**Passes:** `ideas/engine-room-nutrition/mockups/<script>-frame-one.png`
**From:** P189, P160, P159, P89

---

## D. The hook stack

### G16 · The gap · BOTH
**Test:** The file states what the viewer is waiting for, the line that
holds it shut, and the stage that closes it (AUTO: the fields exist and the
closing stage is one of the markers). Line one, read alone, leaves one
specific question a stranger would ask; it's
about them, not a stranger's result; nothing before the closing stage gives
it away, including the named concept; the rehook reopens it before the last
stage (REVIEWER). [C2]
**Evidence:** Without the wall named the hidden wall and held it to stage 4:
39s watched on 1:37, our record. Taper v2, wall v1, enjoy v1 and 200 plans
v1 all gave it away or left no gap (Luke caught each).
**Passes:** "...and when that happens, the gels were never the problem." (what was, then?)
**From:** P176, P186, P149, P112, P120, P41, P12, P38, P71, P11

### G17 · Line one is a picture they'd argue with · REVIEWER
**Test:** You could photograph line one (a watch, a scale, a K marker, a
lamppost). Most runners would disagree with it or do the opposite, and
can't guess why or what answers it (a tip fails). A runner in the start pen wouldn't say
"obviously". It's in the method's own unit (clock or distance).
**Evidence:** "It all comes down to what you cut" (taper): 43.1%. "You should
weigh more on race morning": 34.3%. "Your first K should be the slowest K of
your whole race": 32.4%. 3:30 v1 "run quicker than 3:30 pace" (Luke:
obvious).
**Passes:** "Your first K should be the slowest K of your whole race."
**From:** P116, P120, P130, P87, P94, P139, P53, P177, P60

### G18 · Pain and dream built new · BOTH
**Test:** Pain = the cost, with the feeling or the cruel timing, at the top
of what's plausible; never the cause. Dream = what they'll see on their own
race. Both are things runners have actually described, set where nearly
every viewer has been. The shape isn't one the last 3 scripts used (the
stack table has a "last 3 used" column). AUTO: no "get it wrong / get it
right", "you're the one who", "that's your race going to plan".
**Evidence:** "Get it wrong / get it right" came back in 5 scripts after
being retired (Luke, 17 Oct and 4 Nov: "every single time"). Gels "smell"
(they don't).
**Passes:** Pain: "4 months of training comes down to one morning, and you find out at 32K as the 4-hour flag goes." Dream: "at 40K your watch shows a split quicker than your first."
**From:** P186, P64, P71, P135, P142, P63, P52, P24

### G19 · The hook is short and the CTA comes early · AUTO
**Test:** The whole script is 280 to 330 spoken words and the finished
cut 1:35 or less. Hook (everything before the first marker) 40 to 55
words, about 15 seconds (P198, Luke 11 Nov; was 80 to 95), in this order:
line one (the viewer and the gap), one sentence that does pain and dream
together, the named concept with "save this". The turn goes inside line one
or stage 1, never its own paragraph. The CTA is one sentence offering the free plan,
straight after stage 1, starting within the first 150 spoken words (about
0:45). The audio says who to send it to. [C3] [C4] [C10]
**From 12 Nov (P204, Luke, the 10% rule data):** no email ask in the body: the last
spoken line or the pinned comment only (the ask at 0:38 lost half the viewers left).
"Save this" goes straight after stage 1's action, not in the hook. The send line
goes straight after stage 2 (about 0:45; the 10% send line at 1:26 reached about 3%).
A title can run 3 lines only as Luke's final title (`ost_final_by_luke:`).
**Evidence:** Sleep's 116-word hook pushed the CTA to 0:49, where half of
those left went. 3:45 moved the CTA a third of the way in: "an awful lot"
of emails. Dublin km by km, sent to running partners: 1.8% shares.
**Passes:** "If you want your own, email us your race and goal time through the link in the bio."
**From:** P147, P128, P156, P145, P97, P69, P85, P70, P66

---

### G31 · The turn: what changed, before the method · BOTH
**Test:** Before the first stage marker, one spoken line shows the moment
something changed: what the viewer was doing wrong, or what they (or Luke)
realised, said as a moment they can picture, not a rule. It must be
something the viewer **didn't already believe**: read it to a runner of this
goal; if they'd nod along, there's no turn. It can be line one itself. It
shows what was wrong, never the fix the closing stage pays (G16 still holds:
the sub-4 turn was "sub-4 pace on your watch can still get you a 4:02"; the
reason, the watch reading long, stayed in the last stage). AUTO: the Gate
fields name it ("Turn:" with the line in quotes), the line is spoken before
the first marker, and the file has "## The 4 questions" with all 4 answered.
**Evidence:** Sub-4 (secretly) had a turn (the pace on your watch lies): 23s
watched, 2.3% saves. Parkrun had the method with no turn ("don't sprint,
spread it out", which they already believed): 14s, 0.2% saves. 16 results
had neither a moment nor a turn: 44.4% skip.
**Passes:** "If that's secretly you, sub-4 pace on your watch can still get you a 4:02."
**Fails:** "Most runners go off too fast." (They'd nod along.)
**From:** P194 (Luke 9 Nov, the 4-step story), P175, P186

---

### G32 · A profile sequel is a new reel · BOTH
**Test:** A script with `sequel_of:` (a sequel of a posted reel) either goes
out as a **trial reel** (strangers, so a one-change test is allowed), or, on
the profile, has a **new twist** in the title, a **new line-one shape** and a
**new frame-one picture**, and posts **at least 7 days after the parent**.
AUTO: if the format isn't a trial, the front matter has `parent_posted:` and
`post_date:` (YYYY-MM-DD) at least 7 days apart. REVIEWER: the title twist,
line one's shape and the frame-one picture are each new against the parent.
A script that isn't a sequel passes.
**Evidence:** Sub-4:30 (secretly), 9 Nov: the parent's twist, line one and
method with the goal changed, on the profile 3 days later: skip 51.3%, 10s
watched against the parent's 23s, reach stopped at followers (Feed top
source). One post (P174), but the mechanism is plain: followers had seen it.
**Passes:** a sequel as a trial reel; or a profile sequel 7+ days on with a new twist, line one and picture.
**From:** P195 (Luke 10 Nov), ledger row 31, C21

---


### G33 · One line they'd repeat · AUTO (from 12 Nov)
**Test:** The Gate fields carry `Repeat line:`, one contrast pair a runner would
say on a club run ("tired isn't injured"), and it's spoken word for word.
**Evidence:** every captivating script in Luke's pack has one ("You respond when
you are ready, not when you are triggered"); P200's "one line they'd repeat"
was in the rules but nothing checked it.
**From:** P206, P200
**60-second trial (P208):** with `trial_format: 60s` (trial reels only), G19 takes a
20 to 30 word hook and 140 to 190 spoken words.

## E. The body

### G20 · Stages on one clock, each ending on an action · BOTH
**Test:** 3 to 5 stages (AUTO), in time order on one clock, each a scene
they'll live, opening on the unexpected and ending on something they can do
on the day with a number. No "why" stage after the method; the why is one
line inside the payoff. The biggest reveal is last (REVIEWER).
**Evidence:** Heavy legs was a list of symptoms on no clock: 0.5% saves.
Goal gone's "why" stage at 1:13 lost half of who was left. The wall: 4
clock stages, 184K.
**Passes:** 0-10K: PAY THE SPEED TAX / ... each ending "between 5:45 and 5:50".
**From:** P98, P117, P109, P145, P177, P95, P69, P111, P41

### G21 · Something too long to remember, for a goal most have · BOTH
**Test:** One thing they can't hold after one watch: a schedule with times
and amounts, a table by goal, or a K-by-K plan, with the full table in the
caption. The worked example is a goal most viewers have (sub-4, 3:45 to
4:00) or every common goal is in the caption (AUTO: worked-example field;
caption present; paces in miles too). Schedules say the meal and a.m./p.m.
**Evidence:** Carb load's schedule 4.4% saves, 7 days 3.0%; enjoy's four
easy actions 1.2%; the email reel's 3:23 plan 0.4%.
**Passes:** Sub-4 in the audio; 3:45, 4:00 and 4:30 in the caption, km and miles.
**From:** P152, P127, P115, P121, P123, P129, P91, P84, P102

### G22 · Every fact traced, and the same as before · BOTH
**Test:** A facts table in the file: every number and practical claim
traced to FACTS.md or an earlier script; anything untraced is cut or
marked "Luke to OK" (listed for him, never hidden). AUTO: gel size matches
its interval (30g every 30 min, 40g every 40, 20-25g every 20), no total gel
count, no real food in the race. Fuel in grams an hour first.
**Evidence:** Gel v6 said 20-25g when the baseline was 30g (Luke: "how can I
ensure you remember"); "eleven gels" with no gel size; the 200 plans v2 to
v4 sub-4 first-10K band was goal pace, not 5-10 s/K slower.
**Passes:** "a 30 gram gel at 20 minutes. Then one every 30, with a few sips of water."
**From:** P138, P137, P118, P124, P134, P39, P99, P105, P81

### G23 · Something they'd actually do · BOTH
**Test:** Every action uses what this audience owns and does (one flavour
of gel, jelly sweets, station water and sports drink, the watch on their
wrist), Luke would do it himself, it adds no new worry, and there's no setup
step (alerts, apps). AUTO flags: arm sleeves, bin bags, soft flasks, watch
alerts, apps, pickle juice, bananas, pretzels.
**Evidence:** Arm sleeves ("nobody wears them"); queue twice for the
portaloo ("a bit mad"); set your watch to beep ("I don't even know how to do
that"); pickle juice ("few, if any").
**Passes:** "One lamppost at a time."
**From:** P126, P133, P146, P137, P98

---

## F. The words

### G24 · Said like a friend on a run · BOTH
**Test:** AUTO: no sentence over 22 words; the median under 15; no jargon or
method names (zone, threshold, glycogen, protocol, strategy, optimal,
negative split). REVIEWER: read aloud, understood literally the first time,
no riddle or euphemism, every cue measurable.
**Evidence:** Stomach v5: "Get this right and you run past every queue"
read three ways; "effort you could talk at" was coach-speak; "full
sentences: how long is a sentence?"
**Passes:** "Down to 5 before halfway, you've gone too fast."
**From:** P157, P108, P115, P50, P55, P19

### G25 · No maths · AUTO
**Test:** No multipliers, "plus X", percentages or formulas in the audio. At
most 2 numbers in a sentence, where a 5-second band counts as one and a K
marker doesn't count. [C20] Anything worked out happens the night before,
written on the wrist.
**Evidence:** Goal gone ("your A goal times 0.59") and the 3:45 GPS line:
viewers called the maths complicated (Luke, 27 Oct).
**Passes:** "For a sub-4, that's between 5:45 and 5:50 for the first 10K."
**From:** P155, P143, P62, P84

### G26 · Numbers the way their watch shows them · AUTO
**Test:** Numerals for every number (no "thirty", "four"). Paces as 5-second
bands ending in 0 or 5 ("between 4:50 and 4:55"). Every pace in the caption
in km and miles.
**Evidence:** Luke, 20 Oct: written-out numbers slow the teleprompter;
Garmin live pace moves in 5-second steps; a UK inbox asked for miles.
**Passes:** "between 5:45 and 5:50" (caption: 9:15 to 9:23 a mile).
**From:** P131, P132, P129

### G27 · No statistics, studies, names or medicine · AUTO
**Test:** No percentages or "how many people" about runners in general, no
"study", "research", "experts", no named athletes, coaches, creators or
brands, no medication. Our own counts as proof, said once with the true
base, are allowed. [C11] Race names are fine.
**Evidence:** "Who hits the wall" (four million results, three research
lines) 3.4K; the two biggest videos named nobody and cited nothing.
**Passes:** "16 have raced so far and messaged back."
**From:** P107, P105, P113, P106, P118

### G28 · Nothing that dates · AUTO
**Test:** No "this weekend", "tomorrow", "tonight", "this Sunday", "this
spring" or a season months away in the audio or the title. Dates live in
the caption.
**Evidence:** Enjoy's gate said "this weekend": 1.2 times day one at 2.7
days against our usual 1.6 to 2.1. "This spring" ran 52.1% (one post).
**Passes:** "If you've got a marathon coming up,"
**From:** P153, P82, P68

### G29 · No AI tells, no second meanings · BOTH
**Test:** AUTO: the humanizer's `check.py` gives 0 flags (AI vocabulary,
"not X, it's Y", dashes, missing contractions, colon lists, retired
templates, lines repeated from the last 3 scripts), and the file has the
Humanizer table. REVIEWER: no line that can be heard two ways (sexual or
otherwise), no mockery of any runner, no staccato fragments.
**Evidence:** A viewer called a script "so obviously written by AI" (17
Oct); "it starts on your tongue, before you even swallow" (quit v2).
**Passes:** check.py: 0 flags; Humanizer table filled.
**From:** P169, P125, P35, P21, P60, P114, P66, P136, P33

---

## G. Proof

### G30 · Reviewed, current, and forecast honestly · AUTO
**Test:** `gate/reviews/<script>.md` exists, was written by the
independent reviewer, its hash matches the script's current spoken text and
title, and it has no FAIL. Every "Luke to OK" is listed. The forecast is a
range taken from the last 3 to 5 comparable reels at the same age, with
those numbers stated; it never says "confident".
**Evidence:** "You were so confident this would do well and then you
self-diagnosed" (Luke, 4 Nov). Forecasts off the September grid missed
every time from 20 Oct (email reel saves forecast 2%+, actual 0.4%).
**Passes:** "IG trial at 24h: 300 to 3,500 views, skip 26% to 55% (base:
wall repost 3,537 / 33.3%; long run 290 / 55.5%; match 242 at 2h / 26.2%)."
**From:** P190, P171, P145, P148, P99, P36, P90, P92

---

## Around the gate (process, not tests)

These are standing instructions that aren't about a script's content. They
stay in CLAUDE.md and the files named.
- **Frame one as mocked up** (10 Nov, the sub-4:30 posted with a finish-line crowd, not the wordless picture the gate passed): the posted frame one is the mockup's picture, or one that meets the same spec (no words, no numbers, no crowd). The review checks it after posting.
- **Brief first on a new topic** (P138): method in numbers, line one, pain
  and dream, every fact with its source. Luke says yes, then the script.
- **Ideation** (P168, P182, P184, P6, P18, P17, P22, P8): titles come from
  what the audience wrote; every idea list carries the gate table; a fail
  is cut, not shown.
- **The council** (P150): on topic, title and cover decisions in the brief.
  [C16]
- **Delivery format** (P122): quoted paragraphs, bold bracketed markers,
  title in capitals, never a code box. Captions in prose.
- **Posting** (P174, P96, P76, P156, P173, P111, P4, P13): new reels go out
  as trial reels from ERN first; shared to the profile above 4K views and
  under 40% skip at 24 hours; ERN TikTok only; 80/20 safe and tests.
  [C15] [C18]
- **Privacy** (P154, P172): no subscriber emails, names or quotes in the
  repo; sign-ups counted by day; nothing added to the sign-up form.
- **Reviews** (P148, P156, P171, P174, P144, P36, P86, P65): rates first,
  numbers against the base, no cause from one post, never posting time; a
  review that finds a broken rule names the gate test that should have
  caught it and fixes the test (P190). [C14] [C19]
- **Personal account** (P20, P32, P40, P42, P43, P49, P96, P14, P26, P27,
  P88): its own rules; the gate is for ERN reels.

---

## How a script file is laid out for the gate

The checker reads these. Copy the block from
`ideas/engine-room-nutrition/2026-11-06-script-sub-430-secretly.md` (the 16 results file it used to name is a record in gate/runs/).

```
---
type: script
gate: v1
---
## Gate fields
- OST: LINE ONE / LINE TWO
- Markers: STAGE ONE / STAGE TWO / STAGE THREE / STAGE FOUR
- Gap phrase: <the words in line one they'll wait for>
- Gap held by: <the named concept line>
- Gap closed by: <one of the markers>
- Turn: "<the spoken line before the first marker that shows what changed>"
- Frame one: <what's on screen 0:00 to 0:03>
- Frame one words: title only
- Mockup: <path to the 1080 x 1920 PNG>
- Layer title: <what the title says>
- Layer picture: <what the picture adds>
- Layer line one: <the gap>
- Worked example goal: <sub-4 | 3:45 | 4:00 | none>
- Forecast: <range, with the base reels named>
## Script
"spoken paragraph"
**[STAGE ONE]**
"spoken paragraph"
## The 4 questions   (a table: a moment they recognise? why it matters? what changed? something to do tonight?)
## Caption
## Facts check   (a table; Status: Pass / Luke to OK / Cut)
## Humanizer     (the table)
```

---

## The 24 contradictions, and what each [C#] currently uses

Sent to Luke on 4 Nov to settle in one go. Until he does, the gate uses the
recommendation. The full list with evidence is in `gate/contradictions.md`.

| # | Contradiction | In use until Luke decides |
|---|---|---|
| C1 | Three live gate wordings | "If you've got a marathon coming up," as default; the event named when the title names it |
| C2 | Reframe at the end of every line one vs the gap | The gap wins; reframe only when it happens to everyone and doesn't answer |
| C3 | Five script lengths, three cut lengths | 280 to 330 spoken words; finished cut 1:35 or less; over 1:40 recut |
| C4 | First value in 15 s vs a 80-95-word hook | 80 to 95 words; P69 retired |
| C5 | Title length in words vs characters | Characters only (P170) |
| C6 | Title in capitals vs normal case | Not a gate test; trial-reel A/B |
| C7 | "Marathon" in every title vs name the event | Name the event (P180) |
| C8 | The five-line topic gate vs P166/P173/P179/P181 | Retired; G5 to G7 replace it |
| C9 | Three layers from 0:00 vs one thing for 3 seconds | Title is the only words; one wordless picture allowed |
| C10 | Save prompt in the hook vs after stage 1 | In the hook (Luke's stack); test once as a trial A/B |
| C11 | No "how many people" vs our own counts | Our counts allowed once, with the true base |
| C12 | Gemini cover prompts vs AI covers retired | No AI covers; search terms and Luke's own images |
| C13 | Car and running top: package vs "setting doesn't matter" | Not a test; the default when it costs nothing |
| C14 | What a review leads with | Skip, watch %, sends, saves, then follows and sign-ups |
| C15 | Collab vs trial reels from ERN | Trial from ERN first |
| C16 | Ledger + checklist + council tables in every script vs one gate | The gate table replaces the ledger and checklist tables; council in briefs |
| C17 | Rankings (S to D) vs no gimmicks | Allowed when every placement is Luke's; "hacks" out |
| C18 | A winner at most once a month vs a weekly repost | Weekly repost as a trial |
| C19 | Forecast from type median vs last 3-5 reels | Last 3 to 5 reels (P171) |
| C20 | One number per sentence vs bands and the gel clock | At most 2; a band is one; K markers don't count |
| C22 | Gels: the clock vs 100m before a station | **SETTLED (Luke, 5 Nov):** 20 minutes, then every 30 on the clock; grab a bottle at a station when you pass one |
| C23 | Course videos: is a map fact enough for G17? | **SETTLED (left to the recommendation, 5 Nov):** yes, if the action with it is new |
| C24 | Watch pace vs clock time | **SETTLED (Luke, 5 Nov):** bands on the watch; the clock time at every 10K sign is the check |
| C21 | Re-testing an aha from the last 3 posts (found by the gate on its first run) | G8 fails it; allowed only as a strict one-change A/B on a trial reel |

---

## What came out, and why

**Superseded (the newer rule is in the gate):** P42's "no how-to on ERN"
(P68 and the data: our biggest reels are how-tos); the whisper in P47, P83
(dropped in production, P91); P51's intensifiers (P52); P55 and P104's
lengths, P85's 400 words, P100's 1:20 (C3); P62 and P89's word counts
(P170); P63 and P64's order (P71, P112, P176); P65's "optimise the send"
(P66, then P156); P69 (C4); P72 (P75, C18); P78 and P86's training band
(P92); P84's cards (corrected 24 Sep; P161 for static frames); P90's
24 hours (P92, then P174 for trial decisions); P93's start-crowd row (P104);
P95 and P100's set package (P103 amended, C13); P110's five-line gate (C8);
P111's one safe one creative (P173); P120 and P136's "every line one ends on
a reframe" (P149, P186, C2); P145's motion frame and type-median forecast
(P159, P160, P171); P160's "no numbers on screen" from stage 1 (P161);
P166's "runners only" (P173, P174, C8); ledger rows 24 and 25 (withdrawn
1 Nov); AI covers (retired 18 Oct, C12).

**Merged (duplicates):** P99 and P148 into G30; P106's five hook lines into
G16 to G18; P145's retention table into G19 and G20; P182's gate table
into G5, G10, G11 and G17; the checklist's 151 lines into the 30 above.

**Background, not a test (they explain why the tests exist):** P1 to P18,
P21 to P31, P33 to P38, P41, P45 to P48, P51 to P54, P56 to P61, P65, P67,
P73 to P79, P86, P87, P94, P95, P97, P102. Each one's live part is in the
"From" line of a test above.

## The failure ledger, mapped to the gate

Every row of the CLAUDE.md ledger is caught by a test:
1 answer up front G12, G16 · 2 reassurance G20 · 3 off the clock G5, G6 ·
4 crowd G14 · 5 collage/AI G14 · 6 abstract line one G17 · 7 too long
G19, C3 · 8 why stage G20 · 9 CTA late G19 · 10 sorting G7 · 11 few have it
G7 · 12 mixed timelines G20 · 13 symptom list G20 · 14 cover number G14 ·
15 tip as line one G17 · 16 templates G18, G29 · 17 no gap G16 · 18 nothing
to keep G21 · 19 dated words G28 · 20 story with no stake G2, G14 · 21
maths G25 · 22 busy first second G2 · 23 someone else's numbers G21 · 26
known advice G8 · 27 general title G11 · 28 numbers as failure G12 · 29
picture repeats title G13 · 30 line one about us G1, G4.
