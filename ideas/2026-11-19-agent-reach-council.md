# Agent-Reach: do we need it? (council, 19 Nov)

Luke sent 4 screenshots of a video about github.com/Panniantong/Agent-Reach
(Claude reads YouTube, Instagram, LinkedIn, Reddit, X; turns a creator's
posts into skills; mines Reddit complaints; breaks down competitors' hook,
format and topic). Question: is it possible, is it useful, does it need a new repo?

## What the repo actually is (README read 19 Nov)

- A Python CLI (`agent-reach`) plus an agent skill. MIT, about 113k stars, last commit 8 Nov 2026. Read-only.
- **No TikTok.** Instagram, X and Facebook are "experimental: works, but anti-scraping is stricter and it may stop working at any time". Reddit is optional and needs a login.
- Logged-in platforms reuse **your own Chrome login** (it copies the site's cookies into its own background browser). The README advises a secondary account because platforms may restrict accounts that are automated.
- The README lists profiles, posts, search, comments and transcripts. **It never mentions view counts or engagement**, which an outlier scan needs.
- YouTube needs no login (yt-dlp underneath); speech-to-text needs a Groq or OpenAI key.

## What we already have (since September)

`scripts/yt_outliers.py` (YouTube Data API), `scripts/reddit_scan.py`,
`scripts/ig_outliers.py` and `scripts/tiktok_outliers.py` (Apify), driven by
`/ideate-ern` and `/ideate-personal`. These return view counts and outlier
ratios. **They are switched off in the cloud:** there is no `.env`, no
`APIFY_API_TOKEN` and no `YOUTUBE_API_KEY` in this environment. Windsor covers our own IG numbers.

The competitor list (`brands/engine-room-nutrition/competitors.md`) is mostly
chefs and general YouTubers (Babish, Eater, Bon Appétit, Fallow, Johnny Harris,
David Senra), plus 9 nutrition brands. Few of them are marathon creators who talk to our audience (P126).

## Council

**Contrarian:** Data on other people's hooks isn't what's holding us back. Our
losses this month were frame one (rows 22, 33), the CTA timing (row 9) and
titles. Copying outliers also pulls us towards advice people already know (row 26).
A second scraping system is upkeep we'd stop doing within a month.

**Assumption-ripper:** Three assumptions are wrong. (1) "It reads IG and TikTok":
it has no TikTok, its IG is experimental, and it returns no view counts. (2) "We
don't have this": we've had it since September, switched off. (3) "Our competitors
are the right ones to study": our list analyses food channels for a marathon carb bar.
Running Agent-Reach on Luke's Chrome would also put the ERN or personal account on the line before launch.

**Expansionist:** The upside the video misses is the comments, not the hooks.
Comments under Maurten, SiS and Precision Fuel posts, and Reddit fuelling threads,
are pre-launch product research: "gels wreck my stomach", "too sweet by 25K",
"£3 a gel". That's the bar's positioning and FACTS-checked titles in runners'
own words, which passes P220's must-pass ("they already know it's their problem").

**Outsider:** Why add a new tool when the one you've got is switched off for want of a key?

**Executor:** Keys in by Fri 20 Nov. A marathon competitor list by the Monday
23 Nov loop. Run it for 4 weeks to Mon 14 Dec. It succeeds if at least 1 posted title came from the feed and beat
the base rate; otherwise cancel Apify.

**Blind cross-review:** The Contrarian's point stands, so this has to stay one
feed into the existing Monday loop, not a new system or repo. The Assumption-ripper's
3 points are facts from the README and the repo, not opinion. The Expansionist's
comments-as-product-research point is the strongest idea here and changes what
we scrape. The Executor's kill test makes the Contrarian's upkeep worry something we can measure.

**Chairman verdict:** No new repo, no Agent-Reach. Switch on the scrapers we
already have, rebuild the competitor list around marathon creators and fuel brands, and
add two outputs to the Monday loop: the week's competitor outliers (hook, format,
topic) and the top complaints from Reddit and brand comments, each turned into a
title seed for `title-producer`. Kill it on 14 Dec if nothing it seeded got posted and beat the base rate.

## Next steps

1. **Luke:** say go and Claude asks for the Apify token and the YouTube Data API key through the secure credential form (never in chat). Apify is pay-as-you-go; check what 4 weeks cost on 14 Dec.
2. **Claude:** rebuild `competitors.md` with marathon and running creators (UK, Ireland, Europe first) plus fuel brands, each handle confirmed by a real scrape. Luke approves the list.
3. **Claude:** add a comments pass (brand posts plus Reddit fuelling threads) and a "pains in their words" table to the Monday loop prompt (`ideas/weekly-loop-prompt.md`).
4. **14 Dec:** keep it or kill it on the measure above.
