---
name: title-producer
description: Produce the title (on-screen text) and the verbal hook for an ERN reel: the five levers first, 20 creative and specific titles across our proven devices, the code checker (gate/ost_check.py), the cold ost-reviewer, then the top 3 with their hook stacks for Luke. Use for every reel, carousel cover and trial title before any script. Luke, 18 Nov: "the title checker is by far the most important... a Toyota badge on a Ferrari engine and nobody ever sees the engine."
argument-hint: "[topic, or 'find one'] [optional: the facts or brief file]"
allowed-tools: Bash(python3 *) Bash(node *) Bash(grep *) Bash(ls *) Bash(cat *) Read Write Edit Grep Glob Agent
---

# Title producer

**Why this exists.** Luke, 18 Nov: if the title isn't specific and creative
enough, strangers decide "that's not for me" and swipe, however good the body
is. Every reminder Luke has had to repeat this month was about the title or
the hook ("of what?", "in what sport?", "value quicker"). So the title is
written first, checked in code, reviewed cold, and only then scripted.

## The run (do every step; don't show Luke a title that skipped one)

### 0. Read the library
`ideas/engine-room-nutrition/TITLE-EXAMPLES.md`: the other creators' titles and covers Luke has sent, what works across them, what we take and can't. If Luke sends a new example, save it to `research/title-examples/` and add a row there in the same turn, so he never sends it twice.

### 0b. Read the topic bank (Luke, 21 Nov, P232)
`ideas/engine-room-nutrition/2026-11-20-titles-30-from-the-greats.md`: the 30 headlines Luke liked ("particularly the TED-Ed ones"). When Luke asks for titles or topics, start from this bank: offer the unused ones first, TED-Ed shapes (what happens if, why your X does Y, where the fat goes) at the front, and mark each one used with its date when it's posted.

### 1. The levers before any words
Write the five levers for the topic (`ideas/engine-room-nutrition/2026-11-16-premortem-psychology.md`):
1. **The enemy outside the viewer:** the advice, the myth, the body, the tradition. Never their character or rank.
2. **A belief they hold confidently, broken:** what they'd say in the start pen or the dressing room.
3. **A moment they fear in their own race or match:** 32K, 75 minutes, the ball over the top.
4. **Their number:** 4-HOUR, SUB-4, 30K, 75 MINS.
5. **A peak:** the bracket or count that makes them stay to the end.
Then the facts: every claim the title makes is in FACTS.md, or it's flagged before
any title is written. Anything about Luke needs his own words (`luke_said:`).

### 2. Twenty titles, at least eight devices (P220: wide open)
At least half from routes that aren't fear: HOW TO + number + constraint, identity, a named method, a journey, the problem with, scare quotes, a tier list, a format tag (Briar's grid in TITLE-EXAMPLES.md). Every title names a problem they already know they have, and promises something we can send (comment word -> email).
Write 20. The most aggressive **true** version first. Spread them across the
devices below, at least eight, and never three in a row from one device.

| Device | Luke's example (what made it work) | Ours |
|---|---|---|
| Count + identity + escalation tag | 3 HABITS TO CREATE NERVES OF STEEL (PROGRESSIVELY MORE BRUTAL): 29.7K likes against 1,227 for HOW TO DEVELOP NERVES OF STEEL, the same video | THE MARATHON WALL / HITS YOU IN 5 STAGES / (EACH ONE MORE BRUTAL) |
| Death word + their number + "not your fault" bracket | (ours, the template) | **4-HOUR MARATHONS DIE / IN HOUR 4 / (EVEN THE FIT ONES)**: 18.4K, skip 26.8%, 278 saves |
| HOW TO + outcome + number + event + one-word twist | (ours) | **HOW TO RUN A SUB-4 / MARATHON (SECRETLY)**: skip 18.5% at 1h, 10.4K |
| The tradition or myth killed | Morning Coffee: "Carbs will make you fat... that is the stupidest thing I can say" | **ORANGES WON'T SAVE / YOUR LEGS AT 75 MINS / (SUNDAY LEAGUE)**: 2,308 at 12.5h as a trial |
| ACTUALLY (the hidden truth) | | WHERE THE MARATHON WALL ACTUALLY STARTS: 147K |
| A bad word made good, in quotes | 3 "COLD" BEHAVIOURS YOU SHOULD DO | 3 'LAZY' HABITS OF / SUB-4 MARATHONERS |
| They don't tell you / nobody's doing it | 5 THINGS THEY DON'T TELL YOU ABOUT BECOMING AN ENTREPRENEUR | |
| Two opposites + RARE | OBSESSIVE AMBITION & PLAYFULNESS IS RARE: 11.2K sends | |
| An arc in arrows (only when every stage is admirable) | ATHLETE → ENTREPRENEUR → ARTIST: 29.6K sends | (FINISHER → RACER → HUNTER died: it ranked the viewer low) |
| The danger | "Be warned... massive strain on your nervous system" | |
| The price contrast | | £250 SHOES WON'T FIX / A £0 PACING PLAN |
| A rule-break word in quotes | | HOW TO 'STEAL' 400M / IN A MARATHON |
| The series label | "(MARATHON EDITION)", Part 4 | (SUNDAY LEAGUE EDITION), PREMIER LEAGUE FUEL |

