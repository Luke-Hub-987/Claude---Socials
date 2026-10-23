# Putting the new site live: Shopify and Klaviyo (v2 of this guide, 22 Oct 2026)

About an hour. You build everything on a **copy** of your theme, test it on
your phone, then publish. Nothing changes on the live site until step 21,
and you can undo it in one click.

**Start clean:** delete the half-finished `ERN v5` copy (Online Store >
Themes > ERN v5 > ⋯ > Remove) and follow this from step 1.

## The files (in the zip, same folders as your theme)

Every file name below is exact, **including the ending** (`.liquid`,
`.json`, `.css`, `.js`, `.webp`, `.png`, `.jpg`). In Shopify's code editor a
file created without its ending turns red, shows "Plain Text" at the
bottom, and won't work.

| Theme folder | File | How it goes in |
|---|---|---|
| assets | `ern.css`, `ern.js`, `plan.js` | upload |
| assets | `ern-logo.png`, `ern-share.jpg`, `ern-carb-bar-pack.webp`, `rice-texture.webp`, `bar-closeup.webp`, `founders.webp` | upload |
| layout | `ern.liquid` | new file, paste |
| sections | `ern-home.liquid`, `ern-bar.liquid` | new file, paste |
| templates | `index.json` | already exists: replace its contents |
| templates | `page.the-bar.json` | new file, paste |

`klaviyo/plan-block.html` and `klaviyo/waitlist-email.md` are for Klaviyo
(steps 15 and 16), not Shopify.

**Order matters:** assets, then layout, then sections, then templates. A
template that points at a layout or section that doesn't exist yet won't
save.

## A. Copy the theme (2 min)

1. Admin > **Online Store > Themes**. On your live theme, **⋯ > Duplicate**.
2. On the copy, **⋯ > Rename** to `ERN v5`.
3. On `ERN v5`, **⋯ > Edit code**. Check the title bar says `ERN v5`, not
   your live theme.

## B. Add the files (15 min)

4. **Assets:** right-click the **assets** folder > **Upload files** (or drag
   them onto the folder). Add all 9 asset files. Open `assets` and check
   all 9 are there with the right endings.
5. **Layout:** right-click **layout** > **New file** > type `ern.liquid` >
   Enter. Paste all of `layout/ern.liquid` from the zip. **Save**
   (Ctrl+S). The bottom bar should say **Liquid**, and nothing should be red.
6. **Sections:** right-click **sections** > **New file** > `ern-home.liquid`,
   paste `sections/ern-home.liquid`, **Save**. Again for `ern-bar.liquid`.
7. **Home template:** open the existing **templates > index.json**. Select
   all (Ctrl+A), delete, paste all of `templates/index.json`, **Save**.
8. **Bar template:** right-click **templates** > **New file** >
   `page.the-bar.json`, paste `templates/page.the-bar.json`, **Save**.

If any file goes red or shows an error when you save, stop and send me a
screenshot of it.

## C. The bar page and page titles (3 min)

9. Admin > **Online Store > Pages > Add page**.
   - Title `The Carb Bar`. Leave the content box empty.
   - Right side, **Theme template**: `the-bar`. (It only appears once step
     8 is saved.)
   - **Search engine listing > Edit:** URL handle `the-bar`; page title
     `The ERN Carb Bar | Engine Room Nutrition`; description `30g of carbs
     in a rice crisp square, made in Ireland for race morning. Join the
     waitlist for the first batch.`
   - Visibility **Visible**. **Save**.
10. Admin > **Online Store > Preferences:** homepage title `Free Marathon
    Pace Plan | Engine Room Nutrition`; description `Drag to your goal time
    and get your free marathon pace plan on screen: your time at every 10K
    sign, your watch pace in km and miles, and when to take each gel.`
    **Save**.

## D. Klaviyo (20 min)

11. **Three lists** (Klaviyo > Audience > Lists & segments):
    - Open **Email List > Settings**. Copy the **List ID** (6 characters).
      Set **Opt-in process** to **Single opt-in**. With double opt-in,
      people get a "confirm your email" message first and the plan email
      waits until they click it.
    - **Create new > List**: `Bar waitlist`. Single opt-in. Copy its ID.
    - **Create new > List**: `Race results`. Copy its ID.
12. **Paste the IDs into the site:** Online Store > Themes > `ERN v5` >
    **Customize**.
    - It opens on the Home page. Until the IDs are in, you'll see a **red
      bar** across the top saying the forms won't save. That's on purpose,
      and only you can see it.
    - Click the **ERN Home** section (left). Paste the three IDs into the
      three Klaviyo boxes. The red bar disappears.
    - **Photos > Photo of Luke and Jamie:** leave empty to keep the current
      one, or pick a better one (square, both faces visible).
    - Top dropdown: **Home page > Pages > the-bar**. Click **ERN Bar**, paste
      the same three IDs. Add up to 4 Rice Crisp Graveyard photos (phone
      screenshots of the series work). The photo row stays hidden until you
      add one.
    - **Save** (top right).
