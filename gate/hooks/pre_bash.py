#!/usr/bin/env python3
"""PreToolUse(Bash): no commit carries a script that fails the gate, and no --no-verify (P190)."""
import json, os, re, subprocess, sys

data = json.load(sys.stdin)
cmd = (data.get("tool_input") or {}).get("command", "")
# Only a real `git commit` at the start of a shell command counts, not the words inside a heredoc.
commit = re.search(r"(?:^|[;&|]\s*|\n)\s*git\s+(?:-C\s+\S+\s+)?commit\b([^\n;&|]*)", cmd)
if not commit:
    sys.exit(0)
args = commit.group(1)
if re.search(r"(?:^|\s)(?:--no-verify|-n)(?:\s|$)", args):
    print("GATE (P190): skipping the commit hook isn't allowed. Fix the script so it passes GATE.md.", file=sys.stderr)
    sys.exit(2)
root = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
mode = "--changed" if re.search(r"(?:^|\s)-a\w*|--all", args) else "--staged"
out = subprocess.run([sys.executable, os.path.join(root, "gate", "check.py"), mode, "--brief"],
                     cwd=root, capture_output=True, text=True)
if out.returncode != 0:
    print("GATE (P190): a script fails the gate, so it can't be committed.\n" + out.stdout[-3000:], file=sys.stderr)
    sys.exit(2)
sys.exit(0)
