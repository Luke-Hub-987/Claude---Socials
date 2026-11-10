#!/usr/bin/env python3
"""The gate checker (GATE.md, P190). Runs every AUTO test on a script file.

Usage:
  python3 gate/check.py <script.md> [...]   full gate on the files; exit 1 on any FAIL
  python3 gate/check.py --staged            gate every staged script (git pre-commit)
  python3 gate/check.py --changed           gate every script changed or new in the working tree
  python3 gate/check.py --hash <script.md>  print the hash the reviewer stamps on its review
  python3 gate/check.py --brief <file>      one line per FAIL (for hooks)

A file is gated when its front matter has `gate:`. A NEW script file
(ideas/**/*-script-*.md, not yet in git) without `gate:` fails: no dodging.
"""
import glob, hashlib, os, re, statistics, struct, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REVIEW_DIR = os.path.join(ROOT, "gate", "reviews")
HUMANIZER = os.path.join(ROOT, ".claude", "skills", "humanizer", "check.py")

# Tests the independent reviewer must grade (REVIEWER and BOTH in GATE.md).
REVIEWER_TESTS = ["G2", "G4", "G5", "G6", "G7", "G8", "G9", "G11", "G12", "G13", "G14",
                  "G16", "G17", "G18", "G20", "G21", "G22", "G23", "G24", "G29", "G31", "G32"]
# Two tiers (Luke, 5 Nov): a reviewer FAIL on a BLOCK test stops the script;
# a FAIL on a RISK test goes in the script's "Known risks" box for Luke.
BLOCK_REVIEWER = ["G2", "G6", "G8", "G9", "G12", "G16", "G21", "G22", "G23", "G29", "G31", "G32"]
RISK_REVIEWER = [x for x in REVIEWER_TESTS if x not in BLOCK_REVIEWER]

WORDS = dict(
    jargon=r"zone ?\d|threshold|glycogen|lactate|vo2|negative split|protocol|strategy|optimal|cadence|tempo|taper|splanchnic|anaerobic",
    title_jargon=r"taper|zone|heart rate|threshold|tempo|cadence|glycogen|vo2",
    gimmick=r"hacks?|cheat ?codes?|maxx?ing|like you'?re 10|unethical|10/10",
    dated=r"this (?:weekend|sunday|saturday|week|spring|summer|autumn|winter|month)|tomorrow|tonight|next weekend|next week",
    stats=r"%|\bper ?cent\b|\bstud(?:y|ies)\b|\bresearch(?:ers)?\b|\bexperts?\b|\bscientists?\b|\b(?:most|many|half of|a third of|\d+ in \d+|\d+ out of \d+) (?:runners|people|marathoners|players)\b",
    medicine=r"ibuprofen|paracetamol|painkillers?|nurofen|aspirin|anti-?inflammator\w*|medication|tablets?",
    brands=r"precision|maurten|\bsis\b|high5|puresport|styrkr|torq|garmin|coros|strava|nike|adidas|asics|hoka|saucony",
    not_done=r"arm sleeves?|bin bags?|bin liners?|soft flasks?|watch alerts?|set your watch|\bapps?\b|pickle juice|salt tablets?",
    race_food=r"banana|pretzels?|sandwich|flapjack|energy bar|the bar\b|a bar\b|our bar",
    templates=r"get (?:it|race week|the \w+) (?:wrong|right)|you'?re the one (?:who|passing|still|sending)|that's your race going to plan",
    number_words=r"two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand",
    maths=r"\b\d+(?:\.\d+)? times\b|\bplus \d|\bminus \d|\bdivided\b|\bmultipl\w+|\bx ?\d",
)
TALK_TEST = "I am running a marathon today and I feel good"


def rx(name):
    return re.compile(r"\b(?:" + WORDS[name] + r")\b" if name not in ("stats",) else WORDS[name], re.I)


# ---------- parsing ----------
def read(path):
    return open(path, encoding="utf-8").read()


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
    return fm


