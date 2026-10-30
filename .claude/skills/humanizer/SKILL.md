---
name: humanizer
description: Remove every sign of AI writing from a script, caption, OST, story text or email before Luke sees it. Runs the Wikipedia "Signs of AI writing" catalog plus our own house tells (P35, P125, P157, P169), rewrites what fails, and leaves an audit table in the file. Run it on every piece of copy without being asked; Luke should never have to remind us.
argument-hint: "[path to the script file, or paste the text]"
allowed-tools: Bash(python3 *) Bash(cat *) Bash(ls *) Bash(grep *) Read Edit Write
---

# Humanizer

Luke, 30 Oct: "I don't want to remind you every time." This runs on every
script, caption, pinned comment, OST and story line we write, as the last
step before delivery. It changes the wording, never the framework.

## What it must not touch
The humanizer edits words, not structure. These stay exactly where they are:
- The gate ("If you've got a marathon coming up,"), line one's picture and
  its open loop or reframe (P120, P149), pain and dream, the named
  unknown, the rehook, the one-sentence CTA after stage 1, the send line.
- Every number, pace band and time (FACTS.md). Numerals stay numerals
  (P131); paces stay 5-second bands (P132).
- Stage markers and the OST wording Luke approved.
- Length: spoken text stays 1,550 to 1,670 characters, ceiling 1,800.

## Step 1: run the checker
```
python3 .claude/skills/humanizer/check.py <file>
```
It reads the spoken lines (quoted paragraphs in a script file, or every
line of a .txt teleprompter) and flags the mechanical tells below, plus
any line shared with the last three teleprompter files. It can't judge
rhythm or meaning, so step 2 is still a full read.

## Step 2: read every line against the catalog
From Wikipedia:Signs of AI writing (WikiProject AI Cleanup), the parts
that show up in short spoken scripts and captions:

**Content**
1. **Puffed-up significance:** "a testament to", "a pivotal moment",
   "marks a turning point", "plays a vital role", "it's no secret".
2. **Promotional words:** vibrant, breathtaking, nestled, seamless,
   game-changer, unlock, elevate, supercharge, next level.
3. **Trailing "-ing" analysis:** "..., highlighting how", "...,
   ensuring you", "..., making it the perfect".
4. **Vague authority:** "experts say", "studies show", "many runners
   find", "research suggests" (also banned by P105 and P107).
5. **Generic upbeat endings:** "the possibilities are endless", "you've
   got this", "the rest is history", a feel-good close not tied to a
   number.
6. **False ranges:** "from your first 5K to your fastest marathon".

**Language**
7. **AI vocabulary:** delve, tapestry, testament, landscape, realm,
   crucial, pivotal, intricate, meticulous, robust, leverage, foster,
   garner, underscore, showcase, navigate (a race), journey (for
   training), embark, holistic, optimal, additionally, moreover,
   furthermore, ultimately, essentially, notably.
8. **Dodging "is":** serves as, stands as, acts as, functions as,
   represents, boasts, features (for "has").
9. **Negative parallelism:** "not X, it's Y", "it's not just X, it's
   Y", "not only... but also", "Y rather than X", "less about X, more
   about Y" (P21, P35).
10. **Rule of three by habit:** three items, three adjectives, three
    short sentences in a row. Use the real count (P125).
11. **Synonym cycling:** runner, athlete, competitor for the same person.
    Repeat the plain word.
12. **Filler and hedging:** "in order to", "it's important to note",
    "the thing is", "at the end of the day", "may potentially", "kind
    of", stacked qualifiers.
13. **Signposting:** "let's dive in", "here's the thing", "here's the
    kicker", "buckle up", "the secret is", "spoiler".
14. **Self-asked questions:** "The result? ...", "The fix? ...",
    "Why? Because...".

**Style**
15. **Em dashes and en dashes as pauses.** None, anywhere (Luke's rule).
16. **Staccato fragments** for drama: "No gels. No water. Nothing."
17. **Colon lists read aloud:** "Breakfast: 8am." Times and items go in
    sentences (P125).
18. **Curly quotes, emojis, title case, bold** inside spoken text.

**House tells (ours)**
19. **No contractions:** "you are", "it is", "do not", "he is", "that
    is", "you will". Spoken English contracts (P125).
20. **Our own template lines** from the last three scripts (the checker
    lists them): "that's your race going to plan", "and the last one is",
    "here is the exact plan", "get it wrong... get it right".
21. **Jargon or method names** a friend wouldn't say on a run (P157):
    zones, threshold, glycogen, negative split, protocol.
22. **Written, not said:** any sentence Luke would trip on reading aloud
    in the car. Read each one out loud in your head at his pace.

## Step 3: rewrite
Fix each failing line in Luke's voice: short and long sentences mixed,
contractions, plain words, the picture first. Keep the same facts and the
same job for the line. Re-run the checker until it's clean or each flag
is explained.

## Step 4: leave the audit in the file
Add a "Humanizer (P169)" table to the script file: each check, pass or
the change made (old line, new line, why). In chat, say in one line that
it ran and what changed; don't paste the table unless Luke asks.
