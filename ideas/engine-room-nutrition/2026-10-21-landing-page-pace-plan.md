# Landing page: the free marathon pace plan (21 Oct 2026)

Luke, 21 Oct: the videos send people to the site for a free marathon pace
plan, but the site offers a free "Ultimate Endurance Guide" and a bar
waitlist. Fix the disjoint. Pages read on 21 Oct:
`engineroomnutrition.com/` and `engineroomnutrition.com/pages/fuel-1`.

## What a viewer sees today (the 4:30 video, step by step)

1. Hears: "email us your race and goal time through the link in the bio
   and we'll send you your own times, free."
2. Taps the bio link. Lands on fuel-1 (or the homepage). Headline:
   **"Elite Engine. Empty Tank."** Offer: **"The Ultimate Endurance
   Guide: Elite workouts, Carb mastery, 12 & 16-week training plans."**
3. Scrolls into GAA half time, triathlon T1/T2, cycling stops, CEOs and
   the HPA axis.
4. The form asks for first name and email. **Nowhere to put a race or a
   goal time**, so the thing they came for can't be ordered on the page.

Each step loses people. The ones who get through do it in spite of the
page.

## What's wrong, in order of cost

| # | Problem | Why it costs signups | Fix |
|---|---|---|---|
| 1 | **Offer mismatch.** Video: free pace plan. Page: endurance guide + bar waitlist | The visitor checks in about 3 seconds that they're in the right place. They aren't, so they bounce | A dedicated page whose headline repeats the video's promise word for word |
| 2 | **The form can't take the order** (name + email only) | They have to work out how to send a race and goal time themselves, or they get a generic guide | Add race and goal time fields; save them to the Klaviyo profile |
| 3 | **Audience mismatch.** "Hybrid Professional", GAA, rugby, Hyrox, T1/T2, CEOs | The IG audience is amateur marathoners aiming at 3:30 to 4:30. Four of the five use cases aren't them | Marathon only on the pace plan page. Keep the hybrid story elsewhere if you want it |
| 4 | **The site contradicts the videos.** Blog and newsletter push 90g an hour and "recreational runners take 20 to 40g"; the fuel-1 page says gels cause GI distress and flavour saturation after 2 to 3 | The videos say 60 to 75g an hour and teach them to drink their gel. A runner who checks finds two different brands | Cut the 90g line for marathoners (say 60 to 75g); drop the anti-gel table from any page marathon traffic sees |
| 5 | **Weak proof.** "70+ Hybrid Professionals already on the list"; "5★ average" from 3 reviews | 70 next to 840K views makes the list look dead. If Klaviyo is now higher, the page is under-selling you | Real numbers: total video views, plans sent. Update or remove the 70 |
| 6 | **Study language and elite names** (Limbach and Sonnenburg, Kipchoge, Ingebrigtsen) | Reads as borrowed authority. The videos win because they're specific and practical | Replace with a real sample plan |
| 7 | **The bar is pitched for half time, transitions and ultras** | For this audience the bar's honest job is race morning (90 minutes before the gun). That's already on the page; lead with it | One line on the pace plan page, opt-in only |

## The fix: one page, one offer

Build **`/pages/pace-plan`** and point the bio link (and the pinned
comments) straight at it. Leave fuel-1 for bar traffic. Don't send
Instagram to the homepage: it has six offers (test pack, guide, quiz,
calculator, blog, waitlist) and the visitor wants one.

Why one new page beats editing fuel-1: fuel-1 is built round the bar and
the guide. Rewriting it breaks whatever else links there, and you can't
measure the IG traffic cleanly. A new URL gives you one Klaviyo source to
count signups per video against.

## The page copy (ready to paste)

No em dashes, no jargon, km and miles everywhere (P129).

**Above the fold**

Eyebrow: FREE · FOR YOUR NEXT MARATHON

Headline: **Your marathon pace plan, worked out for your goal time.**

Sub: Tell us your race and your goal. We'll send you the times to hit at
every 10K sign, your watch pace in km and miles, and when to take each
gel. Free.

