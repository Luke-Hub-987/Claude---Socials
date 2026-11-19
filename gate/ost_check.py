#!/usr/bin/env python3
"""The title checker (P210, P218, the stranger's questions; Luke 18 Nov: "the title checker is by far the most important").

Code, not judgement: everything here is countable, so a title that fails never reaches Luke.
The judgement half (the scorecard's 10 tests, the five levers) is the ost-reviewer agent's job.

Usage
  python3 gate/ost_check.py "ORANGES WON'T SAVE / YOUR LEGS AT 75 MINS / (SUNDAY LEAGUE)" --red "WON'T"
  python3 gate/ost_check.py "<title>" --red WORD --hook "line one and the rest of the hook"
  python3 gate/ost_check.py --file ideas/engine-room-nutrition/2026-11-18-titles-brain.md   (every "## " block)

A candidates file has one block per title:
  ## T1
  title: YOUR BRAIN QUITS AT / 30K OF A MARATHON / (IT'S NOT WEAKNESS)
  red: QUITS
  stranger: 30K of what? A MARATHON | quits how? the video (the gap) | not weakness, then what? the video
  luke_said: none
  hook: If your head starts telling you to walk at 30K of your marathon, ...

Exit code 1 if any title FAILs. --no-render skips the phone-size render (needs node + playwright).
"""
import argparse, glob, os, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EVENTS = r"MARATHONS?|MARATHONERS?|HALF[- ]MARATHONS?|PARKRUNS?|(?<![\d.])5K\b|(?<![\d.])10K\b|ULTRAS?|ULTRARUNNERS?|SUNDAY LEAGUE|FOOTBALL|SOCCER|\bMATCH(ES)?\b|\bGAA\b|HURLING|RUGBY|PREMIER LEAGUE|LONG RUNS?|RACE DAY|RACE WEEK|SEVILLE|VALENCIA|LONDON|DUBLIN|BERLIN|MANCHESTER"
PULSE = r"\bDIES?\b|\bDEAD\b|\bQUITS?\b|\bKILLS?\b|\bBRUTAL\b|\bSTOP\b|\bWON'T\b|\bNEVER\b|\bSECRETLY\b|\bACTUALLY\b|\bLI(E|ES|ING)\b|\bTRAP\b|\bSTARVES?\b|\bEMPTY\b|\bRUINS?\b|\bWRONG\b|\bLAZY\b|\bSLOWER\b|\bPANIC\b|\bCRASH(ES)?\b|\bWALL\b|\bBREAKS?\b|\bCOSTS?\b|\bSTEAL\b|\bAGGRESSIVE\b|\bRARE\b|\bFAIL(S|ED)?\b|\bSHOT\b|\bGONE\b|\bWASTED?\b|\bKILLING\b|\bAMAZING\b|\bUNDERFED\b|\bMEANER\b|\bLETHAL\b|\bNOBODY\b|\bSLOWS?\b|\bLATE\b|\bSHORT\b"
HEDGES = r"\bSOME\b|\bMOST\b(?!\s+(IMPORTANT|OVERLOOKED|UNDERRATED|COMMON|BRUTAL|DANGEROUS))|\bMAY\b|\bMIGHT\b|\bCAN\b|\bCOULD\b|\bOFTEN\b|\bSOMETIMES\b|\bPROBABLY\b|\bMAYBE\b|\bPERHAPS\b"
VAGUE_GROUPS = r"\bPROS'?\b|\bEXPERTS\b|\bTHEY\b|\bPEOPLE\b|\bSCIENCE\b|\bSTUDIES\b|\bRESEARCH\b"
VIEWER = r"\bYOU\b|\bYOUR\b|\bYOU'LL\b|\bYOU'RE\b|\b\d+(:\d\d)?-HOUR\b|\bSUB-\d|MARATHONERS?|\bRUNNERS?\b|SUNDAY LEAGUE|\bPLAYERS?\b|FIRST-TIMERS?"
# a number is fine when it carries its unit or counts a plural noun ("3 HABITS", "5 STAGES")
UNIT_AFTER = r"(K|KM|KG|G|M|MI|MILES?|MINS?|MINUTES?|HOURS?|HRS?|H|SECONDS?|SECS?|S|%|WEEKS?|DAYS?|YEARS?|-HOURS?|-MINS?|-MINUTES?|-SECONDS?|-DAYS?|-WEEKS?|ST|ND|RD|TH|')"
SPICE = r"\bTOP 1%|\bELITE\b|\bDNA\b|\bPARADOX\b|\bMETHOD\b|\bLETHAL\b|\bDISGUSTINGLY\b|\bBRUTAL(LY)?\b|\bPERFECT\b|\bMOST IMPORTANT\b|\bUNDERRATED\b|\bOVERLOOKED\b|\bSECRET(LY)?\b|\bNOBODY\b|\bNEVER\b|\bSTOP\b|\bACTUALLY\b|\bREAL\b|\bHARDER\b|\bBEAT\b|\bRANKING\b|\bTIER\b|\bMASTERCLASS\b|\bDESTROY(ING|S)?\b|\bPROOF\b|\bFREAK\b|\bGAS TANK\b|\bUNFIT\b|\bUNDERFED\b|\bRARE\b|\bYET\b|\bEVEN\b|\bWITHOUT\b"
SAFE = r"^(HOW TO (PACE|TRAIN|PREPARE|FUEL|RUN) (A|YOUR) MARATHON$|WHAT TO (DO|EAT)\b|.*\bTIPS\b|.*\bGUIDE\b|WHERE .* GOES WRONG|THE [A-Z0-9 ]+ TRAP$)"
STOP = set("THE A AN AND OR OF IN AT ON TO FOR IS IT ITS IT'S YOUR YOU YOU'LL YOU'RE WITH BY FROM THIS THAT ARE BE NOT NO EVEN SO BUT ONE ONES HOW WHY WHAT".split())

