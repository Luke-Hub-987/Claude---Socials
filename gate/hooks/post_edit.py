#!/usr/bin/env python3
"""PostToolUse(Write|Edit): re-run the gate on a gated script the moment it changes, and tell Claude what fails."""
import json, os, re, subprocess, sys

data = json.load(sys.stdin)
path = (data.get("tool_input") or {}).get("file_path", "")
if not re.search(r"/ideas/.*script[^/]*\.md$", path) or not os.path.exists(path):
    sys.exit(0)
if "gate:" not in open(path, encoding="utf-8").read()[:600]:
    if re.search(r"/ideas/engine-room-nutrition/\d{4}-\d\d-\d\d-script-", path):
        print(f"GATE (P190): {os.path.basename(path)} has no `gate:` front matter. New scripts go through GATE.md.", file=sys.stderr)
        sys.exit(2)
    sys.exit(0)
root = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
out = subprocess.run([sys.executable, os.path.join(root, "gate", "check.py"), path, "--brief"], cwd=root, capture_output=True, text=True)
if out.returncode != 0:
    print("GATE (P190): this script is NOT ready for Luke. Failing:\n" + out.stdout[-2500:], file=sys.stderr)
    sys.exit(2)
sys.exit(0)
