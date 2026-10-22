# Motion graphics

16:9 (1920x1080) clips for the top half of a vertical reel, talking head
underneath, in the style of the two reference reels Luke sent on 22 Oct
(dark particle scenes with a pill and a mono label bar; cream cards with
a stage tag, a condensed headline and a diagram).

- `goal-gone.html`: every scene for "What to do when your marathon goal
  is gone". Open it in a browser to watch them loop (`?s=6` plays one).
- `render.js`: renders each scene to its own MP4.
  `node motion/render.js motion/goal-gone.html <out dir> [scene numbers]`
- Brand colours are the `:root` block at the top of the HTML. Swap them
  for the logo colours and re-render; nothing else changes.

Each clip animates in, then holds with slow movement, so it can be
trimmed to the length of the line. Lay the clips end to end and cut each
one where the next line starts.

## Cue sheet: goal gone

| Clip | Starts on | Length |
|---|---|---|
| 01-hook | "If you're running a marathon..." | 13s |
| 02-chase-it | "Chase it, and at 32K..." | 10s |
| 03-slow-down | "Slow down instead..." | 8s |
| 04-two-numbers | "And you won't have to do a single sum..." | 10s |
| 05-night-before | "The night before, set 3 goals." | 11s |
| 06-wrist-numbers | "Then write 2 numbers on your wrist." | 16s |
| 07-cta | "Want your A, B and C worked out..." | 10s |
| 08-25k-clock | "At the sign, one look at the clock." | 8s |
| 09-next-2k | "Ease off 10 seconds a K..." | 11s |
| 10-rehook | "So why go slower than you need to..." | 6s |
| 11-why-plan-b | "Because 3 minutes down at 25K..." | 19s |

Every number on screen comes from the script (FACTS.md and the 3:45
example): 2:13 at 25K (3:45 x 0.59), B 3:51, B pace 5:25 to 5:30 a K,
2:14 still on, 2:15 A gone, ease off 10 s a K for 2K, 5 words at 37K.
