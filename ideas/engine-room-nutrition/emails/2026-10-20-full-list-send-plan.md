# Sending to the full list (478 profiles), 20 Oct 2026

One Klaviyo campaign, sent in two waves to segments. Not individual emails
(Gmail limits, no SPF/DKIM on the root domain yet, and no tracking).

## Segments to build in Klaviyo

1. **Plan requested** (a list, kept by hand): everyone who has replied or
   DM'd with their race. Add them as replies come in. Always excluded.
2. **Engaged 30 days** (segment): opened or clicked any email in the last
   30 days.
3. **Just joined** (segment): added to Email List in the last 2 days.
   They just got the welcome email with the same offer. Excluded.

## The two waves

| Wave | Who | When | Subject |
|---|---|---|---|
| 1 | Engaged 30 days, minus Plan requested and Just joined | Wed 22 Oct, 8:00 | new subject |
| 2 | Everyone else on Email List, minus Plan requested, Just joined and wave 1 | Thu 23 Oct, 8:00 | same, or the other A/B subject |

Wave 1 first: people who open and reply teach Gmail that the new sending
domain is wanted, which lifts wave 2's inbox placement. Both waves land
before Dublin and Frankfurt on Sunday 26 Oct.

Settings: Smart Sending **on** for campaigns (it stops someone getting two
emails in 16 hours); **off** for the welcome flow (done, 20 Oct).
Klaviyo drops unsubscribed and bounced profiles automatically.

## Before sending

- Check the 16 Oct campaign's Deliverability tab (opens by provider,
  spam complaints). If complaints are above 0.3%, hold wave 2.
- Add SPF and Google DKIM on the root domain: the plans go back by hand
  from Gmail.
- Have the plan template ready: replies arrive fast after a send.

## Individual emails only for

- Everyone who replies (their plan).
- People who messaged to say the welcome email never arrived: a short
  personal email or DM with their plan.

## Measure

Replies per wave (count in the inbox), spam complaints, unsubscribes.
