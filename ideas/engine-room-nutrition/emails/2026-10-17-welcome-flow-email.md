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
