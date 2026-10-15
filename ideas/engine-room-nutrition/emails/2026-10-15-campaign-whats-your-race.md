# Campaign email: your free marathon plan (15 Oct 2026, v3)

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

## How replying works

Pressing reply sends to the campaign's Reply-To address (Klaviyo campaign
settings). The button opens a new email to the same address with the four
questions already typed. Replace `REPLY_ADDRESS` in the HTML first.
Paste the file into Klaviyo's HTML (code) template editor.

## Before sending

1. Replace `REPLY_ADDRESS`; check `[DATE]` in the sender row.
2. Test to a Gmail and an iPhone: name fills in, button opens a prefilled
   email, footer tags render.
3. Send so plans can reach Dublin and Frankfurt runners before 26 Oct.
4. Leave Klaviyo's default suppression of long-inactive profiles on; dead
   addresses, not interest, are what push a domain into spam.
5. Measure replies divided by delivered. Ignore open rate.

## Plain-text version

```
Hi {{ first_name|default:'there' }},

A lot of you found us through our marathon videos over the last few weeks. Most of what we cover comes down to two questions: how fast to go, and when to eat.

Below are the four rules from those videos that hold for almost every runner, whatever your goal time. Under them is what they look like as a full plan for someone aiming to finish under four hours. If you want the same plan worked out for your race, reply to this email. It comes straight to me, and I read every one.

FOUR RULES FOR YOUR MARATHON

1. Start slower than your goal pace. Run the first 10K 5 to 10 seconds per K slower than the pace your goal time needs. You will be up to a minute behind at halfway, and that is your race going to plan.

2. Take a gel every 20 minutes. Take your first at minute 20, before you feel you need it, and every 20 minutes after that. Take each one with water.

3. Check your effort with ten words. Say "I am running a marathon today and I feel good". At 10K you should get all ten words out in one breath. By 20K, ten words but breathy. By 30K, about five. By 40K, two or three.

4. When it hurts, shorten your steps. Take shorter, quicker steps. Then run one K at a time, or one lamppost at a time.

THE FOUR RULES AS ONE PLAN (goal: under four hours)
Watch pace, watch time at the sign, talk test:
10K: 5:42 per K, 57:30, 10 words in one breath
20K: 5:35, 1:54, 10 words, breathy
30K: 5:35, 2:50, about 5 words
40K: 5:35, 3:47, 2 or 3 words
Finish: 5:25 for the last 2K, 3:59, 1 or 2 words
Fuel: a gel every 20 minutes from minute 20, each one with water.

YOUR OWN PLAN, FREE: reply with these four things
1. Your race and the date
2. Your goal time
3. One recent time (any race result, or your longest run and how long it took)
4. What you eat or drink on long runs now (gels, sweets, water only, nothing at all: all useful)

Race in the next seven days? Put RACE WEEK at the top of your reply and I will do yours first.

Already sent us your race? Your plan is on its way, no need to send it again.

Good luck with the training. I am looking forward to seeing which races you are all running.

Luke
Engine Room Nutrition

P.S. There are two of us building a carb bar for marathon runners. It is not out yet, so what you tell me about how you fuel now helps shape it.

P.P.S. No marathon on the calendar? Forward this to a friend who has one. Their plan is free too.

{{ organization.name }}, {{ organization.full_address }}
Unsubscribe: {% unsubscribe_link %}
```
