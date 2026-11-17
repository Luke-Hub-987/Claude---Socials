# Two emails this week (18 Nov 2026): pre-mortems, settings, reply bank

Files: `2026-11-18-email-1-where-your-marathon-starts.html` and
`2026-11-18-email-2-where-will-it-go-wrong.html`. Data:
`ideas/2026-11-17-klaviyo-campaigns-review.md`. Both pass the humaniser
scan (0 hits) and a read-aloud pass.

## What the data says (email and social)
- Opens are 71 to 76% on every send since 22 Oct; Apple Mail inflates
  them. Judge on replies.
- Replies follow urgency and ease: race week with a Friday deadline about
  7 per 100; "reply with your time" about 3; spring splits with no
  deadline about 1.3. On social, the easiest ask won too.
- Unsubscribes 1.7% and 1.6% on the last two sends, one spam complaint.
- Social: "Where [famous problem] actually starts" is the best title
  shape (147K). Training weeks as the subject failed (4.4K to 5.3K).
  Narrow gates cost reach (sub-4 skip 40.8%). Race moments, a paradox
  you can picture, and real numbers win.

## Email 1: Where your marathon actually starts (Wed 8am)
- Subject: **Where your marathon actually starts** (35). Uses the winning
  title shape instead of "London 2027? Start training 4 Jan", which
  speaks to one race. P120 asks for the number in the subject; here the
  number goes in the preview, because the title shape has the best data.
- Preview: London's starts Monday 4 January, in the dark. Find your Monday, then reply by 13 December for your plan.
- Audience: Email List, minus "Replied" (has a plan) and anyone added in
  the last 14 days. Smart Sending on. Sender: Luke.
- Ask: race and goal time by Sunday 13 December.

### Pre-mortem (it flopped; why?) and what changed
| Failure | Why it would happen | Fix in the email |
|---|---|---|
| Opens below the flow's 85.5% | That figure came from brand-new subscribers | Expect 60 to 70%; judge on replies |
| Non-London runners skip it | London-only subject (narrow gate) | Subject names no race; table covers six |
| Feels like a training email | Training weeks failed on social | Framed as the start of the race: "111 days before the gun" |
| Dull | Dates in a table | Opening picture: dark by half four, gloves, the tin of Roses, three days after the turkey |
| Few replies | No deadline | Reply by Sunday 13 December, tied to each runner's first Monday |
| Unsubscribes | Autumn finishers with no spring race | No second email to people who don't open this one |

## Email 2: Where will your marathon go wrong? (Sat 9am)
- Subject: **Where will your marathon go wrong?** (34).
- Preview: Six places it goes wrong. Reply with the number that's yours and I'll send your fix.
- Audience: only people who **opened Email 1** and are not in "Replied".
  Klaviyo segment: "Opened Email" where campaign = Email 1, at least once
  in the last 4 days; and not in list "Replied". Non-openers get nothing,
  so nobody unengaged gets two emails in a week.
- Ask: one number. The easiest reply there is, and each number has a
  ready answer (below), so 50 replies take minutes, not evenings.

### Pre-mortem and what changed
| Failure | Why it would happen | Fix in the email |
|---|---|---|
| Feels negative | Six things going wrong | Every moment ends on its fix, in bold |
| Too long | Six items | Each item is two or three sentences, in race-day order |
| Generic | "Common mistakes" lists are everywhere | Clock times and real moments: 8:45 in the pen, 12K a minute down (a real reader's race), the calf flicker at 35K |
| Not credible | Claims about what runners do | Built on the replies ("around 150") and the brand's own numbers |
| Few replies | Reply needs effort | One number; "more than one? send them all" |
| Luke swamped | Volume | Reply bank below |

Note: number 3 is the 4:05 runner's race, as used on 3 Nov, unnamed.

## Reply bank for Email 2 (paste, then add their goal-time line)
Goal-time bands (first 10K / then): 3:30 5:05-5:10 / 4:50-4:55;
3:45 5:25-5:30 / 5:15-5:20; 4:00 5:45-5:50 / 5:35-5:40; 4:15
6:05-6:10 / 5:55-6:00; 4:30 6:30-6:35 / 6:15-6:20.

1. "Pick the breakfast you'll eat on race morning now: two white bagels
   with jam and a glass of juice, three hours before you start. Have it
   before every long run from here to race day, so by April it's routine.
   (Check with your doctor first if you have diabetes or a medical
   condition.)"
2. "For your goal, run the first 10K at [first band] a K. It will feel too
   easy, and that's the point. You'll be up to a minute behind at
   halfway, and that's your race going to plan."
3. "If you're behind at 10K, hold [then band] a K anyway. The minute comes
   back on its own in the last 10K, when everyone around you slows down."
4. "First gel at 20 minutes, then a 30g gel every 30 minutes, about 60g an
   hour, each with 3 or 4 sips of water just before a station. Take them
   before you feel you need them, and practise it on every long run."
5. "The wall gets set in the first 10K: [first band] a K for your goal. On
   the day, if it comes: shorter, quicker steps, and one K at a time, or
   one lamppost at a time."
6. "Ease off and shorten your stride the moment you feel a twitch. If it
   locks, stop, keep the leg straight and push your heel down, walk for a
   minute, then run again easier with shorter steps."

## Measure
Replies per 100 delivered (Email 1 target 5+; Email 2 target 10+ of
openers), unsubscribes (under 0.8% on Email 1, under 0.5% on Email 2),
and the count of each number (it tells us the next video topic).

## In Klaviyo (pushed 17 Nov, drafts only, nothing scheduled)
- Email 1: campaign "ERN 18 Nov - Email 1 - Where your marathon starts"
  (https://www.klaviyo.com/campaign/01M7MAW4JM6X0NF2CM9QXCG6KH/wizard),
  template XrwRzw. Audience: Email List, excluding segment "ERN - Joined
  in last 14 days (in welcome flow)". Local time zone, Smart Sending on,
  from "Luke".
- Email 2: campaign "ERN 21 Nov - Email 2 - Where will your marathon go
  wrong" (https://www.klaviyo.com/campaign/01M7MAXAAP19GDF6GG4VV5KECT/wizard),
  template WAZ469. Audience: segment "ERN - Opened Email 1" (opened that
  exact message at least once). It fills up only after Email 1 sends.
- No "Replied" list exists in Klaviyo yet, so neither audience leaves out
  people who already have a plan.
- Email 2 copy change: "finished five minutes over her goal" became "over
  goal" (no assumed pronoun for the Dublin runner).