13. **Klaviyo on the site:** still in Customize, click the **App embeds**
    icon (left edge, looks like a puzzle piece or blocks). Switch **Klaviyo**
    on. **Save**.
14. **Old pop-ups off:** Klaviyo > **Sign-up forms**. Any form that's
    **Live** (the "Free Endurance Guide" or "early access" ones): set to
    **Draft**. Otherwise they'll pop up over the new page.
15. **Welcome email with the plan in it:** Klaviyo > **Flows** > your
    welcome flow > **Email 1** > **Edit content**.
    - Drag an **HTML** block to the very top and paste all of
      `klaviyo/plan-block.html`. It shows each person's 4 times, paces and
      gels from their profile. People who signed up before today see
      "reply with your race and goal time" instead.
    - Delete the old "reply with your race and goal time" ask from the rest
      of the email. Keep "Reply with any question. I read every one."
    - **Subject:** `Your marathon pace plan for {{ person|lookup:'race'|default:'your race' }}`
    - **Save.** Leave the email **Live** while you edit it (don't switch it
      to Manual, or sign-ups queue up and arrive hours late).
16. **Waitlist email:** Klaviyo > **Flows > Create flow > Build your own**,
    name `Bar waitlist`. Trigger: **Added to list > Bar waitlist**. Add an
    email with the copy in `klaviyo/waitlist-email.md`. Turn **Smart
    Sending off**. Set the flow **Live**.

## E. Test on your phone (10 min)

17. Online Store > Themes > `ERN v5` > **⋯ > Preview > Share preview** >
    copy the link and open it on your phone.
18. Run through it as a visitor, and check Klaviyo after each one:

| Do this | Check in Klaviyo (Profiles > search your email) |
|---|---|
| Drag to a goal, pick a race, enter your email, tap **Unlock my full plan** | On **Email List**; properties `race`, `goal_time`, `plan_10k` and the rest are filled in; the welcome email arrives with your plan in it |
| Tap **Save to lock screen** | The picture opens; press and hold saves it to Photos |
| Tap **Yes, add me** (race morning) | On **Bar waitlist**; the waitlist email arrives |
| Fill in **Ran with our plan? Tell us your time** | On **Race results** with `result_time` |
| Open `/pages/the-bar` in the preview and join | On **Bar waitlist** |

If the plan shows on screen but nothing lands in Klaviyo, the list IDs
aren't saved (step 12).

## F. Go live (5 min)

19. **Hide the old pages first.** Shopify only redirects a page that no
    longer exists, so while `/pages/fuel-1` is still live, a redirect from
    it is ignored. Online Store > **Pages**: open `fuel-1`, the test pack
    page and `home` (if it exists) one at a time and set **Visibility >
    Hidden**. **Save**. Don't delete them, so you can bring them back.
20. **Redirects:** Online Store > **Navigation > URL redirects > Create**:
    - `/pages/fuel-1` → `/`
    - `/pages/marathon-nutrition-test-pack` → `/`
    - `/pages/home` → `/`
21. Online Store > Themes > `ERN v5` > **Publish**.
22. Open `engineroomnutrition.com` on your phone and do one real sign-up.
23. **Bio links:** Instagram `https://engineroomnutrition.com/?utm_source=instagram`
    and TikTok `https://engineroomnutrition.com/?utm_source=tiktok`.
24. **Clarity:** install **Microsoft Clarity** from the Shopify App Store
    (free), then switch it on under Customize > App embeds.

**To undo:** Online Store > Themes > your old theme > **Publish**, and set
the old pages back to Visible.

## If something goes wrong

| What you see | Fix |
|---|---|
| A file is red or says "Plain Text" | It was created without its ending. Delete it, create it again as `name.liquid` or `name.json`, paste again |
| "Section type 'ern-home' does not refer to an existing section file" when saving `index.json` | Save `sections/ern-home.liquid` first (step 6), then `index.json` |
| "Layout 'ern' does not exist" | Save `layout/ern.liquid` first (step 5) |
| `the-bar` isn't in the Theme template list | Save `templates/page.the-bar.json` (step 8), refresh the page |
| Page has no styling | `ern.css` isn't in assets (step 4) |
| Photos or the logo don't show | Asset missing or misspelled: compare names with the table above |
| Red bar in Customize | Klaviyo list IDs missing (step 12) |
| An old pop-up appears over the page | Klaviyo sign-up form still Live (step 14) |
| A redirect does nothing | The old page is still Visible (step 19) |
| A Shopify upload rejects the `.webp` files | Send me a screenshot and I'll switch the images to `.jpg` |

## Updating the site later

The files in `website/` (index.html, bar.html) are the source. Change them,
run `python3 website/build_shopify.py`, and paste the rebuilt section file
over the old one in the code editor. Photos and list IDs live in Customize
and don't need code changes.
