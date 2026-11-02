---
name: humaniser
description: Check and rewrite any ERN or Luke copy (emails, scripts, captions, on-screen text, replies to subscribers, reports to Luke) so it shows no signs of AI writing and sounds like Luke talking to one runner. Use before delivering any written copy, and whenever Luke asks to "humanise", "de-AI" or check copy for AI tells.
argument-hint: "[file path or pasted text]"
allowed-tools: Read Edit Write Bash(grep *) Bash(python3 *)
---

# Humaniser: no signs of AI writing

Source rules: `principles.md` P21, P35 (Wikipedia: Signs of AI writing,
WikiProject AI Cleanup), P118 (emails too), `voice-rules.md`, and the
"Never" list in `CLAUDE.md`. If this file and those disagree, those win.

## How to run it

1. Get the text (a file path, or the text in the conversation).
2. Run the mechanical scan below. Fix every hit.
3. Read the text aloud, line by line, as Luke would say it to one runner
   on a run. Rewrite any line that fails a check in "Read-aloud checks".
4. Check the facts still match the brand numbers (`emails/flows/00-flow-brief.md`,
   "The numbers"). Humanising must never change a number.
5. Report: a table of each change (before, the tell, after), then the
   clean text. If nothing needed changing, say so plainly.

## Mechanical scan (search for these)

```bash
python3 - "$FILE" <<'PY'
import re,sys
t=open(sys.argv[1]).read()
checks={
 "em or en dash": r"[—–]",
 "curly quotes": r"[“”‘’]",
 "not X, it's Y": r"\b(not|isn't|aren't|wasn't)\b[^.]{0,60}[,;]\s*(it's|it is|but|they're|that's)\b",
 "AI vocabulary": r"\b(delve|tapestry|testament|landscape|pivotal|boasts?|vibrant|seamless|elevate|unlock|journey|crucial|robust|leverage|navigate|realm|embark|furthermore|moreover|additionally|in summary|ultimately)\b",
 "dressed-up 'is'": r"\b(serves as|stands as|acts as a|functions as)\b",
 "filler": r"\b(in order to|due to the fact that|it is important to note|it's worth noting|let's dive in|in today's world|game-changer)\b",
 "stacked hedges": r"\b(may potentially|could potentially|it could be argued|arguably|somewhat|fairly)\b",
 "generic close": r"(the future looks bright|possibilities are endless|the rest is history|and that's the point)",
 "false range": r"\bfrom [a-z ]{2,25} to [a-z ]{2,25},",
}
for k,p in checks.items():
    for m in re.finditer(p,t,re.I): print(f"{k}: ...{t[max(0,m.start()-40):m.end()+40]!r}")
PY
```

## Read-aloud checks (judgement)

- **Rule of three:** a list of three only if the real count is three.
  A slogan triad ("the pace, the fuel and the effort") goes.
- **One idea said once.** The same phrase twice in one email is a tell
  ("straight to me" three times).
- **Full sentences.** No staccato fragments ("By 30K, about five.").
- **No stock sayings** ("race day is no day to try something new").
- **No synonym cycling.** Runner stays "runner"; don't rotate athlete,
  competitor, individual.
- **No bold or headings doing the arguing.** Bold only the one thing to act on.
- **Specific beats vague** (P108, P115): a real number, a real place, a
  real time. "Most runners" without a source becomes the specific case.
- **Spoken register:** contractions, short sentences, the way Luke says
  it. Irish and UK words where natural (K, lamppost, the gun).
- **No jargon:** glycogen, taper, zones, fast-twitch, heart-rate zones.
- **No named methods or people** in brand copy (P105, P113).
- **No mockery, no second readings** (P114).
- **Promises:** nothing Luke can't keep (no turnaround times he didn't
  set; no launch dates; no claims about himself he hasn't made).

## Example

Before: "Running 4:05 is a fantastic achievement and proves beyond doubt
that your aerobic engine is there — you didn't miss it because of your
fitness, you missed it purely due to pacing."
Tells: em dash; "not X, it's Y"; puffery ("fantastic", "beyond doubt");
jargon ("aerobic engine").
After: "4:05 is a strong run, and your splits show the fitness for sub-4
is there. The time went at 12 to 16K, where you ran 5:24 a K to win back
the slow start."
