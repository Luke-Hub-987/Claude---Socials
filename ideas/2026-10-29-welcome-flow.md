---
type: email strategy (Luke, 29 Oct: the layout for the welcome flow; "most welcome flows I just ignore", so every email needs real value and stakes; the bar is close to a commodity with cheaper alternatives, so brand and trust have to carry it) + a vet of Gemini's revenue model + LLM Council (P150)
generated_at: 2026-10-29
basis: Luke's Klaviyo screenshots (profiles, the Welcome Series flow, Email 1 "Guide Delivery"); PLAN-brand-and-business.md; FACTS.md; the reel data (carb load 4.4% to 5.2% saves, 7 days 3.0%, the countdown family, P152 saves need something too long to remember, P156 sends, P158 before and after, P57 process is a reward, P154 no added step)
data care: the screenshots show subscriber addresses. None are recorded here (P154). Counts only.
---

# The welcome flow: built around their race

## 1. What the screenshots say

| Number | Value | Read |
|---|---|---|
| Profiles | 591 (568 active, 23 suppressed) | The list grew about 120 in 8 days after the 21 Oct count (468), most of it race weekend |
| Email 1 open rate (30 days) | 62.8% (245) | Good, but Apple Mail inflates opens. Don't steer by it |
| **Email 1 click rate** | **24.4% (95)** | **Very high.** A typical welcome email gets a fraction of that. People click when it's their plan |
| Emails in the flow | **1** | **The real gap.** After the plan there's nothing, so the list goes cold until launch |
| Bar mention | One P.S. line and a waitlist link | Honest, with the consent built in (CLAUDE.md). Its click count is our first demand number |

**So your instinct is half right.** People ignore welcome flows that are
about the brand: "our story", "follow us", 10% off. They don't ignore
Email 1, because it's what they asked for: one in four clicked. The fix
isn't a better welcome. **It's emails that arrive when their race needs
them, about their race.**

## 2. First principles: why an email gets opened

1. **It's about me.** Their race, their goal, their pace band. Never "us".
2. **It arrives when the stake is highest.** The reels prove this: the
   countdowns are our best keepers (carb load 84K lifetime and a record 5.2%
   saves early on; 7 days 31.4K; 24 hours 30K). In an inbox, a countdown
   tied to *their* race date is the strongest stake there is.
3. **It holds something too long to remember** (P152): a schedule, a
   table, their numbers. That's why they keep it and come back on race
   morning.
4. **A real person is on the other end.** A reply from Luke is the
   strongest trust signal a two-person brand has, and at 568 people it's
   still possible.

