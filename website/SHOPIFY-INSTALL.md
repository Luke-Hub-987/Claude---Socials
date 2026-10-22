# Putting the new site live: Shopify and Klaviyo (22 Oct 2026)

About an hour, start to finish. You work on a **copy** of your theme, test it
in preview, then publish. The live site doesn't change until the last step,
and you can switch back in one click.

Everything you need is in `website/shopify/` (the zip has the same files):

| Folder | Files |
|---|---|
| `assets/` | ern.css, ern.js, plan.js, ern-logo.png, ern-carb-bar-pack.webp, rice-texture.webp, bar-closeup.webp, founders.webp |
| `layout/` | ern.liquid |
| `sections/` | ern-home.liquid, ern-bar.liquid |
| `templates/` | index.json, page.the-bar.json |
| `../klaviyo/` | plan-block.html (welcome email), waitlist-email.md |

## A. Make a copy of your theme (2 min)

1. Shopify admin > **Online Store > Themes**.
2. On your current theme, click **⋯ > Duplicate**. When the copy appears
   under "Theme library", click its **⋯ > Rename** and call it `ERN v5`.
3. On `ERN v5`, click **⋯ > Edit code**.

## B. Add the files (15 min)

In the code editor, the folders are down the left.

4. **Assets:** next to the **assets** folder click the upload icon (or
   **Add a new asset > Upload file**). Upload all 8 files from
   `shopify/assets/`, one at a time if it only takes one.
5. **Layout:** click **Add a new layout**, name it `ern`, click Done. Delete
   everything in the new file, paste in all of `shopify/layout/ern.liquid`,
   click **Save**.
6. **Sections:** click **Add a new section**, name it `ern-home`. Delete
   what's there, paste all of `shopify/sections/ern-home.liquid`, **Save**.
   Do the same for `ern-bar` with `ern-bar.liquid`.
7. **Home template:** open **templates > index.json**. Select all, delete,
   paste all of `shopify/templates/index.json`, **Save**. (This only changes
   the copy, not your live site.)
8. **Bar template:** click **Add a new template**, choose **page**, choose
   **JSON**, name it `the-bar`. Delete what's there, paste all of
   `shopify/templates/page.the-bar.json`, **Save**.

If Shopify shows a red error when you save, send me a screenshot of it.

## C. Make the bar page (2 min)

9. Admin > **Online Store > Pages > Add page**.
   - Title: `The Carb Bar`. Leave the content empty.
   - On the right, **Theme template**: `the-bar`.
   - Scroll to **Search engine listing > Edit**: URL handle `the-bar`;
     page title `The ERN Carb Bar | Engine Room Nutrition`; description
     `30g of carbs in a rice crisp square, made in Ireland for race morning.
     Join the waitlist for the first batch.`
   - **Save**.
10. Admin > **Online Store > Preferences**: homepage title
    `Free Marathon Pace Plan | Engine Room Nutrition`; description
    `Pick your goal time and get your free marathon pace plan on screen:
    your time at every 10K sign, your watch pace in km and miles, and when
    to take each gel.` **Save**.

## D. Klaviyo (20 min)

11. **Lists** (Klaviyo > Audience > Lists & segments):
    - Open **Email List > Settings**. Copy the **List ID** (6 characters).
      Check **Opt-in process** is **Single opt-in**. With double opt-in,
      people get a "confirm" email before anything else.
    - **Create new > List**, name `Bar waitlist`, single opt-in. Copy its ID.
    - **Create new > List**, name `Race results`. Copy its ID.
12. **Paste the IDs into the site:** Shopify > Online Store > Themes >
    `ERN v5` > **Customize**.
    - It opens on the Home page. Click the **ERN Home** section on the left
      and paste the three list IDs into the Klaviyo boxes.
    - Under **Photos**, leave "Photo of Luke and Jamie" empty to keep the
      current one, or pick a better one (square, faces visible).
    - Top of the screen: switch from **Home page** to **Pages > the-bar**.
      Click **ERN Bar**, paste the same three IDs. Add up to 4 Rice Crisp
      Graveyard photos if you have them (screenshots from the series work);
      the photo row stays hidden until you add one.
    - **Save** (top right).
13. **Klaviyo on the site:** still in Customize, click the **App embeds**
    icon (left sidebar) and switch **Klaviyo** on. **Save**. This lets
    Klaviyo see the "plan_unlocked" and "waitlist_yes" events.
14. **Switch off the old pop-ups:** Klaviyo > **Sign-up forms**. Set any
    live "Free Endurance Guide" or "early access" form to **Draft**, or it
    will pop up over the new page.
15. **Welcome email with the plan in it:** Klaviyo > **Flows** > your
    welcome flow > **Email 1** > Edit.
    - Add an **HTML** block at the top and paste all of
      `klaviyo/plan-block.html`. It shows each person's plan from their
      profile. Old sign-ups without a plan see "reply with your race and
      goal time" instead.
    - Remove the old "reply with your race and goal time" ask from the rest
      of the email (the plan block covers it). Keep "Reply with any
      question. I read every one."
    - Subject: `Your marathon pace plan for {{ person|lookup:'race'|default:'your race' }}`
    - Preview it with **Preview > a profile** that has a plan (after step 17).
    - **Save.** Keep the email **Live** while you edit; don't switch it to
      Manual.
16. **Waitlist email:** Flows > **Create flow > Build your own**, name
    `Bar waitlist`. Trigger: **Added to list > Bar waitlist**. Add one
    email using `klaviyo/waitlist-email.md`. Smart Sending **off**. Set it
    **Live**.

## E. Test on your phone before going live (10 min)

17. Themes > `ERN v5` > **⋯ > Preview**, then **Share preview** and open
    that link on your phone.
    - Drag to a goal, pick a race, enter your own email, tap **Unlock my
      full plan**. The plan should appear.
    - Klaviyo > **Profiles** > your email: it should be on **Email List**
      with properties `race`, `goal_time`, `plan_10k` and so on. The welcome
      email should arrive with your plan in it.
    - Tap **Yes, add me** under race morning: you should land on **Bar
      waitlist** and get the waitlist email.
    - Fill in "Tell us your time": you should land on **Race results**.
    - Open `/pages/the-bar` in the preview and join the waitlist there too.

## F. Go live (5 min)

18. Themes > `ERN v5` > **Publish**.
19. **Redirects:** Online Store > Navigation > **URL redirects > Create**:
    - `/pages/fuel-1` → `/`
    - `/pages/marathon-nutrition-test-pack` → `/`
    - `/pages/home` → `/`
20. **Bio links:** Instagram `https://engineroomnutrition.com/?utm_source=instagram`,
    TikTok `https://engineroomnutrition.com/?utm_source=tiktok`.
21. Optional but worth it: install **Microsoft Clarity** from the Shopify
    App Store (free). It records how people use the page on their phones.

**To undo:** Online Store > Themes > your old theme > **Publish**.

## Updating the site later

Edit the files in `website/` (index.html, bar.html), run
`python3 website/build_shopify.py`, and paste the rebuilt section file into
the same section in Shopify's code editor. Photos and list IDs live in
Customize, so they never need code changes.
