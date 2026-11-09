# Gate review: 2026-11-09-script-spring-ranking.md
Script hash: 00ead2ed29e21cfc
Reviewed: 2026-11-09, independent (gate-reviewer), round 1
Mockup: ideas/engine-room-nutrition/mockups/2026-11-09-spring-ranking-frame-one-phone.png (the Gate field names `...-frame-one.png` without `-phone`; correct the field so a new frame re-grades G2 and G14)

| Test | Verdict | The line it rests on (quoted) | Why, and what would pass |
|---|---|---|---|
| G2 [BLOCK] | PASS | Mockup: "RANKING 8 SPRING / MARATHONS FOR A PB" over Luke in the car; "subtitles from 0:03" | Between 0:00 and 0:03 the title is the only text in the video. The "0:00 TO 0:03" tag and the placeholder caption are mockup labels, not video content. |
| G4 [RISK] | PASS | "RANKING 8 SPRING / MARATHONS FOR A PB" | It has a numeral, and "for a PB" is the viewer's goal, not our result. |
| G5 [RISK] | FAIL | "Each race gets one reason and its start Monday, when your 16 weeks begin." | To someone who has already booked, where their race ranks is trivia because they can't switch. The start Monday is a calendar entry (admin) that any 16-week plan already prints. To pass, the stake has to change what they do in the race or the block, not just when it starts. Risk: people watch the list, then neither save nor send, because nothing in it changes their race. |
| G6 [BLOCK] | PASS | "RANKING 8 SPRING / MARATHONS FOR A PB" | The title is the event (spring marathons). Training timing stays inside, and each tier ends on a dated action. |
| G7 [RISK] | FAIL | "Belfast on 2 May is still open... Start Monday 11 January." | Each tier speaks only to the runners of that race (ledger row 10, sorting viewers). Spring races in our own inbox are missing (Athlone, Limerick, Cork), and there's no dream line. Risk: viewers leave once their own race has gone by, or straight away if their race isn't one of the 8. |
| G8 [BLOCK] | FAIL | "Count 16 weeks back from race day: that Monday is when your training starts" (caption) | Counting back 16 weeks is what every club coach and every printed plan already says. The course reasons ("about 6K of the course is cobbles", "short, sharp hills") are standard race-guide lines. To pass, it needs one aha a coach wouldn't give, tied to a complaint from our data. |
| G9 [BLOCK] | FAIL (needs Luke) | "If you've got a spring marathon booked" / file: "Most people with these 5 races in their feed already have a place... Luke to OK." | The whole video assumes a booked audience, and the file still marks that "Luke to OK". The habit the pain rests on ("Start a few weeks late") has no source in our data. It passes when Luke confirms both. |
| G11 [RISK] | FAIL (needs Luke) | "RANKING 8 SPRING / MARATHONS FOR A PB" | Only one of the five counts (the number 8). "Spring" isn't a deadline, and nothing gives a constraint, proof or a method of ours. Risk: it reads like every other "best spring marathons" list and gets scrolled past. |
| G12 [BLOCK] | PASS | Title and frame one: "RANKING 8 SPRING / MARATHONS FOR A PB" | The ranking is held back, so skipping costs the viewer the answer. The only number on screen is 8, and no rate can be worked out from it. |
| G13 [RISK] | PASS | Line one: "your 16 weeks might start before Christmas, or might have started already" | The title gives the event, number and goal, the picture is none, and line one adds the start date. No words or numbers repeat, and together they don't give the ranking away. |
| G14 [RISK] | PASS | Gate field: "no picture"; mockup shows Luke and the title only | "One real image (or none)" allows no picture, and nothing banned is on screen. |
| G16 [BLOCK] | FAIL | Line one: "your 16 weeks might start before Christmas, or might have started already."; turn: "if your longest runs are in January dark"; rehook: "S tier is the only one where your 16 weeks have already started." | The answer is guessable. Only a February race can have started already, and everyone knows Seville is in February. "January dark" points at it, and once B tier says 23 November the rehook leaves only Seville. Each viewer's own question ("has mine started?") is answered by their own tier, mostly before the closing stage. To pass, line one needs a question that arithmetic and the race calendar can't answer, held until S TIER. |
| G17 [RISK] | FAIL | "If you've got a spring marathon booked, your 16 weeks might start before Christmas, or might have started already." | A runner would say "obviously" and count it out themselves, so there's nothing to argue with. Risk: the opening gets a nod and a scroll, not a stop. |
| G18 [RISK] | FAIL | Pain: "Start a few weeks late and you squeeze 16 weeks into 12, and race day takes back minutes your training earned."; dream: none ("No dream line") | The pain is arithmetic with no feeling or cruel timing. It's the same shape as the 200 plans pain ("4 months of training comes down to one morning... you find out at 32K"). There's no dream at all, and a new pain plus a dream of what they'll see would pass. Risk: with no picture of the payoff, nothing holds viewers past the hook. |
| G20 [RISK] | FAIL | "[D TIER] Belfast... Start Monday 11 January." then "[C TIER] Rome... Start Monday 23 November." | The stages follow rank, not one clock: the start dates jump from January to November to December to January to December. Each stage is a course description, not a scene they'll live. Risk: the dates bounce around and viewers lose track of which one is theirs. |
| G21 [BLOCK] | FAIL | "Here's all 8, with the date, the Monday your 16 weeks start, and when your longest run lands" (caption) | Each viewer needs one row, one date they can work out themselves, so there's nothing too long to remember and nothing to come back to on race morning (ledger row 18). It isn't for a goal most have either. To pass, the table has to be something they couldn't hold after one watch, such as a plan by goal for their race. |
| G22 [BLOCK] | FAIL | "and race day takes back minutes your training earned." | That a 12-week block costs minutes on race day isn't in FACTS or in the facts table. Cut the claim or source it. I checked every date, start Monday (race day minus 111 days) and longest run (minus 21) against the FACTS table, and they all hold. |
| G23 [BLOCK] | PASS | "Start Monday 23 November." / "start from the week you're in." | It's a calendar date, with no kit, apps or setup step. |
| G24 [RISK] | FAIL | "Start Monday 28 December, Christmas week." / "in January dark or March light." | 28 December is the Monday after Christmas, and plenty of people will hear "Christmas week" as the week of the 25th. "January dark" is a back-to-front phrase that trips when read aloud. "Between Christmas and New Year" and "dark January mornings" would pass. Risk: Manchester runners may take down the wrong week, and the turn line stumbles out loud. |
| G29 [BLOCK] | FAIL | "Send this to the friend you're running it with, so you both start on the same Monday." | This nearly repeats the send line from the last 3 scripts ("Send this to the friend you're running with who's also...", "Send this to whoever you're running your next marathon with"), which is ledger row 16. A send line in new words would pass. There's no double meaning, mockery or staccato. The Humanizer table isn't in the packet, so check.py must confirm it. |
| G31 [BLOCK] | FAIL (needs Luke) | Turn: "Writing spring plans, we found the date matters as much as the course." | This is a general rule, not a moment you can picture, and any runner would nod along to "the date matters". Its follow-up, "longest runs are in January dark", hints at the closing stage's answer. To pass, it needs a moment the viewer lived and didn't believe, one that shows what was wrong without pointing at Seville. |

