"""Real messages from runners, rebuilt to look like the app they came in.

Word for word from Luke's screenshots (23 Oct; Dublin results added 28 Oct). Names changed for privacy,
as Luke asked; the page says so. No surnames, handles, photos or email
addresses. Luke's own replies are included where they were in the thread.
build_shopify.py writes these into index.html between the messages markers.
"""
from html import escape

THREADS = [
    {"app": "tiktok", "name": "Tom", "big": "3:19:25", "tag": "Chicago Marathon · aimed for sub-3:30",
     "items": [("img", "assets/proof-chicago-splits.webp", "Chicago Marathon splits, finish 3:19:25"),
               ("in", "Mate!!!"), ("in", "3:19:25!!"),
               ("in", "Thankyou mate - did as you said and we got it done 🤝"),
               ("in", "Was dead around 38k but we powered on 🤣")]},
    # Dublin Marathon results, 25 Oct (Luke's screenshots, 28 Oct). Names changed; words untouched.
    {"app": "gmail", "name": "Brian", "big": "3:28:48", "tag": "Dublin Marathon · first marathon", "subject": "My marathon time - Dublin Marathon",
     "thread": [], "date": "11:48",
     "body": ["Hi Luke,", "Race: Dublin Marathon", "Finish time: 3:28:48 - First Marathon",
              "How the plan went: The plan you gave me regarding pacing (where and when to push), milestone times and the gels worked out really well. I felt in control throughout and was able to push after heartbreak hill with my 3rd fastest 5k pace.",
              "Thank you so much for the advice and guidance it really made a massive difference for me on the day."]},
    {"app": "instagram", "name": "Fergal", "big": "3:36", "tag": "Dublin Marathon · aimed for 3:38",
     "items": [("in", "Goal time is sub 3.40... in a perfect world 3.38. I use the precise gels, jelly babies and squares bar during the race.. And i did Sydney maro last year and my time was 3.52"),
               ("out", "That’s with you now Fergal - all the best for the day!"),
               ("in", "Ok perfect thank so much Luke, really appreciate it 🙏", "❤️"),
               ("time", "11:45"),
               ("in", "Hi Luke !! I just wanted to say a massive thank you for the plan you emailed me before Dublin Marathon. I followed your pacing plan and fueling protocol. I was hoping for a sub 3.40 (3.38 was my goal).. I got my PB and finished at 3.36 so I was buzzin. Thanks again for the plan, it really helped!!", "❤️")]},
    {"app": "instagram", "name": "Declan", "big": "−4 min", "tag": "Dublin Marathon · 3:35 PB",
     "items": [("time", "10:04"),
               ("in", "Thanks a million for all the amazingly helpful and super insightful videos ahead of Dublin - superb content! Your wind advice and sub 3.30 pacing guide got me a 4mins PB (3.35). Keep up the good work 🙌")]},
    {"app": "gmail", "name": "Clare", "big": "3:36", "tag": "Dublin Marathon · from a 1:40 half", "subject": "My marathon plan",
     "thread": [("Clare", "20 Oct", "Race and date:Dublin Marathon Goal ti..."),
                ("me", "21 Oct", "Hey Clare, A 1:40 half marathon is a...")],
     "date": "11:45",
     "body": ["Hi Luke", "I stuck to your pacing plan in Dublin on sunday. Got my PB 3.36- 10mins faster than what i thought i would get. Your adive was amazing.  Thank you so mucj"]},
    {"app": "instagram", "name": "Emma", "big": "3:59:35", "tag": "Dublin Marathon · first marathon",
     "items": [("sys", "Replied to your story: “DM your results to be added”"),
               ("in", "Thanks so much for all the marathon info and marathon split times. Despite the conditions, managed 3:59:35 fpr my first marathon. Thanks a million, Emma")]},
    {"app": "instagram", "name": "Ronan", "big": "3:59", "tag": "Dublin Marathon · PB",
     "items": [("sys", "Replied to your story: “Send us your Dublin Marathon time and if the videos helped!”"),
               ("in", "3:59 PB! I’m running a marathon today and I feel good on repeat from 0-40k. 40k to finish I don’t think I could even remember the words 😂 great tips!")]},
    {"app": "gmail", "name": "Kevin", "big": "", "tag": "Dublin Marathon · 4:20 plan", "subject": "My marathon plan",
     "thread": [("Kevin", "18 Oct", "Race and date: Dublin Marathon 25/10/..."),
                ("me", "19 Oct", "Hey Kevin, Targeting a 4:20 finish fo...")],
     "date": "20 Oct",
     "body": ["Luke,", "Thank you so much for this guide, you should be <mark>charging</mark> for such valuable information!",
              "I will continue to support you on the social media platforms and try some of your products in the future.",
              "Thanks again."]},
    {"app": "instagram", "name": "Ciara", "big": "−12 min", "tag": "Chip time 3:23:58",
     "items": [("link", "sporthive.com", "Chip time 03:23:58 · Pace 04:50 min/km"),
               ("in", "‼️"), ("in", "12 minute pb ❤️")]},
    {"app": "gmail", "name": "Mark", "big": "", "tag": "Dublin Marathon · from a 1:29:30 half", "subject": "My marathon plan",
     "thread": [("Mark", "20 Oct", "Race and date: Dublin Marathon, 25th..."),
                ("me", "21 Oct", "Hey Mark, A 1:29:30 half marathon is a...")],
     "date": "22 Oct",
     "body": ["Hi Luke,", "Thank you getting back to me. This is really helpful. I should be able to program those target pace zones in to my garmin watch.",
              "I'll follow the plan and the fueling protocol. If you're running Sunday or another marathon later in the year best of luck to you!",
              "Mark"]},
    {"app": "instagram", "name": "Sean", "big": "3h 28m", "tag": "Antwerp Marathon · goal time hit",
     "items": [("link", "Strava", "Antwerp Marathon · 42.23 km · 3h 28m"),
               ("in", "Hey Luke hope things are well man! Just wanted to let you know that I ... got the time I was looking for."),
               ("in", "Not to cringe it up or anything but it was one [of] the best days of my life 😂")]},
    {"app": "tiktok", "name": "Orla", "big": "", "tag": "Plan sent the day before",
     "items": [("time", "Yesterday 8:55 am"), ("out", "Should be with you now Orla!"), ("seen", "Seen"),
               ("in", "Thank you SO much. I have it! Just in work so will read later. Really appreciate it sooooo much!", "❤️")]},
    {"app": "gmail", "name": "Eoin", "big": "", "tag": "Dublin Marathon · from a 1:18 half", "subject": "RACE WEEK: My marathon plan",
     "thread": [("Eoin", "22 Oct", "Race and date: Sunday 25th Dublin Ma..."),
                ("me", "22 Oct", "Hey Eoin, A 1:18 half and a 2:52 in Cor...")],
     "date": "22 Oct",
     "body": ["This is great, thank you so much!", "Kind regards", "Eoin"],
     "reply": "No worries at all, Eoin. Go get it done on Sunday!"},
    {"app": "instagram", "name": "Niamh", "big": "", "tag": "Dublin Marathon",
     "items": [("sys", "Replied to your story: “Marathon questions for Dublin and giving free personalised pace plans”"),
               ("in", "Just wanted to say thanks, your videos have helped"),
               ("out", "Unreal Niamh - give it socks on the day!"), ("seen", "Seen")]},
    {"app": "tiktok", "name": "Sarah", "big": "", "tag": "3:40 plan",
     "items": [("time", "Monday 9:17 pm"), ("out", "Should be with you now Sarah!"), ("seen", "Seen"),
               ("time", "Monday 10:14 pm"), ("in", "Perfect thank you I’ll have a wee look"),
               ("time", "Monday 10:20 pm"), ("in", "That’s so good much appreciated Luke", "❤️")]},
    {"app": "gmail", "name": "Ben", "big": "", "tag": "Jervis Bay, Australia", "subject": "My marathon plan",
     "thread": [("Ben", "22 Oct", "Race and date: Husskerson, Jervis Bay..."),
                ("me", "22 Oct", "Hey Ben, Great to hear from you lad!...")],
     "date": "22 Oct",
     "body": ["Thank you Luke!!", "Keep up the videos, enjoying them all 🫡"], "react": "🙌 1"},
    {"app": "gmail", "name": "Darragh", "big": "", "tag": "Race week", "subject": "My marathon plan",
     "thread": [("Darragh", "17 Oct", "Race week!! Hi lads, Thanks a mil for t..."),
                ("me", "22 Oct", "Hey Darragh - Yeah your logic makes com...")],
     "date": "22 Oct",
     "body": ["This is great, thanks so much for the advice Luke!"]},
    {"app": "gmail", "name": "Shane", "big": "", "tag": "Dublin Marathon · 3:22 plan", "subject": "My marathon plan",
     "thread": [("Shane", "18 Oct", "Race and date: Dublin Marathon 25 Oc..."),
                ("me", "19 Oct", "Hey Shane Targeting a 3:22 finish lad at...")],
     "date": "23 Oct",
     "body": ["Thank you, Luke - great guidance!", "Sent from my iPhone"]},
]

