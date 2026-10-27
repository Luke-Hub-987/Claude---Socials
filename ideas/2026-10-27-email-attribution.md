---
type: decision (P150 council) + data
generated_at: 2026-10-27
basis: Luke's Klaviyo profiles screenshot (27 Oct, 6:57am). No email addresses are recorded here (subscribers' personal data): counts and times only.
---

# Which video brings the emails? Attribution

## What the screenshot shows (sign-ups by profile-created time)
| Day | Sign-ups visible | New reel that day |
|---|---|---|
| Sat 24 Oct (from 8pm only; the list is cut off above) | 9+ between 8:08pm and 10:42pm | Enjoy (about 2pm) |
| Sun 25 Oct (race day) | 7 | Surprise (about 2:25pm) |
| **Mon 26 Oct (bank holiday)** | **11** | **None** |
| Tue 27 Oct (to 6:40am) | 1 | None |

- **Monday had no new reel and brought the most sign-ups (11).** Luke's
  point holds: the old videos are doing a lot of the work. The caption and
  pinned-comment CTA sits on every reel since 14 Oct, and the wall, carb
  load and without the wall are still being served.
- A cluster of 4 between 5:33pm and 5:47pm on Monday points to one source
  at that moment (a reel picked up again, a story, a share). We can't tell
  which from Klaviyo alone.
- **So we can't yet judge the mid-video CTA step** (ledger row 9): the
  emails may come from the audio CTA, the caption, the pinned comment or
  old reels.

## LLM Council (P150): how do we attribute sign-ups to videos?
- **Contrarian:** Anything that adds a step to the sign-up loses sign-ups.
  A comment keyword with an auto-DM tool changes a CTA that's working, costs
  money, and needs setting up and approving on the account. Don't change the
  CTA until we know what it's doing.
- **Assumption-ripper:** We assume we need exact attribution per video.
  What we need is two decisions: is the mid-video audio CTA worth its
  retention cost, and which topics bring emails? A rough answer to both
  beats a perfect answer in three weeks. We also assume the link in the bio
  is where they come from: some may come from the caption, which points to
  the same link.
- **Expansionist:** A comment keyword ("comment PLAN and we'll send you the
  link") fixes two things at once: every DM link carries the video's name,
  and comments, our weakest number, go up. That's worth testing on one
  video later.
- **Outsider:** "Why not just ask them which video they saw?"
- **Executor:** The fastest fix that works today, for free, and covers old
  videos: **add one dropdown to the Klaviyo sign-up form: "Which video sent
  you?"** Options: the 6 most recent reels by title, "An older video", and
  "Somewhere else". Save it as a profile property. Five minutes. Update the
  options with each new post.
- **Blind cross-review:** All five accept the dropdown as step one: free,
  immediate, works for old videos. The keyword DM is accepted as a later
  test (it also tests comments), not a CTA change now. The rough read from
  sign-up times is accepted as a stopgap.
- **Chairman's verdict:** **Add the "Which video sent you?" dropdown today.**
  Keep the CTA as it is. Read sign-ups per day against posting days in each
  review until the dropdown has a week of answers. Test comment-keyword DMs
  on one video once the dropdown is live, as an A/B on comments and sign-ups.

## How to set it up (Klaviyo)
1. Sign-up forms, open the form the bio link uses, add a field: dropdown
   (or radio buttons), label "Which video sent you?", saved as a profile
   property named `video_source`.
2. Options now: Enjoy your marathon; My co-founder has no idea; Can't sleep
   before a marathon; Goal gone at 25K; Can't face another gel; 3:45 /
   3:30 / 4:30 pacing (one option); Without the wall; Carb load; An older
   video; Somewhere else.
3. Make it required, or optional if sign-ups drop (watch for a week).
4. Each review: Audience, Profiles, filter by `video_source`, count.

## Data care
Subscriber emails are personal data. They don't go into this repo, the
review files or anywhere public, and screenshots of the profile list
shouldn't be shared beyond Luke and Jamie. Counts only.
