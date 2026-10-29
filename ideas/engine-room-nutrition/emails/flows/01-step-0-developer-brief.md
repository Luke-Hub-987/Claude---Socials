# Step 0: brief for the site developer (plan builder to Klaviyo)

Send this file to the developer as it is.

## What we need

When a visitor presses the button that shows their plan, the builder
sends the plan to Klaviyo in two forms:

1. **An event called `Plan Built`** with the properties below. It starts
   the race-countdown emails and records every build.
2. **The same values as profile properties** on the visitor's Klaviyo
   profile. The countdown emails go out days or weeks later, timed from
   the race date, and at that point Klaviyo can only read profile
   properties, not the event. Klaviyo can't do sums either, so every
   number an email shows has to arrive already worked out.

Send it once per press of the "show my plan" button, not on every drag
of the clock. Send it again if they change the race or the goal and press
the button again (the new values replace the old ones).

## The properties (exact names and formats)

| Property | Example | Format |
|---|---|---|
| `race_name` | Dublin Marathon | text |
| `race_date` | 2027-04-25 | date, `YYYY-MM-DD` only |
| `goal_time` | 3:45 | text, h:mm |
| `first10k_pace_km` | 5:25 to 5:30 | text, the 5-second band the builder shows |
| `first10k_pace_mi` | 8:45 to 8:50 | text |
| `main_pace_km` | 5:15 to 5:20 | text, the pace after 10K |
| `main_pace_mi` | 8:25 to 8:35 | text |
| `clock_10k` | 54:40 | text, race clock at the 10K sign |
| `clock_20k` | 1:46:40 | text |
| `clock_halfway` | 1:52:30 | text |
| `clock_30k` | 2:39:30 | text |
| `clock_40k` | 3:32:20 | text |
| `finish_time` | 3:44:30 | text |
| `gel_times` | 20, 50, 80, 110, 140, 170, 200 | text, minutes into the race, as the builder shows them |
| `plan_url` | https://engineroomnutrition.com/pages/plan?race=dublin-2027&goal=3:45 | a link that reopens this exact plan |
| `pace_band_url` | the same link with `&print=1` | opens a printable pace band |
| `plan_built_on` | 2026-10-29 | date, `YYYY-MM-DD` |

The example numbers are placeholders: the builder's own figures are the
ones to send. `plan_url` means the builder must open with a race and goal
already set when those are in the address. If it doesn't do that yet,
please add it, plus a print view of the pace band.

## Case 1: Klaviyo already knows the visitor (they came from one of our emails)

Our emails add a `_kx` code to links to our site, and Klaviyo's script
(already on the Shopify site through the Klaviyo app embed) uses it to
recognise the visitor. In that case, on "show my plan":

```js
function sendPlanToKlaviyo(plan) {
  // plan = the object above, built from the builder's own numbers
  if (!window.klaviyo) return;
  window.klaviyo.isIdentified().then(function (known) {
    if (!known) return;                 // Case 2 handles unknown visitors
    window.klaviyo.identify(plan);      // saves the values on their profile
    window.klaviyo.track('Plan Built', plan);
  });
}
```

Please check this against Klaviyo's current klaviyo.js documentation
(`isIdentified`, `identify`, `track`) before shipping.

## Case 2: an unknown visitor (the optional "Send this plan to my inbox" box)

Under the plan, add an optional box. Nobody has to fill it in to see
their plan.

- Heading: **Send this plan to my inbox**
- One email field and a button: **Send it**
- Line under the button: "You'll get this plan and Luke's emails for
  your race. Unsubscribe any time."
- After sending: "Done. Check your inbox in a few minutes, and your
  Promotions tab if it's not there."

On submit:

1. Subscribe them to our **Email List** with consent, using Klaviyo's
   Client API "Create Client Subscription"
   (`POST https://a.klaviyo.com/client/subscriptions?company_id=<public site key>`,
   list = Email List, `custom_source`: "Plan builder"). This records
   their consent. Calling `identify` with an email does not.
2. Then `window.klaviyo.identify({ email: <their email>, ...plan })` and
   `window.klaviyo.track('Plan Built', plan)`.

Luke will give you the Email List ID (Klaviyo > Lists & segments > Email
List > Settings) and the public site key (Klaviyo > Settings > API keys,
the 6-character public key). Never use the private key in the browser.

## Cookie banner

If the site has a cookie banner and a visitor declines tracking,
Klaviyo's script may not run and no event is sent. That's expected; it
means some builds won't show up.

## How we'll know it works

Luke runs the test in `02-step-0-test.md`. It has to pass all seven
checks before the flows go live.
