# Topic map before more filming (Luke, 22 Nov: "posting off into the abyss")

**Verdict:** yes, research first, in this chat, time-boxed to 2 days. Routes (a) and (b) are one route:
(b) finds the demand, (a) is our angle on it (Briar: a high-TAM topic people already search for, plus a counter-position only a fuel brand would take).

## Positioning (Luke, 22 Nov, second pass): performance, not weight loss
Weight loss is out as a lane: too big a switch from what followers came for, crowded, no right to win,
and a carb bar sits badly next to it ('I let myself go': 807 views, 58.9% skip). The line that holds
everything together is **amateurs who compete and want to perform**, fuelled right:
- **Status:** beat your time, beat your teammates, be the one still flying at 85 minutes or 38K.
- **Freedom from fear:** fading in front of people (walking at 30K, legs gone in the last 15, subbed off).
- **Affiliation:** people who take their amateur sport seriously.
Two lanes cover the year: **marathon** (spring and autumn blocks) and **team sport** (Sunday league,
GAA, rugby, hockey: their season runs while marathons are quiet). The oranges trial (2,468, skip 33.4%)
says the team lane works. The restarter only stays when there's a performance goal (first parkrun, a time).

## Accounts Luke rates (22 Nov)
The Running Effect (IG), Steve Magness (YouTube), Stephen Scullion (YouTube), Spencer Matthews' podcast
(plain questions to pros: a podcast format to copy), Slow Internet Club (YouTube: '10/10 free...' lists
with links: the again-series shape, for performance topics). Add team-sport performance accounts to the pull.

## Hypothesis to test (superseded in part: weight loss dropped)
Our one 18K reel (the fourth hour) was fuel numbers in a seasonal lane. Evergreen topics with big audiences
(zone 2, running to lose weight, starting again, easy runs feeling hard) have a fuel angle almost nobody takes:
- Running to lose weight: you run empty, so the run is short and the evening binge wins.
- Zone 2: it feels hard because you run it fasted, not because you're unfit.
That fits the bar (a training bar, P237) and the again series.

## Steps
1. **Pull (day 1):** Apify over about 20 accounts (IG + TikTok) and YouTube outliers: running coaches, beginner and
   weight-loss running accounts, Rory-style list accounts. Last 12 months. Plus Reddit (r/running, r/C25K, r/loseit
   running threads) for the pain in their own words.
2. **Rank:** outlier score = views / that account's median. Tag each winner by topic, evergreen or seasonal,
   title shape, cover and frame one. Topics that win on 3+ accounts = proven demand.
3. **Pick:** 5 topics with the most demand where we have a counter-position from FACTS. Title-producer on each.
4. **Test:** 2 trial reels a week to non-followers (P174, row 34); judge on emails per reel and follows, not views.
5. **Keep:** the map goes in the topic bank; re-pulled monthly by the weekly loop.

## Needs
- An Apify API token (saved as a network secret for api.apify.com; the scripts move from ?token= to a Bearer header).
- Luke's list of accounts he rates (I draft the rest from brands/engine-room-nutrition/competitors.md).
- Cost: roughly $5 to $15 of Apify credit.

## The accounts to pull (22 Nov). Picked for audience overlap, not size
Handles get verified by search and a test scrape before the pull (competitors.md: guessed handles were mostly wrong).
- **Tier 1, the same viewer (amateur marathoners, UK/IE/EU):** Ben Parkes, The Running Channel, Stephen Scullion,
  The Running Effect, Runner's World UK, Marathon Handbook, Rory (bingethinking).
- **Tier 2, the science lens our audience follows:** Steve Magness, Asker Jeukendrup (mysportscience),
  Precision Fuel & Hydration, Renee McGregor, Stacy Sims, Untapped (Spencer Matthews; guest topics that pull).
- **Tier 3, team sport performance (amateurs):** found by search, not guessed: 5 to 8 accounts on Sunday league,
  GAA and club rugby fitness and fuel, plus Science for Sport.
- **Reddit (the pain in their words):** r/running, r/AdvancedRunning, r/Marathon_Training, r/C25K, r/bootroom, r/GAA.
- **Format only, not topics:** Slow Internet Club, TED-Ed, Rory's list shape, Untapped's plain questions.
- **Left out:** elite and US-heavy accounts (their winners are about problems our viewers don't have), weight-loss accounts.

## Adjusting for TAM
Score = outlier (views / that account's median) x share of our viewers who have the problem x fuel angle (1 if we
can counter-position from FACTS, 0.5 if not).
Share examples: what to eat before a run, about 100%; easy runs feeling hard, high; the wall, most marathoners;
an ultra or a sub-3 topic, about 5%. A topic only counts if it wins on 3+ accounts, across at least 2 tiers.
