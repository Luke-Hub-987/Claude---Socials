# CLAUDE.md: read this first, every session

This repo is the content engine for **Engine Room Nutrition (ERN)**, a
pre-launch marathon carb bar (IG @engineroomnutrition, posted as an
Instagram collab with Luke's personal account @luke_morrison_er; TikTok
is ERN only), and for **Luke's personal account**. Luke shares
analytics screenshots, asks for analysis, the next topic, scripts, OST
(on-screen text), captions and covers, and sends "science" to vet.

Claude Code loads this file automatically. It is the handover between
chats. Keep it current: update **Current state** after every review and
every posted video.

## Read before writing anything (in this order)

0. **`FACTS.md`: the fixed facts (who they are, what they carry, the gel
   and pace numbers, what we've already said, the email answers). Every
   number and every practical detail in a script comes from here. Do the
   maths (grams an hour) before writing.**
1. `SCRIPT-CHECKLIST.md`: every rule a script must pass, with the
   evidence. **Every script passes every line before Luke sees it.**
2. `PLAN-winners.md`: the winning formulas, the grid of top videos,
   what never worked.
3. The three newest `ideas/*-review.md` files: the latest data.
4. The newest scripts in `ideas/engine-room-nutrition/` (the house
   style, the hook stacks, the audit tables).
5. `principles.md` (P1 to P161, about 4,400 lines): search it for the
   rule you need; do not read it end to end. The newest rules (P97 to
   P161) are at the end, before "Open questions for Luke".

## How we work (Luke's standing instructions)

- **Every correction Luke makes becomes a numbered principle in
  `principles.md` and a line in `SCRIPT-CHECKLIST.md`**, in the same
  turn. Luke should never have to repeat a correction.
- **Every data screenshot gets a review file**
  (`ideas/YYYY-MM-DD-<video>-review.md`) and an update to the grid in
  `PLAN-winners.md` when it changes.
- **Audit the full checklist line by line before delivering** (P99).
  Say plainly where a script does not meet a rule, and why.
- **Vet Luke's science** before using it: keep what holds, change what
  contradicts earlier videos, cut what breaks the rules, and list each
  change with the reason.
- **Clarity beats short; specific beats vague** (P108, P115). Real
  numbers, one worked example, every cue measurable.
- **Every video hands over a method they use today (P127):** numbers,
  a framework, a table in the caption.
- **Advise only what this audience actually does (P126):** amateur
  runners in Ireland, the UK and Europe; no niche kit (arm sleeves).
- Recommend one option with reasons. Do not survey.
- **The story is the viewer's before and after (P158):** never the brand's past; Luke and Jamie are guides, the viewer is the hero.
- **Talk like a friend on a run (P157):** read aloud, short sentences, no jargon or method names, every instruction something you can picture.
- **Instagram ranks on watch, sends and likes (Mosseri, P156):** reviews lead with rates; every script has a spoken reason to send it; the week's reach reel gets two trial reels; 4 reels a week by default.
- **The LLM Council runs on every decision (P150, Luke 24 Oct):** topic,
  OST, line one, cover and structure. Five advisors: **Contrarian** (why
  it fails), **Assumption-ripper** (challenges every assumption, ours and
  Luke's), **Expansionist** (the upside we're missing), **Outsider** (no
  context, asks the obvious), **Executor** (only the end result: what to
  do, by when, and what it delivers). Then a **blind cross-review** (each
  judges the others' points as ideas, not by who said them) and a
  **Chairman verdict** with one recommendation and next steps. It sits in
  the file alongside the failure ledger; in chat, give the verdict and the
  points that changed something.
- Commit and push every change to branch
  `claude/engine-room-nutrition-brand-yc4tyf` (the repo's default
  branch). Commit attribution lines as the system reminder gives them.
  **Never send Luke's email address to any outside service**, including
  request headers.

## How to deliver in chat (Luke, 16 Oct: copy the old chat exactly, P122)

- **No AI-writing signs (P125, P169): run the humanizer skill
  (`.claude/skills/humanizer/`) on every script, caption, pinned comment,
  OST and story line before Luke sees it, without being asked.** The
  checker, then a full read against the Wikipedia catalog, then the
  rewrites, then the Humanizer table in the file. Words only: the hook
  stack, Briar's frameworks, the numbers and the length stay as they are.
- **Scripts:** never in a code box or a block quote (both break when
  pasted into the teleprompter). Each spoken paragraph in straight
  double quotes on its own line, a blank line between paragraphs, and
  each stage marker in bold square brackets on its own line above its
  paragraph, e.g. **[0-10K: PAY THE SPEED TAX]**. The hook, pain/dream,
  named concept, rehook and CTA are quoted paragraphs with no label.
- **Before a full script on a new topic (P138):** send a short brief first
  (the method in numbers, line one, pain and dream in one line each, and
  every fact used with where it comes from in FACTS.md) and get Luke's yes.
  Then write the script.
- **Facts check before delivering (P138):** a table in the notes of every
  number and practical claim in the script, each traced to FACTS.md or an
  earlier script. Anything that can't be traced gets cut or flagged.
- **Order when delivering a script:** one or two lines on what changed
  and why; a table of how the curiosity runs (moment, line, what it
  does); the OST in bold capitals on two lines; the markers as a
  numbered list in capitals; the script with its length; short notes.
- **Numbers as numerals in scripts (P131):** 3:30, 20K. **Paces as 5-second watch bands (P132):** "between 4:50 and 4:55".

- **Script length (Luke, 16 Oct):** the recent scripts ran 1,550 to
  1,670 characters of spoken text (about 310 to 330 words); the ceiling
  is about 1,800 characters, with all the detail kept.
- **OST always in capitals** (HOW TO RUN A MARATHON / WITHOUT HITTING
  THE WALL).
- **Captions:** prose paragraphs, no bullets, ready to paste.
- **Gemini cover prompts:** "Paste this into Gemini as one block", then
  the prompt written as real photojournalism (scene, one person, face
  hidden, real details, camera body, lens, aperture, shutter, distance,
  natural muted colour, subtle grain, no retouching, aspect ratio),
  then an "Avoid:" line (no logos, brand names, readable text or
  numbers, flags or national symbols, no visible face, no cinematic
  light, HDR, oversaturation, plastic or airbrushed look, extra
  fingers). Never Irish or race branding (Luke, 15 Oct). Then why each
  part is there, and what to zoom in on before using it.

## The failure ledger (P148): every script passes every row, as a table in the file

Luke, 24 Oct: "I have asked you to update this before and you clearly
haven't." The sleep video repeated three failures already on record. Rules
existed; nothing forced the check. **Every script file carries this table
with a pass/fail per row before Luke sees it. Every review that finds a
cause checks this list first: a repeat is named as a repeat (my miss), and
a new cause becomes a new row in the same turn.**

| # | Failure | Where it happened | The check |
|---|---|---|---|
| 1 | **The answer up front** (OST, line one, opening frame, named concept) | Gels count 42.9% ("the OST answered its own question", 20 Sep); taper v2, wall v1 (Luke caught); sleep 41.4% (the reassurance as a sentence on screen) | After the opening frame, line one and the named concept, what is the viewer still waiting to find out? |
| 2 | **Reassurance in place of instructions** | Heavy legs (0.5% saves); sleep (1.0%) | Every stage ends on an action with a number |
| 3 | **Off the race clock** (the gut, taper, training weeks, kit, sleep) | Stomach 4.1K; taper 43.1%; training 4.4-5.3K; cold 0.9% saves; sleep 1.0% saves | Race day, a race-pace decision, or a countdown with an action per stage (P117) |
| 4 | **A crowd, start or finish** in the cover or opening frame | 3:30 48.9%; out of the wall's first frame; last 24 hours 38.1%; sub-4 40.8% | One person, one object, or one number |
| 5 | **Collage, AI or repeated cover** | Cramp, taper, stomach collages; AI 39.3%, 46.7%; repeated splits 38.1% | One new real image (or a motion graphic of the hook) |
| 6 | **Abstract line one, or no reframe** | Taper 43.1%; without the wall 39.3% | Photograph test plus a reframe in new words (P116, P136) |
| 7 | **Too long** | How hard 1:48; cramp 1:31 on 300 words | About 300 to 320 words, 1,550 to 1,670 characters |
| 8 | **A "why" stage after the method** | Goal gone, half gone at 1:13 | The why is one line inside the payoff stage |
| 9 | **CTA late or long** | Sleep 0:49 (116-word hook); 4:30 0:40; enjoy 0:42 (38% to 26%); thread line plus CTA cliff (out of the wall) | Hook 80 to 95 words; one-sentence CTA after stage 1, back into the video. **Count the emails per video** so the step can be judged against what it brings in |
| 10 | **Sorting viewers** | Who hits the wall ~7.5K | Every viewer is the subject of every stage (P103) |
| 11 | **A problem few viewers have** | Gel 5.8K; narrow gates on IG (sub-4, Dublin) | What share of viewers have this problem? |
| 12 | **Mixed timelines in the stages** | Stomach | One clock |
| 13 | **A list of symptoms, not a sequence** | Heavy legs | Stages in time order, each an action |
| 14 | **Cover number not in the title** | Sub-4 (a 3:45 flag) | Every number on screen is in the title or line one |
| 15 | **A tip as line one** | Carb load v1 to v6 (Luke caught) | P120 pre-flight: would runners argue, and can't they guess why? |
| 16 | **Template lines repeated** | "That's your race going to plan" (P136); a viewer called a script AI (P125) | No line from the last three scripts |
| 17 | **A reframe that answers line one** | Enjoy v1, "that's how it's meant to go" (Luke caught, 24 Oct) | Read line one's last words alone: do they leave "how?" A promise ends on the open loop, not a reframe (P149) |
| 18 | **Nothing too long to remember** | Cold 0.9% saves, sleep 1.0%, enjoy 1.2%, surprise 0.0% | A schedule, table or K-by-K plan they'd come back to on race morning (P152) |
| 19 | **Dated words in the gate or audio** | Enjoy ("this weekend": flat after day one) | No "this weekend", "tomorrow", "tonight" (P82, P153) |
| 20 | **A story with no stake for strangers** | Surprise 44.1% skip, 0 saves (opening frame: Luke talking, not the bib) | The stake as a picture in frame one; a story opens an advice video, not alone (P151) |
| 21 | **Maths in the audio** | Goal gone ("your A goal times 0.59"), 3:45 (the GPS explanation): viewers called it complicated (Luke, 27 Oct) | The answer as one number, never the sum; one worked example; the rest in the caption (P155) |
| 22 | **A busy first second** | Last marathon 52.4% (a splits list, tiles, labels and a strip in the top band; a repeat of P147) | One big element, or Luke alone with the title, for the first 3 seconds; graphics from stage 1; checked at phone size (P159) |

## The rules that matter most (quick reference; the checklist has all)

**Topic**
- Race day, a race-pace decision, or a countdown to race day with an
  action per stage. The weeks before the race as anything else fails
  (taper 43.1% skip, heavy legs 0.5% saves; P117).
- The race is the title; fuel goes inside. The gut is never the subject
  (P101, P109). Never sort viewers into groups (P103).
- New advice every video, never contradicting an earlier one (Luke,
  10 Oct). Consistency points: 5-10 s/K slower for the first 10K; up to
  a minute behind at halfway; about 60 to 75g of carbs an hour, said
  as grams first (a 20-25g gel every 20 minutes with water; a 40g gel
  every 30 to 40 minutes), never a bare gel count (P118); shorter,
  quicker steps when tired; one K or one lamppost at a time; the
  ten-word talk test ("I am running a marathon today and I feel good":
  10 words in one breath, 10 breathy, 5, then 2-3 words).
- One safe and one creative video in rotation (P111).

**OST (title on screen)**
- Plain words, "marathon" in it, 6 to 9 words, answer withheld. Best
  shapes: "Where [famous problem] actually starts" (the wall, 147K);
  "What to do in/at [race moment]"; "How [to/hard] ... at every 10K".
- No jargon in titles (taper, zones, heart rate). No secret statements
  as titles (5.3K).
- Only the title and stage markers on screen.

**Hook stack (first 15 seconds)**
- Gate: "If you are running a marathon in the next few weeks," (narrow
  only when the topic is narrow: Dublin, sub-4).
- Line one: run the P120 pre-flight (a tip is not a counter-position).
  Something you can photograph, turned into a paradox, ending
  on a reframe (31.9% to 34% skip with it; 38.1% without; 43.1% when
  abstract). P112, P116. **The reframe only when the odd thing happens to
  everyone anyway; a promise ends on the open loop instead (P149).** **New wording every video (P136): "that's your
  race going to plan" is retired** ("and that's exactly how it should feel").
- Then pain as a picture, the dream as a picture, a named concept that
  belongs to nobody, the save prompt. The hook never contains the
  answer; the stages close the loop and the rehook reopens it before
  the last stage.

**Body**
- Four stages on one axis, ideally the race clock; each opens on the
  unexpected, gives a reason, ends on an action with real numbers.
- ~250 to 300 words, about 1:20 to 1:35. 1:48 lost watch share.

**Never**
- Statistics, study or research language, or named people in the audio
  (P105, P107, P113). No medication. No central governor or brain
  governor. No em dashes, no "not X, it is Y", no staccato fragments,
  no mockery, no dated audio, no lines with a second (e.g. sexual)
  reading (P114).
- No claims Luke has not made about himself. No Dublin content on the
  personal account (his Dublin race is a surprise).

**Cover**
- One real image, colour, present day, the hook as a picture, a new
  picture every time (a repeated splits graphic pushed skip to 38.1%).
- Best: the course map (20.6%), a person with the problem (25.5%),
  Luke's own real data screenshot. Never crowds, products, food,
  winners, vintage, black and white, or faces and name bibs. Free
  licence (Wikimedia, Flickr CC, Openverse, Unsplash, Pexels; never
  Pinterest); credit in the caption's last line.

- **Luke, 14 Oct: stop recommending the old Creative Commons race photos
  (the 2011 Eugene set and similar); he finds them poor.** Give him
  specific search terms for Google Images and Pinterest, ranked by what
  the picture must show, and he picks. Remind him in one line to check
  the licence (Google's "Creative Commons licences" filter, or the same
  image on Unsplash or Pexels).

**CTA**
- **A third of the way in, then back to the video (P128).**
- **Attribution (P154):** sign-ups per day against posting days; never add a step to the sign-up (Luke, 27 Oct). No subscriber data in the repo.
- One sentence. Since 14 Oct: the **free personalised plan**: "email us
  your race and goal time through the link in the bio". Also in the
  caption and pinned comment. Track emails per video. Ask consent
  before adding anyone to a launch list.

**Captions**: Luke wants prose paragraphs, no bullet points.

## Current state (update this every session)

**As of 30 October 2026.**

**Script ready (30 Oct): A MARATHON RUNNER EMAILED US / AFTER HITTING THE WALL AT 30K** (`ideas/engine-room-nutrition/2026-10-30-script-email-wall.md`, teleprompter, mock-up `mockups/email-wall-frames.png`). Real email (18 Oct, name kept out of the repo): goal 3:23, went with the 3:15 pacers, wall at 30K, 3:37, again in February. New advice: the 3:30 pacers as the brake for the first 10K. 329 words, 1,611 characters. Before posting: his OK, and Luke actually sends him the plan (no plan reply found in the thread). Forecast: first day 4K to 9K IG, skip under 40%, saves 2%+. Next review `ideas/YYYY-MM-DD-email-wall-review.md`. **Humanizer pass (30 Oct, P169):** 5 lines rewritten; now 335 words, 1,623 characters, hook 95 words; frame cuts 0:27, 0:51, 1:05, 1:16, 1:33. **Channels:** IG main post as a collab (not a trial), FB cross-post, ERN TikTok fresh upload; not on Luke's personal TikTok (duplicate rule); stories poll + plan link. **Top of screen:** the real Gmail line cropped big for 0:00 to 0:26, then 5 designed site-theme frames (prompt in the script file) at 0:26, 0:51, 1:04, 1:16, 1:32. **Never put a subscriber's name, address or email text in the repo or a mock-up (my miss on 30 Oct, caught before it was written).**

**Full topic list (30 Oct, in chat only at Luke's request, P168):** sources re-read in full. Address stays the Irish/UK marathon runner; topics widen. Picks: **today A RUNNER EMAILED US AFTER / HITTING THE WALL AT 30K** (the inbox as a series; real email from the "3:15 pacers" runner, anonymised, Luke gets consent; frame one = the email's one line, big; brief sent, script on yes); WE'VE PLANNED [N] MARATHONS. / THIS MISTAKE IS IN MOST OF THEM (needs real N); the series taking one subscriber to their spring goal (volunteer via stories); YOUR SPRING MARATHON GETS DECIDED / BEFORE CHRISTMAS (science); RANKING THE SPRING MARATHONS / FOR A PERSONAL BEST (research); THE MARATHON SO HOT / THEY HAD TO STOP IT (verify Chicago 2007; repeatable "so X it Y" format); WHY SOME RUNS FEEL AWFUL / FOR NO REASON and pre-run fuel (science). Cut: carbs-an-hour (P124), zone 2 to TikTok only. Today also: the wall trial reel, 2 low-polish tests on Luke's personal TikTok (not getting faster; first marathon from scratch).

**No hacks (30 Oct, P167):** Luke: "I don't want to become a running hacks channel, sloppy and gimmicky." Hacks, "like you're 10" and similar packaging are out (heel lock 1.1M sits on 1,684 followers: hack views don't convert). Keep the mechanism (one thing shown on a real object). Today's trial: the wall only. **Wed 4: WHY YOU'RE NOT GETTING ANY FASTER / AT RUNNING** (the talk test shown mid-run), Tue 3 trials A that title, B THE RUN THAT'S STOPPING YOU / GETTING ANY FASTER; brief Mon. Below, the hacks and heel-lock lines are superseded.

**Trial reels (30 Oct, `ideas/engine-room-nutrition/2026-10-30-trial-reels-today.md`):** Luke's first. **HEEL LOCK has 1.1M on Luke's personal TikTok** (the hacks format, proven; gels meme 45.8K). Today on ERN Instagram, no filming, auto-share off: HEEL LOCK (original file, no TikTok watermark) and the wall reposted; optional the gels meme. Judge at 24h: share to profile if skip under 38%, watch over a quarter, shares 0.5%+. Trials can't be collabs (as far as we know): post from ERN. Personal TikTok = test bed for new formats, fresh takes only (never the same file on both TikToks). Personal TikTok bio says "Free fuel guide": change to "Free race plan + early bar access". Next: Tue 3 hacks A/B; Fri 6 not-faster title A/B.

**Wider topics (30 Oct, `ideas/engine-room-nutrition/2026-10-30-interest-topics.md`, P166):** Luke: "very one track minded". Until spring races are 6 weeks out, Wed and the weekend trial are interest topics for any runner with a stake and a bridge to the plan or pre-run fuel (the bar's slot); Mon stays marathon goal time for emails; runners only (no GAA/gym on this account); trial reel first. Ready now: LEGAL RUNNING HACKS / THAT FEEL LIKE CHEATING (**Wed 4**, replaces start-too-fast), WHY YOU'RE NOT GETTING ANY FASTER / AT RUNNING vs HOW TO GET FASTER AT RUNNING, / EXPLAINED LIKE YOU'RE 10 (same script, title A/B, Fri 6). Waiting on Luke's science: fitness lost when you stop, what to eat before a morning run, pre-run snack tier list; also running-advice ranking, "we asked [N] runners" (real counts only), fastest 5K (needs 5K pacing in FACTS). Wrist video to Fri 13. Judge on Fri 13. Need: can the plan cover 5K/10K/half?

**Creative strategy (30 Oct, `ideas/engine-room-nutrition/2026-10-30-creative-strategy.md`):** Luke dropped the 42.2K and next-goal topics ("who gives a fuck? nobody cares"): **P165, the "who cares" test before any score; timing never rescues a dull topic.** Through line: "the exact plan for your marathon, K by K, so it doesn't fall apart." Two locked formats plus one test a week (70/30): **Mon HOW TO PACE A [GOAL] MARATHON / AT EVERY 10K (emails; 5:00, 4:15, 3:15, 5:30); Wed WHAT TO DO WHEN [FEAR] / IN A MARATHON (reach); Fri the creative test; weekend an old winner reposted as a trial reel.** Tests in order: WHAT TO WRITE ON YOUR WRIST / BEFORE A MARATHON (Fri 6), the wall explained like you're 10 vs how to pass people at 30K (trial reels), ranking marathon mistakes by minutes (needs Luke's science), 3 things I wish I knew before my first marathon, ranking what runners eat (TikTok). Brand: tops as the on-camera uniform and the reward for a race result, never a merch post; sell in stories, a monthly Live and emails, never reels; proof stories from plan users. Pro list: the gap is the fuel-testing season (sell in January; is the race pack real?), comment-keyword auto-DM test for per-video attribution (one reel), a small paid test for cost per email, YouTube Shorts, a Strava club, collabs with run clubs. Need from Luke: race pack yes/no, does he write on his wrist, mistake minutes, ManyChat yes/no, sign-ups 29 and 30 Oct. **This week: Fri 30 the wall as a trial reel; Mon 2 5:00; Wed 4 WHAT TO DO IF YOU START / YOUR MARATHON TOO FAST; Fri 6 wrist.**

Latest review: `ideas/2026-10-29-nyc-review.md` (NYC at ~4h: skip 43.2%, Lower than typical, the narrow-gate range; **saves 2.3% and shares 0.6% Higher**; 25s on 1:39; no CTA step at 0:42; reach below typical; no forecast given, my miss). Course videos are judged on saves, sends and emails, not reach. **Week plan 29 Oct (`ideas/engine-room-nutrition/2026-10-29-week-plan.md`): most sign-ups came on 24, 26 and 28 Oct, when runners were planning a race (race eve, the day after Dublin, the "next one" video), not on big-reach days; the CTA now speaks to the next race.** **Stories (29 Oct, `ideas/engine-room-nutrition/2026-10-29-stories-plan.md`): one question a day (Mon next race and goal, Tue title poll, Wed reel quiz, Thu what you eat before the start, Fri long run, Sat where it went wrong, Sun how it went); reply to every answer with the plan link; counts in `ideas/stories-log.md`.** **Spring (29 Oct): most say spring races, mostly Irish and UK. Order: 42.2K (Fri 30), next-race goal (moved up), gone out too fast (reach), 5:00, first-timer how hard (if Tuesday's poll says so), wind (science); course videos 2 to 4 weeks before each spring race (Seville first, late January). Stories: Mon which spring race, Tue first marathon?, Sun countdown sticker.** **Luke 29 Oct: no Dublin race reel (it's the podcast's).** Ideation `ideas/engine-room-nutrition/2026-10-29-ideation.md` (10 topics scored): **Fri 30 WHY YOUR MARATHON WAS / LONGER THAN 42.2K; Mon 2 5:00; Wed 4 WHAT TO DO WHEN YOU'VE GONE OUT / TOO FAST IN A MARATHON (reach, trial A/B Tue); Fri 6 race morning.** (Old: our Dublin race read with the 3 numbers (brief `ideas/engine-room-nutrition/2026-10-29-brief-dublin-numbers.md`: broad gate, Luke's splits as frame one, both runners' first 10K, first gel and the K it turned; title depends on the numbers; waiting on the numbers from Friday's podcast). Then Mon 2 Nov: 5:00 pacing. Next reach reel: a famous fear not yet covered (the wall family has 5). Next course video (Valencia): trial-reel A/B of frame one, bare map vs labelled (P159 vs P161). Need from Luke: sign-ups Thu 29 and Fri 30.

Latest review: `ideas/2026-10-28-last-marathon-review.md` (posted to the profile at ~12:27pm, read at ~6h): **skip 52.4%, our worst** (a busy motion frame, a repeat of P147, plus a narrower gate than P153: both my miss); 23s on 1:26; **saves 1.8% and comments 0.3% Higher**; 4 follows IG, 5 TikTok; body flat at ~17%; the CTA step was small. Motion graphics stay in the body; the first 3 seconds are one big thing (P159). **Motion graphics off the main post (P160, Luke 28 Oct):** photo-top reels median about 29K, the 4 motion reels about 11K. Every reel uses the winners' 3 layers (a real picture on top, blue title then stage markers in the middle, Luke below, one line of subtitles), with a mock-up image of the frames (New York: `ideas/engine-room-nutrition/mockups/nyc-frames.png`). Motion only as a trial reel against it.

**After the autumn season (`ideas/2026-10-28-off-season-plan.md`):** the season moves to December and spring; 5 pillars (race-day fears as the weekly reach reel, the viewer's before and after, goal times for emails, course breakdowns 2 to 4 weeks before each big race, podcast clips); training weeks still out. **Scripts ready (28 Oct):** walk (`2026-10-27-script-walk.md`: still posts, A and B as trial reels today, winner to the profile Thu); New York (`2026-10-28-script-nyc.md`, film Thu, post Fri); the last-marathon test (`2026-10-28-script-last-marathon.md`, trial reel only). **Test this week:** WHAT YOUR LAST MARATHON SAYS / ABOUT YOUR NEXT ONE as a trial reel (brief `ideas/engine-room-nutrition/2026-10-28-brief-last-marathon.md`: 3 numbers from their watch: first 10K, first gel, the K it turned), recorded with the walk today.

Latest review: `ideas/2026-10-27-enjoy-and-surprise-review.md`. **Enjoy:** 10.4K IG at 2.7 days (16.9K with FB), skip 38.2%, 30s on 1:32, a quarter still watching at 1:20 (the body held), save 1.2% (nothing too long to remember, P152), the CTA cost a third of who was left at 0:42, flat after day one because the posted gate said "this weekend" (P153); TikTok 4.1K. **Surprise:** 4.2K IG (6K with FB), skip 44.1% (opening frame Luke talking, not the bib: a repeat of ledger row 1), 0 saves, 0.1% shares, but flat at ~22% from 0:13 to the end and 13.6% full on TikTok (P151: a story opens an advice video). Follows read 0 on both from Luke's side: check the ERN side. **Emails (27 Oct, `ideas/2026-10-27-email-attribution.md`):** Klaviyo has no per-video attribution; sign-ups ran 9+ (Sat evening), 7 (Sun), **11 on Mon with no new reel** (old videos drive them). No dropdown or extra step on the form (Luke: friction, P154): each review counts sign-ups on the post's day and the day after, against no-post days as the baseline. Never put subscriber emails in the repo.

Lifetime on the grid (24 Oct): carb load 84.4K, without the wall 83.8K, 3:45 51K, how hard 46.5K, sub-4 30.4K, second half 29.2K. Lifetime runs 1.6 to 2.1 times the first-day read: forecast with that.

Grid (Instagram, ERN side): the wall 147K; **3:45 pacing 29.1K at ~17h, TikTok 10.9K (record), emails up with the CTA a third of the way in (P128)**; **carb load 52.8K at ~20h (our #2: 1.3K saves, 60 follows, a record; skip 46.7%)**; **without the wall 41.5K at
18h** (record 39s watched on 1:37, save 3.2%, 25 comments; skip 39.3%
with no reframe in line one and the first AI cover); out of the wall
40.8K; 7 days 31.4K at 14h; 24 hours 30K; first 10 minutes 27.1K at
12h (share 1.4%, a record); how hard at every 10K 25.1K at 13.5h (skip
31.9%; first plan CTA: 4 emails); goal pace 25.3K; cramp 25K; second
half 17.6K at 14h; sub-4 at every 10K 14.5K at 18h (skip 40.8%) but
**9.5K on TikTok, the best TikTok yet** (without the wall: 6.3K, second
best); quit ~14K at 14h; Dublin course (small reach, deepest
engagement); taper and heavy legs missed.

Before that: `ideas/2026-10-24-sleep-review.md` (sleep at ~12.75h: 6.4K, **skip 41.4%**: the opening frame was a sentence that gave away the reassurance, P147; save 1.0%, off the race clock; the CTA at 0:49 lost half of who was left, because the hook ran 116 words). Before it: `ideas/2026-10-23-goal-gone-review.md` (goal gone at ~9h,
10pm post: 6.5K, **skip 31.9% joint best** with a motion graphic of the hook
as the opening frame; save 2.4%; share 0.1%; the "why" rehook stage lost
half the remaining viewers). Before it: gel (5.8K, narrow topic); 4:30
(14.6K, skip 37.0%); 3:45 (29.1K).
Earlier: cold marathon (real cover 35.1% skip, 0.9% saves; AI covers
retired), carb load (52.8K, our #2).

**Week plan (demand-led, 19 Oct):** `ideas/engine-room-nutrition/2026-10-19-demand-led-week.md`
(from Luke's inbox themes and TikTok search). Tue 20: 3:30 pacing. Wed 21
(views): what to do when you can't face another gel. Thu 22: how to turn
your half marathon time into a marathon goal (incl. after illness). Fri 23
(views): how to run the New York marathon. Sat 24: how to actually enjoy
your marathon. 4:30 goes TikTok-only. Luke's goal: 1M lifetime IG views
(840K on 19 Oct). Every pace in km and miles in captions (P129).

**Why no 100K since the wall** (`ideas/2026-10-27-why-no-100k.md`): median skip rose from 34% (28 Sep to 14 Oct) to 40% (15 to 25 Oct), and only 1 of the last 12 was the wall family. It matters for the 1M, not for emails: **one reach reel a week to the wall formula, skip target under 32%**; the rest for emails.

**This week (27 Oct, `ideas/engine-room-nutrition/2026-10-27-week-plan.md`):** Wed 28 WHAT TO DO WHEN YOU HAVE TO / WALK IN A MARATHON (**script ready: `2026-10-27-script-walk.md`**, trial reels A and B tonight; next review `ideas/YYYY-MM-DD-walk-review.md`); Thu 29 free (film New York; 5:00 moves to Mon 2 Nov, P156 pace); the walk is the first trial-reel test (two first lines, Tue evening); **Fri 30 HOW TO PACE THE NEW YORK / MARATHON, SECTION BY SECTION** (brief `2026-10-27-brief-nyc.md`, film Thu; worked 4:00 plan in miles, km in the caption; course map cover; check the official map) and Luke and Jamie record podcast episode 1 (Dublin at every 10K; `podcast/README.md`, its own chat in this repo; plan `podcast/2026-10-27-episode-1-plan.md`, waiting on the facts list; Sat's hook lines recorded straight after the podcast); Sat 31 WHAT WE DID AT EVERY 10K / OF THE DUBLIN MARATHON, cut from the podcast (Jamie story opens, Luke's splits as cover); wind moves to next week; Sun 1 no reel. **New gate: "If you've got a marathon coming up,"** (P153). Brief first each time. **Next (27 Oct):** the audience calendar has moved on from race weekend (New York 1 Nov; spring pivot). Next script: a lived race fear on the race clock with a schedule to keep (P152), the Jamie story as the opening of an advice video if used at all (P151), no dated gate (P153). Posted 24 Oct: enjoy script v2 `ideas/engine-room-nutrition/2026-10-24-script-enjoy.md` (line one ends on the open loop, P149; 0-10K let them go, 10-20K head up, 20-30K your name, 32K your people; opening frame a bare 32K marker; failure ledger table passed; two P146 checks flagged: name on the top, supporters at 32K). Next review file: `ideas/YYYY-MM-DD-enjoy-review.md`. **Sun 25: Luke surprises Jamie (co-founder) by running Dublin too;** plan and shot list in `ideas/engine-room-nutrition/2026-10-24-plan-surprise-jamie.md` (OST: MY CO-FOUNDER HAS NO IDEA / I'M RUNNING THIS MARATHON; reaction held to the end; cover never Jamie's face; nothing posted before the reveal). Post Mon 26 (council v2, P150: context + real stake in 10s, "my own entry", vertical 2 phones, edit decided by the reaction); Tue: the race at every 10K as the advice sequel. The no-Dublin rule on the personal account lifts after the reveal. Walk moves to Tue; spring pivot from 27 Oct.
Next review file: `ideas/YYYY-MM-DD-<video>-review.md`.
Motion graphics (22 Oct, Luke asked): `motion/` renders 16:9 scene clips for the top half of the reel (`motion/README.md`). Goal gone is built in placeholder colours; waiting on Luke's logo to set the brand colours. Run it as a trial reel A/B against the plain version: the checklist still says only the title and stage markers on screen (P84, P95). Race night (sleep, Sat 24) built 23 Oct in the website theme (`motion/race-night.html`); that theme is the default for motion graphics now. Enjoy built 24 Oct (`motion/enjoy.html`): illustrated characters, the 32K marker alone as the opening frame (P147), and a course bar with a locked 32K pin as the on-screen open loop. Last marathon built 28 Oct (`motion/last-marathon.html`): splits screen as the opening frame, a 3-number strip with number 3 locked, ending on a filled-in card to save (P152). NYC course frames v2 (28 Oct, Luke: the first ones "suck", P161): 6 frames, 1920 x 1080, site theme, each stage zoomed with landmarks, mile markers, the 4:00 pace in miles and km and the cues, plus a whole-plan frame; `motion/nyc-maps/frames/`, same artifact https://claude.ai/artifact/4fb7kihUqVTYc1Eo6tHy7K. Reuse `motion/nyc-maps/tools/` for the course breakdowns pillar.

Rejected topics: the last 10K (covered across six videos); anything
after the finish line (Luke, 15 Oct); in-race fuel amounts while the
"eleven gels" argument is live (Luke, 17 Oct, P124). TikTok-only idea: goal-time
versions (sub-3:30, sub-4:30) using the sub-4 template.

Upcoming races in the audience: Amsterdam 18 Oct, **Dublin and Frankfurt
Sunday 25 Oct** (26 Oct is the bank holiday Monday), New York 1 Nov. Held: the "how to actually enjoy your marathon"
creative for the day before Dublin. Covers: Luke picks from search
terms (Google Images, Pinterest), with a licence check.

The plan CTA keeps bringing in emails (Luke, 15 Oct): keep it on every video.
