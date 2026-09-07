# Claude — Socials

Content ideation engine covering two separate brands:

- **Personal** — Luke's personal brand (@luke_morrison_er)
- **Engine Room Nutrition (ERN)** — the company account (@engineroomnutrition)

Each brand has its own voice, pillars, audience, and competitor set,
and its own `/onboard-*` and `/ideate-*` skill so ideas never blend the
two voices together.

## Layout

```
brands/
  personal/                  voice.md, pillars.md, audience.md, competitors.md
  engine-room-nutrition/     same, for ERN
principles.md                Briar Cochran / Paddy Galloway / Heaton Ralston / Ogilvy positions (shared, live)
hook-frameworks.md           named hook patterns + swipe file (shared, live)
voice-rules.md               universal style rules (shared, drafted)
research/                    raw transcripts principles.md / hook-frameworks.md were built from,
                              plus Reddit running research for ERN's audience
scripts/                     yt_outliers.py, reddit_scan.py, ig_outliers.py, tiktok_outliers.py, validator.py
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
   - `APIFY_API_TOKEN` (console.apify.com) — covers Instagram
     (`ig_outliers.py`), Reddit (`reddit_scan.py`, via
     `trudax/reddit-scraper-lite`), and TikTok (`tiktok_outliers.py`,
     via `clockworks/tiktok-scraper`) — one token, three platforms. No
     separate Reddit credential exists: Reddit's current developer
     signup rules made an OAuth app hard to get approved, and even
     Reddit's own public unauthenticated endpoints return a 403
     straight from Reddit's servers when called directly from a
     datacenter IP (confirmed directly). Apify's actors route around
     that.
3. Run `/onboard-personal` and/or `/onboard-ern` to fill in each
   brand's voice, pillars, audience, and competitors.
4. Run `/ideate-personal` or `/ideate-ern` to generate a 10-idea brief.

## Network access in a Claude Code on the web / remote session

If you're running the `/ideate-*` skills from a hosted Claude Code
session (as opposed to your own machine), the environment's network
egress policy can block some hosts outright. In this environment,
`api.apify.com` was initially blocked by policy and later opened up
after the environment's network settings were widened (see
code.claude.com/docs/en/claude-code-on-the-web for where that's
configured) — everything below was verified working only after that
change. Direct `reddit.com` access stays blocked at the Reddit-server
level regardless of environment policy, which is exactly why
`reddit_scan.py` goes through Apify instead of hitting Reddit directly.

## Status

- Repo scaffold: done
- `principles.md`, `hook-frameworks.md`: live — built from Luke's
  uploaded research (Briar Cochran, Paddy Galloway, Heaton Ralston
  brothers) plus his own on-screen-text/Ogilvy operating principle
  (P15) — see `research/` for the source transcripts
- Scraper scripts: all four confirmed working end-to-end with live
  keys — `yt_outliers.py` (YouTube Data API direct), `ig_outliers.py`
  (`apify/instagram-scraper`), `reddit_scan.py`
  (`trudax/reddit-scraper-lite`), `tiktok_outliers.py`
  (`clockworks/tiktok-scraper`)
- `brands/personal/voice.md` + `pillars.md` and
  `brands/engine-room-nutrition/voice.md` + `pillars.md`: drafted from
  real on-screen text + view counts across both accounts, pending
  Luke's confirmation
- `brands/*/audience.md` and `brands/*/competitors.md`: still pending
  for both brands — see `research/reddit-running-themes-summary.md`
  for draft ERN audience/competitor signal from Luke's own Reddit
  research