Form (one card, five fields, button):
- First name
- Email
- Your race (dropdown: Dublin, Frankfurt, New York, Valencia, Seville,
  London, Other: type it)
- Race date
- Goal time (dropdown, 5-minute steps from 2:59 to 5:30, plus "Not sure
  yet")
- Tickbox, unticked: "Tell me when the Engine Room bar launches."
- Button: **Send me my pace plan**
- Under the button: Free. No card. Unsubscribe any time.

Proof line under the form: **Over 840,000 views on our marathon videos.
[N] pace plans sent so far.** (Fill N from Klaviyo; drop the clause if
it's small.)

**What you'll get (a real example)**

Show the 3:30 plan as a picture of the email, not a list of features:

> **Your 3:30 plan**
> 10K sign: 50 min. 20K: 1:39. 30K: 2:29. 40K: 3:18.
> Watch pace: 4:55 to 5:00/K (7:55 to 8:05/mi) for the first 10K, then
> 4:50 to 4:55/K (7:45 to 7:55/mi). Last 2K: 4:40 to 4:45/K.
> Gels: first at 20 minutes, then a 30g gel every 30 minutes, with 3 or
> 4 sips of water. Carry 7.

Line under it: Every number checked against the 10K signs on the course,
not your watch, because your watch reads about 1% long.

**Three short blocks (how it works)**

1. **Tell us your race and goal.** Two fields, ten seconds.
2. **Get your plan by email.** Your 4 checkpoint times, your watch
   pace, your gel times.
3. **Write it on your arm or your band.** Check it at every 10K sign.

**From the videos** (3 embeds or screenshots with view counts: the wall
147K, carb load 52.8K, 3:45 pacing 29.1K)

**Who's behind it** (two lines)

We're Luke and Jamie. We've run the marathons and hit the wall, and now
we make the videos you came from. We're also building a carb bar for
race morning.

**FAQ**

- *Is it really free?* Yes. You'll get your plan and our race-week
  emails. Unsubscribe any time.
- *My race isn't listed.* Pick Other and type it.
- *I don't have a goal time.* Pick "Not sure yet" and tell us your last
  half marathon time in the reply; we'll work it out.
- *Miles or km?* Both.

Repeat the form once at the bottom.

## Klaviyo set-up (so it scales past replying by hand)

- Save **race**, **race_date** and **goal_time** as profile properties,
  and `source = ig_pace_plan`.
- One welcome flow. Its first email uses a conditional block per goal
  band (the same templates the videos use: 3:30, 3:45, 4:00, 4:30, and
  every 5 minutes between). That sends the plan in minutes, which
  matters: the request comes in the week of the race.
- The bar launch tickbox goes to a separate list. CLAUDE.md: ask consent
  before adding anyone to a launch list. Today's page implies everyone
  joins it; fix that too.
- Email 2 the Thursday before their race_date (race-week checklist),
  email 3 the day after (how did it go? reply). That's the reply data the
  videos feed on.

## What to fix on the rest of the site (after the page is live)

- Blog "Why elite runners eat twice your carbs" and Newsletter Issue 02:
  change the marathon advice to 60 to 75g an hour, so a viewer who
  reads them doesn't find the opposite of the video.
- fuel-1 "The problem with gels" table: remove or move off any page
  marathon traffic sees, while the videos teach gels.
- "70+ on the list": update to the real Klaviyo number or remove.
- Homepage hero: add a third button, "Free marathon pace plan", during
  the autumn race season.

## Waiting on Luke (blocks the build)

1. Where the bio link points now (fuel-1, the test pack page, or a link
   tool).
2. How the pace plan requests arrive today: replies to the welcome email,
   direct emails, or DMs? And who writes the plans, by hand?
3. Klaviyo: list size now vs 14 Oct, signups per day since the CTA went
   in, and the form's conversion (views to signups).
4. Can you add a page and a custom Liquid section in the Shopify theme,
   or does someone else edit it?
