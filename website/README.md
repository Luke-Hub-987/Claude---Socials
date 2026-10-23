> **To put it live:** follow `SHOPIFY-INSTALL.md`. Shopify files are built into `shopify/` by `build_shopify.py`.

# ERN website v5 (22 Oct 2026)

v5 turns visitors into customers, not just emails. Brief: `BRIEF-v5.md`.
Mail-tester 10/10 since the SPF and DKIM fix (22 Oct).

**What v5 changed**
- **First screen on a phone:** compact proof chips, the results ticker, the
  headline and the **goal slider**. Drag to your goal and the 10K time
  shows free; 20K, 30K, 40K and gels show as locked until the email.
- **The bar inside the plan:** a race-morning step (3 hours before: 2g carbs
  per kg; 45 minutes before: 30g, "a banana does it, so will our Carb Bar")
  with the waitlist button right there.
- **The founders in motion:** a video slot (10 to 15 s of reel outtakes,
  muted loop) beside the photo, captions under both, and "Our race CV, the
  honest version".
- **Results form ("Ran with our plan? Tell us your time")** with a share
  tick, so the results wall refills after Dublin and Frankfurt.
- **Events at every step** (`ERN.track`): `plan_form_started`,
  `goal_slider_used`, `plan_unlocked`, `lock_screen_saved`,
  `pace_band_printed`, `waitlist_yes`, `result_submitted`. They go to
  Microsoft Clarity, the dataLayer (GA4) and Klaviyo ("plan_unlocked" can
  trigger a flow).