def section(text, title):
    m = re.search(r"^## " + re.escape(title) + r"[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else None


def fields(text):
    sec = section(text, "Gate fields") or ""
    out = {}
    for m in re.finditer(r"^- ([^:]+):\s*(.*)$", sec, re.M):
        out[m.group(1).strip().lower()] = m.group(2).strip()
    return out


def script_items(text):
    """Ordered list of ('para', text) and ('marker', NAME) from the ## Script section."""
    sec = section(text, "Script") or ""
    items = []
    for line in sec.splitlines():
        line = line.strip()
        mk = re.match(r"^\*\*\[(.+?)\]\*\*$", line)
        if mk:
            items.append(("marker", mk.group(1).strip()))
            continue
        sp = re.match(r'^"(.+)"$', line)
        if sp:
            items.append(("para", sp.group(1)))
    return items


def sentences(para):
    return [s.strip() for s in re.split(r"(?<=[.?!])\s+", para) if s.strip()]


def words(s):
    return re.findall(r"[A-Za-z0-9'’:\-]+", s)


def norm_tokens(s):
    return [w.lower().strip("'’") for w in words(s)]


def script_hash(text):
    f = fields(text)
    items = script_items(text)
    blob = "OST:" + f.get("ost", "") + "\n" + "\n".join(f"{k}:{v}" for k, v in items)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


def png_size(path):
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", head[16:24])


def numbers_in(s):
    return set(re.findall(r"\d+(?::\d+)*", s))


def counted_numbers(sentence):
    """Numbers per P155 as settled in C20: a 5-second band is one, a K marker doesn't count."""
    s = re.sub(r"between \d+:\d+ and \d+:\d+", " BAND ", sentence, flags=re.I)
    s = re.sub(r"\b\d+K\b", " ", s)
    s = s.replace(TALK_TEST, " ")
    return len(re.findall(r"\d+(?::\d+)*(?:\.\d+)?", s)) + s.count("BAND")


# ---------- the gate ----------
def run(path):
    text = read(path)
    fm = front_matter(text)
    f = fields(text)
    items = script_items(text)
    paras = [t for k, t in items if k == "para"]
    markers_in_script = [t for k, t in items if k == "marker"]
    spoken = " ".join(paras)
    spoken_no_talk = spoken.replace(TALK_TEST, "")
    all_sents = [s for p in paras for s in sentences(p)]
    ost = f.get("ost", "")
    ost_lines = [l.strip() for l in ost.split("/")] if ost else []
    markers = [m.strip() for m in f.get("markers", "").split("/") if m.strip()]
    res = []

    def add(tid, ok, msg, level=None):
        res.append((tid, level or ("PASS" if ok else "FAIL"), msg))

    if not fm.get("gate"):
        add("G0", False, "no `gate:` in the front matter, so this script was never gated")
    if not paras:
        add("G0", False, "no spoken paragraphs found under '## Script'")
        return res

    # G1 first words are the viewer
    first = norm_tokens(paras[0])
    bad_first = first[0] in ("we", "we've", "weve", "i", "i'm", "im", "our", "my", "us")
    you_early = any(w in ("you", "your", "you've", "you're", "youve", "youre") for w in first[:8])
    add("G1", (not bad_first) and you_early,
        f"first words: '{' '.join(first[:8])}'" + ("" if not bad_first else " (starts on us)") + ("" if you_early else " (no 'you' in the first 8 words)"))

    # G2 one thing to read for 3 seconds (mechanical part)
    fw = f.get("frame one words", "").lower()
    add("G2", fw.startswith("title only") and bool(f.get("frame one")),
        f"Frame one words: '{f.get('frame one words', 'MISSING')}'" + ("" if fw.startswith("title only") else " (must be 'title only')") + "; the picture is judged by the reviewer on the mockup")

    # G3 gap phrase inside the first 12 spoken words
    gp = norm_tokens(f.get("gap phrase", ""))
    toks = norm_tokens(" ".join(paras))
    pos = None
    if gp:
        for i in range(len(toks) - len(gp) + 1):
            if toks[i:i + len(gp)] == gp:
                pos = i + len(gp)
                break
    add("G3", pos is not None and pos <= 12,
        f"gap phrase '{f.get('gap phrase', 'MISSING')}' ends at spoken word {pos}" if gp else "no 'Gap phrase' field")

    # G4 numeral in the title
    add("G4", bool(re.search(r"\d", ost)), f"title '{ost}' " + ("has a number" if re.search(r"\d", ost) else "has no number"))

    # G10 title shape
    probs = []
    if len(ost_lines) != 2:
        probs.append(f"{len(ost_lines)} lines, not 2")
    for l in ost_lines:
        if len(l) > 22:
            probs.append(f"'{l}' is {len(l)} characters (max 22)")
    if sum(len(l) for l in ost_lines) > 40:
        if fm.get("ost_final_by_luke"):
            # Luke's call on the title (e.g. 6 Nov): each line must still fit; the total is shown, not blocked
            res.append(("G10", "INFO", f"{sum(len(l) for l in ost_lines)} characters in total (over 40): Luke's final title ({fm['ost_final_by_luke']}); each line fits"))
        else:
            probs.append(f"{sum(len(l) for l in ost_lines)} characters in total (max 40)")
    for name in ("title_jargon", "gimmick", "dated"):
        m = rx(name).search(ost)
        if m:
            probs.append(f"{name.replace('_', ' ')}: '{m.group(0)}'")
    for mk in markers:
        if len(mk) > 22:
            probs.append(f"marker '{mk}' is {len(mk)} characters")
    add("G10", not probs, "; ".join(probs) or f"{' / '.join(f'{l} ({len(l)})' for l in ost_lines)}")

    # G13 layers
    lt, lp, l1 = f.get("layer title"), f.get("layer picture"), f.get("layer line one")
    if not (lt and lp and l1):
        add("G13", False, "the three layer lines (title, picture, line one) aren't all in Gate fields")
    else:
        shared = (numbers_in(lp) & numbers_in(ost)) if "none" not in lp.lower()[:6] else set()
        add("G13", len({lt, lp, l1}) == 3 and not shared,
            "layers distinct" + (f"; the picture repeats the title's numbers {sorted(shared)}" if shared else ""))

    # G15 mockup at phone size
    mk = f.get("mockup", "")
    mp = os.path.join(ROOT, mk) if mk else ""
    if not mk or not os.path.exists(mp):
        add("G15", False, f"mockup '{mk or 'MISSING'}' not found")
    else:
        size = png_size(mp)
        phone = mp[:-4] + "-phone.png"
        ok = size == (1080, 1920) and os.path.exists(phone)
        add("G15", ok, f"{mk}: {size}" + ("" if os.path.exists(phone) else "; no -phone.png preview"))

    # G16 the gap fields
    closed = f.get("gap closed by", "")
    held = f.get("gap held by", "")
    in_line_one = gp and " ".join(gp) in " ".join(norm_tokens(paras[0]))
    ok = bool(gp and held and closed) and closed in markers and bool(in_line_one)
    add("G16", ok, f"closed by '{closed or 'MISSING'}'" + ("" if closed in markers else " (not one of the markers)")
        + ("" if in_line_one else "; gap phrase not in line one") + ("" if held else "; no 'Gap held by'"))

    # G31 the turn (mechanical part; Luke 9 Nov, P194): named, spoken before the first marker, the 4 questions answered
    fm_i = next((i for i, (k, _) in enumerate(items) if k == "marker"), len(items))
    hook_text = " ".join(norm_tokens(" ".join(t for k, t in items[:fm_i] if k == "para")))
    turn = re.sub(r'^["\u201c]|["\u201d]$', "", f.get("turn", "").strip())
    turn_toks = " ".join(norm_tokens(turn))
    turn_ok = bool(turn_toks) and turn_toks in hook_text
    q4 = section(text, "The 4 questions") or ""
    q_rows = [r for r in re.findall(r"^\|(.+)\|\s*$", q4, re.M) if not re.match(r"\s*-+\s*\|", r) and not re.match(r"\s*Question", r)]
    answered = [r for r in q_rows if len([c for c in r.split("|") if c.strip()]) >= 2]
    probs31 = []
    if not turn_toks:
        probs31.append("no 'Turn:' in the Gate fields")
    elif not turn_ok:
        probs31.append("the Turn line isn't spoken before the first marker")
    if len(answered) < 4:
        probs31.append(f"'## The 4 questions' has {len(answered)} of 4 answered")
    add("G31", not probs31, "; ".join(probs31) or "turn named and spoken before the method; the 4 questions answered (the reviewer judges if it's new)")

    # G32 a profile sequel is a new reel (Luke 10 Nov, P195): one-change only as a trial; on the profile, 7+ days after the parent
    if fm.get("sequel_of"):
        fmt = fm.get("format", "").lower()
        if "trial" in fmt and "not a trial" not in fmt:
            add("G32", True, "a sequel posted as a trial reel (a one-change test is allowed)")
        else:
            import datetime as _dt
            try:
                gap = (_dt.date.fromisoformat(fm.get("post_date", "")) - _dt.date.fromisoformat(fm.get("parent_posted", ""))).days
            except ValueError:
                gap = None
            add("G32", gap is not None and gap >= 7,
                (f"profile sequel {gap} days after the parent" if gap is not None else "profile sequel: no `parent_posted:` and `post_date:` (YYYY-MM-DD) in the front matter")
                + ("" if gap is not None and gap >= 7 else " (needs 7+ days, or post it as a trial)") + "; the reviewer checks the twist, line one and picture are new")
    else:
        add("G32", True, "not a sequel")

    # G18 retired templates
    m = rx("templates").search(spoken)
    add("G18", not m, f"retired template: '{m.group(0)}'" if m else "no retired templates")

    # G19 hook, CTA, send, save, total length
    first_marker = next((i for i, (k, _) in enumerate(items) if k == "marker"), None)
    hook = [t for k, t in items[:first_marker] if k == "para"] if first_marker is not None else paras
    hook_words = sum(len(words(p)) for p in hook)
    total_words = len(words(spoken))
    cta_idx = next((i for i, (k, t) in enumerate(items) if k == "para" and re.search(r"link in (?:the )?bio", t, re.I)), None)
    probs = []
    if not 80 <= hook_words <= 95:
        probs.append(f"hook {hook_words} words (80 to 95)")
    if not 280 <= total_words <= 330:
        probs.append(f"script {total_words} spoken words (280 to 330) [C3]")
    if not re.search(r"\bsave this\b", " ".join(hook), re.I):
        probs.append("no 'save this' in the hook [C10]")
    if not re.search(r"\bsend (?:\w+ ){0,2}(?:this|it)\b", spoken, re.I):
        probs.append("no send line in the audio")
    if cta_idx is None:
        probs.append("no CTA (link in the bio)")
    else:
        mk_pos = [i for i, (k, _) in enumerate(items) if k == "marker"]
        before = sum(len(words(t)) for k, t in items[:cta_idx] if k == "para")
        cta = items[cta_idx][1]
        if len(mk_pos) < 2 or not (mk_pos[0] < cta_idx < mk_pos[1]):
            probs.append("CTA isn't straight after stage 1")
        if len(sentences(cta)) != 1:
            probs.append(f"CTA is {len(sentences(cta))} sentences")
        if before > 150:
            probs.append(f"CTA starts at spoken word {before} (by 150, about 0:45)")
    add("G19", not probs, "; ".join(probs) or f"hook {hook_words} words, script {total_words}, CTA after stage 1, save and send in")

    # G20 stages
    ok = 3 <= len(markers) <= 5 and markers == markers_in_script
    add("G20", ok, f"{len(markers)} markers" + ("" if markers == markers_in_script else f"; script markers {markers_in_script} don't match the field"))

    # G21 something to keep, for a goal most have
    we = f.get("worked example goal", "").lower()
    cap = section(text, "Caption")
    has_pace = bool(re.search(r"\b[3-9]:[0-5]\d\b.{0,25}\b(?:a K|a mile|per K)|between [3-9]:[0-5]\d and", spoken, re.I))
    probs = []
    every_goal = bool(cap) and all(g in cap for g in ("sub-4", "3:45", "4:30")) if "every common goal" in we else False
    if not (re.match(r"(sub-4|3:45|3:50|3:55|4:00|4-hour|none)\b", we) or every_goal):
        probs.append(f"worked example goal '{we or 'MISSING'}' isn't sub-4 or 3:45 to 4:00, and the caption doesn't carry every common goal (row 23)")
    if not cap or len(cap.strip()) < 100:
        probs.append("no caption carrying the full table")
    elif has_pace and "mile" not in cap.lower():
        probs.append("paces in the audio but no miles in the caption")
    add("G21", not probs, "; ".join(probs) or f"worked example {we}; caption has the table")

    # G22 facts
    facts = section(text, "Facts check")
    probs, open_items = [], []
    if not facts:
        probs.append("no '## Facts check' table")
    else:
        rows = [r for r in facts.splitlines() if r.startswith("|") and not re.match(r"^\|[\s\-|]+\|$", r)][1:]
        if len(rows) < 3:
            probs.append(f"facts table has {len(rows)} rows")
        for r in rows:
            st = r.rstrip("|").split("|")[-1].strip().lower()
            if not re.search(r"pass|luke to ok|cut|flag", st):
                probs.append(f"facts row without a status: {r[:60]}")
            if "luke to ok" in st or "flag" in st:
                open_items.append(r.split("|")[1].strip()[:70])
    for p in paras:
        g = re.search(r"\b(\d+) ?(?:g|gram)s?\b(?= gel)|\b(\d+) ?(?:g|gram)s? gel", p, re.I)
        e = re.search(r"\bevery (\d+)\b", p, re.I)
        if g and e and "gel" in p.lower():
            grams, every = int(g.group(1) or g.group(2)), int(e.group(1))
            want = {20: 20, 22: 20, 25: 20, 30: 30, 40: 40}.get(grams)
            if want and want != every:
                probs.append(f"a {grams}g gel every {every} minutes (FACTS: every {want})")
    m = re.search(r"\b\d+ gels\b", spoken, re.I)
    if m:
        probs.append(f"a total gel count in the audio: '{m.group(0)}'")
    m = rx("race_food").search(spoken)
    if m:
        probs.append(f"real food or the bar in the audio: '{m.group(0)}'")
    add("G22", not probs, "; ".join(probs) or "facts table present; gel numbers match FACTS")
    for o in open_items:
        add("G22", True, f"open for Luke: {o}", "INFO")

    # G23 things they don't do
    m = rx("not_done").search(spoken)
    add("G23", not m, f"'{m.group(0)}' isn't something this audience does" if m else "nothing off the FACTS 'never do' list")

    # G24 sentence length and jargon
    lens = [len(words(s)) for s in all_sents]
    long = [(n, s) for n, s in zip(lens, all_sents) if n > 22]
    probs = [f"{n} words: '{s[:60]}...'" for n, s in long]
    if lens and statistics.median(lens) >= 15:
        probs.append(f"median sentence {statistics.median(lens)} words (under 15)")
    m = rx("jargon").search(spoken_no_talk)
    if m:
        probs.append(f"jargon: '{m.group(0)}'")
    add("G24", not probs, "; ".join(probs) or f"longest sentence {max(lens)} words, median {statistics.median(lens)}")

    # G25 no maths
    probs = []
    m = rx("maths").search(spoken)
    if m:
        probs.append(f"maths: '{m.group(0)}'")
    for s in all_sents:
        n = counted_numbers(s)
        if n > 2:
            probs.append(f"{n} numbers in '{s[:60]}...' [C20]")
    add("G25", not probs, "; ".join(probs) or "no sums; 2 numbers or fewer a sentence")

    # G26 numerals and watch bands
    probs = []
    m = rx("number_words").search(spoken_no_talk)
    if m:
        probs.append(f"written-out number: '{m.group(0)}'")
    for a, b in re.findall(r"between (\d+:\d\d) and (\d+:\d\d)", spoken, re.I):
        sa = int(a.split(":")[0]) * 60 + int(a.split(":")[1])
        sb = int(b.split(":")[0]) * 60 + int(b.split(":")[1])
        if sb - sa != 5 or sa % 5:
            probs.append(f"band {a} to {b} isn't a 5-second watch band")
    for pace in re.findall(r"\b([3-9]:[0-5]\d)\b(?= ?(?:a K|a mile|per K))", spoken):
        if int(pace[-1]) % 5:
            probs.append(f"pace {pace} isn't how the watch shows it")
    add("G26", not probs, "; ".join(probs) or "numerals; bands in 5-second steps")

    # G27 statistics, studies, names, medicine
    probs = []
    for name in ("stats", "medicine", "brands"):
        m = (re.compile(WORDS["stats"], re.I) if name == "stats" else rx(name)).search(spoken)
        if m:
            probs.append(f"{name}: '{m.group(0)}'")
    add("G27", not probs, "; ".join(probs) or "none")

    # G28 dated words
    m = rx("dated").search(spoken + " " + ost)
    add("G28", not m, f"dated: '{m.group(0)}'" if m else "nothing that dates")

    # G29 humanizer
    try:
        out = subprocess.run([sys.executable, HUMANIZER, path], capture_output=True, text=True, timeout=60).stdout
        flags = int(re.search(r"(\d+) flags", out).group(1))
        detail = [l.strip() for l in out.splitlines() if l.strip().startswith("line ")][:4]
    except Exception as e:  # noqa
        flags, detail = 99, [f"humanizer didn't run: {e}"]
    has_table = section(text, "Humanizer") is not None
    add("G29", flags == 0 and has_table, f"humanizer {flags} flags" + ("" if has_table else "; no '## Humanizer' table") + (f": {detail}" if flags else ""))

    # G30 independent review, current hash, teleprompter, forecast
    probs = []
    h = script_hash(text)
    rpath = os.path.join(REVIEW_DIR, os.path.basename(path))
    if not os.path.exists(rpath):
        probs.append(f"no independent review at gate/reviews/{os.path.basename(path)}")
    else:
        rv = read(rpath)
        m = re.search(r"Script hash:\s*([0-9a-f]+)", rv)
        if not m or m.group(1) != h:
            probs.append(f"review is for another version (hash {m.group(1) if m else 'none'}, script {h}): re-run the reviewer")
        verdicts = dict(re.findall(r"^\|\s*(G\d+)\b[^|]*\|\s*(PASS|FAIL)\b", rv, re.M))
        missing = [t for t in REVIEWER_TESTS if t not in verdicts]
        fails = [t for t, v in verdicts.items() if v == "FAIL"]
        if missing:
            probs.append(f"review has no verdict for {missing}")
        # A reviewer FAIL can be held as BLOCKED only when the front matter says `gate: blocked`,
        # lists the test in `blocked_on:`, and the reviewer's own row says it needs Luke.
        # AUTO fails can never be held. A blocked script is never "ready to film".
        blocked_on = re.findall(r"G\d+", fm.get("blocked_on", "")) if fm.get("gate") == "blocked" else []
        rows = dict(re.findall(r"^\|\s*(G\d+)\b([^\n]*)$", rv, re.M))
        held = [t for t in fails if t in blocked_on and "luke" in rows.get(t, "").lower()]
        fails = [t for t in fails if t not in held]
        risks = [t for t in fails if t in RISK_REVIEWER]
        fails = [t for t in fails if t not in RISK_REVIEWER]
        if fails:
            probs.append(f"reviewer FAIL on {fails} (BLOCK tier)")
        if risks:
            box = section(text, "Known risks") or ""
            missing_box = [t for t in risks if t not in box]
            if missing_box:
                probs.append(f"RISK fails {missing_box} aren't in the script's '## Known risks' box for Luke")
            for t in risks:
                add(t, True, "RISK (reviewer FAIL on a judgement test): in the Known risks box for Luke", "RISK")
        for t in held:
            add(t, True, "BLOCKED on Luke (the reviewer says this needs his decision); NOT ready to film", "BLKD")
    tp = fm.get("teleprompter")
    if tp:
        tpp = os.path.join(os.path.dirname(path), tp)
        if not os.path.exists(tpp):
            probs.append(f"teleprompter {tp} missing")
        else:
            tl = [l.strip() for l in read(tpp).splitlines() if l.strip()]
            if tl != paras:
                probs.append("teleprompter doesn't match the script word for word")
    fc = f.get("forecast", "")
    if not fc or not re.search(r"\d.*\bto\b.*\d", fc):
        probs.append("no forecast range")
    if re.search(r"confident|will do well|sure to", text, re.I):
        probs.append("says 'confident' (P190)")
    add("G30", not probs, "; ".join(probs) or f"reviewed at hash {h}; teleprompter matches; forecast is a range")
    return res


# ---------- git helpers ----------
def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True).stdout


