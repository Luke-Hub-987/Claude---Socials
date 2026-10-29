---
type: handover prompt (Luke, 29 Oct: the emails move to a separate project; this is the prompt to paste there so it can walk him through Klaviyo)
source: ideas/2026-10-29-welcome-flow.md (P162), FACTS.md, the carb-load script (2026-10-16)
data care: no subscriber addresses and no sender address in the prompt
---

# Paste this into the email project as the first message

You're helping me (Luke, co-founder of Engine Room Nutrition) build our Klaviyo welcome flows. I'll do the clicking in Klaviyo and send you screenshots; you give me exact step-by-step instructions and the finished copy for each email, one email at a time, and wait for my go before moving on.

ABOUT US
- Engine Room Nutrition (ERN): two founders, Luke and Jamie, building a carb bar: 30g of carbs in a rice crisp square, for the 30 minutes before a race. It isn't out yet; the recipe is being finalised. Never imply it's available or give a launch date.
- Our audience: amateur marathon runners in Ireland and the UK, goals mostly 3:30 to 4:30 (most ask for 3:45 to 4:00), many think in miles. They come from our Instagram and TikTok reels.
- How they join: the reels say "email us your race and goal time through the link in the bio". Our site has a free plan builder: drag the clock to your goal time, pick your race, and the plan shows on screen (watch pace in km and miles, the race clock at every 10K sign, and when to take each gel).

WHERE KLAVIYO IS NOW
- 591 profiles (568 active, 23 suppressed). Most are on Gmail; more are UK than Irish.
- One flow, "Email Welcome Series", with one email: "Email 1 - Guide Delivery" (subject "Your marathon, sorted"; preview "A free, personalised plan designed for you"; from Luke). Over 30 days: 62.8% open, 24.4% click. It has four rules, a sample sub-4 plan, a link to the builder, a "Race in the next seven days? Reply RACE WEEK" box, and a P.S. about the bar with a waitlist link.
- Keep Email 1 as it is. Its click rate is our best number. The gap is that nothing follows it.

THE PRINCIPLE
Every email is about their race, timed to it, with something too long to remember. People ignore welcome flows about the brand; they open emails about their own race in the week they need them. The bar lives in the P.S. and in one insider email, never as a pitch.

WHAT TO BUILD

Step 0, tracking (no extra step for subscribers):
- When someone shows their plan in the site builder, send a Klaviyo event "Plan Built" with race_name, race_date (as a date) and goal_time, and save those three as profile properties. This works when Klaviyo already knows them (they arrived from an email click). Tell me exactly what to give our site developer, and how to test it with my own profile.
- Add an optional "Send this plan to my inbox" box to the builder for people who arrive without signing up. Nobody else gets an extra step.

