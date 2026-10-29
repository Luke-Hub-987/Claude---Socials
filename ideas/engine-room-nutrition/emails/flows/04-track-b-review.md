# Track B review (29 Oct 2026)

No "AI council" review exists in the repo; Luke to paste it. Reviewed
against the 16 Oct Klaviyo AI review criteria, the flow brief and a
professional email marketer's checks.

## Already passes
16px body, labels at least 13px, #2563eb links, plain white layout, one
table, P118 writing audit, numbers match the brief and the sub-4 sample.

## Fixed 29 Oct
- Data tables had role="presentation", which hides the headers from
  screen readers. Removed; headers now scope="col".
- B1 and B4: the builder link now sits on its own line.

## Luke to decide
1. **B2 should ask for the race.** "What's your next marathon, and your
   goal time?" With the site tracking down, a reply is the only way to
   learn the race date; tag each reply in Klaviyo (race_name, race_date,
   goal_time) and Flow 2 can run. Move the fear question to a campaign.
2. **Swap B1 and B4 until February.** People joining in Nov to Jan
   mostly race in spring: the block start is what they need first;
   race-day pacing can wait. Change back for summer sign-ups.
3. **B1 repeats Email 1's first rule.** Open on what's new: the table by
   goal time in km and miles and the 10K sign clock.
4. **Subject "The K that decides your marathon":** many readers think in
   miles. "The first 10K decides your marathon" says it plainly.
5. **Check every B4 race is in the builder's race list**, or the link
   lands on a plan they can't build.
6. **B3 tester offer:** food sent to testers needs a full ingredients and
   allergen list (FSAI in Ireland, FSA in the UK), and the replies need a
   plan for collecting addresses.
7. **Miles bands are 10 seconds wide** in three rows (the km band
   converted). The brief says 5-second bands; keep, or round to 5 and
   accept a small mismatch with km.
8. **Plain-text versions:** paste one per email; Klaviyo's automatic one
   breaks tables.
9. **Replies are the metric:** create a Klaviyo list "Replied" and add
   people by hand weekly, so B2 replies are counted and can be excluded
   from later asks.
