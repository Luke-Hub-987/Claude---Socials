# Website v4 brief: deeper, not bigger (21 Oct 2026)

## Checked today: why sign-ups land in spam

DNS for engineroomnutrition.com, read on 21 Oct:

| Record | Found | Meaning |
|---|---|---|
| SPF on the root domain | **None** (only `klaviyo-site-verification`) | Mail from luke@engineroomnutrition.com via Gmail isn't authorised |
| Google DKIM (`google._domainkey`) | **None** | Luke's hand-sent plans aren't signed |
| DMARC | `p=none`, **no report address** | No protection and no reports, so the failures are invisible |
| Klaviyo sending domain `luke.` | SPF and MX set up | Klaviyo's own sends are set up correctly |

The welcome email (Klaviyo) is configured properly. **The plan itself goes
out from Gmail with no SPF and no DKIM**, which is the classic recipe for
spam. Flagged on 20 Oct and still open. Fix (15 minutes, in the domain DNS
and Google Admin):

1. TXT on the root: `v=spf1 include:_spf.google.com ~all`
2. Google Admin > Apps > Gmail > Authenticate email: generate a DKIM key,
   add the TXT at `google._domainkey`, click Start authentication.
3. DMARC: `v=DMARC1; p=none; rua=mailto:<a reports inbox>`. Reports first;
   tighten to `quarantine` once both pass.
4. Check: send a plan to mail-tester.com and aim for 9/10 or better. Add
   the domain to Google Postmaster Tools.

## What a top conversion professional would do that wasn't asked for

1. **Fix delivery before design.** The page promises a plan the inbox then
   hides. No headline fixes that.
2. **Give the plan on screen the moment they enter their email.** Email
   is the gate, the screen is where they get it, and the email is a copy.
   Spam can no longer eat the value, and the gate stays.
3. **Prove the results with records.** Each PB story needs a name, a
   race, a before time and an after time, with permission. Then one
   aggregate: "N runners got a plan; M ran a PB". In Ireland and the UK an
   unproven results claim is a consumer-law risk as well as a trust risk.
4. **Write with the runners' own words.** Lift the headlines, pains and
   objections from replies, DMs and comments.
5. **Match the message to each source.** Tag each video's link, so you
   know which video brings sign-ups and the page can greet that viewer.
6. **Measure a baseline, then change one thing at a time.**
7. **Differentiate the bar against what runners actually eat at 7am**
   (porridge, a banana, a shop rice crisp square, a gel in the pen), not
   against "gels".

## Raw material to start from

- **The inbox:** every plan request, reply, "I didn't get it" and PB report,
  verbatim. The plans as actually sent.
- **PB evidence:** race, previous time, new time, results-site link,
  permission (screenshots of DMs and comments).
- **Klaviyo:** form views and submits by day; welcome email delivered,
  opened and clicked by inbox provider (Gmail, Outlook, iCloud); spam
  complaints; list growth since 14 Oct.
- **Shopify analytics:** sessions by source and device, landing pages,
  bounce.
- **Instagram:** link taps per video and profile visits.
- **DNS records** (done, above).
- **Bar:** the lab nutrition panel, tester feedback in their words, cost
  and price.

## Methods and tools

- **Voice of customer:** sort the inbox into pains, desires, objections and
  results; copy lifted, not invented.
- **Deliverability:** Google Admin DKIM, SPF and DMARC; mail-tester.com;
  MXToolbox; Google Postmaster Tools; seed sends to Gmail, Outlook and
  iCloud.
- **Analytics:** Microsoft Clarity (free Shopify app) for heatmaps and
  session recordings; UTM links per video; GA4 or Shopify funnel.
- **Testing:** a 5-second test with 5 runners who've never seen the account
  ("what's on offer, what would you do?"); Klaviyo A/B on the headline;
  PageSpeed Insights on mobile.
- **Build:** an instant plan generator in the browser (the video method,
  turned into code and signed off by Luke), Klaviyo client API, plan
  properties on the profile.

## What would show it's right (other than Luke or Claude)

- **Page conversion** (sign-ups ÷ visits) from Clarity or Shopify plus
  Klaviyo, before vs after, by video.
- **Inbox placement:** mail-tester 9+/10; Postmaster domain reputation
  "High"; welcome email open rate by provider; "I didn't get it" messages
  falling towards zero.
- **The waitlist yes rate** on the thank-you step.
- **The 5-second test:** strangers can say what's offered and what to do.
- **PB claims** that match public race results.
- **An A/B winner** with about 100 sign-ups per arm before calling it.

## The rewritten prompt

> Rebuild the ERN home page (free marathon pace plan) and the Carb Bar
> waitlist page, keeping the v3 look (light, ERN blue, the pack's label
> bands), to raise sign-ups from Instagram and TikTok and the bar waitlist
> yes rate. Start from raw material, not summaries: my inbox replies, DMs
> and PB reports (I'll export them), Klaviyo form and deliverability data
> by inbox provider, Shopify and Instagram link-tap numbers, the plans I
> actually send, and the bar's lab panel. Before any design:
> (1) give me the DNS and Google Admin steps so the plan emails stop going
> to spam, and a mail-tester score to hit;
> (2) mine the inbox into pains, objections and results, and write the
> copy from their words;
> (3) turn my pacing method into code that shows the full plan on screen
> the moment someone enters their email, with the emailed copy as a
> backup, and tell them plainly where it'll land and what to do if it
> doesn't;
> (4) build the social proof from real PBs (name, race, before and after
> times, results link, permission) plus one aggregate number;
> (5) position the bar against what runners actually eat on race morning,
> with numbers.
> Use 865,000 views. Tag every bio link per video. Install Clarity. Define
> the baseline conversion rate now and the target, and set up one A/B test.
> It's right when page conversion and inbox placement beat the baseline,
> strangers pass a 5-second test, and every claim on the page can be
> checked.
