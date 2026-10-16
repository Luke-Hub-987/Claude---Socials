# Campaign email: your free marathon plan (v5, 16 Oct 2026)

HTML: `2026-10-15-campaign-whats-your-race.html`. Sent as a campaign to
the whole list (Luke, 15 Oct: the office-era subscribers are likely
marathon runners too).

## Subject and preview

- **Subject: Your free marathon plan** (23 characters). Says the offer in
  plain words, the way Ogilvy would: what you get, and that it is free.
- **Preview text: Reply with your race and goal time, and I will send back
  your pace and fuel for every 10K.**
- From name: Luke from Engine Room. Reply-To: an inbox Luke reads.

## v3 changes (Luke, 15 Oct)

- No turnaround promise anywhere (Luke will not commit to 48 hours).
- Value first: four race-day rules anyone can use without replying, all
  taken from the videos (5-10 s/K slower for the first 10K and up to a
  minute behind at halfway; gel every 20 minutes from minute 20, with
  water; the ten-word talk test at 10K, 20K, 30K, 40K; shorter, quicker
  steps and one K or one lamppost at a time). Nothing new, nothing that
  contradicts a video.
- The sample sub-4 plan now shows the four rules as one plan, using the
  sub-4 video's exact numbers.
- Plain headings that say what the section gives you. No slogans.
- More movement (Apple Mail and iPhone Mail only): headline rises in, a
  runner dot travels the race line, rule numbers pop in one by one, plan
  rows rise in while their bars fill, the fuel dot pulses, the button
  glows. Gmail and Outlook show the finished, still version.

## v4 changes (Klaviyo review, 16 Oct)

- Removed the Google Fonts `<link>`: Klaviyo does not support it and it
  blocked the preview. Headings fall back to Impact, body to Arial.
- Button now addresses luke@engineroomnutrition.com, with a prefilled
  subject and body (race and goal time first, the rest marked optional).
  Same button added straight under the intro.
- Race and goal time required; recent time and current fuel optional.
- `[DATE]` removed from the sender row.
- Body text 16px, labels at least 11-12px, buttons #2563eb.
- Sample plan recalculated so every number adds up (pace is real pace
  for the 10K before each sign; time is total race time):
  10K 5:45, 57:30 / 20K 5:40, 1:54:10 / halfway 2:00:23 /
  30K 5:40, 2:50:50 / 40K 5:40, 3:47:30 / finish 5:25 for the last
  2.2K, 3:59:23. A note covers GPS watches reading long, so it squares
  with the sub-4 video's watch paces (5:42, 5:35).
- Rules framed as a starting point; the gel rule now says to use the
  gels you train with and keep a routine that works.

## v5 changes (Luke's test, 16 Oct)

- Company address removed from the footer (Luke). Note: US law (CAN-SPAM)
  expects a postal address in marketing email to US subscribers; a PO
  box or registered office is enough if we ever add one back.
- Dark mode: removed the header's gradient image. Gmail's dark mode
  turns the text dark but leaves a background image dark, which made
  the header unreadable. Solid colours now, so text and background flip
  together.
- Motion: Gmail strips all CSS animation. A GIF would move in Gmail but
  needs uploading to Klaviyo for every email; Luke chose no upload step,
  so the race line is coded again. It moves in Apple Mail and on iPhone
  Mail, and shows still everywhere else.
- Reply wording: pressing reply is now named as the main route; the
  buttons stay as a shortcut.

## Spam: the cause and the fix (checked 16 Oct)

Public DNS for engineroomnutrition.com shows:

| Record | Found | Needed |
|---|---|---|
| SPF (TXT at the root) | **none** | `v=spf1 include:_spf.google.com ~all` |
| DKIM for Google Workspace | none at the default selector | turn on in Google Admin |
| Klaviyo sending domain | none found | set up in Klaviyo |
| DMARC | `v=DMARC1; p=none` | fine for now |

Gmail cannot confirm the email really comes from engineroomnutrition.com,
so it goes to spam. Fix, in this order:

1. **Klaviyo:** Settings, Domains, set up a sending domain (for example
   send.engineroomnutrition.com). Add the records it shows at your domain
   host and press verify.
2. **SPF:** add the TXT record above at the root of the domain.
3. **Google DKIM:** Google Admin, Apps, Google Workspace, Gmail,
   Authenticate email. Generate the key, add it as a TXT record, then
   press Start authentication.
