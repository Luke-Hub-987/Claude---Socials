# Flow 1, Welcome Series: what goes in Klaviyo (v3, 29 Oct 2026)

v3: all four emails rebuilt in the ERN theme with a reply button near
the top (Luke, P119). Order, delays and subjects unchanged.

Luke approved two changes on 29 Oct: B2 now asks for the next race and
goal time, and B4 (block start) moves to the front until February.
No split (the site tracking doesn't work yet), so everyone gets these.

## The flow, in order

| Step | Klaviyo step | File | Subject | Preview |
|---|---|---|---|---|
| 1 | Email 1 (live, unchanged) | | Your marathon, sorted | A free, personalised plan designed for you |
| 2 | Time delay: 2 days | | | |
| 3 | Email 2 = B4 | `B4-your-block-starts.html` | Your block starts sooner than you think | Spring marathons and the Monday each 16-week block starts. |
| 4 | Time delay: 3 days | | | |
| 5 | Email 3 = B2 | `B2-one-question.html` | One question | Which marathon are you running next? |
| 6 | Time delay: 4 days | | | |
| 7 | Email 4 = B3 (Draft) | `B3-what-goes-in-your-hand-DRAFT.html` | What goes in your hand before the gun | The start pen, the nerves, and the gel you can't face. |
| 8 | Time delay: 5 days | | | |
| 9 | Email 5 = B1 | `B1-the-k-that-decides.html` | The K that decides your marathon | The wall gets built in the first 10K. Here's the pace that stops it. |

Sends land on days 0, 2, 5, 9 and 14. B3 stays in Draft until Luke sends
the batch number, what failed and a photo: Klaviyo moves people past a
Draft email without sending it.

## Settings for every new email

- Name: "Email 2 - Block starts", "Email 3 - One question", "Email 4 -
  The bar", "Email 5 - First 10K".
- Sender name: Luke. Sender email and reply-to: luke@engineroomnutrition.com.
- Smart Sending: on. UTM tracking: on.
- Content: Edit email > HTML / code editor (not drag and drop) > delete
  everything > paste the whole file > Save.
- Plain text tab: paste the version from `05-plain-text-versions.md`.
- Before setting Live: search the HTML for `PASTE_`. Replace
  `PASTE_BUILDER_LINK` (Emails 2 and 5) and `PASTE_WAITLIST_LINK` (all)
  with the links in your live Email 1. None may be left.
- Preview with your own profile: name fills in, links open the right
  pages, Unsubscribe works. Then set Live.

## Recording the race replies (Email 3)

Email 3's replies are now the only way to learn people's race dates.
Once a week:

1. Make a spreadsheet with four columns: `Email`, `race_name`,
   `race_date` (format 2027-04-18), `goal_time` (format 3:45).
2. One row per reply.
3. Klaviyo > Lists & segments > Create list "Replied" (first time only).
   Open it > Import contacts > upload the sheet. Map the three columns to
   new custom properties with those exact names, and set race_date's
   type to **Date**.
4. Reply to each person with their plan, as the email promises.

This builds the data the Race Countdown (Flow 2) needs: race_date saved
as a real date. Never send me the sheet; counts only.

## Also do

- Check every race in Email 2 is in the builder's race list (Brighton,
  Manchester, London, Belfast, Limerick, Edinburgh, Cork).
- **Review Email 2 by 14 Dec 2026**: remove races whose block has
  started. **Swap Emails 2 and 5 back in February**, when summer and
  autumn racers start joining.
- Only new sign-ups enter these steps. The 568 already on the list don't.

## Measure (every two weeks)

Per email: clicks, replies, unsubscribes (under 0.5%). Email 3: race
replies recorded. Share of active profiles on the waitlist.
