# Step 0: test with your own profile (Luke)

Do this once the developer says the builder sends to Klaviyo. About 15
minutes. Screenshot anything that fails.

## Before you start
- In Klaviyo, open Profiles and search your own name. Open your profile
  and note what's under Custom properties. You need to be a subscribed
  profile on Email List.
- Use a real email you received from us (a campaign or Email 1), not a
  test send: test sends don't identify you on the site.

## Case 1: known visitor (you, from an email)
1. Open a real ERN email on your phone or laptop and click the builder
   link. **Check 1:** the address bar shows `_kx=` in the link. If not,
   tell me: link identification is off.
2. In the builder, pick any race and set a date about 40 days away if
   the builder lets you; otherwise any future race. Goal 3:45. Press the
   button that shows the plan.
3. Back in Klaviyo, refresh your profile (allow 1 to 2 minutes).
   - **Check 2:** the activity feed on the right shows "Plan Built" with
     the race, date and goal.
   - **Check 3:** Custom properties shows race_name, race_date,
     goal_time and the pace and clock properties, matching the numbers
     on screen.
   - **Check 4:** race_date is stored as a date. Go to Flows > Create
     flow > Build your own > Trigger > Date property. race_date should
     be in the list. If it isn't, it was saved as text: tell me.
     (Leave without saving.)
4. In the builder, change the goal to 4:00 and press the button again.
   **Check 5:** a second "Plan Built" appears, and goal_time and the
   paces on your profile have changed to the 4:00 numbers.

## Case 2: unknown visitor (the inbox box)
5. Open a private or incognito browser window (so the site doesn't know
   you). Build a plan and enter a new address in "Send this plan to my
   inbox": your work address with `+test1` before the @
   (for example `name+test1@yourdomain`). Gmail and Google Workspace
   deliver it to your normal inbox.
6. **Check 6:** in Klaviyo a new profile exists for that address. It's
   subscribed to Email List (Channel consent shows Email: Subscribed),
   the source says Plan builder, and it has "Plan Built" plus the plan
   properties.
7. **Check 7:** without your answering anything else, that address
   received Email 1 of the Welcome Series within a few minutes.

## Afterwards
- Send me screenshots of checks 2, 3 and 6 (they show no one else's
  data). Crop out any other subscriber's details.
- Leave the `+test1` profile in place: we'll use it to test the flows.
  Don't add any other made-up addresses to the list.
