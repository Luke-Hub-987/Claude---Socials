#!/usr/bin/env python3
"""Stop: the turn can't end quietly with a failing script in the working tree (P190).
First time: block, so the fails get fixed. If it's still failing on the retry, let the turn end
but put a warning in front of Luke saying the script is not ready."""
import json, os, subprocess, sys

data = json.load(sys.stdin)
root = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
out = subprocess.run([sys.executable, os.path.join(root, "gate", "check.py"), "--changed", "--brief"], cwd=root, capture_output=True, text=True)
if out.returncode == 0:
    if "BLKD" in out.stdout:
        print(json.dumps({"systemMessage": "GATE: a script is BLOCKED on Luke's decision and is not ready to film.\n" + out.stdout[-800:]}))
    sys.exit(0)
if not data.get("stop_hook_active"):
    print("GATE (P190): a changed script fails the gate. Fix every FAIL (or tell Luke plainly it is blocked and why) before finishing:\n" + out.stdout[-2500:], file=sys.stderr)
    sys.exit(2)
print(json.dumps({"systemMessage": "GATE WARNING: a script in the working tree still FAILS GATE.md. It is not ready to film.\n" + out.stdout[-1200:]}))
sys.exit(0)
