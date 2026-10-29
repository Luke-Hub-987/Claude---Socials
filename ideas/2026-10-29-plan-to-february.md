---
type: action plan (Luke, 29 Oct: "Is this the right direction overall, diversifying? I need clear specific tasks and deadlines, reels to post and trial, and website edits for testing") + LLM Council (P150)
generated_at: 2026-10-29
basis: the live site (engineroomnutrition.com and /pages/the-bar, read 29 Oct), PLAN-brand-and-business.md, the welcome flow, team sports, dressing-room plan, why our bar, the week plan (27 Oct), P72, P150, P156, P163, P164
owners: L = Luke, J = Jamie, C = Claude (in this repo), E = the email project, D = whoever built the site
status: v1. Dates are targets; when one slips, the ones after it move, not the gates
---

# The plan to the end of February

## 1. Is diversifying the right direction?

**As a sequence, yes. As "diversify now", no.**

- **Launch on the marathon, in January.** It's the only market where you
  have an audience (1M views in a month), a list (591), a working plan
  builder, a waitlist and a bar page. The spring training blocks start in
  January, and "nothing new on race day" means that's when runners pick
  what they'll eat for the next 16 weeks.
- **Team sport is a test alongside it, about a fifth of your time,** GAA
  only, through trial reels and one squad. Decide at the end of February.
- **Two things I'd correct in our own reasoning:**
  1. **"Year-round revenue" is a weaker argument than it looks.** Marathon
     training runs January to April and June to October. GAA runs roughly
     January to October (check the fixtures calendar). **They overlap; GAA
     doesn't fill the gap** (November and December, and a bit of May).
     Winter rugby and soccer would, but they're the hardest to own. **The
     real reason for team sport is that players eat it every week**, not
     the calendar.
  2. **Don't let "two halves" delay the launch.** Ask the food scientist
     what it costs in time and money. **If it pushes the first batch past
     January, launch the single bar and make halves version two.**

## 2. What the site already does (read 29 Oct)

It's further on than our plans assumed:
- **The builder is the sign-up.** Goal clock, a race dropdown (Dublin,
  Frankfurt, New York, Valencia, Seville, Barcelona, Paris, London,
  Manchester, Belfast, Cork, Other) and an email field unlock the plan.
- **A pace band to print** and a lock-screen save already exist. The
  pace-band test from the business plan is running; it just isn't counted.
- **A results form** (race, finish time, PB, email, consent) already
  exists. That's the "how did it go" email's landing page.
- **A waitlist** (yes or no) and a bar page: 30g of carbs, about 40g,
  under 1g of fat, protein and fibre, 8 ingredients (crisped rice, honey,
  maple syrup, sugar, coconut oil, beef gelatine, sea salt, vanilla), not
  vegetarian, salt figure not yet given, "coming soon", a founding price
  for the waitlist. Its comparison table already covers the banana,
  porridge and the gel, including "survives a squashed kit bag".
- **The proof bar says "100+ free pace plans sent"**, which is out of date
  (591 profiles).
- It looks like Shopify (from the page addresses). I haven't seen the
  theme code or the admin, so the edits below are written for whoever
  built it.

## 3. Website edits (for testing)

| # | Edit | Why | Owner | By |
|---|---|---|---|---|
| W1 | **On "Unlock my free plan", send race_name, race_date and goal_time to Klaviyo** (map each dropdown race to its date; for "Other", show an optional date box only when "Other" is picked) | Starts the race countdown emails (Flow 2); nobody else gets an extra step | D | 9 Nov |
| W2 | **Count the clicks on "print a pace band" and "save to lock screen"** (a Klaviyo event or a Shopify analytics event) | The pace-band test, measured | D | 9 Nov |
| W3 | **Update the proof bar** to the real number of plans sent (check Klaviyo; about 500+) | It undersells you by five times | L | 2 Nov |
| W4 | **Results form: one optional question,** "What did you eat in the 30 minutes before the start?" | Free product research from every result | D | 13 Nov |
| W5 | **Bar page comparison table: add "a supermarket rice crisp square" and "a sports drink" as columns**, with honest pack numbers (generic names, no brands) | The Outsider's question, answered where they decide | L | 13 Nov |
| W6 | **Bar page: add the salt figure** once the food scientist gives it | The spec on the front, complete | L | when known |
| W7 | **A test page, /pages/match-day:** kick-off time in, a schedule out (the meal before, the last 30 minutes, half-time, after); email optional. Not linked from the menu: only from the GAA trial reels | The GAA test needs somewhere to send people | D, numbers from C | 27 Nov |
| W8 | **A founding pre-order page,** built but hidden: the price, a refundable deposit, the batch size | Ready to switch on the day the price is set | D | 11 Dec |
| W9 | **"Two halves" stays off the site** until the food scientist confirms it | No promises the bar can't keep | L | — |