Specific beats clever: the event, the number with its unit, the group named
exactly (PREMIER LEAGUE, not PROS), a picture they've lived.

### 2b. Push every title further before checking (P221: never revert to safe)
- **Bold first, Luke trims:** at least 5 of the 20 should feel like too much (the strongest true word, the flip, the paradox, the identity taken away). Luke pulls back more easily than he pushes forward, and he's had to push every time.
- **The 24x edit on every title** (TITLE-EXAMPLES.md, dull → bold pairs): a count? a stronger verb? a bracket that escalates, adds a constraint or a number? the feeling word, not the report word (brutal, not effective)?
- **Original, not copied:** take the creator's move, write our own line in runners' words.
- **The swap test:** if any running account could post it unchanged, rewrite it.
- **The pub test:** would a runner say it to a mate after one read?

### 3. The code check
Write the 20 into `ideas/engine-room-nutrition/YYYY-MM-DD-titles-<topic>.md`,
one block each:

```
## T1
title: YOUR BRAIN QUITS AT / 30K OF A MARATHON / (IT'S NOT WEAKNESS)
red: QUITS
stranger: 30K of what? A MARATHON | quits how? the video (the gap) | not weakness, then what? the video
luke_said: none
hook: (only for the top 5 after step 4)
```

Run `python3 gate/ost_check.py --file <that file>`. It checks what can be
counted: lines and characters (G10), the red word, a pulse word and the top
line, hedge words, the event named ("in what?"), every number's unit ("of
what?"), vague groups ("pros in what?"), the viewer, the stranger's questions
answered, anything about Luke sourced, repeats of every past title, and the
size at phone size (7.0vw minimum; the unreadable 10% title was 6.1).
**Drop every FAIL. Fix or drop every WARN** unless you can say in one line why
the warning is wrong for this title.

### 4. The cold review
Run the `ost-reviewer` agent once on the file. Don't argue with it in the
file; if it ranks something you'd have ranked lower, its view goes to Luke too.

### 5. The hook for the top 3 (the verbal half of the title)
For each of the reviewer's top 3, write the hook stack and add it as `hook:`:
- **Line one:** the viewer + the title's keywords said back + the gap, inside
  20 words. The title's promise is heard in the first 5 seconds.
- **The turn** in line one or the next sentence: the thing that changed, one
  they didn't believe (P194).
- **One pain-and-dream sentence**, a new shape (P186).
- **The named concept** that keeps the question shut (P176).
- **40 to 45 words in all,** so stage 1 starts by about 0:15 with something
  usable (P218, a repeat of P69). The question the title opened stays open
  until the last stage.
- **The curiosity loop:** one line saying what they're waiting for, what holds
  it, and which stage closes it.
Re-run `ost_check.py --file`: the H tests check length, "you" in the first 8
words, the title's keywords in the first 20, and no "study/research" (G27).

### 6. Deliver to Luke
The top 3, best first, each with:
- the title in bold capitals, the red word named, the score (the reviewer's,
  not yours) and the phone size;
- the stranger's questions table;
- the hook;
- one line on why it would flop and the fix.
Then **one recommendation**. Keep the file; the scorecard gets a row for the
one Luke picks.

### 7. After Luke picks
Same chat: the brief if the topic is new (P138), the script through GATE.md,
then the title card with `node motion/title-cards/make_title.js` (white card,
the red or blue word, the 9:16 overlay and the text-only cover).
