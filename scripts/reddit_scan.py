#!/usr/bin/env python3
"""Scan subreddits for top posts worth adapting into content ideas.

Usage:
    python3 reddit_scan.py "subreddit1,subreddit2" --output /tmp/reddit_posts.json

Uses Reddit's public, unauthenticated JSON endpoints
(reddit.com/r/<sub>/top.json), not the official OAuth Data API — no
developer app registration needed. This is the fallback for personal,
low-volume, read-only use when a Reddit dev app isn't available (e.g.
Reddit's tightened developer signup rules). It's more likely to get
rate-limited (HTTP 429) than an authenticated app, especially from a
datacenter IP, so failures here are handled per-subreddit rather than
aborting the whole run. Requires REDDIT_USER_AGENT in the environment
(or .env) — Reddit rejects generic/default user agents.
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

POSTS_PER_SUBREDDIT = 15
TIME_FILTER = "month"  # top.json ?t= param: hour|day|week|month|year|all
REQUEST_DELAY_SECONDS = 2  # be polite to the unauthenticated endpoint


def fetch_top_posts(name, user_agent):
    url = f"https://www.reddit.com/r/{name}/top.json"
    resp = requests.get(
        url,
        params={"t": TIME_FILTER, "limit": POSTS_PER_SUBREDDIT},
        headers={"User-Agent": user_agent},
        timeout=15,
    )
    if resp.status_code == 429:
        raise RuntimeError("rate-limited (429) — try again later or with fewer subreddits")
    resp.raise_for_status()
    data = resp.json()
    posts = []
    for child in data.get("data", {}).get("children", []):
        d = child.get("data", {})
        posts.append({
            "subreddit": name,
            "title": d.get("title", ""),
            "url": f"https://www.reddit.com{d.get('permalink', '')}",
            "score": d.get("score", 0),
            "num_comments": d.get("num_comments", 0),
            "author": d.get("author") or "[deleted]",
            "selftext": (d.get("selftext") or "")[:500],
        })
    return posts


def main():
    parser = argparse.ArgumentParser(description="Scan subreddits for top posts.")
    parser.add_argument("subreddits", help="Comma-separated subreddit names (r/ prefix optional)")
    parser.add_argument("--output", required=True, help="Path to write JSON output")
    args = parser.parse_args()

    load_dotenv()
    user_agent = os.environ.get("REDDIT_USER_AGENT")
    if not user_agent:
        print("ERROR: REDDIT_USER_AGENT not set.", file=sys.stderr)
        sys.exit(1)

    names = [s.strip().lstrip("r/").lstrip("/r/") for s in args.subreddits.split(",") if s.strip()]

    posts = []
    errors = []
    for i, name in enumerate(names):
        try:
            if i > 0:
                time.sleep(REQUEST_DELAY_SECONDS)
            posts.extend(fetch_top_posts(name, user_agent))
        except Exception as e:
            errors.append(f"r/{name}: {e}")

    posts.sort(key=lambda p: p["score"], reverse=True)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump({"posts": posts, "errors": errors}, f, indent=2)

    print(f"Wrote {len(posts)} posts to {args.output}")
    if errors:
        print(f"Errors: {errors}", file=sys.stderr)


if __name__ == "__main__":
    main()
