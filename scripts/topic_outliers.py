#!/usr/bin/env python3
"""Topic map (P243): per-account outliers from raw Apify pulls.

    python3 scripts/topic_outliers.py research/topic-map/raw/ig-all.json research/topic-map/raw/tt-kelsey.json --min-x 3 --out research/topic-map/outliers.csv

Views only (IG videoPlayCount, TikTok playCount). Baseline = the account's median
over its videos in the pull; pinned posts and ads are skipped.
"""
import argparse, csv, json, statistics
from collections import defaultdict


def rows(path):
    for x in json.load(open(path)):
        if "playCount" in x:  # TikTok
            if x.get("isPinned") or x.get("isAd") or x.get("isSponsored"):
                continue
            yield dict(account=x["authorMeta"]["name"], platform="tiktok", views=x.get("playCount") or 0,
                       saves=x.get("collectCount"), shares=x.get("shareCount"), date=x.get("createTimeISO", "")[:10],
                       secs=(x.get("videoMeta") or {}).get("duration"), url=x.get("webVideoUrl"),
                       text=(x.get("text") or "").replace("\n", " ")[:220], followers=x["authorMeta"].get("fans"))
        elif x.get("type") == "Video" or x.get("productType") == "clips":
            if x.get("isPinned") or x.get("paidPartnership") or (x.get("caption") or "").startswith("AD"):
                continue
            yield dict(account=x.get("ownerUsername"), platform="instagram", views=x.get("videoPlayCount") or x.get("videoViewCount") or 0,
                       saves=None, shares=None, date=(x.get("timestamp") or "")[:10], secs=x.get("videoDuration"),
                       url=x.get("url"), text=(x.get("caption") or "").replace("\n", " ")[:220], followers=None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--min-x", type=float, default=3)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    by = defaultdict(list)
    for f in a.files:
        for r in rows(f):
            by[(r["platform"], r["account"])].append(r)
    out, summary = [], []
    for (plat, acc), rs in by.items():
        if len(rs) < 10:  # collabs and tagged posts from accounts we didn't pull
            continue
        med = statistics.median(r["views"] for r in rs) or 1
        summary.append((plat, acc, len(rs), int(med), max(r["views"] for r in rs)))
        for r in rs:
            r["median"], r["x"] = int(med), round(r["views"] / med, 1)
            if r["x"] >= a.min_x:
                out.append(r)
    out.sort(key=lambda r: -r["x"])
    with open(a.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["x", "views", "median", "account", "platform", "date", "secs", "saves", "shares", "url", "text", "followers"])
        w.writeheader()
        w.writerows(out)
    for s in sorted(summary, key=lambda s: -s[3]):
        print(f"{s[0]:9} {s[1]:26} videos {s[2]:3}  median {s[3]:>9,}  max {s[4]:>10,}")
    print(f"{len(out)} outliers at {a.min_x}x+")


if __name__ == "__main__":
    main()
