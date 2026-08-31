#!/usr/bin/env python3
"""Scan subreddits for top posts worth adapting into content ideas.

Usage:
    python3 reddit_scan.py "subreddit1,subreddit2" --output /tmp/reddit_posts.json

Uses the Apify "trudax/reddit-scraper-lite" actor rather than hitting
reddit.com directly. Two things ruled out the direct approach: Reddit's
current developer signup rules made an official OAuth app hard to get
approved, and even the public unauthenticated JSON endpoints
(reddit.com/r/<sub>/top.json) get a 403 straight from Reddit's own
servers when called from a datacenter IP (confirmed directly, this
isn't a guess). The Apify actor scrapes Reddit's own listing pages
through Apify's infrastructure and returns real, current post data.
Requires APIFY_API_TOKEN in the environment (or a .env file in the
repo root) — the same token ig_outliers.py uses, no separate Reddit
credential needed.
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

ACTOR_ID = "trudax~reddit-scraper-lite"
POSTS_PER_SUBREDDIT = 15
TIME_FILTER = "month"  # matches the actor's "time" enum: hour|day|week|month|year|all
POLL_INTERVAL_SECONDS = 5
MAX_WAIT_SECONDS = 180


def strip_subreddit_prefix(raw):
    name = raw.strip()
    if name.startswith("/r/"):
        name = name[3:]
    elif name.startswith("r/"):
        name = name[2:]
    return name.strip("/")


def run_actor(token, names):
    run_url = f"https://api.apify.com/v2/acts/{ACTOR_ID}/runs?token={token}"
    payload = {
        "startUrls": [{"url": f"https://www.reddit.com/r/{name}/top/?t={TIME_FILTER}"} for name in names],
        "skipComments": True,
        "includeMediaLinks": True,
        "maxItems": POSTS_PER_SUBREDDIT * len(names),
        "maxPostCount": POSTS_PER_SUBREDDIT,
    }
    resp = requests.post(run_url, json=payload, timeout=30)
    resp.raise_for_status()
    run = resp.json()["data"]
    run_id = run["id"]

    status_url = f"https://api.apify.com/v2/actor-runs/{run_id}?token={token}"
    waited = 0
    status = "READY"
    while waited < MAX_WAIT_SECONDS:
        resp = requests.get(status_url, timeout=30)
        resp.raise_for_status()
        status = resp.json()["data"]["status"]
        if status in ("SUCCEEDED", "FAILED", "TIMED-OUT", "ABORTED"):
            break
        time.sleep(POLL_INTERVAL_SECONDS)
        waited += POLL_INTERVAL_SECONDS

    if status != "SUCCEEDED":
        raise RuntimeError(f"Apify run ended with status {status}")

    dataset_id = requests.get(status_url, timeout=30).json()["data"]["defaultDatasetId"]
    items_url = f"https://api.apify.com/v2/datasets/{dataset_id}/items?token={token}&clean=true"
    resp = requests.get(items_url, timeout=60)
    resp.raise_for_status()
    return resp.json()


def main():
    parser = argparse.ArgumentParser(description="Scan subreddits for top posts.")
    parser.add_argument("subreddits", help="Comma-separated subreddit names (r/ prefix optional)")
    parser.add_argument("--output", required=True, help="Path to write JSON output")
    args = parser.parse_args()

    load_dotenv()
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        print("ERROR: APIFY_API_TOKEN not set. Add it to .env or the environment.", file=sys.stderr)
        sys.exit(1)

    names = [strip_subreddit_prefix(s) for s in args.subreddits.split(",") if s.strip()]

    errors = []
    try:
        items = run_actor(token, names)
    except Exception as e:
        print(f"ERROR: Apify run failed: {e}", file=sys.stderr)
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w") as f:
            json.dump({"posts": [], "errors": [str(e)]}, f, indent=2)
        sys.exit(1)

    posts = []
    seen_communities = set()
    for item in items:
        if item.get("dataType") not in (None, "post"):
            continue
        community = item.get("parsedCommunityName") or (item.get("communityName") or "").lstrip("r/")
        seen_communities.add(community)
        posts.append({
            "subreddit": community,
            "title": item.get("title", ""),
            "url": item.get("url") or item.get("link", ""),
            "score": item.get("upVotes", 0),
            "num_comments": item.get("numberOfComments", 0),
            "author": item.get("username") or "[deleted]",
            "selftext": (item.get("body") or "")[:500],
        })

    for name in names:
        if name not in seen_communities:
            errors.append(f"r/{name}: no posts returned (private, banned, or scrape failed)")

    posts.sort(key=lambda p: p["score"], reverse=True)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump({"posts": posts, "errors": errors}, f, indent=2)

    print(f"Wrote {len(posts)} posts to {args.output}")
    if errors:
        print(f"Errors: {errors}", file=sys.stderr)


if __name__ == "__main__":
    main()
