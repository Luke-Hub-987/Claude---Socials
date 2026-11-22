---
type: idea review (P150 council)
generated_at: 2026-11-22
idea: Luke, 22 Nov: a web app that connects your training plan (Garmin, Strava) to your life calendars (Google, Outlook, work), finds the realistic slot for each run, adjusts intensity around stress, parties, kids and niggles. For time-strapped, previously fit people with money (running, Hyrox, team sport, cycling)
status: for Luke and Jamie to decide; nothing built
---

# The life-calendar training app

## Verdict in one line

**The problem is real and it suits the bar, but don't build the app yet. Test the
service by hand, by email, for 4 weeks. Build only if people come back for week 2.**

## What's strong

- **It's a real frustration, and it's ours.** "I have 14K to run and a 7am
  school run" is the time-strapped professional's week. The plans from Runna,
  Garmin and Strava assume you have time. That's the specific, felt problem
  Seth says to start from.
- **It creates the bar's moment.** If the plan puts your run at 6am before the
  school run, you have no time for breakfast, and that's exactly the moment a
  training bar is for (P237). A plan that says "6:00 run, bar at 5:30" sells the
  bar without an ad. No other idea we have does that as directly.
- **It's an email engine.** People have to come back every week for next week's
  plan. That's Seth's subscriber, not a newsstand buyer.

## What's weak (the honest part)

1. **You're the customer (Seth's trap 1).** A tax director with a work
   calendar and long runs is describing his own week. That doesn't make it
   wrong, but it hasn't been checked with anyone else yet. The 10 fan calls are
   the test: do other people actually move runs around work, or do they just
   skip them?
2. **It's a second business.** Two founders with full-time jobs, a bar still
   with the food scientist, plus reels, a podcast and YouTube. Seth: building
   isn't the hard part any more, attention is. An app needs support,
   integrations, bug fixes and privacy compliance, forever.
3. **The integrations are the hard part, not the code.**
   - **Work calendars:** many companies on Microsoft 365 need an IT admin to
     approve third-party access to Outlook, and many won't. Our target user is
     the one most likely to be blocked.
   - **Garmin and Strava:** Garmin's developer program needs an application and
     approval. Strava tightened its API terms in late 2024 (I haven't re-checked
     the details today).
   - **Health data:** "my knee hurts" and "I'm stressed" are health data, a
     special category under GDPR, with stricter rules. Injury advice also carries
     liability.
4. **The audience widened again.** Hyrox, team sport, cycling and "just
   exercise" is four sports and four kinds of plan. Seth would start with one:
   runners.
5. **Others are close.** Runna (owned by Strava since 2025) and Garmin Coach
   already let you move sessions. I don't know of one that reads your work
   calendar and picks the slot for you, but I haven't searched, so check before
   calling it a gap.

## The cheap test (Seth's Superhuman hour, done by email)

- **Week 1 (from the next email):** "Send us your week: the fixed things (work,
  school runs, late calls) and your goal. We'll send back your runs slotted
  around it, and when to eat." Luke and Jamie do it by hand, with Claude doing
  the drafting. 10 minutes a person.
- **Weeks 2 to 4:** the same people get next week's plan if they reply with
  next week's calendar.
- **The bar to pass:** 50 people ask for a plan within 2 weeks, and **20 of
  them come back for week 2**. Coming back is the behaviour that matters; "I'd
  use that" is what people say.
- **If it passes:** a simple web form (your fixed commitments + goal → a week
  plan by email). Claude can build it in days, with no calendar or Garmin
  access. Calendar sync comes last, and only if the form has weekly users.
- **If it fails:** we've lost 4 weeks of email replies, we've gained 50 emails,
  and we know what time-strapped runners actually do.

## LLM Council (P150)

**Contrarian:** It fails as an app. The best version needs the integrations
that are hardest to get (work Outlook, Garmin), the users most likely to be
blocked, and health data we'd have to protect. And it pulls the two founders
away from the bar, which is the actual business. Strava or Runna could ship
"suggest a slot from your calendar" as a feature next quarter.

**Assumption-ripper:** Three assumptions. (1) Time-strapped people want *more*
planning. Many want less: they'd rather be told "do 30 minutes, any time
today". (2) The problem is *when* to run. It may be *whether*, because
motivation drops after a bad week. (3) People with money will pay for it.
Runna's price is the ceiling we'd have to beat. Ask in the calls, and watch what
people do instead of what they say.

**Expansionist:** The upside is bigger than an app. "Training for people with
a real job" is a brand position, not a feature: the podcast, the again series
and the bar all fit under it. The 6am "no time for breakfast" run is the bar's
best ad. And a weekly plan by email is the reason to be on the list that the
true-fans plan was missing.

**Outsider:** "So it's a calendar that tells me when to run? Can't I just look
at my calendar?" Also: "You make a snack bar. Why are you making software?"

**Executor:** The next email (this week) offers "your week, planned around your
life". Luke and Jamie answer every reply by hand, by Fri 18 Dec. Count requests
and week-2 returns in the weekly loop. Decide on a web form on Mon 21 Dec. Cost:
about 10 minutes a person, no code, no integrations.

**Blind cross-review:**
- The Contrarian's integration and privacy points hold for the app and fall
  away for the email test. That's the case for testing by hand first.
- The Assumption-ripper's "whether, not when" point is the most useful thing to
  learn, and only the hand test can find it. The calls should ask it.
- The Expansionist's "real job" position and the 6am bar moment are the reasons
  to do anything at all. They don't need an app to be true.
- The Outsider's "can't I just look at my calendar?" is answered only if people
  come back for week 2. That's why week-2 returns are the test, not sign-ups.
- The Executor's plan is the only one that costs nothing and gives an answer
  before Christmas.

**Chairman's verdict:** **Don't build. Run the service by hand, by email, from
the next send to 18 Dec, for runners only.** Pass: 50 requests and 20 week-2
returns. Then a simple web form with no integrations; calendar sync only if the
form has weekly users. Every plan says when to eat, which is how this sells the
bar. Hyrox, cycling and team sport wait until runners have passed.
