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
principles.md                Briar's PBA principles (shared, pending)
hook-frameworks.md           Briar's PBA hook patterns (shared, pending)
voice-rules.md               universal style rules (shared, drafted)
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
   - `REDDIT_CLIENT_ID` / `REDDIT_CLIENT_SECRET` / `REDDIT_USER_AGENT` (reddit.com/prefs/apps)
   - `APIFY_API_TOKEN` (console.apify.com)
3. Paste Briar's actual PBA course content into `principles.md` and
   `hook-frameworks.md` at the repo root (shared by both brands). These
   can't be filled in without the real course material.
4. Run `/onboard-personal` and/or `/onboard-ern` to fill in each
   brand's voice, pillars, audience, and competitors.
5. Run `/ideate-personal` or `/ideate-ern` to generate a 10-idea brief.

## Status

- Repo scaffold: done
- Scraper scripts (YouTube/Reddit/IG) + validator: done, untested against live API keys
- `brands/*/*.md`: pending, run `/onboard-personal` / `/onboard-ern`
- `principles.md`, `hook-frameworks.md`: pending, need Briar's actual course content pasted in
