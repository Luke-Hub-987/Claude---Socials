# Claude — Socials

Content ideation engine covering two separate brands:

- **Personal** — Luke's personal brand
- **Engine Room Nutrition (ERN)** — the company account

Each brand has its own voice, pillars, audience, and competitor set,
and its own `/onboard-*` and `/ideate-*` skill so ideas never blend the
two voices together.

## Layout

```
brands/
  personal/                  voice.md, pillars.md, audience.md, competitors.md
  engine-room-nutrition/     same, for ERN
principles.md                Briar Cochran / Paddy Galloway / Heaton Ralston positions (shared, live)
hook-frameworks.md           named hook patterns + swipe file (shared, live)
voice-rules.md               universal style rules (shared, drafted)
research/                    raw transcripts principles.md / hook-frameworks.md were built from
scripts/                     yt_outliers.py, reddit_scan.py, ig_outliers.py, validator.py
ideas/
  personal/                  generated briefs land here
  engine-room-nutrition/     generated briefs land here
.claude/skills/
  onboard-personal/          interviews you, fills brands/personal/*.md
  onboard-ern/                interviews you, fills brands/engine-room-nutrition/*.md
  ideate-personal/           generates 10 ideas for the personal brand
  ideate-ern/                 generates 10 ideas for ERN
```

## Setup

1. `pip install -r requirements.txt`
2. `cp .env.example .env` and fill in:
   - `YOUTUBE_API_KEY` (Google Cloud Console, YouTube Data API v3)
   - `REDDIT_USER_AGENT` (no dev app needed — `reddit_scan.py` uses
     Reddit's public JSON endpoints, since Reddit's current developer
     signup rules can be hard to clear for a small project)
   - `APIFY_API_TOKEN` (console.apify.com — covers Instagram scraping;
     no separate Instagram or TikTok key needed)
3. Run `/onboard-personal` and/or `/onboard-ern` to fill in each
   brand's voice, pillars, audience, and competitors.
4. Run `/ideate-personal` or `/ideate-ern` to generate a 10-idea brief.

## Network access in a Claude Code on the web / remote session

If you're running the `/ideate-*` skills from a hosted Claude Code
session (as opposed to your own machine), the environment's network
egress policy can block some of these hosts outright — confirmed in
this environment: `reddit.com` and `api.apify.com` are blocked by
policy (`403` at the proxy, before the request even reaches Reddit or
Apify), while `googleapis.com` (YouTube Data API) is not. If
`reddit_scan.py` or `ig_outliers.py` fail with a connection/403 error
that isn't from Reddit or Apify themselves, this is almost certainly
why. Fix it by widening the environment's egress allowlist (see
https://code.claude.com/docs/en/claude-code-on-the-web for how
environment network policy is configured) or by running the pipeline
from a machine/environment without that restriction.

## Status

- Repo scaffold: done
- `principles.md`, `hook-frameworks.md`: live, built from Luke's
  uploaded research (Briar Cochran, Paddy Galloway, Heaton Ralston
  brothers) — see `research/` for the source transcripts
- Scraper scripts: `yt_outliers.py` confirmed working end-to-end with
  a live key. `reddit_scan.py` and `ig_outliers.py` are written and
  keyed but unverified from this environment due to the network policy
  above — verify from an environment/machine that can reach
  reddit.com and api.apify.com
- `brands/*/*.md`: pending, run `/onboard-personal` / `/onboard-ern`