**Why this answers "the bar is a commodity":** a rice crisp square *is* a
commodity, on purpose (it's familiar). What isn't a commodity is the people
who handed you your race plan, checked in the week of the race, asked how
it went and told you what to change. Ireland already buys commodities on
loyalty (Barry's or Lyons is a tribe, not a taste test). **The flow is the
trust machine; the bar rides on it.**

The order trust is built in, strongest first:
1. **A promise kept on race day** (the plan worked).
2. **A personal reply.**
3. **Being let inside** (the batches, the testing, a say in the bar).
4. **Consistency** (every number matches the videos).
5. **Honesty** (it isn't out yet, and we say so).

## 3. The flow map

```
Signs up (bio link or caption)
   │
   ▼
E1  The plan (now, as it is)  ── builds a plan on the site? ──► sends "Plan Built"
   │                                                          (race, race date, goal)
   wait 2 days                                                      │
   │                                                                ▼
Has built a plan? ── yes ──────────────────────────────►  TRACK A: THE RACE COUNTDOWN
   │                                                      (timed to their race date)
   no                                                     A1 on build: your plan + pace band
   ▼                                                      A2 race −7 days: carb load, day by day
TRACK B: NO RACE YET (weekly)                             A3 race −2 days: your last 48 hours
B1 day 2:  the K that decides your marathon               A4 race morning, 6:30am: 3 numbers
B2 day 5:  one question (reply)                           A5 race +2 days: how did it go? (reply)
B3 day 9:  the bar, from the inside (taste panel)         A6 race +10 days: your next one ──► back to A
B4 day 14: when your block starts                                  │
   │                                                               │
   └──────────────► monthly email (one a month) ◄──────────────────┘
```

**Rules for the map:** never more than one email a week outside race week;
race week gets three because that's when the stakes peak. Anyone who
builds a plan leaves Track B and enters Track A. A new race date re-enters
Track A.

## 4. Each email

Subject lines follow the OST rules: plain words, the race moment, the
answer held back (ledger row 1). The race name in the subject line is the
stake. Every number comes from FACTS.md.

### E1: the plan (live; keep it)
It works (24.4% clicks). Three changes:
1. **The site builder sends a "Plan Built" event to Klaviyo** with the
   race, the race date and the goal time (section 6). No new step: they
   already pick the race and drag the clock.
2. **The builder gets an optional "Send this plan to my inbox" box** for
   people who arrive from the bio without signing up. Nobody else gets an
   extra step (P154), and it grows the list straight from the tool.
3. **The P.S. stays.** Count its clicks every review: it's the first
   number that says whether anyone wants the bar.

### A1: on building a plan
- **Subject:** Your 3:45 plan for Valencia (their goal and race)
- **Preview:** Print it, fold it, race with it
- **The stake (first 2 lines):** their goal time and race, and the one
  mistake that costs it (going out too fast).
- **Body:** their table (10K signs, watch pace, race clock, talk test,
  gels) and **a printable pace band** (the test from PLAN-brand-and-business
  section 5). One line: "Print it, fold it, and keep it in your pocket or
  round your wrist."
- **CTA:** "Reply with your longest run so far and I'll tell you if the
  goal's right." (Answers the sceptic, P141; starts the reply habit.)
- **Send line (P156):** "Running it with someone? Forward this so they can
  build their own."
- **P.S.:** the bar in one line, new wording.

### A2: race minus 7 days
- **Subject:** 7 days to Valencia: your carb load
- **Preview:** What to eat, day by day, to the start line
- **Stake:** a week out, the one thing they can still change.
- **Body:** the carb-load schedule from the carb-load script (every meal,
  its clock time and amount, P121, P123), as a table. Nothing else.
- **CTA:** "Screenshot the table." One link back to their plan.
- **P.S.:** "Race in a week? Reply RACE WEEK and I'll answer yours first."

### A3: race minus 2 days
- **Subject:** Your last 48 hours before Valencia
- **Stake:** the highest of the whole flow.
- **Body:** one timeline: dinner the night before, bedtime, breakfast time
  and what, the last 30 minutes, the first gel at 20 minutes, their first
  10K pace band. **The last 30 minutes is the bar's slot.** Until it
  exists, say what most runners do there, honestly, and then one line:
  "This half hour is exactly why we're making the bar."
- **CTA:** none but the plan link.

### A4: race morning, 6:30am
- **Subject:** Today: 3 numbers
- **Body:** under 50 words. Their first 10K pace band, their first gel
  time, the 10 words. "Good luck. Reply after with your time."
- Why: it's the moment they remember you were there. Nobody else emails
  them on race morning.

### A5: race plus 2 days (the most important email in the flow)
- **Subject:** How did Valencia go?
- **Body:** "Reply with 3 numbers: your 10K split, when you took your first
  gel, and the K it got hard. I'll tell you what to change for the next
  one." (The before and after, P158; the last-marathon brief's 3 numbers.)
- **Luke answers these personally.** It's the promise kept, the customer
  research, and, with their permission, the before and after stories for
  reels and the launch.

### A6: race plus 10 days
- **Subject:** Your next one
- **Body:** when their next block would start for the spring races (16
  weeks before; check each date), and the builder. Then **the founding
  invite** (B3's offer) if they haven't had it.

### B1: day 2, no race yet
- **Subject:** The K that decides your marathon
- **Body:** the first 10K, the wall's real start (our biggest video, 147K),
  as a 3-line method with numbers, and the builder to get theirs.
- **CTA:** build your plan.

### B2: day 5
- **Subject:** One question
- **Body:** under 60 words, plain: "What scares you most about race day?
  Hit reply, one line is plenty." Replies train Gmail to keep us in the
  Primary tab, and they're next month's reel topics (demand-led, like the
  19 Oct week).

### B3: day 9, the bar from the inside
- **Subject:** What goes in your hand before the gun
- **Body:** their before and after first (the pen, the nerves, the gel
  they force down), then the honest build: the batch number, what failed,
  one real photo from the kitchen. This is where process content belongs:
  P57 says it's a reward for people who already care, and the list already
  does.
- **The offer:** "We want 50 runners to test it before anyone else, before
  their long runs. Reply TEST or join the list." Consent is the click.
  This is the taste panel from PLAN-brand-and-business section 7.
- Nobody swaps a bar they helped make.

### B4: day 14
- **Subject:** Your block starts sooner than you think
- **Body:** the spring races and the week each 16-week block starts
  (check every date). "The race starts before the gun." CTA: pick your
  race, get your plan.

## 5. Layout rules for every email after E1

- **From Luke, a plain look:** white background, no banner, one table at
  most, his name at the end. E1 stays designed because it is the
  deliverable. Designed, image-heavy emails tend to land in Gmail's
  Promotions tab, and most of the list is on Gmail.
- **The stake and the first value in the first 3 lines** (P69).
- **One thing too long to remember** (P152), except the one-question email.
- **One CTA** (a reply or one link) and a P.S.
- **A forward line** where it fits (P156).
- **The P.S. carries the bar** in one line, new words each time (P136).
- **Under 200 words** except the schedules.
- **No dated words in Track B** (P153). Track A can be dated: it's timed
  per person.
- **No maths** (P155): the email gives the answer, the builder does the sum.
- **No discount codes, ever.** There's no product, and a discount teaches a
  commodity buyer to wait for the next one.

## 6. Setting it up in Klaviyo

1. **The builder, on "show my plan":** if Klaviyo knows the visitor (they
   came from an email click, so onsite tracking identifies them), send a
   "Plan Built" event with the race, race date and goal, and save
   `race_name`, `race_date` (a date) and `goal_time` to the profile. Whoever
   built the site adds this; it's a few lines of the Klaviyo onsite script.
2. **Track A:** its own flow, triggered by the `race_date` date property,
   with emails at −7 days, −2 days, the day itself at 6:30am, +2 days and
   +10 days. Flow filter: race date still in the future at entry. Test with
   your own profile what happens when someone builds a second plan with a
   new date.
3. **The Welcome Series:** after E1, wait 2 days, then a conditional split
   on "Plan Built at least once". Yes: exit (Track A has them). No: B1 to
   B4, each with a filter to leave the flow the moment a plan is built.
4. Smart Sending on, so nobody gets two emails in a day unless it's race
   week.

## 7. What to measure

| Signal | Why | Target to start |
|---|---|---|
| **Clicks and replies** per email | Opens are inflated | Clicks over 8% after E1 |
| Unsubscribes per email | The cost of each email | Under 0.5% |
| **The waitlist share** of active profiles | The first demand number for the bar | Set once we have 2 weeks |
| Plan builds per sign-up | Whether Track A fills | Set once we have 2 weeks |
| A5 replies | Trust and research | Count them; every one is a customer call you didn't have to book |

## 8. Gemini's revenue model, vetted

Useful as a frame, wrong on the number that decides everything.

| Gemini's claim | Holds? | Why |
|---|---|---|
| €240K of margin to replace two €100K salaries and €40K overhead | The sum holds | It's a 3-to-5-year number, not a launch target. The gates in PLAN-brand-and-business section 8 come first |
| One founder out first (~€100K) | **Yes** | Same as our triggers |
| A shared commercial kitchen (Bia Innovator Campus, Athenry) | **Worth costing** | No co-packer minimum order, and you control the recipe. Is this one you're looking at? It changes section 6 of the business plan |
| €0.39 cost per 45g bar (16c ingredients, 11c packaging, 12c labour) | **Optimistic** | Leaves out waste, shelf-life and allergen testing, labels and storage. 12c of labour means about 200 finished, wrapped bars an hour per person. Cost a real test day |
| €19 a 12-pack = €1.58 a bar of revenue | **Check VAT** | If the bar is standard-rated, that's about €1.29 ex-VAT. You'll know the rate |
| 35c a bar to ship (€4.20 a box) | **Low** | Packing plus postage in Ireland is likely more, and the UK more again |
| **1,330 subscribers on 24 bars a month** | **The flaw** | That's 288 bars a year each. A marathoner eating one before each long run in two blocks eats about 35. At 35 a year you need roughly 8,000 customers, not 1,330. **How many bars a runner eats a year is the number the customer calls must answer** |
| Price at €19 a box | **Wrong way round** | Pricing near the supermarket square starts a price fight you lose, which is your own commodity worry. Price within the performance-bar range (check run-shop shelves) and sell it inside the plan |
| 55 cafés selling 50-60 bars a week each | **High** | A new bar in a café rarely does that, and someone has to deliver to and restock 55 accounts every week |
| GAA and rugby "matchday crates" | **Later** | A different customer and buyer (a club treasurer). €99K to €112K is revenue, not margin. It's the expansion path, not the beachhead |
| A €19 digital fuelling blueprint | **Cut** | It sells what we give away, on a team-sport topic our audience doesn't have, and 250 a month from a 568 list isn't credible |
| Merch | After the bar | Tiny now |
| Race fuel contracts | **Backwards** | Brands usually pay, or give product, to be official fuel. And our runners won't eat real food mid-race (P134). Sampling at events is a marketing cost |
| Its closing question: subscribers or 20 café and club accounts first? | **A false choice** | Neither, until 50 runners have eaten the bar before long runs and said they'd reorder |

## 9. LLM Council (P150)

- **Contrarian:** More emails mean more unsubscribes. Track A needs
  someone to change the site, and it misses everyone who never builds a
  plan. Luke can't answer hundreds of replies once the list is in the
  thousands. A plain email after a designed one can look cheap.
- **Assumption-ripper:** We assumed the welcome email is the problem; it's
  our best number. The problem is there's no second email. Luke assumes
  everyone ignores welcome flows because he does: he ignores brands
  selling to him; these runners asked for a plan and one in four clicked.
  We assume opens are real (Apple Mail inflates them) and that the builder
  captures a race date (check it).
- **Expansionist:** A5 turns every race into data, a story for the reels
  (with permission) and a way back in for the next race. B2's answers
  write the next reels. The taste panel turns 50 people into co-makers.
  "Send this plan to my inbox" grows the list from the tool itself.
- **Outsider:** "If you emailed me my plan the week of my race with my
  carb load, I'd open every one. If you sent me your founder story, I'd
  unsubscribe."
- **Executor:** This week: the Plan Built event (ask whoever built the
  site); write A1 to A5 and B1 to B4. By 15 Nov, both tracks live. Read
  clicks, replies, unsubscribes and the waitlist share at 2 weeks.

**Blind cross-review:**
- Plain from E2 onwards, accepted; E1 stays designed.
- The reply load: Luke answers A5 personally (the trust peak); other
  replies get answered in batches with a personal first line. Revisit when
  the list passes 2,000.
- "Too many emails": answered by the cap (one a week; three in race week).
- Track B is the fallback for anyone without a plan, so nobody is missed.

**Chairman's verdict:** **Build the flow around their race date.** Keep E1.
Add the Plan Built event so the race countdown (A1 to A6) arrives the
week their race needs it, with Track B for anyone who hasn't picked a race.
The bar lives in the P.S. and in one insider email with the taste-panel
offer, never as a pitch. Judge it on clicks, replies and the waitlist
share, not opens. Rule P162.

## 10. Needed from Luke

1. Does the site builder know the race date, or only the race? Who built
   the site, and can they add the Klaviyo event?
2. How many have clicked the P.S. waitlist link, and how many are on the
   waitlist now?
3. Is the Athenry kitchen a real option you're costing?
4. The batch number and one honest photo for B3.