## Stranger's question (G16)
"Which one has already started, and is it mine?" It's guessable: the February one, Seville, and anyone can count 16 weeks back from their own race date.

## FAILs, in the order to fix them
1. G9 (needs Luke): confirm the premise that the audience has booked, and give a source for "start late", or drop the line.
2. G8: find one aha that no coach's 16-week count gives, from our inbox or comments. Without it the topic doesn't hold, and G5, G21 and G16 fail with it.
3. G31 (needs Luke, the turn is his): a pictured moment the viewer didn't believe, with no hint at the answer the S tier pays.
4. G16: a line-one question that arithmetic and the calendar can't answer, kept shut until S TIER. Cut "January dark" from the turn and stop the rehook from giving the answer away.
5. G21: something they can't hold after one watch, for a goal most have (by goal, per race).
6. G22: cut or source "race day takes back minutes your training earned".
7. G29: a send line in new words.
8. G5: a stake that changes what they do, not a date in the calendar.
9. G7: stages every viewer lives through, plus a dream; cover the inbox's Irish races or say who it's for.
10. G18: a new pain with feeling or cruel timing, plus a dream of what they'll see.
11. G17: a line one they'd argue with.
12. G20: stages on one clock (date order), each a scene.
13. G11 (needs Luke, his OST): add a second of the five, such as a deadline or our method.
14. G24: fix "Christmas week" for 28 December and "January dark or March light".