Flow 1: Welcome Series (exists). After Email 1, wait 2 days, then a conditional split: has "Plan Built" at least once? Yes: exit (Flow 2 has them). No: Track B. Every Track B email has a filter so they leave the flow the moment they build a plan.
- B1, day 2. Subject: "The K that decides your marathon". The first 10K is where the wall really starts: run it 5 to 10 seconds per K slower than goal pace; up to a minute behind at halfway is fine. Link to the builder.
- B2, day 5. Subject: "One question". Under 60 words: "What scares you most about race day? Hit reply, one line is plenty."
- B3, day 9. Subject: "What goes in your hand before the gun". Their before and after first (the start pen, the nerves, forcing down a gel), then the honest build of the bar: the batch number, what failed, one real photo (I'll give you these). The offer: "We want 50 runners to test it before anyone else, before their long runs. Reply TEST or join the list." Consent is the click: never add anyone to a launch list without it.
- B4, day 14. Subject: "Your block starts sooner than you think". The spring marathons and the week each 16-week training block starts (check every date before using it). The line: "The race starts before the gun." Link to the builder.
- Then they move to a monthly email.

Flow 2: Race Countdown (new). Trigger: the race_date date property. Filter: race date still in the future at entry.
- A1, on entry. Subject: "Your [goal_time] plan for [race_name]". Their plan and a printable pace band: "Print it, fold it, keep it in your pocket or round your wrist." CTA: "Reply with your longest run so far and I'll tell you if the goal's right." Forward line: "Running it with someone? Forward this so they can build their own."
- A2, race date minus 7 days. Subject: "7 days to [race_name]: your carb load". The carb-load schedule below, as a table. CTA: screenshot it.
- A3, race date minus 2 days. Subject: "Your last 48 hours before [race_name]". One timeline: the last big meal, bedtime, breakfast time and what, the last 30 minutes, the first gel at 20 minutes, their first 10K pace. For the last 30 minutes, say honestly what most runners do, then: "This half hour is exactly why we're making the bar."
- A4, race day at 6:30am. Subject: "Today: 3 numbers". Under 50 words: their first 10K pace, their first gel time, the 10-word talk test. "Good luck. Reply after with your time."
- A5, race date plus 2 days. Subject: "How did [race_name] go?" "Reply with 3 numbers: your 10K split, when you took your first gel, and the K it got hard. I'll tell you what to change for the next one." I answer these personally.
- A6, race date plus 10 days. Subject: "Your next one". When their next block would start for the spring races, the builder, and the taste-panel invite if they haven't had it.
- A new plan with a new race date should put them back into Flow 2. Tell me how Klaviyo handles a changed date property, and how to test it.

LAYOUT RULES FOR EVERY EMAIL AFTER EMAIL 1
- Plain, from Luke: white background, no banner, at most one table, signed "Luke". Designed, image-heavy emails tend to land in Gmail's Promotions tab.
- The stake and the first useful thing in the first 3 lines.
- One thing too long to remember (a table or a schedule), except B2.
- One call to action (a reply or one link), and a P.S. that mentions the bar in one line, in new words each time, with the waitlist link.
- Under 200 words, except the schedules.
- No dated words ("this weekend") in Track B. Flow 2 can be dated, because it's timed per person.
- No maths in the email: give the answer; the builder does the sums.
- No discount codes, ever.
- Talk like a friend on a run: contractions, short sentences, no jargon (no "glycogen", "taper", "zones"), no em dashes, no "it's not X, it's Y".
- Smart Sending on; never more than one email a week outside race week.

THE NUMBERS WE USE (never change or contradict these; they match our videos)
- Pacing: the first 10K 5 to 10 seconds per K slower than goal pace; up to a minute behind at halfway; watches read about 1% long, so trust the 10K signs over the watch; paces as 5-second bands ("between 5:35 and 5:40").
- Talk test: "I am running a marathon today and I feel good": 10 words in one breath at 10K, 10 but breathy at 20K, about 5 at 30K, 2 or 3 at 40K.
- Fuel in the race: about 60g of carbs an hour, said as grams first. First gel at 20 minutes, then a 30g gel every 30 minutes (40g gels every 40 minutes, 20 to 25g gels every 20), each with 3 or 4 sips of water about 100m before a station, never washed down with sports drink, none in the last 20 minutes. Never two gels together. Never a total gel count.
- When it hurts: shorter, quicker steps; one K or one lamppost at a time.
- Carb load (the two days before; Friday and Saturday for a Sunday race): 8 to 10g of carbs per kg each day (60kg 480 to 600g, 70kg 560 to 700g, 80kg 640 to 800g, 90kg 720 to 900g). Everything white and low in fat and fibre. Friday: 8am two white bagels with jam and a big glass of apple juice; 11am a banana and a sports drink; 1pm a big bowl of white rice with chicken, teriyaki sauce and a can of fizzy drink; 4pm two crumpets with honey and a handful of pretzels; 7pm white pasta with tomato sauce, two slices of white bread and a glass of juice. Saturday: the same up to the 4pm snack, plus an extra glass of apple juice; dinner at 5pm is the last meal, normal size (white rice, a little chicken, soy sauce and a glass of juice), then only water until bed. Race morning, 3 hours before the start (6am for a 9am start): two white bagels with jam and a glass of juice, about 2g of carbs per kg, then sips of water. Practise the race breakfast on a long run first. Anyone with diabetes or a medical condition checks with their doctor first.
- The bar is only ever for before the start, never during the race.

DATA CARE
- Never ask me to paste subscriber email addresses, and don't repeat any that show in my screenshots. Counts only.

WHAT TO MEASURE
- Clicks and replies per email (Apple Mail inflates opens), unsubscribes per email (under 0.5%), the share of active profiles on the waitlist, plan builds per sign-up, and the number of A5 replies. Report these back to me every two weeks in one table.

HOW TO WORK WITH ME
- Start with Step 0 (what to give the developer, and how to test it). Then Flow 1, then Flow 2, one email at a time: the exact Klaviyo clicks, then the subject, preview text and full body, ready to paste. Wait for my go after each.
- Recommend one option, not a list. If something I ask for breaks a rule above, say so and why.
- Ask me for anything you need that isn't here (the batch number, a photo, the waitlist link).
