# Email autopilot: plan (22 Nov 2026)

Luke asked: can Claude create campaigns, send them, review the analytics and
write the next one from the feedback, without him? Recommendation: automate
everything except the decision to send, for the first four sends; then move
to "sends unless Luke stops it" with hard limits that pause the system.

## Why not fully hands-off from day one
- The list (about 550) is the asset; one wrong number or invented claim to
  everyone costs more than the 5 minutes an approval takes. Luke has
  corrected every batch so far (P118 to P120, the pronoun on 17 Nov).
- Unsubscribes are already 1.6 to 1.7% a send against a 0.5% limit.
- The time sink is answering replies (about 40 per good send), not writing
  campaigns. Automate that first.
- Klaviyo can't see replies (mailto clicks aren't counted), and opens are
  inflated by Apple Mail, so the review step has to read Gmail as well.
- Small numbers: 16 replies against 38 is a real difference; 30 against 33
  is noise. The loop must not change direction on one email.

## The loop (one scheduled session a week, Monday 9:12)
1. Review: Klaviyo report for the last send (delivered, opens, unsubs, spam
   complaints) plus Gmail reply counts and themes, counted by the campaign's
   own mailto subject. Writes `ideas/YYYY-MM-DD-<campaign>-review.md` and one
   row in `emails/SCOREBOARD.md`.
2. Choose: next topic from the scoreboard, the race calendar and the social
   grid (`PLAN-winners.md`). One topic, with the reason.
3. Draft: HTML from the theme template, subject 30 to 35 characters,
   preview, unique mailto subject. Passes the humaniser scan, the checklist,
   numbers only from `flows/00-flow-brief.md`, and a 390px render check.
4. Push: template and draft campaign into Klaviyo, audience set, not
   scheduled. Sends Luke a test email and a push notification with the
   subject, the topic reason and the pre-mortem.
5. Luke approves: clicks Schedule in Klaviyo (phase 1), or does nothing and
   it sends in 48 hours (phase 2).
6. Replies (daily, 7:41): Gmail drafts for every new reply, built from the
   answer bank and the runner's goal band. Luke or Jamie checks and sends.
   Nothing goes out from Gmail automatically.

## Hard limits (in the runbook; breaking one pauses everything and alerts Luke)
- At most one campaign a week outside race week.
- Unsubscribes over 1% on two sends in a row, or any send with spam
  complaints over 0.1%: stop, alert, propose a list clean-up.
- No claim, number or story that isn't in the brief, the videos or a real
  reply; no launch date, no discount, the bar only before the start.
- Never deletes or edits a sent campaign, a list or a flow; never imports
  addresses from outside Klaviyo.
- Every send goes to subscribed profiles only, with Smart Sending on.

## Phases
- Phase 0 (this week): Luke answers four questions (below); Claude writes
  the runbook `emails/AUTOPILOT.md`, the scoreboard, the Gmail labels and a
  "Replied" list; sets up the two scheduled tasks with the Klaviyo and
  Gmail connectors.
- Phase 1 (four sends): draft and alert, Luke schedules.
- Phase 2 (after four sends with no corrections): auto-schedule 48 hours
  out, Luke can cancel. Any correction drops it back to phase 1.
- Phase 3: Flow 2 (race countdown, A1 to A6) carries race-specific emails;
  campaigns drop to every two weeks.

## Decisions for Luke
1. Approval: Luke clicks Schedule (recommended) or 48-hour veto?
2. Send day and time: Wednesday 8am (recommended, based on the last sends)?
3. Reply drafts in Gmail every morning: yes or no? Jamie on half?
4. List clean-up: drop profiles with no opens in 90 days before each send?
