# Motion graphics

16:9 (1920x1080) clips for the top half of a vertical reel, talking head
underneath, in the style of the two reference reels Luke sent on 22 Oct
(dark particle scenes with a pill and a mono label bar; cream cards with
a stage tag, a condensed headline and a diagram).

- `goal-gone.html`: every scene for "What to do when your marathon goal
  is gone". Open it in a browser to watch them loop (`?s=6` plays one).
- `race-night.html`: the sleep video (Sat 24), in the website's theme:
  ERN blue, navy night scenes with the gold clock digits, cream sections
  with white cards, DM Serif Display headlines with blue italics,
  Barlow Condensed labels and buttons. This is the house style from now on.
- `enjoy.html`: how to actually enjoy your marathon (Sat 24), same theme,
  told with illustrated characters (a side-view runner rig with a run
  cycle, spectators, signs, a kid on a parent's shoulders) and a course
  bar along the bottom with a locked "?" pin at 32K that only opens in the
  last clip.

## Rules the motion follows (from the reviews)
- **P147: the opening frame is one picture or one number**, never a
  sentence and never the answer. The only words on it are the OST. Race
  night broke this (the reassurance as big type, 41.4% skip); enjoy opens
  on a bare 32K marker.
- Characters and objects carry each beat; on-screen words are stage
  markers, numbers and labels of two or three words.
- Keep one open loop visible on screen until the payoff (the 32K pin,
  the blank text bubble).
- `render.js`: renders each scene to its own MP4.
  `node motion/render.js motion/goal-gone.html <out dir> [scene numbers]`
- Brand colours are the `:root` block at the top of each HTML file. Swap them
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

## Cue sheet: race night (sleep)

| Clip | Starts on | Length |
|---|---|---|
| 01-hook | "If you're running a marathon..." | 9s |
| 02-2am | "It's 2am." | 13s |
| 03-in-the-bank | "Get the 2 nights before right..." | 10s |
| 04-one-thing | "And there's one thing to do at 3am..." | 9s |
| 05-two-nights-before | "The night that counts is 2 nights before." | 12s |
| 06-cta | "Want your whole race weekend planned..." | 9s |
| 07-6pm-laid-out | "By 6pm, everything's laid out." | 11s |
| 08-bedtime | "Then lights out at your normal time..." | 9s |
| 09-rehook | "So what do you do at 3am?" | 5s |
| 10-3am-box | "Don't look at the clock..." | 22s (the box runs in real time, 4 s a side, from 4.6s) |
| 11-get-up-and-go | "And even if you never drop off..." | 9s |

The box shows all 4 sides (in 4, hold 4, out 4, hold 4). The script as
sent has 3; add "and hold for 4 again" or the dot won't match the words.

## Cue sheet: enjoy

| Clip | Starts on | Length | On screen |
|---|---|---|---|
| 01-hook-32k | "If you're running a marathon..." | 12s | Frame 1: the 32K marker alone. A runner, legs gone, comes in; at "one text" a phone with a blank, typing bubble |
| 02-watch-staring | "You know the long runs..." | 11s | Head down at the watch, the park fades to nothing; then race day, blurred and grey |
| 03-head-up | "Or you finish with your head up..." | 6s | Arm up, pint, medal, "next one?" |
| 04-save-send | "Save this, and send it..." | 5s | Two runners at the start; a paper plane between phones |
| 05-0-10k | "If the first K feels exciting..." | 16s | The 10 words light up in one breath; the fast starters leave; "you'll pass them at 32K" points at the pin |
| 06-cta | "Want your race planned K by K?" | 8s | Site CTA card, 42 K blocks filling |
| 07-10-20k | "10 to 20K is the best..." | 18s | Head down until 5.8s, then once a K at the markers, signs, the high-five at 13.4s, then it goes grey and quiet |
| 08-your-name | "The night before, write your first name..." | 13s | SAM going on the top in marker, as tall as a hand; then a stranger shouts it, wave back |
| 09-the-text | "And then there's the text..." | 6s | The text to Mam, still blurred |
| 10-32k-the-text | "Text whoever's coming to watch you." | 11s | The text typed out; finish packed vs your people at 32K; "See you at 32K" |
| 11-32k-running-to-them | "32K is where it goes quiet..." | 14s | 30K, 31K, 32K; they're there at 6s, arms up; send button; a stranger shouts SAM |
