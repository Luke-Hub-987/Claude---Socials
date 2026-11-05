---
type: gate run record (NOT a script: it failed the gate; do not film)
generated_at: 2026-11-05
review: gate/reviews/2026-11-05-script-just-to-finish.v1-review.txt
last version: gate/runs/2026-11-05-just-to-finish-v1-full-file.txt
---

# Gate run 3: "Just to finish" (idea #9, ideas chat, 5 Nov)

The checker passed v1 first time. The reviewer failed 13 tests. Three of them
are the topic, and those need Luke:
- **G8, a repeat:** idea #9 is the 14 Oct sub-4 reel (the GPS buffer, the sign
  times 57:30 / 1:54 / 2:50 / 3:47, "trust the sign") with a new hook.
- **G5, no stake now:** no race inside about 4 weeks; no result only we have.
- **G9, an unconfirmed premise:** nothing on record shows runners saying "just
  to finish" while wanting sub-4.
**My error (G22):** my bands (5:45-5:50, then 5:35-5:40) ignored the GPS
buffer, so on a watch reading 1% long they finish about 4:01, the trap the
video warned about. FACTS corrected the same day.

**Gate fixes from this run (P190):** G8 now says "any reel we've posted",
checked by searching the scripts, not just the last 3. The ideas-chat prompt
now greps old scripts before offering a title, and needs a source for any
premise about the viewer.

**Recommendation for today:** repost the 14 Oct sub-4 reel itself as a trial
reel (no filming). It's the content idea #9 was reaching for, already
approved and already proven (30.4K lifetime; 9.5K on TikTok, our best then).
If Luke wants the "just to finish" hook tested, it's a one-change A/B (C21):
a new first 15 seconds on the 14 Oct body, and the premise confirmed first.

## Update: Luke said "Just write the script" (5 Nov)
Recorded as his call on C21 (the repeat), G9 (the premise) and G5 (no
deadline). v2 to v6 then fixed every writing fail. Reviewer FAILs by version:
13, 5, 4, 4, 2, 2. v6 passes the checker and 18 of 20 reviewer tests.
**Still failing: G16 and G17.** The answer is the GPS buffer and the 10K-sign
check, which we taught on 14 Oct, so a runner who's seen that reel can guess
it however line one is worded. The reviewer's suggestions went round in a
circle between v3 and v6. That's a consequence of the repeat Luke allowed, so
it's his call: film v6 as it is, or don't. v6 is in
gate/runs/2026-11-05-just-to-finish-v6-full-file.txt (review .v6-review.txt).

## Faster reviews (Luke, 5 Nov: "10 minutes is way too long")
`check.py --packet` builds one ~11K-token packet; the reviewer reads only that
and the phone frame, re-grades only FAILs, changed lines and G13/G16/G18, and
replies in one line. Before: 4.5 to 8 minutes, 95K to 145K tokens, 20 tests
every round. After: 1:46 to 3:14, 49K to 66K tokens, 4 to 12 tests on a
re-review.
