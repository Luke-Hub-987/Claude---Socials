# 3:59 reel: full-screen cutaways (TED-Ed style)

Luke, 20 Nov: full screen, his audio runs underneath, no stick figures, our runner a
fair-skinned white guy, the ERN logo on every frame (P229).

| Clip | Length | Lay it so 0.5 s in lands on | Ends after |
|---|---|---|---|
| `out/cutaway-1-round-number.mp4` | 20.8 s | "In the minute just under 3 hours..." | "...so you know your number." (the clock card + SAVE THIS) |
| `out/cutaway-2-last-2k.mp4` | 16.4 s | "The minute shows up in the last 2.2K..." | "...but the clock said go." |
| `out/cutaway-3-40k-check.mp4` | 21.2 s | "So look at the clock at the 40K sign." | "...so run your own race home." |
| `out/cutaway-4-next-run.mp4` | 19.4 s | "Pick a round number for your next long run..." | "...before you reach a 40K sign." |

On camera (no cutaway): the hook (0:00 to ~0:15), "Send this to whoever...",
"And you don't need a marathon...", "There's more your legs are hiding...".

Timed to the script at about 2.9 words a second (the hook's 43 words in ~15 s). If a
stage runs faster or slower in the take, speed the clip to fit (95% to 110% looks
fine) or trim the 1 s hold at the end. Nothing that matters sits in the bottom 30%
(subtitles) or under the logo.

Files: `cutaways.html` (the four scenes; preview a frame with `?s=2&t=9.5`),
`rig.js` (runner rig, tokens, clock, lettering), `render9.js` (renders 1080x1920
MP4s: `node motion/three-59/teded/render9.js motion/three-59/teded/cutaways.html motion/three-59/teded/out`),
`preview.js`, `grain.png` (paper grain and vignette), `scenes.html` + `shoot.js`
(the style stills).
