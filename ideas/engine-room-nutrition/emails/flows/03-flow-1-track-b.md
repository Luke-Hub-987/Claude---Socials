# Flow 1, Track B: emails B1 to B4 (29 Oct 2026)

The site tracking didn't work, so there is no "Plan Built" event yet.
Track B therefore goes to **everyone** after Email 1, with no split.
When tracking works, add the split back (see the end).

## Files

| Email | File | Subject | Preview | Send |
|---|---|---|---|---|
| B1 | `B1-the-k-that-decides.html` | The K that decides your marathon | The wall gets built in the first 10K. Here's the pace that stops it. | day 2 |
| B2 | `B2-one-question.html` | One question | One line is plenty. | day 5 |
| B3 | `B3-what-goes-in-your-hand-DRAFT.html` | What goes in your hand before the gun | The start pen, the nerves, and the gel you can't face. | day 9 |
| B4 | `B4-your-block-starts.html` | Your block starts sooner than you think | Spring marathons and the Monday each 16-week block starts. | day 14 |

## Before pasting: two links in every file

Copy them from your live Email 1:
- `PASTE_BUILDER_LINK` (B1, B4): the plan builder page.
- `PASTE_WAITLIST_LINK` (all four): the waitlist link from Email 1's P.S.

Search each file for `PASTE_` before saving: there should be none left.
B3 also has yellow slots (batch number, what failed, the photo). **Keep B3
in Draft until they're filled.** In a live flow, Klaviyo moves people past
a Draft email without sending it.

## Klaviyo clicks

1. Flows > Email Welcome Series > Edit flow.
2. Under Email 1, click **+** > **Time delay** > 2 days > Save.
3. Under it, **+** > **Email**. Name "B1 - The K that decides". Subject and
   preview from the table. Sender name: Luke. Sender email and reply-to:
   luke@engineroomnutrition.com. **Smart Sending: on.** UTM tracking: on.
4. Click **Edit email** > choose the **HTML / code** editor (not drag and
   drop) > delete everything > paste the whole B1 file > Save.
5. Preview it with your own profile: the name fills in, both links open
   the right pages, and Unsubscribe works.
6. Set B1 to **Live**.
7. Repeat: **+ Time delay 3 days > B2**; **+ Time delay 4 days > B3 (Draft)**;
   **+ Time delay 5 days > B4**.
8. Save. Only people who join from now on get Track B. The 568 already on
   the list do not; reach them with the monthly campaign.

## Checks done

- Every number matches the brief: first 10K 5 to 10 s/K slower; up to a
  minute behind at halfway; watches read about 1% long; 5-second bands
  in km. The 4:00 row (5:45 to 5:50, 57:30 at 10K) matches the sub-4
  sample sent on 15, 17 and 24 Oct. 4:15 uses 6:05 to 6:10 (2 to 7 s
  slower) so it stays inside "up to a minute behind at halfway".
- Miles: the km band converted and rounded to 5 seconds, so some bands
  are 10 seconds wide.
- Spring dates checked on 29 Oct: Brighton 4 Apr, Manchester 18 Apr,
  London 24 and 25 Apr (two days, one-off), Belfast 2 May, Limerick
  2 May, Edinburgh 30 May, Cork 6 Jun 2027. Paris left out (sources
  disagree, 4 or 11 Apr). Block start = the Monday 15 weeks before race
  week (16 weeks including race week).
- **Review B4 by 14 Dec 2026**, when the first block starts: remove rows
  whose start date has passed and add the autumn 2027 races by May.
- P118 writing audit: no em dashes, no "not X, it's Y", no fragments, no
  repeated phrases, straight quotes; plain white layout, one table, one
  link plus the P.S.

## Conflicts with the brief (Luke to decide)

- **Frequency:** day 2, 5, 9 and 14 is four emails in under two weeks,
  against "never more than one a week outside race week". Recommendation:
  keep this timing (people read most in their first two weeks) and change
  the rule to "outside race week and the first two weeks after sign-up".
- **B3 cannot be finished without Luke's facts:** the real batch number,
  what failed in each batch, and one real photo (uploaded to Klaviyo's
  image library; paste its link in place of `PASTE_PHOTO_LINK`).

## When tracking works later

Add after the 2-day delay: Conditional split > "What someone has done" >
Plan Built > at least once > over all time. Yes: end. No: Track B. And on
each B email: Flow filter "Plan Built zero times since starting this flow".

## Flow 2 without the developer

Recommendation: add three fields to the Klaviyo sign-up form (Race, Race
date as a Date field, Goal time as a dropdown 3:00 to 5:00). Klaviyo saves
them as profile properties, race_date as a real date, with no website
code. That is enough to run the Race Countdown on the date, with the
numbers taken from a goal-time table inside each email.