- **Lighter:** images now WebP (about 460 KB for the whole page's own files).

**Headlines to A/B test** (Ogilvy and Caples: test on real traffic)
- A (live): "Your free marathon pace plan, on screen in 20 seconds."
- B: "Free: the time to hit at every 10K sign of your marathon."
- C: "Dave took 45 minutes off at Dublin. Here's the plan he used."
  (only with Dave's OK)

**To fill**
- The founders video: an MP4 under 3 MB in `<video src="...">` in the
  founders section.
- Install Microsoft Clarity (free Shopify app) so the events have
  somewhere to land; note today's sign-up rate as the baseline.

---

# v4 notes (21 Oct 2026)

Light and bright, built on the Carb Bar pack. v4 goes deeper, not bigger:
the plan shows **on screen the moment someone gives their email**, the
proof is real results, and we're upfront about spam.

| File | What it is |
|---|---|
| `index.html` | **Home** = the free marathon pace plan. All Instagram and TikTok traffic lands here |
| `bar.html` | **/pages/the-bar** = the Carb Bar waitlist |
| `plan.js` | The pace plan engine: the video method as code (table below) |
| `ern.css`, `ern.js` | Shared styles; Klaviyo, scroll reveals, sticky mobile button |
| `assets/` | Logo, pack cut-out, rice texture, bar close-up, founders photo |
| `BRIEF-v4.md` | The deeper brief: raw material, methods, what proves it right |

## The flow (home page)

1. **Race countdown bar** (dynamic): "Dublin and Frankfurt are in 4 days".
   Rolls to New York, then hides. Add races to `RACES` in `index.html`.
2. **Hero:** proof first (900K+ views, 100+ plans, 18,700 saves), the offer,
   the form (race, goal, email, first name optional) and a spam warning
   before they submit. Next to it, a **live preview**: the course map follows
   the goal they pick, the 10K time is free, the other 3 are blurred.
3. **After the email:** the full plan builds on the page: 4 sign times, watch
   pace per stage in km and miles, effort, a gel timeline, what to do if you
   lose time. Then **Save to lock screen** (a phone-sized image) and **Print a
   pace band** (4 strips to cut out). Then the "probably in the wrong folder"
   box with Gmail, Outlook and iPhone steps. Then the bar waitlist, one tap.
   If Klaviyo fails, they still get the plan.
4. **Proof:** 3 results as message cards, names left out (P143). Tally below.
5. **Why it works:** one even pace vs your plan.
6. **The Carb Bar:** what's in your kit bag at 7am (bar vs banana vs porridge
   vs gel), with an email field to join the waitlist right there.
7. **Who we are**, **FAQ** (incl. "I never got the email"), **final CTA**.

## The plan engine: check this table (Luke)

The 4 goals from videos return the published numbers. Every other goal uses
the same method: 0-10K in the 5-second band containing goal pace (behind on
real distance, since the watch reads about 1% long); 10-40K the band that
finishes with time in hand even if the watch reads 1.5% long, with the
smallest pick-up that allows; last 2K 10 s/K quicker again. 4:30 and slower
walk every drink station (inside the times). Gels: 30g at 20 min, then every
30, none in the last 20 min, one spare.

| Goal | 10K | 20K | 30K | 40K | Finish | 0-10K /K | 10-40K /K | Last 2K /K | 10-40K /mi | Carry |
|---|---|---|---|---|---|---|---|---|---|---|
| 3:00 | 43:30 | 1:25 | 2:07 | 2:48 | 2:57 | 4:15 to 4:20 | 4:05 to 4:10 | 3:55 to 4:00 | 6:35 to 6:40 | 6 |
| 3:05 | 44:00 | 1:28 | 2:11 | 2:54 | 3:03 | 4:20 to 4:25 | 4:15 to 4:20 | 4:05 to 4:10 | 6:50 to 7:00 | 6 |
| 3:10 | 46:00 | 1:30 | 2:14 | 2:58 | 3:08 | 4:30 to 4:35 | 4:20 to 4:25 | 4:10 to 4:15 | 7:00 to 7:05 | 6 |
| 3:15 | 46:30 | 1:32 | 2:17 | 3:02 | 3:11 | 4:35 to 4:40 | 4:25 to 4:30 | 4:15 to 4:20 | 7:05 to 7:15 | 7 |
| 3:20 | 47:30 | 1:34 | 2:21 | 3:08 | 3:18 | 4:40 to 4:45 | 4:35 to 4:40 | 4:25 to 4:30 | 7:25 to 7:30 | 7 |
| 3:25 | 49:00 | 1:37 | 2:24 | 3:12 | 3:22 | 4:50 to 4:55 | 4:40 to 4:45 | 4:30 to 4:35 | 7:30 to 7:40 | 7 |
| 3:30 (video) | 50:00 | 1:39 | 2:29 | 3:18 | 3:28 | 4:55 to 5:00 | 4:50 to 4:55 | 4:40 to 4:45 | 7:45 to 7:55 | 7 |
| 3:35 | 52:00 | 1:42 | 2:32 | 3:22 | 3:33 | 5:05 to 5:10 | 4:55 to 5:00 | 4:45 to 4:50 | 7:55 to 8:05 | 7 |
| 3:40 | 52:30 | 1:44 | 2:34 | 3:25 | 3:36 | 5:10 to 5:15 | 5:00 to 5:05 | 4:50 to 4:55 | 8:05 to 8:10 | 7 |
| 3:45 (video) | 54:00 | 1:46 | 2:39 | 3:32 | 3:43 | 5:20 | 5:13 | 5:03 | 8:25 | 8 |
| 3:50 | 55:00 | 1:49 | 2:42 | 3:35 | 3:47 | 5:25 to 5:30 | 5:15 to 5:20 | 5:05 to 5:10 | 8:25 to 8:35 | 8 |
| 3:55 | 56:00 | 1:51 | 2:46 | 3:41 | 3:53 | 5:30 to 5:35 | 5:25 to 5:30 | 5:15 to 5:20 | 8:45 to 8:50 | 8 |
| Sub-4 (video) | 57:30 | 1:54 | 2:50 | 3:47 | 3:59 | 5:42 | 5:35 | 5:25 | 9:00 | 8 |
| 4:05 | 58:30 | 1:55 | 2:52 | 3:49 | 4:01 | 5:45 to 5:50 | 5:35 to 5:40 | 5:25 to 5:30 | 9:00 to 9:05 | 8 |
| 4:10 | 1:00 | 1:59 | 2:57 | 3:56 | 4:08 | 5:55 to 6:00 | 5:45 to 5:50 | 5:35 to 5:40 | 9:15 to 9:25 | 8 |
| 4:15 | 1:01 | 2:00 | 3:00 | 3:59 | 4:12 | 6:00 to 6:05 | 5:50 to 5:55 | 5:40 to 5:45 | 9:25 to 9:30 | 9 |
| 4:20 | 1:02 | 2:03 | 3:04 | 4:05 | 4:18 | 6:05 to 6:10 | 6:00 to 6:05 | 5:50 to 5:55 | 9:40 to 9:45 | 9 |
| 4:25 | 1:04 | 2:05 | 3:07 | 4:09 | 4:22 | 6:15 to 6:20 | 6:05 to 6:10 | 5:55 to 6:00 | 9:45 to 9:55 | 9 |
| 4:30 (video) | 1:05 | 2:08 | 3:11 | 4:14 | 4:28 | 6:20 to 6:25 | 6:10 to 6:15 | 6:00 to 6:05 | 9:55 to 10:05 | 9 |
| 4:35 | 1:07 | 2:11 | 3:15 | 4:19 | 4:32 | 6:30 to 6:35 | 6:15 to 6:20 | 6:05 to 6:10 | 10:05 to 10:10 | 9 |
| 4:40 | 1:07 | 2:12 | 3:17 | 4:22 | 4:36 | 6:35 to 6:40 | 6:20 to 6:25 | 6:10 to 6:15 | 10:10 to 10:20 | 9 |
| 4:45 | 1:09 | 2:16 | 3:22 | 4:29 | 4:43 | 6:45 to 6:50 | 6:30 to 6:35 | 6:20 to 6:25 | 10:30 to 10:35 | 10 |
| 4:50 | 1:10 | 2:17 | 3:25 | 4:32 | 4:46 | 6:50 to 6:55 | 6:35 to 6:40 | 6:25 to 6:30 | 10:35 to 10:45 | 10 |
| 4:55 | 1:11 | 2:20 | 3:29 | 4:38 | 4:53 | 6:55 to 7:00 | 6:45 to 6:50 | 6:35 to 6:40 | 10:50 to 11:00 | 10 |
| 5:00 | 1:12 | 2:22 | 3:32 | 4:42 | 4:57 | 7:05 to 7:10 | 6:50 to 6:55 | 6:40 to 6:45 | 11:00 to 11:10 | 10 |
| 5:05 | 1:13 | 2:24 | 3:35 | 4:46 | 5:01 | 7:10 to 7:15 | 6:55 to 7:00 | 6:45 to 6:50 | 11:10 to 11:15 | 10 |
| 5:10 | 1:15 | 2:27 | 3:40 | 4:52 | 5:08 | 7:20 to 7:25 | 7:05 to 7:10 | 6:55 to 7:00 | 11:25 to 11:30 | 10 |
| 5:15 | 1:16 | 2:29 | 3:42 | 4:56 | 5:11 | 7:25 to 7:30 | 7:10 to 7:15 | 7:00 to 7:05 | 11:30 to 11:40 | 11 |
| 5:20 | 1:18 | 2:32 | 3:46 | 5:00 | 5:16 | 7:35 to 7:40 | 7:15 to 7:20 | 7:05 to 7:10 | 11:40 to 11:50 | 11 |
| 5:25 | 1:18 | 2:34 | 3:50 | 5:06 | 5:22 | 7:40 to 7:45 | 7:25 to 7:30 | 7:15 to 7:20 | 11:55 to 12:05 | 11 |
| 5:30 | 1:19 | 2:36 | 3:53 | 5:09 | 5:26 | 7:45 to 7:50 | 7:30 to 7:35 | 7:20 to 7:25 | 12:05 to 12:10 | 11 |

## Klaviyo

- One list for every form (P146): paste the Email List ID into each section
  in the theme editor (it becomes `planList`; the waitlist and results forms
  use it too and tag the profile with `bar_waitlist` or `result_time`).
  Empty = preview mode, nothing sent.
- Each plan sign-up saves these on the profile, so the welcome email can be
  the plan itself: `race`, `goal_time`, `plan_10k`, `plan_20k`, `plan_30k`,
  `plan_40k`, `plan_pace_1`, `plan_pace_2`, `plan_pace_3`, `plan_gels`,
  `plan_carry`, `plan_finish`. In the email: `{{ person.plan_10k }}` etc.
  Wrap the plan block in "show if goal_time is set and isn't Not sure yet".
- Subject line: "Your {{ person.goal_time }} plan for {{ person.race }}".

## Fix the spam (DNS, about 15 minutes)

Checked 21 Oct: the root domain has **no SPF and no Google DKIM**, and DMARC is
`p=none` with no reports. Klaviyo's own sending domain is fine; it's the
emails you send from Gmail (the plans, your replies) that go unsigned.

1. **Google Admin** (admin.google.com) > Apps > Google Workspace > Gmail >
   Authenticate email > Generate new record (2048-bit). Copy the host name
   (`google._domainkey`) and the long TXT value.
2. **Shopify** (the domain was bought through Shopify): Settings > Domains >
   engineroomnutrition.com > Domain settings > Edit DNS settings > Add
   custom record. Add:
   - TXT, name `google._domainkey`, value from step 1.
   - TXT, name `@`, value `v=spf1 include:_spf.google.com ~all`. Add it as a
     new record; keep the `klaviyo-site-verification` one. Only ever one
     `v=spf1` record.
   - Edit the `_dmarc` TXT to `v=DMARC1; p=none; rua=mailto:` plus an inbox you
     check, so you get reports.
3. Wait an hour, go back to Google Admin and click **Start authentication**.
4. Test: send an email from Gmail to the address on mail-tester.com. Aim for
   9/10 or better.

## Photo slots

Striped boxes show a brief; swap `src` for a Shopify file URL. Main one: a
real photo of the two of you, faces visible (home and bar page polaroids).

## Install on Shopify

Upload `ern.css`, `ern.js`, `plan.js` and `assets/` to the theme assets and
link them with `asset_url`. Home page: a Custom Liquid section with the body
and `<style>` of `index.html`. Page "The bar" (handle `the-bar`) with
`bar.html`. Change `bar.html` and `index.html` links to `/pages/the-bar` and `/`.
Redirect `/pages/fuel-1` and `/pages/marathon-nutrition-test-pack` to `/`.
Point the bio links at the home page, with `?utm_source=instagram&utm_content=<video>`.

## Still open (Luke)

1. Do the DNS fix above.
2. Tom's message word for word, and a yes to use it (no name). Confirm the
   12-minute PB and Antwerp runners followed our videos or plans.
3. Bar: eating time (the page says 45 minutes before the gun), founding price,
   shipping countries, lab figures (the pack's "<1g fat" vs about 1g from the
   coconut oil), FSAI registration.
4. Check the plan table above.
5. Install Clarity (free Shopify app) and note today's sign-up rate as the
   baseline.
