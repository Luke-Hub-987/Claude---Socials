# Welcome flow email: Email 1 (17 Oct 2026)

HTML: `2026-10-17-welcome-flow-email.html`. Replaces "Email 1 - Guide
Delivery" in the welcome flow. Built from the campaign email (v5.1), which
already sends cleanly through Klaviyo.

## What changed and why

- **Lead magnet:** the free personalised marathon plan is the main offer,
  because that is what the videos promise ("email us your race and goal
  time through the link in bio"). The Ultimate Endurance Guide stays as a
  P.P.S. download link, so anyone whose sign-up form still promises the
  guide still gets it.
- **One ask: reply with race and goal time.** The old "reply or future
  emails go to Promotions" line is gone. A real reason to reply (the plan)
  gets more replies, and replies are the strongest inbox signal.
- **Value first:** the four race-day rules and the sub-4 sample plan, all
  matching the videos.
- **Office-era copy removed** (sleep, coffee, the work week).
- Signed by Luke; the P.S. names Jamie.

## Subject and preview (A/B test in the flow)

Subject lines work like on-screen text: plain words, "marathon" in it,
specific, the answer held back.

| | Subject | Preview |
|---|---|---|
| **A (clear offer)** | Your free marathon plan is one reply away | Send me your race and goal time. Here is what to do on race day until your plan arrives. |
| **B (curiosity, OST style)** | What pace should your first 10K be? | Reply with your race and goal time and I will work yours out. |

B is answered inside the email (rule 1), so it keeps its promise. Judge
the winner on **replies**, not opens: count replies in the inbox per
variation after 100+ sends each.

## Klaviyo settings

- Sender name: Luke. Sender and reply-to: luke@engineroomnutrition.com.
- **Smart Sending: off** for this email, so every new subscriber gets it
  even if they had another email in the last 16 hours.
- Delay: none (send on sign-up).
- Paste into the HTML (code) editor. Plain-text version: the campaign's,
  with "A lot of you found us..." swapped for the first paragraph here.

## Also change

The sign-up form or landing page behind the link in bio should promise
the same thing: "Get your free marathon plan". Promise and delivery must
match, or people do not reply.

## Copy audit (P118, Luke 17 Oct)

Rewritten to remove AI-writing tells: the repeated "the pace, the fuel
and the effort" triad, the stacked hedges, "race day is no day to try
something new", the talk-test fragments, "straight to me" said three
times, curly quotes, and "free" in every heading. Two reply buttons stay:
one under the intro, one in the dark card near the end.

## Why the 16 Oct campaign opened at 18.7% (was about 60%)

Most likely causes, biggest first:

1. **A brand-new sending domain.** luke.engineroomnutrition.com had no
   history when the campaign went out. Gmail and Outlook treat a new
   domain with caution, so more of the send lands in spam or Promotions.
   Long term this domain is the right move; it needs a few weeks of
   sends to well-engaged people to build trust.
2. **Two months of silence.** It lowers engagement and makes providers
   re-check you, but alone it rarely cuts opens by two thirds.
3. **The old 60% was flattered.** Early lists are friends and family,
   and Apple Mail counts every delivered email as opened.

Check, in the campaign's Deliverability tab: bounces, spam complaints and
opens by email provider. Gmail near zero while iCloud is high means
Gmail put it in spam. Then compare the welcome flow's open rate before
and after the domain was activated: if it held up, the domain is fine and
the gap is the cause.

Next: resend once to people who did not open, 3 days after the first
send, with subject A from the welcome test. Skip the resend if spam
complaints are above 0.3%. Send something every week or two from now on.

## "I signed up but never got the email" (20 Oct)

Example profile: subscribed 17 Oct 5:27 pm, Klaviyo "Received email"
9:51 pm. "Received" means the recipient's mail server accepted it, so the
email reached their provider and was then filed (spam, Promotions, All
Mail) or went to a mistyped address.

Findings and fixes:

1. **4.5-hour gap between sign-up and send.** The welcome email should go
   within a minute. Check the flow for a time delay, a "send only between"
   window, or a queue on the new sending domain.
2. **Signing up again does nothing.** A profile enters the welcome flow
   once; repeat sign-ups with the same address never resend.
3. **Skipped profiles:** the flow email's Recipient activity, Skipped
   tab, gives a reason per person (Smart Sending, already in flow,
   suppressed, no consent, filter not met). Turn Smart Sending off on the
   welcome email.
4. **Do not depend on the email arriving:** put the guide download link
   and "Reply to luke@engineroomnutrition.com with your race and goal
   time" on the sign-up form's success screen, and add "check spam and
   Promotions, and add us to your contacts".
5. Root domain still has no SPF and no Google DKIM (checked 20 Oct), so
   Luke's own replies with plans can land in spam. Klaviyo's sending
   domain luke.engineroomnutrition.com is set up correctly.

For anyone who messages to say it never arrived: confirm the address on
their profile, ask them to search Gmail for "in:anywhere Engine Room",
and send the plan directly.

## Flow data review (20 Oct, Luke's screenshots)

- Flow: trigger "added to Email List", no re-entry, no filters, Email 1
  at Day 0 with **Smart Sending on** and the A/B test live.
- Email 1, week to date: **53.45% open rate (31 people), 3.45% click
  rate (2 people)**, about 58 delivered. Healthy; the welcome email lands
  for most people. Compare the 16 Oct campaign at 18.7%.
- Recipient activity, 17 Oct: sends at 10:52 am, 11:00, 11:15, 2:13 pm,
  then nothing until a burst from 9:51 pm to about 10:23 pm (10+ sends in
  30 minutes). The example profile subscribed at 5:27 pm and was sent at
  9:51 pm. A burst after a long gap means sends were held and released at
  once: most likely Email 1 was out of Live (Manual or Draft) while the
  new A/B version was being set up, then switched back to Live around
  9:50 pm. **Never take Email 1 out of Live to edit it.**
- The example profile: delivered, 0 opens. Delivered means Gmail
  accepted it. Zero opens with "checked every folder" points to spam
  (images are blocked there, so even opening it there records no open)
  or a Gmail tab or account he did not check.

Actions: turn Smart Sending off on Email 1; check the Skipped filter in
Recipient activity for reasons; add the guide link and the reply address
to the form's success screen; add SPF and Google DKIM on the root domain.
