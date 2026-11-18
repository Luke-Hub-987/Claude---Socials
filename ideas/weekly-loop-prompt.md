---
type: the weekly results loop (Luke, 18 Nov: "we can do a weekly loop"), to be set up as a scheduled task when Luke approves it
schedule: every Monday 7:41am Irish time, a fresh session, with the Windsor.ai for Social Media connector, push notification when done
---

Weekly results loop for Engine Room Nutrition (ERN). Work in the repo luke-hub-987/claude---socials on branch claude/engine-room-nutrition-brand-yc4tyf (check it out; commit and push only to that branch). Read CLAUDE.md first, then ideas/engine-room-nutrition/OST-SCORECARD.md, PLAN-winners.md and the newest ideas/*-review.md files.

1. Pull the last 7 days from the Windsor.ai for Social Media connector: instagram, account 17841468879026012 (get_fields first; timestamp, media_type, media_product_type, media_caption, media_views, media_reach, media_reel_skip_rate, media_reel_avg_watch_time, media_saved, media_shares, media_total_like_count, media_total_comments_count), plus the 7 days before that to refresh them. No force_refresh (the trial plan refuses it). Read only.
2. Update ideas/results-log.md: one row per post (date, title, device, profile or trial, hook words, frame one type, views, reach, skip, watch, saves and %, shares and %, likes, comments), the title, device and hook from the matching file in ideas/engine-room-nutrition/ or "unknown".
3. Write ideas/YYYY-MM-DD-weekly-results.md: rates first; the best and worst post and why, against the OST scorecard, the five levers, P218 and the failure ledger (a repeat named as a repeat); one table of which tests and devices went with the best skip and watch so far, with the sample-size caveat; at most 3 proposed rule changes with evidence, "for Luke to approve" (never edit OST-SCORECARD.md, GATE.md, principles.md or gate/ost_check.py yourself).
4. A PLAN-winners row for any new post, two lines in CLAUDE.md "Current state", commit with the attribution lines, push. Never send Luke's email address to any outside service. Summary to Luke: the best post, its numbers, the proposals.