def norm(t):
    return re.sub(r"\s+", " ", t.replace("’", "'").upper()).strip()

def lines_of(title):
    return [l.strip() for l in norm(title).split("/") if l.strip()]

def words(t):
    return re.findall(r"[A-Z0-9£%'\-:.]+", norm(t))

def past_titles(exclude_file=None):
    out = []
    for f in glob.glob(os.path.join(ROOT, "ideas", "**", "*.md"), recursive=True):
        if exclude_file and os.path.abspath(f) == os.path.abspath(exclude_file):
            continue
        try:
            txt = open(f, encoding="utf-8").read()
        except Exception:
            continue
        for m in re.finditer(r"^(?:- OST(?: B)?: |# )(.+/.+)$", txt, re.M):
            out.append((m.group(1).strip(), os.path.relpath(f, ROOT)))
        for m in re.finditer(r"\*\*([A-Z0-9£'’ ,.\-()%:?!→]+ / [A-Z0-9£'’ ,.\-()%:?!/→]+)\*\*", txt):
            out.append((m.group(1).strip(), os.path.relpath(f, ROOT)))
    return out

def content(t):
    return {w.strip("().,:!?'") for w in words(t)} - STOP - {""}

def render_sizes(ls, red):
    q = {"spec": "white", "fit": "line", "who": "check"}
    for i, l in enumerate(ls[:3], 1):
        q["t%d" % i] = l
    if red:
        q["red"] = red
    from urllib.parse import urlencode
    out = os.path.join(tempfile.mkdtemp(), "ost.png")
    try:
        r = subprocess.run(["node", os.path.join(ROOT, "gate", "shoot_frame.js"), out, urlencode(q)],
                           capture_output=True, text=True, timeout=90, cwd=ROOT)
    except Exception as e:
        return None, str(e)
    m = re.search(r"title font ([\d./]+)vw", r.stdout)
    if not m:
        return None, (r.stdout + r.stderr).strip()[-200:]
    return [float(x) for x in m.group(1).split("/") if x], out.replace(".png", "-phone.png")