4. Wait for the records to go live (minutes to a few hours), then send a
   fresh test. In Gmail open it, the three dots, Show original: SPF, DKIM
   and DMARC should all say PASS.
5. Mark the test "Not spam" and add the sender to your contacts.

Links in a message Gmail treats as suspicious can stop working, so test
the buttons again once the email lands in the inbox. If a button still
does nothing, long-press it and see the link: if it starts with a Klaviyo
tracking address instead of `mailto:`, click tracking has wrapped it.

## How replying works

Pressing reply sends to the campaign's Reply-To address. The buttons open
a new email to luke@engineroomnutrition.com with the questions typed.
Keep both: the button helps on phones, reply covers everyone else.
Set Reply-To to luke@engineroomnutrition.com in the campaign settings.

## Test emails not arriving: check in this order

1. Send the test to a personal Gmail too. If it arrives there, the
   problem is the company inbox, not the email.
2. Check spam, and the Google Workspace or Microsoft 365 quarantine
   (admin console). Mail "from" your own domain sent by Klaviyo is often
   quarantined when the domain is not authenticated.
3. Set up a branded sending domain in Klaviyo (Settings, Domains) and add
   the DNS records it gives you, so SPF and DKIM pass for
   engineroomnutrition.com.
4. In Klaviyo, check your own profile is not suppressed (unsubscribed or
   bounced). Suppressed profiles get nothing.
5. Check the template saves and previews without errors (the `<link>`
   that broke the preview is gone in v4).

## Plain-text version

```
Hi {{ first_name|default:'there' }},

A lot of you found us through our marathon videos over the last few weeks. Most of what we cover comes down to two questions: how fast to go, and when to eat.

Below are four rules from those videos. Treat them as a starting point: they suit most runners, and your own plan adjusts them to you. Under them is what they look like as a full plan for someone aiming to finish under four hours. If you want the same plan worked out for your race, reply to this email. It comes straight to me, and I read every one.

FOUR RULES FOR YOUR MARATHON

1. Start slower than your goal pace. Run the first 10K 5 to 10 seconds per K slower than the pace your goal time needs. You will be up to a minute behind at halfway, and that is your race going to plan.

2. Take a gel every 20 minutes. Take your first at minute 20, before you feel you need it, and every 20 minutes after that, each one with water. Use the gels you have used on your long runs. If you have a fuelling routine that works in training, keep it; race day is no day to try something new.

3. Check your effort with ten words. Say "I am running a marathon today and I feel good". At 10K you should get all ten words out in one breath. By 20K, ten words but breathy. By 30K, about five. By 40K, two or three.

4. When it hurts, shorten your steps. Take shorter, quicker steps. Then run one K at a time, or one lamppost at a time.

THE FOUR RULES AS ONE PLAN (goal: under four hours)
Pace per K for the 10K before the sign, total time at the sign, talk test:
10K: 5:45, 57:30, 10 words in one breath
20K: 5:40, 1:54:10, 10 words, breathy
30K: 5:40, 2:50:50, about 5 words
40K: 5:40, 3:47:30, 2 or 3 words
Finish: 5:25 for the last 2.2K, 3:59:23, 1 or 2 words
Halfway: 2:00:23, under a minute behind even pace. GPS watches often read a little long, so yours may show a few seconds per K quicker.
Fuel: a gel every 20 minutes from minute 20, each one with water.

YOUR OWN PLAN, FREE: reply with your race and goal time
1. Your race and the date
2. Your goal time
3. Optional: one recent time (any race result, or your longest run and how long it took)
4. Optional: what you eat or drink on long runs now (gels, sweets, water only, nothing at all: all useful)

Race in the next seven days? Put RACE WEEK at the top of your reply and I will do yours first.

Already sent us your race? Your plan is on its way, no need to send it again.

Good luck with the training. I am looking forward to seeing which races you are all running.

Luke
Engine Room Nutrition

P.S. There are two of us building a carb bar for marathon runners. It is not out yet, so what you tell me about how you fuel now helps shape it.

P.P.S. No marathon on the calendar? Forward this to a friend who has one. Their plan is free too.

{{ organization.name }}
Unsubscribe: {% unsubscribe_link %}
```
