#!/usr/bin/env python3
"""Scan a list of YouTube channels for outlier videos.

An "outlier" is a video that overperformed relative to that channel's
own baseline (its median views over the same recent window). This
finds videos worth studying regardless of channel size.

Usage:
    python3 yt_outliers.py @handle1 @handle2 ... --output /tmp/yt_outliers.json

Requires YOUTUBE_API_KEY in the environment (or a .env file in the
repo root, loaded via python-dotenv).
"""
import argparse
import json
import os
import statistics
import sys
from pathlib import Path

from dotenv import load_dotenv
from googleapiclient.discovery import build

MAX_VIDEOS_PER_CHANNEL = 25
OUTLIER_MULTIPLIER = 2.0


def resolve_channel_id(youtube, handle):
    handle = handle.lstrip("@")
    resp = youtube.channels().list(part="id,snippet,contentDetails", forHandle=handle).execute()
    items = resp.get("items", [])
    if not items:
        resp = youtube.search().list(part="snippet", q=handle, type="channel", maxResults=1).execute()
        items = resp.get("items", [])
        if not items:
            return None, None
        channel_id = items[0]["snippet"]["channelId"]
        resp = youtube.channels().list(part="contentDetails", id=channel_id).execute()
        items = resp.get("items", [])
        if not items:
            return None, None
        uploads_playlist = items[0]["contentDetails"]["relatedPlaylists"]["uploads"]
        return channel_id, uploads_playlist
    channel_id = items[0]["id"]
    uploads_playlist = items[0]["contentDetails"]["relatedPlaylists"]["uploads"]
    return channel_id, uploads_playlist


def fetch_recent_video_ids(youtube, uploads_playlist, limit):
    video_ids = []
    page_token = None
    while len(video_ids) < limit:
        resp = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=uploads_playlist,
            maxResults=min(50, limit - len(video_ids)),
            pageToken=page_token,
        ).execute()
        video_ids.extend(item["contentDetails"]["videoId"] for item in resp.get("items", []))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return video_ids[:limit]


def fetch_video_stats(youtube, video_ids):
    videos = []
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i + 50]
        resp = youtube.videos().list(part="snippet,statistics", id=",".join(batch)).execute()
        for item in resp.get("items", []):
            videos.append({
                "id": item["id"],
                "title": item["snippet"]["title"],
                "published_at": item["snippet"]["publishedAt"],
                "views": int(item["statistics"].get("viewCount", 0)),
                "url": f"https://www.youtube.com/watch?v={item['id']}",
            })
    return videos


def find_outliers(handle, videos):
    if len(videos) < 3:
        return []
    view_counts = [v["views"] for v in videos]
    baseline = statistics.median(view_counts)
    if baseline == 0:
        return []
    outliers = []
    for v in videos:
        multiplier = v["views"] / baseline
        if multiplier >= OUTLIER_MULTIPLIER:
            outliers.append({
                "channel": handle,
                "title": v["title"],
                "url": v["url"],
                "views": v["views"],
                "channel_baseline_views": int(baseline),
                "outlier_multiplier": round(multiplier, 2),
                "published_at": v["published_at"],
            })
    outliers.sort(key=lambda o: o["outlier_multiplier"], reverse=True)
    return outliers


def main():
    parser = argparse.ArgumentParser(description="Find outlier YouTube videos across competitor channels.")
    parser.add_argument("handles", nargs="+", help="Channel handles, e.g. @dan-koe")
    parser.add_argument("--output", required=True, help="Path to write JSON output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("YOUTUBE_API_KEY")
    if not api_key:
        print("ERROR: YOUTUBE_API_KEY not set. Add it to .env or the environment.", file=sys.stderr)
        sys.exit(1)

    youtube = build("youtube", "v3", developerKey=api_key)

    all_outliers = []
    errors = []
    for handle in args.handles:
        try:
            channel_id, uploads_playlist = resolve_channel_id(youtube, handle)
            if not channel_id:
                errors.append(f"{handle}: channel not found")
                continue
            video_ids = fetch_recent_video_ids(youtube, uploads_playlist, MAX_VIDEOS_PER_CHANNEL)
            videos = fetch_video_stats(youtube, video_ids)
            all_outliers.extend(find_outliers(handle, videos))
        except Exception as e:
            errors.append(f"{handle}: {e}")

    all_outliers.sort(key=lambda o: o["outlier_multiplier"], reverse=True)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump({"outliers": all_outliers, "errors": errors}, f, indent=2)

    print(f"Wrote {len(all_outliers)} outliers to {args.output}")
    if errors:
        print(f"Errors: {errors}", file=sys.stderr)


if __name__ == "__main__":
    main()
