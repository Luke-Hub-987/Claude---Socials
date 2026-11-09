# Plan frames (static, 1920 x 1080)

Static top-of-reel frames for a goal-time plan, in the ERN theme (P161):
navy body, a cream race strip across the top (START, 10K, HALF, 30K,
FINISH, the current section in ERN blue) with the ERN logo top right, gold
for the key numbers, red only for the "too fast" thing.

- `plan-323.html`: the 3:23 plan (4:50 a K), 5 frames. Luke's prompt, 30 Oct.
- `shoot.js`: renders a page's frames to PNGs.
  `node motion/plan-frames/shoot.js motion/plan-frames/plan-323.html motion/plan-frames 323 <names...>`
- Logo: `motion/brand/ern-logo.png` (from Luke, 30 Oct).
- Downloads: https://claude.ai/artifact/XHuCgjjDcTa45o2x1YvEcP

For another goal time, copy `plan-323.html` and change only the numbers.
- `where-it-goes-wrong.html`: Sunday 1 Nov, 5 frames (an IOU to the clock, the downhill with its bill, paying the minute back, the two runners at 34K, the plan for 3:45, sub-4 and 4:30). Rendered as `wgw-*.png`.
- `just-to-finish.html`: SAID JUST TO FINISH. / WANT SUB-4 MARATHON? (5 Nov), 5 frames: the 4:02 watch (from 0:03), start to 10K, 10K to 30K, 30K to the finish, the hand plan to save. The hand plan card fills in one number per stage. Rendered as `jtf-*.png`.
- `parkrun-25.html`: HOW TO BREAK 25 MINS / AT PARKRUN (NO SPRINT) (6 Nov), 5 frames: 25:04, 4 seconds off, with the 3 ranges blank (from 0:03; v2 6 Nov, Luke: match the rest), the first K, K2 to K4, the 4K beep, the last 100m (24:37 and the 3 ranges to save). The 3 ranges card fills in one range per stage. Rendered as `pr25-*.png`.
- `spring-ranking.html`: RANKING 8 SPRING / MARATHONS FOR A PB (9 Nov), 6 frames, one layout (P193): the S-to-D board and a "your one change" card. The board fills in one tier per stage (D, C, B, A, S); the courses still to rank stay face down, and the last one shows as THE FLATTEST for the rehook. Rendered as `spring-*.png`.
