#!/usr/bin/env python3
"""Run any Apify actor with a JSON input and save the raw items (topic map, P243).

    APIFY_API_TOKEN=... python3 scripts/apify_run.py <actor~id> <input.json> --output <items.json>

The token goes in an Authorization header, never the URL. Runs that outlast
--max-wait are aborted so they don't keep spending credit.
"""
import argparse, json, os, sys, time
from pathlib import Path
from _http import make_session

API = "https://api.apify.com/v2"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("actor")
    ap.add_argument("input")
    ap.add_argument("--output", required=True)
    ap.add_argument("--max-wait", type=int, default=900)
    a = ap.parse_args()
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        sys.exit("APIFY_API_TOKEN not set")
    s = make_session()
    s.headers["Authorization"] = f"Bearer {token}"
    payload = json.loads(Path(a.input).read_text())
    r = s.post(f"{API}/acts/{a.actor}/runs", json=payload, timeout=60)
    r.raise_for_status()
    run = r.json()["data"]
    rid = run["id"]
    waited, status = 0, run["status"]
    while status not in ("SUCCEEDED", "FAILED", "TIMED-OUT", "ABORTED") and waited < a.max_wait:
        time.sleep(10)
        waited += 10
        run = s.get(f"{API}/actor-runs/{rid}", timeout=30).json()["data"]
        status = run["status"]
    if status not in ("SUCCEEDED", "FAILED", "TIMED-OUT", "ABORTED"):
        s.post(f"{API}/actor-runs/{rid}/abort", timeout=30)
        sys.exit(f"aborted after {a.max_wait}s")
    items = s.get(f"{API}/datasets/{run['defaultDatasetId']}/items?clean=true", timeout=120).json()
    Path(a.output).parent.mkdir(parents=True, exist_ok=True)
    Path(a.output).write_text(json.dumps(items, indent=1))
    usage = run.get("usageTotalUsd")
    print(f"{status}: {len(items)} items, cost ${usage}")


if __name__ == "__main__":
    main()