## 4. Reels to post and trial

**The main grid stays marathon** (P72). Three a week while the business
tasks are heavy, back to four once the price is set (P156). The weekly
reach reel gets two trial reels (P156). Every one gets a brief first
(P138), with "If you've got a marathon coming up" as the gate (P153).
**GAA reels are trial reels only** until they beat the marathon reels (P163).

| Date | Reel | Type | Status |
|---|---|---|---|
| Fri 30 Oct | HOW TO PACE THE NEW YORK / MARATHON, SECTION BY SECTION | Course breakdown | Script ready |
| Sat 31 Oct | WHAT WE DID AT EVERY 10K / OF THE DUBLIN MARATHON | From the podcast | Brief after the recording |
| Mon 2 Nov | HOW TO PACE A 5:00 MARATHON / AT EVERY 10K | Goal time (emails) | Brief Fri 30 |
| Wed 4 Nov | A wall-family reel, trial reels A and B the evening before | Reach, skip under 32% | Brief Mon 2 |
| Fri 6 Nov | WHAT TO DO ON THE MORNING / OF A MARATHON (the queue's #5; the bar's slot, said honestly) | Countdown (saves) | Brief Wed 4 |
| Mon 9 Nov | WHAT YOUR LAST MARATHON SAYS / ABOUT YOUR NEXT ONE, re-cut: one big thing in frame one, the standard gate | Trial reel only | Script exists; re-cut the opening |
| Wed 11 Nov | Reach reel, trial reels A and B | Reach | Brief Mon 9 |
| **Thu 12 Nov** | **GAA trial 1: WHERE THE LAST 10 MINUTES / OF A MATCH ARE ACTUALLY LOST** | Trial reel only | Brief Tue 10, after the GAA facts |
| Fri 13 Nov | HOW TO PACE THE VALENCIA / MARATHON, SECTION BY SECTION (check the date; 2 to 4 weeks before) | Course breakdown | Reuse the New York tools |
| Mon 16 Nov | Goal time or a podcast clip (picked from the data) | Emails | Brief Fri 13 |
| Wed 18 Nov | Reach reel, trial reels A and B | Reach | |
| **Thu 19 Nov** | **GAA trial 2: WHAT TO EAT ON MATCH DAY, / HOUR BY HOUR** | Trial reel only | Links to /pages/match-day once it's live |
| Fri 20 Nov | HOW TO PACE A MARATHON / IN THE WIND (once the science is vetted) | Race-pace decision | Needs Luke's science |
| **Thu 26 Nov** | **GAA trial 3: WHAT TO DO AT HALF-TIME / WHEN YOUR LEGS ARE GONE** | Trial reel only | |

