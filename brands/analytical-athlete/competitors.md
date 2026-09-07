---
type: my-brand
section: competitors
status: draft
updated_at: 2026-09-07
---

# Competitors / Reference Creators — The Analytical Athlete (LinkedIn)

**Incomplete — only two references named so far, both structural/style
references rather than a competitor list to scan for topics.** Unlike
the personal and ERN brands, this file does not (yet) drive an
automated scrape: `scripts/*_outliers.py` covers YouTube, Instagram,
Reddit, and TikTok, and there is no equivalent LinkedIn scraper in this
repo. LinkedIn is a materially harder scrape target (aggressive
anti-scraping, ToS exposure) than the other three platforms already
wired up here. Until/unless that changes, this brand's primary fuel is
Luke's own `swipe-file.md`, not competitor outliers — see
`ideate-analytical-athlete`'s SKILL.md for how that trade-off is
handled.

## Named references (style/structure, not topic sources)

- **Justin Welsh** — named by Luke directly as the structural model:
  "very clear, very concise, easy structured... he'd often have a link
  down to his email list. Generally, if you want to achieve the above,
  then you need to go here." This matches the CTA structure already
  confirmed in `voice.md` from Luke's own top posts.
- **Ogilvy / John Caples-style direct-response copywriting** — named
  by Luke as the copywriting philosophy: "people don't care about us,
  we're looking to give them valuable information they can apply, but
  in a format/impact they've never really seen before." This isn't a
  LinkedIn account to scan, it's the underlying copywriting doctrine
  behind the line-by-line hook mechanic in `voice.md`.

## Open — needs Luke

- **LinkedIn accounts/creators he actually wants studied**, even
  without an automated scraper: 2-5 handles or post URLs he admires
  structurally, that I can pull manually with WebFetch the same way
  `swipe-file.md` was built, rather than scraping at scale.
- Whether a LinkedIn Apify actor is worth wiring up as a real scraper
  (`scripts/linkedin_outliers.py`, mirroring the existing four) — worth
  attempting only if Luke wants ongoing competitor-outlier scanning
  rather than a one-off manual pull.
