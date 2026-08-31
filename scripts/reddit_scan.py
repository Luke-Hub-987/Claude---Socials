#!/usr/bin/env python3
"""Scan subreddits for top posts worth adapting into content ideas.

Usage:
    python3 reddit_scan.py "subreddit1,subreddit2" --output /tmp/reddit_posts.json

Requires REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT in
the environment (or a .env file in the repo root).
"""
import argparse
import json
import os
import sys
from pathlib import Path

import praw
from dotenv import load_dotenv

POSTS_PER_SUBREDDIT = 15
TIME_FILTER = "month"


def main():
    parser = argparse.ArgumentParser(description="Scan subreddits for top posts.")
    parser.add_argument("subreddits", help="Comma-separated subreddit names (r/ prefix optional)")
    parser.add_argument("--output", required=True, help="Path to write JSON output")
    args = parser.parse_args()

    load_dotenv()
    client_id = os.environ.get("REDDIT_CLIENT_ID")
    client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
    user_agent = os.environ.get("REDDIT_USER_AGENT")
    if not (client_id and client_secret and user_agent):
        print("ERROR: REDDIT_CLIENT_ID / REDDIT_CLIENT_SECRET / REDDIT_USER_AGENT not set.", file=sys.stderr)
        sys.exit(1)

    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

    names = [s.strip().lstrip("r/").lstrip("/r/") for s in args.subreddits.split(",") if s.strip()]

    posts = []
    errors = []
    for name in names:
        try:
            subreddit = reddit.subreddit(name)
            for submission in subreddit.top(time_filter=TIME_FILTER, limit=POSTS_PER_SUBREDDIT):
                posts.append({
                    "subreddit": name,
                    "title": submission.title,
                    "url": f"https://www.reddit.com{submission.permalink}",
                    "score": submission.score,
                    "num_comments": submission.num_comments,
                    "author": str(submission.author) if submission.author else "[deleted]",
                    "selftext": (submission.selftext or "")[:500],
                })
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
