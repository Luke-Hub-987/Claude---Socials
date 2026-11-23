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
  The Running Effect, Runner's World UK, Marathon Handbook, Charlie Norris (cnozrun), Matt the endurance scientist (IG).
  Rory (bingethinking) is format only: he isn't in running.
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

## Luke's notes, 22 Nov (third pass)
- Precision Fuel's content is good but doesn't perform, and most sports accounts are small. So we never rank by
  raw views: always views / that account's median, and we look for **creators** who beat their own median often.
- His feed is lifestyle (finish photos, training clips). Few accounts post useful training videos consistently,
  so step 2 below **discovers** them instead of relying on names we know.
- Reddit: the October bundle (research/reddit-running-research-manual.txt, themes summary) is the base; Luke can add threads.

## Tomorrow (23 Nov): the run, in order
1. **Keys (10 min).** Luke saves the Apify key in the secure form (host api.apify.com). I move the scripts from
   ?token= to a Bearer header, raise posts per account from 20 to about 100 (12 months), and run a 1-account test.
2. **Discover (45 min).** Keyword and hashtag searches on TikTok and IG (marathon fuelling, marathon training tips,
   long run, easy run, parkrun, Sunday league fitness, GAA fitness, half-time food). Keep creators under 500K
   followers, posting at least weekly, with 3+ videos at 3x their median. Target 10 new names, verified by a test scrape.
3. **Luke cuts the list (10 min).** Named + discovered, about 25 accounts in 3 tiers. He kills any that are lifestyle.
4. **Pull (1 hour, runs in the background).** IG and TikTok for all 25, YouTube outliers for the YouTube ones
   (Magness, Scullion, Ben Parkes, The Running Channel, Untapped). Cost check after the first platform.
5. **Rank (1 hour).** Every video at 3x+ its account's median gets: topic, evergreen or seasonal, lane (marathon,
   team sport, restart with a goal), title shape, frame one, cover. Topic score = outlier x TAM share x fuel angle.
   A topic counts only if it wins on 3+ accounts across 2 tiers.
6. **Cross-check with Reddit (20 min).** Each top topic gets its pain in the runners' own words from the October
   bundle. No Reddit pain, it drops a place.
7. **The map (30 min).** One page: the top 10 topics, why each wins, our counter-position from FACTS, and the
   title and frame-one shapes that won. Council verdict on the top 5.
8. **Titles (rest of the day).** Title-producer on the top 2; the first goes to script and films as a trial reel.

Done = a ranked map of 10 topics, 2 titled, 1 scripted. Each topic in it traced to the videos behind it.

## 23 Nov, the start
- Luke declined the key form in chat. Route: he adds it in the environment settings (Network secrets, host api.apify.com),
  then a new session picks it up.
- Web search can't confirm Matt the endurance scientist or cnozrun: Luke sends the handles (copy from the app).
- Found by search, to verify by test scrape: Phily Bowden (coach, 2:25, YouTube 225K), Brady Holmer (Run Long Run Healthy,
  with Marathon Handbook's Thomas Watson), The Football Nutritionist (Craig), The Foodie Footballer (Marc Pugh, IG).
  Web search finds media lists, not consistent creators, so discovery waits for the Apify keyword search.

## 23 Nov, the account plan (P243: format first)
The mistake last time: Max Jolliffe and BPN, views from stunts and film crews, so the advice became "run 50K".
Rule: an account is scraped for topics only if it makes Luke's kind of video (one person to camera, teaching,
like a podcast clip); every outlier is tagged by what drove it and only topic outliers count.

**A. Same format, same niche (topics we can take; ranked):**
runcoachcath (IG, closest to Luke's videos), The Running Effect, Matt the endurance scientist, cnozrun (if to camera),
Steve Magness (YouTube talking head), Stephen Scullion (to-camera videos only), Precision Fuel & Hydration (education),
Ben Parkes (to-camera videos only, not race vlogs), Brady Holmer, The Football Nutritionist, The Foodie Footballer.
Plus discovery: keyword search, keeping only to-camera teachers (checked by their covers), under 500K followers.

**B. Podcast clips in the niche (the questions that pull, not the guests):**
Nick Bare podcast clips, Untapped (Spencer Matthews), Steve Magness's podcast clips. Tag each clip by its question;
drop any clip whose views track the guest's fame. These double as our podcast's episode questions (Luke + Jamie, no guests).

**C. Same format, other niches (mechanics only: what makes topics pull every time):**
conor.talks (finance), maya.mental.fitness, the Motional Intelligence podcast (handle to confirm), Rory (bingethinking),
Slow Internet Club. Read for title shapes, topic types and why their floor is high, never for topics.

**Out:** Max Jolliffe, BPN, Nick Bare's vlogs and stunts, race-day and lifestyle accounts, and anything with a film crew.

**Tags on every outlier (3x+ its account's median):** driver (topic, stunt, guest, trend, event), format, topic, lane
(marathon, team sport, restart with a goal), evergreen or seasonal, title shape, frame one. Then the TAM score.
**Final filter:** could Luke say it sat at his desk tomorrow, from FACTS, with no guest and no stunt? If not, out.

**Cost:** about 20 accounts in A + B, 5 in C, so roughly $13 to $24 as estimated; C pulls 50 posts each.

## 23 Nov, handles confirmed (Instagram details scrape) and the pull
A (to camera, our niche): runcoachcath 17K, mattendurancescientist 29K, cnozrun 26K, runningcoachmegan 74K, ben_is_running 163K,
justalilbester 111K, benparkes 90K, stevemagness 246K, precisionfandh 133K, therunningeffect 254K, mcgurnfitness 61K (GAA),
thefootballnutritionist 36K, thefoodiefootballer 73K. TikTok: kelsey.poulter.
B (podcasts: the questions, not the guests): thenickbarepodcast, untapped.podcast 111K, richroll 1.6M, extramilest 3K,
thetenacitypodcast 5K, motionalintelligencepod 20K, jakedearden_ 681K (HYROX; tag stunts hard).
C (mechanics only): conor.talks 25K, maya.mental.fitness 673K.
Not found on IG: Stephen Scullion (YouTube only), Brady Holmer, On Coaching, Some Work All Play (YouTube later).
Not every post from these accounts is in our lane: every outlier is tagged by lane, and off-lane posts are dropped.
**Seth Godin tag (Luke, 23 Nov):** every topic says which want it serves (status, freedom from fear, affiliation). No want, it's out.
Cost so far: test $0.23, handle checks $0.09.