def is_script(p):
    return re.search(r"(^|/)ideas/.*script[^/]*\.md$", p) is not None


def gated_or_new(paths, new):
    out, errs = [], []
    for p in paths:
        full = os.path.join(ROOT, p)
        if not os.path.exists(full) or not is_script(p):
            continue
        if front_matter(read(full)).get("gate"):
            out.append(full)
        elif p in new:
            errs.append(f"{p}: a new script with no `gate:` in its front matter. Every new script goes through the gate (GATE.md).")
    return out, errs


def report(path, res, brief=False):
    fails = [r for r in res if r[1] == "FAIL"]
    if brief:
        for t, lv, msg in res:
            if lv in ("FAIL", "BLKD"):
                print(f"{os.path.relpath(path, ROOT)} {t} {lv}: {msg}")
        return not fails
    print(f"\n== GATE {os.path.relpath(path, ROOT)}")
    for t, lv, msg in res:
        print(f"  {t:4} {lv:4}  {msg}")
    blk = sorted({r[0] for r in res if r[1] == "BLKD"})
    verdict = ('FAIL on ' + ', '.join(sorted({r[0] for r in fails}, key=lambda x: int(x[1:])))) if fails else (
        f"BLOCKED on Luke ({', '.join(blk)}): every other test passes; NOT ready to film" if blk else (
        "PASS, with known risks for Luke: " + ", ".join(sorted({r[0] for r in res if r[1] == "RISK"}, key=lambda x: int(x[1:]))) if any(r[1] == "RISK" for r in res) else "PASS"))
    print(f"  -> {verdict}")
    return not fails