**One question before any GAA reel: who's the face?** If neither of you
plays GAA, say so and speak as the runners who fuel for a living, or film
with a player who does (P23: no claims you haven't made).

## 5. Business tasks, week by week

### Week of 2 Nov
| Task | Owner | Done when |
|---|---|---|
| Send the food scientist the brief (`why-our-bar.md` section 4): two halves (time and cost), the salt figure, gluten in the crisped rice, and whether a non-beef gelatine is possible (vegetarian and halal buyers) | J | Sent Mon 2 |
| Buy a supermarket rice crisp square, a sports drink, 2 gels and a flapjack; build a price-per-30g-carbs table against ours | L and J | Table done Wed 4 |
| Trademark search and filing, EUIPO and UKIPO, classes 29 and 30 | L | Filed Fri 6 |
| Quotes requested: 3 co-packers and the Bia Innovator Campus in Athenry (MOQ, cost, lead time) | J | Emails out Wed 4 |
| Paste the prompt into the email project; Step 0 to D | L | Thu 5 |
| Message 3 club players: what did they eat before their last match and at half-time? | J | Fri 6 |
| Draft the GAA match-day facts (the same checks as FACTS.md) | C | Fri 6, for L's yes |

### Week of 9 Nov
| Task | Owner | Done when |
|---|---|---|
| W1 and W2 live; test with your own profile | D | Mon 9 |
| Book 20 calls: 10 runners from the list, 10 GAA players | L 10, J 10 | Booked Wed 11 |
| Food business registration and label rules: call the FSAI and the local environmental health officer (for the Athenry kitchen) | J | Fri 13 |
| Product liability insurance: 2 quotes | L | Fri 13 |
| W4 and W5 live | D, L | Fri 13 |

### Week of 16 Nov
| Task | Owner | Done when |
|---|---|---|
| All 20 calls done; one line per call on what they eat now, when, and what they paid | L and J | Fri 20 |
| Welcome flows live (both tracks) | E, L | Fri 20 |
| LEO Sligo meeting booked; the next Food Academy intake checked | L | Fri 20 |
| Read the first 2 GAA trial reels against the marathon reels (skip, watch, sends) | C | Thu 26 |

### Week of 23 Nov
| Task | Owner | Done when |
|---|---|---|
| Quotes in; fill the cost model (PLAN-brand-and-business section 6) | L | Wed 25 |
| **Set the price** (the per-use price close to the sports drink they buy now) | L and J | **Fri 27** |
| W7 (/pages/match-day) live | D | Fri 27 |

### December
| Task | Owner | Done when |
|---|---|---|
| W8 (founding pre-order page) built, hidden | D | 11 Dec |
| Logo and pack final, the spec on the front | L and J | 18 Dec |
| GS1 barcodes; shelf-life test started | J | 18 Dec |
| **Samples: 50 runners from the list and 1 GAA squad** (3 questions after each run or match) | L and J | As soon as samples exist; target mid-December |

### January
| Task | Owner | Done when |
|---|---|---|
| **Gate 1 check** (PLAN-brand-and-business section 8): cost known, 50 have tried it, at least 60% would reorder at the price | L and J | Fri 8 Jan |
| If Gate 1 passes: **open the founding pre-order** to the waitlist, timed to the spring blocks | L | Mon 11 Jan |
| GAA: 2 more trial reels for club pre-season; the squad test across 3 or 4 matches | L, J | Through January |

### End of February
| Decision | On what |
|---|---|
| **GAA: go or stop** | The table in `team-sports.md` section 7: coaches and players who'd buy, match-day page use per 1,000 views, trial reel rates, the squad's swap answers |
| **Gate 2 progress** | Pre-orders against the first batch; early reorders |

## 6. Every Monday: one table (C reads it in the review)

| Number | Where from |
|---|---|
| Sign-ups that week, and on post days against no-post days (P154) | Klaviyo |
| Waitlist share of active profiles | Klaviyo or Shopify |
| Plans built, pace bands printed | W1, W2 |
| Results forms sent | The site |
| Each reel's skip, watch, sends and saves | Instagram, TikTok |
| Tasks done against this plan | This file |

## 7. LLM Council (P150): is diversifying the right direction?

- **Contrarian:** Diversifying before you've sold one bar is the classic
  way a small brand stalls. GAA has no audience, possibly no face you can
  claim, and no facts file. Changing the recipe for two halves could cost
  the January launch, which is worth more than any format.
- **Assumption-ripper:** "Year-round revenue" assumes there's revenue to
  smooth; there isn't yet. It also assumes GAA fills the marathon's gap;
  it mostly overlaps it. The real gain is how often a player eats it. And
  our plans assumed the site needed building; most of it exists.
- **Expansionist:** The site already has the pace band, the results form
  and a comparison table: three tests that only need counting. The
  match-day page reuses the same builder idea. Team sport is where weekly
  buying happens.
- **Outsider:** "On Instagram you're a running page. If you start posting
  GAA, what are you?"
- **Executor:** Monday morning: send the food scientist the brief, buy
  the competitors for the price table, update the proof bar, file the
  trademark, request the four quotes, and paste the email prompt.

**Blind cross-review:**
- The Outsider's question is answered by keeping GAA in trial reels and
  on an unlinked page until it earns a place.
- The Contrarian's launch point wins: halves only if they don't delay
  January.
- The Assumption-ripper's calendar point changes the reason, not the
  test: GAA is about weekly use, not seasons.
- The Expansionist's point becomes W2, W4 and W5: count what the site
  already does before building anything new.

**Chairman's verdict:** **Launch on the marathon in January; test GAA at
a fifth of your time; decide at the end of February.** Don't trade the
January launch for the two halves. Count what the site already does (the
pace band, the waitlist, the results form) before building anything new.
Follow the dates above; when one slips, move the ones after it, never the
gates.
