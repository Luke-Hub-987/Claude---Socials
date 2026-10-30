#!/usr/bin/env python3
"""Flag mechanical signs of AI writing in spoken script text.

Usage: python3 check.py <script.md | teleprompter.txt> [more files...]
Reads quoted paragraphs from .md files (the spoken lines) or every
non-empty line of a .txt file. Compares against the three newest
teleprompter files in ideas/engine-room-nutrition/ for repeated lines.
"""
import glob, os, re, sys

VOCAB = r"delve|tapestry|testament|landscape|realm|crucial|pivotal|intricate|meticulous|robust|leverage|foster|garner|underscore|showcase|embark|holistic|optimal|additionally|moreover|furthermore|ultimately|essentially|notably|vibrant|breathtaking|nestled|seamless|game.changer|unlock|elevate|supercharge|next level|journey"
PATTERNS = [
    ("AI vocabulary", re.compile(r"\b(" + VOCAB + r")\b", re.I)),
    ("dodging 'is'", re.compile(r"\b(serves as|stands as|acts as|functions as|represents|boasts)\b", re.I)),
    ("negative parallelism", re.compile(r"\b(not just|not only|rather than|isn't about|it's not .{1,40}, it's|less about)\b", re.I)),
    ("filler or hedging", re.compile(r"\b(in order to|it's important to|important to note|the thing is|at the end of the day|may potentially|kind of|sort of)\b", re.I)),
    ("signposting", re.compile(r"\b(let's dive|here's the thing|here's the kicker|buckle up|the secret is|spoiler)\b", re.I)),
    ("self-asked question", re.compile(r"\b(The (result|fix|answer|catch|truth|problem)\?)", re.I)),
    ("vague authority", re.compile(r"\b(experts|studies show|research|scientists|many runners find)\b", re.I)),
    ("dash as a pause", re.compile(r"[—–]| - ")),
    ("curly quote or emoji", re.compile(r"[‘’“”]|[\U0001F300-\U0001FAFF]")),
    ("no contraction", re.compile(r"\b(you are|it is|do not|does not|he is|she is|that is|you will|we are|they are|I am|is not|are not|cannot|will not|did not|there is)\b", re.I)),
    ("jargon", re.compile(r"\b(zone ?\d|threshold|glycogen|negative split|protocol|lactate|VO2)\b", re.I)),
    ("colon list", re.compile(r"\b[A-Za-z ]{2,20}: [0-9]")),
    ("generic ending", re.compile(r"(you've got this|possibilities are endless|the rest is history)", re.I)),
]
# The talk-test sentence is a quote, not a missing contraction.
ALLOWED = ["I am running a marathon today and I feel good"]

def spoken_lines(path):
    text = open(path, encoding="utf-8").read()
    if path.endswith(".md"):
        return [m.group(1) for m in re.finditer(r'^"(.+)"\s*$', text, re.M)]
    return [l.strip() for l in text.splitlines() if l.strip()]

def sentences(lines):
    out = []
    for l in lines:
        out += [s.strip().lower() for s in re.split(r"(?<=[.?!])\s+", l) if len(s.split()) >= 5]
    return out

def main(paths):
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.abspath(os.path.join(here, "..", "..", ".."))
    tele = sorted(glob.glob(os.path.join(root, "ideas/engine-room-nutrition/*teleprompter*.txt")))
    flags = 0
    for path in paths:
        lines = spoken_lines(path)
        others = [t for t in tele if os.path.abspath(t) != os.path.abspath(path)
                  and os.path.basename(t)[:10] != os.path.basename(path)[:10]][-3:]
        old = set()
        for t in others:
            old |= set(sentences(spoken_lines(t)))
        print(f"== {path}: {len(lines)} spoken lines; repeats checked against {[os.path.basename(t) for t in others]}")
        for i, l in enumerate(lines, 1):
            check = l
            for a in ALLOWED:
                check = check.replace(a, "")
            for name, rx in PATTERNS:
                for m in rx.finditer(check):
                    print(f"  line {i}: {name}: '{m.group(0)}'")
                    flags += 1
            frags = re.findall(r"(?:^|[.?!]\s)([^.?!]{1,18}[.?!])", l)
            short = [f for f in frags if len(f.split()) <= 3]
            if len(short) >= 2:
                print(f"  line {i}: staccato fragments: {short}")
                flags += 1
            if re.search(r"\b\w+, \w+(?: \w+)?,? and \w+", l):
                print(f"  line {i}: possible list of three (check it's the real count): '{l[:70]}...'")
            for s in sentences([l]):
                if s in old:
                    print(f"  line {i}: repeated from a recent script: '{s[:70]}'")
                    flags += 1
    print(f"{flags} flags")

if __name__ == "__main__":
    main(sys.argv[1:])
