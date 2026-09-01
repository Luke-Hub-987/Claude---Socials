#!/usr/bin/env python3
"""Scan TikTok competitor accounts for outlier videos via Apify.

Uses the "clockworks/tiktok-scraper" actor. Requires APIFY_API_TOKEN
in the environment (or a .env file in the repo root) — the same token
ig_outliers.py and reddit_scan.py use, no separate TikTok credential
needed.

Usage:
    python3 tiktok_outliers.py handle1 handle2 --output /tmp/tiktok_outliers.json
"""
import argparse
import json
import os
import statistics
import sys
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

from _http import make_session

ACTOR_ID = "clockworks~tiktok-scraper"
VIDEOS_PER_HANDLE = 20
OUTLIER_MULTIPLIER = 2.0
POLL_INTERVAL_SECONDS = 5
MAX_WAIT_SECONDS = 480  # see reddit_scan.py / ig_outliers.py for why this is generous


def run_actor(token, handles):
    session = make_session()
    run_url = f"https://api.apify.com/v2/acts/{ACTOR_ID}/runs?token={token}"
    payload = {
        "profiles": [h.lstrip("@") for h in handles],
        "resultsPerPage": VIDEOS_PER_HANDLE,
        "profileSorting": "latest",
        "excludePinnedPosts": True,
        "shouldDownloadVideos": False,
        "shouldDownloadCovers": False,
        "shouldDownloadSubtitles": False,
        "shouldDownloadSlideshowImages": False,
    }
    resp = session.post(run_url, json=payload, timeout=30)
    resp.raise_for_status()
    run = resp.json()["data"]
    run_id = run["id"]

    status_url = f"https://api.apify.com/v2/actor-runs/{run_id}?token={token}"
    waited = 0
    status = "READY"
    while waited < MAX_WAIT_SECONDS:
        resp = session.get(status_url, timeout=30)
        resp.raise_for_status()
        status = resp.json()["data"]["status"]
        if status in ("SUCCEEDED", "FAILED", "TIMED-OUT", "ABORTED"):
            break
        time.sleep(POLL_INTERVAL_SECONDS)
        waited += POLL_INTERVAL_SECONDS

    if status not in ("SUCCEEDED", "FAILED", "TIMED-OUT", "ABORTED"):
        try:
            session.post(f"https://api.apify.com/v2/actor-runs/{run_id}/abort?token={token}", timeout=30)
        except requests.RequestException:
            pass
        raise RuntimeError(f"Apify run did not finish within {MAX_WAIT_SECONDS}s, aborted it (was: {status})")

    if status != "SUCCEEDED":
        raise RuntimeError(f"Apify run ended with status {status}")

    dataset_id = session.get(status_url, timeout=30).json()["data"]["defaultDatasetId"]
    items_url = f"https://api.apify.com/v2/datasets/{dataset_id}/items?token={token}&clean=true"
    resp = session.get(items_url, timeout=60)
    resp.raise_for_status()
    return resp.json()


def find_outliers(handle, items):
    engagements = []
    for item in items:
        stats = item.get("diggCount", 0) + item.get("commentCount", 0) + item.get("shareCount", 0)
        engagements.append(stats)
    if len(engagements) < 3:
        return []
    baseline = statistics.median(engagements)
    if baseline == 0:
        return []
    outliers = []
    for item, engagement in zip(items, engagements):
        multiplier = engagement / baseline
        if multiplier >= OUTLIER_MULTIPLIER:
            outliers.append({
                "handle": handle,
                "url": item.get("webVideoUrl"),
                "caption": (item.get("text") or "")[:300],
                "plays": item.get("playCount"),
                "likes": item.get("diggCount"),
                "comments": item.get("commentCount"),
                "shares": item.get("shareCount"),
                "outlier_multiplier": round(multiplier, 2),
                "created_at": item.get("createTimeISO"),
            })
    outliers.sort(key=lambda o: o["outlier_multiplier"], reverse=True)
    return outliers


def main():
    parser = argparse.ArgumentParser(description="Find outlier TikTok videos across competitor accounts.")
    parser.add_argument("handles", nargs="+", help="TikTok handles, with or without @")
    parser.add_argument("--output", required=True, help="Path to write JSON output")
    args = parser.parse_args()

    load_dotenv()
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        print("ERROR: APIFY_API_TOKEN not set. Add it to .env or the environment.", file=sys.stderr)
        sys.exit(1)

    errors = []
    try:
        items = run_actor(token, args.handles)
    except Exception as e:
        print(f"ERROR: Apify run failed: {e}", file=sys.stderr)
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w") as f:
            json.dump({"outliers": [], "errors": [str(e)]}, f, indent=2)
        sys.exit(1)

    by_handle = {}
    for item in items:
        author = ((item.get("authorMeta") or {}).get("name") or "").lower()
        by_handle.setdefault(author, []).append(item)

    all_outliers = []
    for handle in args.handles:
        clean = handle.lstrip("@").lower()
        videos = by_handle.get(clean, [])
        if not videos:
            errors.append(f"{handle}: no videos returned (private, missing, banned, or scrape failed)")
            continue
        all_outliers.extend(find_outliers(handle, videos))

    all_outliers.sort(key=lambda o: o["outlier_multiplier"], reverse=True)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump({"outliers": all_outliers, "errors": errors}, f, indent=2)

    print(f"Wrote {len(all_outliers)} outliers to {args.output}")
    if errors:
        print(f"Errors: {errors}", file=sys.stderr)


if __name__ == "__main__":
    main()
