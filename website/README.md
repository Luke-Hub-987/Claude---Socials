# ERN website v2 (21 Oct 2026)

Two pages, built to drop into the Shopify theme:

- `index.html`: the **home page**, now the free marathon pace plan page.
  Everything from Instagram and TikTok lands here.
- `bar.html`: **/pages/the-bar**, the bar waitlist.

Brief and diagnosis of the old site: `ideas/engine-room-nutrition/2026-10-21-landing-page-pace-plan.md`.

## The funnel (one job per page)

```
Video CTA ("email us your race and goal time, link in bio")
  -> Home: race + goal time + name + email        (conversion 1: the list)
  -> Thank-you state: 3 race-day rules now,
     then "want first go at the bar?" one click    (conversion 2: the waitlist, separate consent)
  -> Welcome email -> Luke's plan -> reply
Bar page: waitlist form, then "got a marathon? get your plan"
```

Why the waitlist ask comes **after** the plan form, not as a tickbox on
it: every extra field costs signups, and the moment right after someone
says yes is when the next yes is cheapest. It's also explicit consent for
the launch list (CLAUDE.md).

## Copy decisions and where they come from

| Choice | Why |
|---|---|
| Headline repeats the video's promise | Message match: the visitor checks in about 3 seconds that they're in the right place |
| Specifics everywhere (4 times, 30g, every 30 minutes, km and miles) | Ogilvy: specific facts sell; our data: numbers and one worked example win (P108, P115, P127) |
| The 4 sample plans given free, no email | Unexpected value before the ask (Briar Cochran). Every number is from a published video and caption, so nothing contradicts |
| "At 10K you should be behind your goal time" | Our best hook shape: a paradox that ends in a reframe (sub-4 video, skip 31.9% to 34%) |
| "Get my plan for 3:45" pre-fills the goal | One less decision |
| Proof = real view counts and list size | Real and checkable. The test pack reviews are gone with the test pack |
| Bar = race morning, "before the run, never during it" | The audience never eats food in a race (FACTS.md); the videos teach gels; no contradiction |
| Beef gelatine said up front | Honest, and stops the vegetarian refund later |

Cut from the old site: the test pack, the quiz, the carb calculator (it
pushes 90g an hour, the videos say 60 to 75g), "Hybrid Professional",
GAA and triathlon, the CEO study, the anti-gel table.

## Install on Shopify

1. Online Store > Pages > Add page "The bar", handle `the-bar`.
2. Theme editor > Home page: remove the old sections, add a **Custom
   Liquid** section, paste everything inside `<body>` from `index.html`
   plus the `<style>` block. Same for the bar page template.
3. Add the Google Fonts `<link>` to `theme.liquid` if the theme lacks it.
4. Upload a better bar photo and swap the `bar-closeup.jpg` URL.
5. Point the Instagram and TikTok bio links at the home page.
6. Redirect `/pages/fuel-1` and `/pages/marathon-nutrition-test-pack` to
   `/` (Navigation > URL redirects) so old links still land.

## Klaviyo

- Fill in `planList` and `waitlistList` in the `KLAVIYO` object at the
  bottom of each page (Lists & segments > the list > Settings > List ID).
  Until then the forms run in preview mode and send nothing.
- Make a new list **Bar waitlist**. Keep the plan sign-ups on the
  existing Email List so the welcome flow still fires.
- The form saves `race`, `goal_time` and `plan_requested_at` on the
  profile, so Luke can see what to write without waiting for a reply.
  Add them to the welcome email: "Your {{ person.goal_time }} plan for
  {{ person.race }}".
- Test once with a real address before switching the bio link.

## Before it goes live (Luke)

1. **How fast do plans go out?** The page says "usually within a day".
   Change it if that isn't true.
2. **3 real replies** for the "From the inbox" cards (first name and race,
   with permission). They're placeholders now and must not go live empty.
3. **The bar**: I don't have the design we settled on in the other chat.
   Send the pack image and I'll put it in the hero. Also: price (or
   "founding price" only), shipping countries, and whether "Made in
   Ireland, in small batches" is accurate.
4. **Selling food**: check FSAI registration and labelling before any
   bar is sold, even a small first batch.