def check(title, red=None, stranger=None, luke_said=None, hook=None, render=True, file_mode=False, exclude=None):
    res = []
    add = lambda t, ok, msg, lvl=None: res.append((t, lvl or ("PASS" if ok else "FAIL"), msg))
    T = norm(title); ls = lines_of(title); body = " ".join(ls)

    # T1 lines and characters (G10)
    n = [len(l) for l in ls]
    if len(ls) == 2:
        add("T1 lines", all(x <= 22 for x in n) and sum(n) <= 40, f"2 lines {n}, {sum(n)} total (22 a line, 40 total)")
    elif len(ls) == 3:
        ok = all(x <= 26 for x in n)
        add("T1 lines", ok, f"3 lines {n} (26 a line; needs Luke's sign-off: ost_final_by_luke)")
    else:
        add("T1 lines", False, f"{len(ls)} lines: 2, or 3 with Luke's sign-off")

    # T2 the red word
    if red:
        r = norm(red)
        add("T2 red word", r in body, f"'{r}' in red" + ("" if r in body else ": not in the title"))
    else:
        add("T2 red word", False, "no red word named (one feeling word in red, P207)")

    # T3 pulse word, and the top line carries it (scorecard 1 and 10)
    has_pulse = re.search(PULSE, body) is not None
    add("T3 pulse word", has_pulse, "a pulse word" + ("" if has_pulse else ": none (DIE, QUITS, WON'T, BRUTAL, SECRETLY...)"), None if has_pulse else "WARN")
    top = ls[0] if ls else ""
    if top.endswith("?") or re.match(r"(WHY|WHAT|IS|ARE|DO|DOES|SHOULD)\b", top):
        add("T3 top line", False, f"top line is a question or a filter: '{top}' (verdict first, scorecard 10)", "WARN")
    elif re.search(PULSE, top) or re.match(r"HOW TO\b|\d+\b", top):
        add("T3 top line", True, "the top line carries the pulse, a count or HOW TO")
    else:
        add("T3 top line", False, f"no pulse on the top line: '{top}'", "WARN")

    # T4 hedge words
    h = re.findall(HEDGES, body)
    add("T4 no hedge", not h, "no hedge word" if not h else f"hedge {sorted(set(h))}: find a stronger true claim")

    # T5 the event or sport named on screen (the stranger's "in what?")
    ev = re.search(EVENTS, body)
    add("T5 in what?", ev is not None, f"names '{ev.group(0)}'" if ev else "no event or sport on screen (MARATHON, PARKRUN, SUNDAY LEAGUE...): 'in what?'")

    # T6 every number carries its unit or counts a noun
    bad = []
    for m in re.finditer(r"(?<![\w:£])(\d+(?:\.\d+)?)(?![\d:])", body):
        after = body[m.end():]
        if re.match(UNIT_AFTER + r"\b", after) or re.match(r"'|%", after):  # % is a unit; "60% of what?" goes in the stranger line
            continue
        nxt = re.match(r"\s+([A-Z'\-]+)", after)
        prev = body[:m.start()].rstrip().split(" ")[-1] if body[:m.start()].strip() else ""
        if nxt and re.match(UNIT_AFTER + r"$", nxt.group(1)):
            continue
        if re.match(r"\s+(A|AN|PER|EVERY)\s+(HOUR|DAY|WEEK|GAME|MATCH|RACE)\b", after):
            continue  # 2 AN HOUR
        if re.match(r"-\d", after) or re.search(r"\d-$", body[:m.start()]):
            continue  # 9-5, 3-4
        if re.match(r"\s+(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)[A-Z]*\b", after):
            continue  # 6 DECEMBER
        if prev in ("HOUR", "STAGE", "PART", "WEEK", "DAY", "SUB-", "MILE", "KM", "K") or re.search(r"SUB-$|-$", prev):
            continue
        if nxt and nxt.group(1).endswith("S") and not nxt.group(1).startswith("MIN") and m.start() < len(body) and not re.match(r"(AT|IN|BY)$", prev):
            continue  # a count: 3 HABITS, 5 STAGES, 8 WAYS
        bad.append(m.group(1) + (" (after " + prev + ")" if prev else ""))
    add("T6 of what?", not bad, "every number has its unit" if not bad else f"bare number {bad}: 75 of what? add MINS, K, MINUTES...")

    # T7 vague groups (the stranger's "pros in what?", and no 'study' on screen)
    vg = re.findall(VAGUE_GROUPS, body)
    add("T7 who?", not vg, "every group named exactly" if not vg else f"vague {sorted(set(vg))}: name them (PREMIER LEAGUE, not PROS)")

    # T8 the viewer or their goal
    vw = re.search(VIEWER, body)
    add("T8 viewer", vw is not None, f"the viewer: '{vw.group(0)}'" if vw else "no YOU/YOUR or goal (4-HOUR, SUB-4, SUNDAY LEAGUE)", None if vw else "WARN")

    # T9 the stranger's questions written and answered (file mode)
    if file_mode or stranger is not None:
        qs = [q.strip() for q in (stranger or "").split("|") if q.strip()]
        unanswered = [q for q in qs if "?" not in q or not q.split("?", 1)[1].strip()]
        add("T9 stranger", bool(qs) and not unanswered,
            f"{len(qs)} questions answered" if qs and not unanswered else ("no 'stranger:' line" if not qs else f"unanswered {unanswered}"))

    # T10 anything about Luke needs his words
    unquoted = re.sub(r"(^|\s)['\"‘“][^'\"’”]*['\"’”]", " ", body)  # the runner's own words in quotes aren't Luke
    if re.search(r"\bI\b|\bI'M\b|\bI'VE\b|\bMY\b|\bME\b", unquoted):
        ok = bool(luke_said and luke_said.strip().lower() not in ("", "none", "n/a"))
        add("T10 Luke said", ok, "Luke's own words cited" if ok else "a claim about Luke with no 'luke_said:' source (never put a habit in his mouth)")

    # T11 repeats against every past title
    mine = content(T); hits = []
    for pt, f in past_titles(exclude):
        other = content(pt)
        if not mine or not other:
            continue
        j = len(mine & other) / len(mine | other)
        if norm(pt) == T:
            hits.append(("same", pt, f))
        elif j >= 0.5:
            hits.append((f"{j:.0%}", pt, f))
    same = [x for x in hits if x[0] == "same"]
    near = sorted({(x[1], x[2]) for x in hits if x[0] != "same"})[:3]
    if same:
        add("T11 repeat", True, f"already on file in {same[0][2]} (fine if this is that title)", "INFO")
    elif near:
        add("T11 repeat", False, "close to " + "; ".join(f"'{p}' ({f})" for p, f in near), "WARN")
    else:
        add("T11 repeat", True, "no close past title")

    # T13 the dull floor (P221): at least 2 things a stranger would remember
    spice = []
    if re.search(r"\d", body): spice.append("a number")
    if "(" in body: spice.append("a bracket")
    if re.search(r"(^|\s)['\"‘“]\w", body): spice.append("quotes")
    sp = sorted({m.group(0) for m in re.finditer(SPICE + "|" + PULSE, body)})
    if sp: spice.append("strong words " + ", ".join(sp[:3]))
    if len(sp) >= 2: spice.append("a second strong word")
    safe = re.match(SAFE, body) is not None
    if len(spice) >= 2:
        add("T13 not dull", True, "spice: " + ", ".join(spice))
    elif safe or not spice:
        add("T13 not dull", False, f"dull: {'a safe fallback shape (how to pace, what to do, tips, guide, the X trap)' if safe else 'nothing a stranger would remember'}; add a number, an identity or strong word, a named method, quotes, a bracket twist or a flip")
    else:
        add("T13 not dull", False, f"thin: only {spice}; fine if the shape carries it (a flip, a contradiction), otherwise push it", "WARN")

    # T12 readable at phone size (row 33: the 10% title measured 6.1vw)
    if render and ls:
        sizes, info = render_sizes(ls, red)
        if sizes:
            add("T12 phone size", min(sizes) >= 7.0, f"{'/'.join(str(s) for s in sizes)}vw at phone size (7.0 minimum; mockup {info})")
        else:
            add("T12 phone size", False, f"couldn't render ({info}); run with node + playwright", "WARN")

    # H: the verbal hook (P198, P218, G1, G27): value by 0:15, the title's keywords spoken early
    if hook:
        hw = re.findall(r"[A-Za-z0-9'’:.\-]+", hook)
        add("H1 length", 40 <= len(hw) <= 45, f"hook {len(hw)} words (40 to 45, so stage 1 starts by about 0:15: P218)")
        first8 = " ".join(hw[:8]).lower()
        add("H2 viewer first", re.search(r"\byou(r|'re|'ll)?\b", first8) is not None, "you/your in the first 8 words (G1)")
        early = {w.upper().strip(".,'’") for w in hw[:20]}
        keys = {k for k in mine if not k.startswith("(") and len(k) >= 2}
        echoed = sorted(k for k in keys if k in early or k.rstrip("S") in early or (k + "S") in early)
        add("H3 keywords", len(echoed) >= 2, f"title keywords spoken in the first 20 words: {echoed or 'none'} (the title's promise heard at once)")
        st = re.findall(r"\b(study|studies|research|researchers)\b", hook, re.I)
        add("H4 no 'study'", not st, "no study/research words (G27)" if not st else f"{sorted(set(s.lower() for s in st))} in the hook: say who and what, not 'a study'")
    return res

