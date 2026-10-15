# Campaign email: what's your race? (15 Oct 2026)

HTML: `2026-10-15-campaign-whats-your-race.html` (v2, redesigned; Luke
15 Oct: v1 looked bland, and this goes to the **whole existing list as a
campaign**, not as a welcome email).

v2 design: dark hero with the race line (start to finish), sender row,
pull quote, three-step "how it works" cards, a **sample sub-4 plan** (the
exact numbers from the sub-4 video, so nothing contradicts it), the four
questions, a dark reply card with the RACE WEEK line, and two P.S. lines.
Animations play in Apple Mail only; every other client shows the finished
state. About 31 KB, well under Gmail's 102 KB clipping limit.

## Who to send it to

The list mixes old newsletter subscribers (sleep and office topics) and
new marathon signups. Send first to people who signed up or engaged in the
last 90 days. Hold the older, quiet part of the list, or send to it a week
later once the first send has built up replies. A cold segment that
marks it as spam drags the whole domain into spam. Exclude anyone who has
already emailed their race (the email also tells them not to resend).

## The one job of this email

Get a reply. A reply gives Luke the race and goal time for the plan,
and it is the strongest signal Gmail and Outlook get that this sender
belongs in the inbox. Every other email we send later benefits from it.
So the email has one ask, and everything else was cut.

## How replying works

Everyone can simply press reply. It goes to the campaign's Reply-To
address (set in Klaviyo's campaign settings, under the From address).
The button is a shortcut: it opens a new email to the same address with
the four questions already typed. Both land in the same inbox. If the
button does nothing (a desktop with no mail app set up), the "or just hit
reply" line covers it.

## Settings

| Setting | Value | Why |
|---|---|---|
| Subject | **What's your race?** (17 characters) | A question gets answered; short enough to show whole on any phone. |
| A/B subject | Your marathon plan: one reply (29) | Tests "plan" (the thing they asked for) against curiosity. |
| Preview text | Reply with your race and goal time and I will build the rest. | Adds the how; does not repeat the subject. |
| From name | Luke from Engine Room | A person's name gets more opens and replies than a brand. |
| From address | a real inbox Luke reads (luke@ domain) | Never noreply. Replies must land somewhere. |
| Reply-to | the same address | |
| Button `mailto:` | replace `REPLY_ADDRESS` with that address | Placeholder so the address is not stored in the repo. **The button is broken until this is done.** |
| Klaviyo template | Templates, create, HTML (code) editor; paste the whole file | A text block would show the code as text. |
| Plain-text version | paste the one below; do not use the auto version | The auto version mangles the numbered list. |
| Send time | Tuesday to Thursday morning; before Dublin and Frankfurt (26 Oct) | Plans must land before the races. |

## Plain-text version

```
Hi {{ first_name|default:'there' }},

A lot of you have found us through our marathon videos over the last few weeks. So for every one of you with a race booked, we are building a free plan around your race and your goal time.

All you have to do is reply to this email. It comes straight to me, and I read every one.

Send me these four things. Short answers are perfect.

1. Your race and the date
2. Your goal time
3. One recent time (any race result, or your longest run and how long it took)
4. What you eat or drink on long runs now (gels, sweets, water only, nothing at all: all useful)

Your plan comes back within 48 hours: your pace for every 10K, when to fuel, and how each stage should feel.

Race in the next seven days? Put RACE WEEK at the top of your reply and yours goes first.

Already sent us your race? Your plan is on its way, no need to send it again.

I am looking forward to seeing which races you are all running.

Talk soon,
Luke
Engine Room Nutrition

P.S. There are two of us building a carb bar for marathon runners. It is not out yet, so what you tell me about how you fuel now helps shape it.

P.P.S. No marathon on the calendar? Forward this to a friend who has one. Their plan is free too.

{{ organization.name }}, {{ organization.full_address }}
Unsubscribe: {% unsubscribe_link %}
```

## What changed from the old newsletter template, and why

- **Topic.** The sleep and office-culture angle is gone. These people
  signed up from a marathon video for a marathon plan.
- **One ask instead of six sections.** TL;DR box, research box, timeline,
  steps and snapshot table all removed. Each one is a reason to stop
  reading before the ask. A plain, letter-like email also looks less like
  a promotion, which helps it reach the Primary tab (a tendency, not a
  guarantee).
- **No animation.** Gmail strips CSS animations, so most readers never saw
  the timeline move.
- **Fonts now load** (Apple Mail and iOS). The old template named Barlow
  Condensed but never loaded it, so everyone saw Impact.
- **Bugs fixed.** The greeting line was broken (`color:#0a0f1e }},` with
  the name tag missing). The footer used `{{ unsubscribe_url }}`, which is
  not Klaviyo syntax; it now uses `{% unsubscribe_link %}`. Added the
  company name and postal address, which the law and Klaviyo require.
- **No images, two links.** Fewer links and no images keep the spam score
  low and nothing breaks when images are blocked.
- **Question 4 (current fuel) is product research.** It is also what makes
  the plan's fuel section personal.

## Deliverability checklist (do once, before the flow goes live)

1. Branded sending domain set up in Klaviyo (SPF and DKIM pass on
   engineroomnutrition.com, and a DMARC record exists). Gmail and Yahoo
   have required this for bulk senders since February 2024.
2. Unsubscribe in the footer (done) and Klaviyo's one-click unsubscribe
   header on (it is on by default).
3. Send yourself a test to a Gmail and an Outlook address. Check: the
   name fills in, the button opens a new email with the four lines typed,
   the footer tags render, and it lands in Primary.
4. Answer every reply. A two-way thread is what tells the inbox providers
   this sender is wanted.

## What to measure

**Reply rate: replies divided by emails delivered.** Count it by hand
weekly. Ignore open rate: Apple Mail opens every email automatically, so
the number is inflated and tells you little. Also track how many replies
arrive with RACE WEEK, and which videos people name.

## Open risk

The 48-hour promise. Plans are built by hand. If replies outrun Luke's
time, the first promise the brand makes is broken. Decide now what the
plan contains (pace per 10K from goal time, a fuel schedule of a gel
every 20 minutes with water, the talk test, the late-race cues from the
videos) and build it as a template that takes ten minutes to fill in.
If that is not possible, change the line to "within a few days".
