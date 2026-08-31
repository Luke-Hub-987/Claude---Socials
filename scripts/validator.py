#!/usr/bin/env python3
"""Validate an ideate draft: every source URL must resolve, and no two
ideas may cite the same creator.

Usage:
    python3 validator.py /tmp/ideate-draft.json

Exits 0 if valid, 1 if any errors found (errors printed to stdout).
"""
import argparse
import json
import sys

import requests

TIMEOUT_SECONDS = 10
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; ideate-validator/0.1)"}


def check_url(url):
    try:
        resp = requests.head(url, timeout=TIMEOUT_SECONDS, allow_redirects=True, headers=HEADERS)
        if resp.status_code >= 400:
            resp = requests.get(url, timeout=TIMEOUT_SECONDS, allow_redirects=True, headers=HEADERS)
        return resp.status_code < 400
    except requests.RequestException:
        try:
            resp = requests.get(url, timeout=TIMEOUT_SECONDS, allow_redirects=True, headers=HEADERS)
            return resp.status_code < 400
        except requests.RequestException:
            return False


def main():
    parser = argparse.ArgumentParser(description="Validate an ideate draft JSON file.")
    parser.add_argument("path", help="Path to draft JSON, e.g. /tmp/ideate-draft.json")
    args = parser.parse_args()

    with open(args.path) as f:
        data = json.load(f)

    ideas = data.get("ideas", [])
    errors = []

    seen_creators = {}
    for idea in ideas:
        idea_id = idea.get("id")
        source = idea.get("source", {})
        url = source.get("url")
        creator = source.get("creator")

        if not url:
            errors.append(f"Idea {idea_id}: missing source.url")
        elif not check_url(url):
            errors.append(f"Idea {idea_id}: source.url unreachable ({url})")

        if creator:
            if creator in seen_creators:
                errors.append(
                    f"Idea {idea_id}: duplicate creator '{creator}' "
                    f"(already used in idea {seen_creators[creator]})"
                )
            else:
                seen_creators[creator] = idea_id
        else:
            errors.append(f"Idea {idea_id}: missing source.creator")

    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"VALIDATION PASSED: {len(ideas)} ideas, all sources reachable, no duplicate creators.")
        sys.exit(0)


if __name__ == "__main__":
    main()