# Gmail-style avatar colours, by first letter
COLOURS = ["#1A73E8", "#188038", "#E8710A", "#D93025", "#9334E6", "#12B5CB", "#C5221F", "#0B8043"]


def colour(name):
    return COLOURS[sum(map(ord, name)) % len(COLOURS)]


def esc(t):
    # keep the <mark> highlight from the real screenshot, escape the rest
    return escape(t).replace('&lt;mark&gt;', '<mark>').replace('&lt;/mark&gt;', '</mark>')


def header(t):
    big = '<b>%s</b>' % escape(t["big"]) if t["big"] else ''
    return '<div class="ph-tag">%s<span>%s</span></div>' % (big, escape(t["tag"]))


def gmail(t):
    n = t["name"]
    rows = ''.join(
        '<div class="g-row"><i class="g-av" style="background:%s">%s</i><div><div class="g-l"><b>%s</b><span>%s</span></div><p>%s</p></div></div>'
        % ('#3C4043' if who == 'me' else '#5F6368', 'L' if who == 'me' else escape(who[0]), escape(who), d, escape(snip))
        for who, d, snip in t["thread"])
    body = ''.join('<p>%s</p>' % esc(p) for p in t["body"])
    react = '<div class="g-react">%s</div>' % t["react"] if t.get("react") else ''
    reply = ('<div class="g-msg g-me"><div class="g-h"><i class="g-av" style="background:#3C4043">L</i><div><b>me</b><small>to %s</small></div></div>'
             '<div class="g-body"><p>%s</p></div></div>' % (escape(n), escape(t["reply"]))) if t.get("reply") else ''
    return ('<div class="phone2 ph-gmail" data-app="gmail">%s<div class="screen">'
            '<div class="g-top"><span>‹</span><span class="g-icons">⇩ 🗑 ✉ ⋯</span></div>'
            '<div class="g-subj">%s <em>External</em><em class="b">Inbox</em></div>%s'
            '<div class="g-msg"><div class="g-h"><i class="g-av" style="background:%s">%s</i><div><b>%s <span>%s</span></b><small>to me ⌄</small></div><span class="g-acts">☺ ↩ ⋯</span></div>'
            '<div class="g-body">%s</div>%s</div>%s'
            '<div class="g-btns"><span>↩</span><span>Reply all</span><span>Forward</span></div></div></div>'
            % (header(t), escape(t["subject"]), rows, colour(n), escape(n[0]), escape(n), t["date"], body, react, reply))


