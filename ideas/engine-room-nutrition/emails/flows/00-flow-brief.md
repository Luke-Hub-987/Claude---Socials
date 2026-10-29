# Klaviyo flows: the brief (Luke, 29 Oct 2026)

Source of truth for the welcome and race-countdown flows. Work one email
at a time: exact Klaviyo clicks, then subject, preview and body; wait for
Luke's go after each. Order: Step 0, Flow 1 (B1 to B4), Flow 2 (A1 to A6).

## About us
- ERN: Luke and Jamie, building a carb bar: 30 g of carbs in a rice crisp
  square, for the 30 minutes before a race. Not out yet; recipe being
  finalised. Never imply it is available or give a launch date. The bar is
  only ever for before the start, never during the race.
- Audience: amateur marathon runners in Ireland and the UK, goals mostly
  3:30 to 4:30 (most ask 3:45 to 4:00), many think in miles. From IG and
  TikTok reels ("email us your race and goal time through the link in
  the bio").
- Site plan builder: drag the clock to a goal time, pick a race; shows
  watch pace (km and miles), the race clock at every 10K sign, and when
  to take each gel.

## Klaviyo now (29 Oct)
- 591 profiles (568 active, 23 suppressed). Mostly Gmail; more UK than
  Irish.
- Flow "Email Welcome Series", one email, "Email 1 - Guide Delivery"
  (subject "Your marathon, sorted"; preview "A free, personalised plan
  designed for you"; from Luke). 30 days: 62.8% open, 24.4% click. Four
  rules, sample sub-4 plan, builder link, RACE WEEK box, P.S. with
  waitlist link. **Keep Email 1 as it is.**

## Principle
Every email is about their race, timed to it, with something too long to
remember. The bar lives in the P.S. and in one insider email (B3), never
as a pitch.

## Step 0: tracking
"Plan Built" event (race_name, race_date as a date, goal_time) plus the
same as profile properties, for profiles Klaviyo already knows. Optional
"Send this plan to my inbox" box for unknown visitors. See
`01-step-0-developer-brief.md`.

## Flow 1: Welcome Series
Email 1 (keep) > wait 2 days > split: Plan Built at least once? Yes: exit.
No: Track B. Every Track B email filters out anyone who has built a plan.
- B1, day 2: "The K that decides your marathon". First 10K 5-10 s/K
  slower; up to a minute behind at halfway is fine. Builder link.
- B2, day 5: "One question". Under 60 words: "What scares you most about
  race day? Hit reply, one line is plenty."
- B3, day 9: "What goes in your hand before the gun". Before and after
  (start pen, nerves, forcing down a gel), then the honest build of the
  bar (batch number, what failed, one real photo from Luke). Offer: "We
  want 50 runners to test it before anyone else, before their long runs.
  Reply TEST or join the list." Consent is the click.
- B4, day 14: "Your block starts sooner than you think". Spring marathons
  and the week each 16-week block starts (check every date). "The race
  starts before the gun." Builder link.
- Then monthly email.

## Flow 2: Race Countdown
Trigger: race_date. Filter: race date in the future at entry.
- A1 on entry: "Your [goal_time] plan for [race_name]". Plan and a
  printable pace band ("Print it, fold it, keep it in your pocket or round
  your wrist."). CTA: "Reply with your longest run so far and I'll tell
  you if the goal's right." Forward line.
- A2, race minus 7 days: "7 days to [race_name]: your carb load". Table.
  CTA: screenshot it.
- A3, race minus 2 days: "Your last 48 hours before [race_name]". One
  timeline; last 30 minutes honest, then "This half hour is exactly why
  we're making the bar."
- A4, race day 6:30am: "Today: 3 numbers". Under 50 words: first 10K
  pace, first gel time, talk test. "Good luck. Reply after with your time."
- A5, race plus 2 days: "How did [race_name] go?" Reply with 10K split,
  first gel time, the K it got hard. Luke answers personally.
- A6, race plus 10 days: "Your next one". Next block start for spring,
  builder, taste-panel invite if not had.
- A new plan with a new race date puts them back into Flow 2.

## Layout rules (every email after Email 1)
- Plain, from Luke: white, no banner, at most one table, signed "Luke".
- Stake and first useful thing in the first 3 lines.
- One thing too long to remember (table or schedule), except B2.
- One CTA (a reply or one link). P.S.: the bar in one line, new words
  each time, with the waitlist link.
- Under 200 words, except schedules. No dated words in Track B.
- No maths in the email; the builder does the sums. No discount codes.
- Friend-on-a-run voice: contractions, short sentences, no jargon
  (glycogen, taper, zones), no em dashes, no "it's not X, it's Y".
- Smart Sending on; at most one email a week outside race week.

## The numbers (never change or contradict)
- Pacing: first 10K 5-10 s/K slower than goal pace; up to a minute behind
  at halfway; watches read about 1% long, trust the 10K signs; paces as
  5-second bands ("between 5:35 and 5:40").
- Talk test: "I am running a marathon today and I feel good": 10 words in
  one breath at 10K, 10 breathy at 20K, about 5 at 30K, 2 or 3 at 40K.
- Race fuel: about 60 g of carbs an hour, grams first. First gel at 20
  minutes, then a 30 g gel every 30 minutes (40 g every 40, 20-25 g every
  20), each with 3 or 4 sips of water about 100 m before a station, never
  washed down with sports drink, none in the last 20 minutes. Never two
  together. Never a total gel count.
- When it hurts: shorter, quicker steps; one K or one lamppost at a time.
- Carb load, the two days before (Fri and Sat for a Sunday race): 8-10 g
  per kg a day (60 kg 480-600 g; 70 kg 560-700 g; 80 kg 640-800 g; 90 kg
  720-900 g). Everything white, low fat and fibre.
  - Friday: 8am two white bagels with jam, big glass of apple juice; 11am
    banana and a sports drink; 1pm big bowl of white rice, chicken,
    teriyaki sauce, can of fizzy drink; 4pm two crumpets with honey and a
    handful of pretzels; 7pm white pasta, tomato sauce, two slices of
    white bread, glass of juice.
  - Saturday: same up to the 4pm snack, plus an extra glass of apple
    juice; 5pm dinner is the last meal, normal size (white rice, a little
    chicken, soy sauce, glass of juice), then only water until bed.
  - Race morning, 3 hours before (6am for a 9am start): two white bagels
    with jam and a glass of juice, about 2 g/kg, then sips of water.
    Practise it on a long run first. Diabetes or a medical condition:
    check with a doctor first.

## Data care
Never ask for subscriber email addresses; never repeat any shown in
screenshots. Counts only.

## Measure (report every two weeks, one table)
Clicks and replies per email; unsubscribes per email (under 0.5%); share
of active profiles on the waitlist; plan builds per sign-up; A5 replies.