# ---------- the review packet (fast reviews, 5 Nov) ----------
ALWAYS_REGRADE = ["G13", "G16", "G18"]  # whole-script tests: re-graded on every version
FRAME_TESTS = ["G2", "G14"]  # re-graded whenever the mockup is new to the last review


def gate_tests():
    g = read(os.path.join(ROOT, "GATE.md"))
    out = {}
    for m in re.finditer(r"^### (G\d+) · (.+?) · (\w+)\n\*\*Test:\*\* (.*?)\n\*\*Evidence", g, re.M | re.S):
        out[m.group(1)] = (m.group(2), " ".join(m.group(4).split()))
    return out


def script_files(exclude):
    fs = sorted(glob.glob(os.path.join(ROOT, "ideas/engine-room-nutrition/2026-*-script-*.md")))
    return [f for f in fs if os.path.abspath(f) != os.path.abspath(exclude)]


def stack_of(path):
    t = read(path)
    title = (re.search(r"^# (.+)$", t, re.M) or re.search(r"\*\*OST:\*\*\s*(.+)", t) or [None, "?"])[1]
    items = script_items(t) or [("para", m.group(1)) for m in re.finditer(r'^"(.+)"\s*$', t, re.M)]
    paras = [x for k, x in items if k == "para"]
    mk = [i for i, (k, _) in enumerate(items) if k == "marker"]
    rehook = items[mk[-1] - 1][1] if mk and mk[-1] > 0 and items[mk[-1] - 1][0] == "para" else ""
    return title.strip(), paras, rehook