def parse_file(path):
    txt = open(path, encoding="utf-8").read()
    blocks = re.split(r"^## ", txt, flags=re.M)[1:]
    for b in blocks:
        name = b.splitlines()[0].strip()
        get = lambda k: (re.search(rf"^{k}:\s*(.+)$", b, re.M) or [None, None])[1]
        if get("title"):
            yield name, dict(title=get("title"), red=get("red"), stranger=get("stranger") or "", luke_said=get("luke_said"), hook=get("hook"))

def show(name, res):
    worst = "FAIL" if any(l == "FAIL" for _, l, _ in res) else ("WARN" if any(l == "WARN" for _, l, _ in res) else "PASS")
    print(f"\n{name}: {worst}")
    for t, l, m in res:
        print(f"  {l:4}  {t:15} {m}")
    return worst

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("title", nargs="?")
    ap.add_argument("--red"); ap.add_argument("--stranger"); ap.add_argument("--luke-said"); ap.add_argument("--hook")
    ap.add_argument("--file"); ap.add_argument("--no-render", action="store_true")
    a = ap.parse_args()
    worst = []
    if a.file:
        for name, d in parse_file(a.file):
            worst.append(show(f"{name}  {d['title']}", check(render=not a.no_render, file_mode=True, exclude=a.file, **d)))
    elif a.title:
        worst.append(show(a.title, check(a.title, a.red, a.stranger, a.luke_said, a.hook, render=not a.no_render)))
    else:
        ap.print_help(); sys.exit(2)
    print(f"\n-> {'FAIL' if 'FAIL' in worst else 'PASS'} ({len(worst)} title{'s' if len(worst) != 1 else ''})")
    sys.exit(1 if "FAIL" in worst else 0)

if __name__ == "__main__":
    main()