def chat(t, app):
    n = t["name"]
    out = []
    for it in t["items"]:
        k = it[0]
        if k == 'time':
            out.append('<div class="c-time">%s</div>' % escape(it[1]))
        elif k == 'sys':
            out.append('<div class="c-sys">%s</div>' % escape(it[1]))
        elif k == 'seen':
            out.append('<div class="c-seen">%s</div>' % escape(it[1]))
        elif k == 'img':
            out.append('<div class="c-in"><img class="c-img" src="%s" alt="%s" loading="lazy" width="478" height="842"></div>' % (it[1], escape(it[2])))
        elif k == 'link':
            out.append('<div class="c-in"><div class="c-link"><small>%s</small><b>%s</b></div></div>' % (escape(it[1]), escape(it[2])))
        elif k == 'in':
            heart = '<i class="c-heart">%s</i>' % it[2] if len(it) > 2 else ''
            out.append('<div class="c-in"><span class="c-av" style="background:%s">%s</span><p class="c-b">%s%s</p></div>' % (colour(n), escape(n[0]), escape(it[1]), heart))
        elif k == 'out':
            out.append('<div class="c-out"><p class="c-b">%s</p></div>' % escape(it[1]))
    head = ('<div class="c-head"><span class="c-back">‹</span><span class="c-av big" style="background:%s">%s</span><b>%s</b><span class="c-icons">%s</span></div>'
            % (colour(n), escape(n[0]), escape(n), '☏ ⋯' if app == 'tiktok' else '☏ ▭'))
    foot = ('<div class="c-foot"><span>%s</span><em>Message...</em></div>' % ('📷' if app == 'tiktok' else '◉'))
    return ('<div class="phone2 ph-%s" data-app="%s">%s<div class="screen">%s<div class="c-body">%s</div>%s</div></div>'
            % (app, app, header(t), head, ''.join(out), foot))


def render_all():
    html = []
    for t in THREADS:
        html.append(gmail(t) if t["app"] == 'gmail' else chat(t, t["app"]))
    return '\n'.join('      ' + h for h in html) + '\n'


def counts():
    c = {"gmail": 0, "tiktok": 0, "instagram": 0}
    for t in THREADS:
        c[t["app"]] += 1
    return c
