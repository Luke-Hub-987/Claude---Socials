# ERN website v3 (21 Oct 2026)

Light, bright redesign built on the Carb Bar pack: ERN blue bands with the
double rule, the serif "Carb Bar" face (DM Serif Display), Barlow Condensed
for labels and numbers, and the rice crisp texture.

| File | What it is |
|---|---|
| `index.html` | **Home page** = the free marathon pace plan. All Instagram and TikTok traffic lands here |
| `bar.html` | **/pages/the-bar** = the Carb Bar waitlist |
| `ern.css`, `ern.js` | Shared styles and behaviour (Klaviyo, scroll reveals, sticky mobile button) |
| `assets/` | Logo, pack cut-out, rice texture, bar close-up, founders photo |

Brief and diagnosis of the old site: `ideas/engine-room-nutrition/2026-10-21-landing-page-pace-plan.md`.

## The funnel

```
Video CTA -> Home: race + goal + name + email           (yes 1: the list)
          -> thank-you: 3 race-day rules, then one tap
             "want first go at the bar?"                (yes 2: the waitlist, its own consent)
          -> welcome email -> Luke's plan -> reply
Bar page: waitlist form -> "got a marathon? get your plan"
```

## Home page, top to bottom (and why)

1. **Hero:** the video's promise word for word, the form above the fold on a
   phone, and a live sample plan: pick 3:30, 3:45, sub-4 or 4:30 and the 4
   times appear on a course map, with watch pace and gels to carry (no email).
   Unexpected value before the ask; every number is from a published video.
2. **"A pace calculator gives you one number. Your plan gives you four."**
   Counter-position: the slow first 10K (53:20 vs 54:00), the 1% watch error,
   30g on the clock, room for a portaloo.
3. **"Here's what lands in your inbox":** 3 steps and a mock of the plan
   email (3:45 for Dublin) with a sticky note. Showing the product sells it.
4. **Who's behind it:** two polaroid photo slots of Luke and Jamie.
5. **Proof:** 3 reel tiles with view counts, 3 real replies.
6. **The Carb Bar:** the pack on the rice texture, link to the waitlist.
7. **FAQ**, then a final call to action styled as the pack label.

## Bar page, top to bottom

Blue hero with the pack on a "plate" of rice crisp and two stickers; the
waitlist form; the nutrition band off the pack; a race morning timeline
(breakfast at −3:00, the bar at −0:45, the gun, first gel at +0:20); the 8
ingredients and what each does; "the bar before the gun, gels after it";
the Rice Crisp Graveyard (4 photo slots); founders; FAQ.

## Photo slots (swap `src` for a Shopify file URL)

An empty `src` shows a striped placeholder with a brief. Upload in Shopify
under Content > Files and paste the URL.

| Page | Slot | Brief | Shape |
|---|---|---|---|
| Home | Polaroid 1 | Luke and Jamie together, faces visible, at a race or on a run (currently the old founders image) | 4:3.4 |
| Home | Polaroid 2 | The two of you testing the bar, or a finish line | square |
| Home | 3 reel tiles | The covers of the wall, carb load and 3:45 videos | 9:14 |
| Bar | Polaroid | Luke and Jamie, ideally in the kitchen with a tray of bars | square |
| Bar | Graveyard x4 | Failed batches from the series | square |
| Both | Pack | `assets/ern-carb-bar-pack.webp`: swap for a real photo of the packed bar when you have one | wide |

## Install on Shopify

1. Theme code > Assets: upload `ern.css`, `ern.js` and the files in `assets/`.
   Change `assets/...` paths and the `ern.css` / `ern.js` links to
   `{{ 'ern.css' | asset_url }}` etc.
2. Add the Google Fonts `<link>` to `theme.liquid`.
3. Home page: remove the old sections, add a Custom Liquid section with the
   body of `index.html` and its `<style>` block. Pages > Add page "The bar"
   (handle `the-bar`) with the body of `bar.html`. Change the `bar.html` and
   `index.html` links to `/pages/the-bar` and `/`.
4. Redirect `/pages/fuel-1` and `/pages/marathon-nutrition-test-pack` to `/`.
5. Point the Instagram and TikTok bio links at the home page.

## Klaviyo

- In `ern.js`, fill in `planList` (the existing Email List, so the welcome
  flow still fires) and `waitlistList` (a new list, "Bar waitlist"). Until
  then forms run in preview mode and send nothing.
- Plan sign-ups save `race`, `goal_time` and `plan_requested_at` on the
  profile. Use them in the welcome email: "Your {{ person.goal_time }} plan
  for {{ person.race }}".
- Test once with a real address before switching the bio link.

## Before it goes live (Luke)

1. **Plan turnaround:** the page says "usually within a day".
2. **3 real replies** for the proof cards (first name, race, goal, with
   permission). They must not go live as placeholders.
3. **Bar timing:** the timeline says the bar 45 minutes before the gun
   (the old page said 90, the commercial plan said 30). Pick one.
4. **The pack says <1g fat.** The v2 recipe has 5g coconut oil per 5-bar
   batch, about 1g a bar. Get the lab figure before the label is printed.
5. **The mock email** (3:45, Dublin) should match what you actually send.
6. **Shipping countries** (bar FAQ) and the founding price.
7. **FSAI registration and labelling** before any bar is sold.