def previous_review(path, h):
    rp = os.path.join(REVIEW_DIR, os.path.basename(path))
    if not os.path.exists(rp):
        return None
    rv = read(rp)
    return dict((r[0], (r[1], r[2])) for r in re.findall(r"^\|\s*(G\d+)\b[^|]*\|\s*(PASS|FAIL)[^|]*\|\s*(.*?)\s*\|", rv, re.M))


def packet(path):
    """One file with everything the reviewer grades against, instead of ~15 reads."""
    text = read(path)
    h = script_hash(text)
    items = script_items(text)
    spoken = " ".join(t for k, t in items if k == "para")
    tests = gate_tests()
    prev = previous_review(path, h)
    regrade, carried = list(REVIEWER_TESTS), []
    if prev:
        regrade = []
        # a new frame one (a mockup the last review never saw) re-grades the frame tests
        mock = os.path.basename(fields(text).get("mockup", "")).replace(".png", "")
        rp_text = read(os.path.join(ROOT, "gate", "reviews", os.path.basename(path)))
        new_frame = bool(mock) and mock not in rp_text
        for t in REVIEWER_TESTS:
            v, quote = prev.get(t, ("FAIL", ""))
            quotes = re.findall(r'"([^"]{12,})"', quote)
            still = all(q.rstrip(".?!…").split("...")[0] in spoken + text for q in quotes) if quotes else False
            if v == "FAIL" or t in ALWAYS_REGRADE or not still or (t in FRAME_TESTS and new_frame):
                regrade.append(t)
            else:
                carried.append(t)
    con = read(os.path.join(ROOT, "gate", "contradictions.md"))
    settled = (re.search(r"## Settled by Luke.*?(?=\n## )", con, re.S) or [""])[0]
    claude = read(os.path.join(ROOT, "CLAUDE.md"))
    ledger = (re.search(r"\| # \| Failure .*?(?=\n\n## )", claude, re.S) or [""])[0]
    out = [f"# Review packet: {os.path.basename(path)}", f"Script hash: {h}", "",
           "## Grade these tests (PASS or FAIL, quote the line)" + (" (re-review: the rest carry over)" if prev else "")]
    for t in regrade:
        name, body = tests.get(t, ("?", "?"))
        out.append(f"- **{t} {name}** [{'BLOCK' if t in BLOCK_REVIEWER else 'RISK'}]: {body}")
    if carried:
        out += ["", "## Carried over from the last review (their quoted lines are unchanged): copy these rows as PASS"]
        out += [f"- {t}: {prev[t][1][:160]}" for t in carried]
    out += ["", "## Luke's settled decisions", settled.strip(), "",
            "## The script file (as written)", text.split("## Humanizer")[0].strip(), "",
            "## The last 3 scripts' hook lines (for G18 shapes and G8 repeats)"]
    others = script_files(path)
    for f in others[-3:]:
        title, paras, rehook = stack_of(f)
        out.append(f"- **{os.path.basename(f)}** {title}: line one \"{paras[0] if paras else ''}\" / pain \"{paras[1] if len(paras) > 1 else ''}\" / dream \"{paras[2] if len(paras) > 2 else ''}\" / rehook \"{rehook}\" / send \"{paras[-1] if paras else ''}\"")
    out += ["", "## Every script we've written: title and line one (G8 repeats; grep the file if one looks close)"]
    for f in others:
        title, paras, _ = stack_of(f)
        out.append(f"- {os.path.basename(f)[:10]} {title[:60]} | {paras[0][:110] if paras else ''}")
    out += ["", "## The failure ledger (repeats)", ledger.strip(), "", "## FACTS.md", read(os.path.join(ROOT, "FACTS.md"))]
    pdir = os.path.join(ROOT, "gate", "packets")
    os.makedirs(pdir, exist_ok=True)
    pp = os.path.join(pdir, os.path.basename(path))
    open(pp, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"{os.path.relpath(pp, ROOT)}: grade {len(regrade)} ({', '.join(regrade)}), carried {len(carried)}; {len(open(pp).read())//4} tokens approx")
    return 0


def main(argv):
    if argv[:1] == ["--packet"]:
        return packet(os.path.abspath(argv[1]))
    brief = "--brief" in argv
    argv = [a for a in argv if a != "--brief"]
    if argv[:1] == ["--hash"]:
        print(script_hash(read(argv[1])))
        return 0
    errs = []
    if argv[:1] == ["--staged"]:
        st = git("diff", "--cached", "--name-status").splitlines()
        paths = [l.split("\t")[-1] for l in st if not l.startswith("D")]
        new = {l.split("\t")[-1] for l in st if l.startswith("A")}
        files, errs = gated_or_new(paths, new)
    elif argv[:1] == ["--changed"]:
        st = git("status", "--porcelain").splitlines()
        paths = [l[3:].strip() for l in st]
        new = {l[3:].strip() for l in st if l.startswith("??") or l.startswith("A")}
        files, errs = gated_or_new(paths, new)
    else:
        files = [os.path.abspath(a) for a in argv]
    ok = True
    for e in errs:
        print(e)
        ok = False
    for p in files:
        ok = report(p, run(p), brief) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
