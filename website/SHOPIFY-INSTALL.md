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
| assets | `ern-logo.png`, `ern-share.jpg`, `ern-carb-bar-pack.webp`, `rice-texture.webp`, `bar-closeup.webp`, `founders.webp`, `proof-chicago-splits.webp` | upload |
| assets | the 6 fonts: `ern-font-barlow-700.woff2`, `ern-font-barlow-800.woff2`, `ern-font-barlow-800-italic.woff2`, `ern-font-dmserif-400.woff2`, `ern-font-dmserif-400-italic.woff2`, `ern-font-inter.woff2` | upload |
| layout | `ern.liquid` | new file, paste |
| sections | `ern-home.liquid`, `ern-bar.liquid` | new file, paste |
| templates | `index.json` | already exists: replace its contents |
| templates | `page.the-bar.json` | new file, paste |

`klaviyo/welcome-email.html` is for Klaviyo
(step 14), not Shopify.

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
   them onto the folder). Add all 16 asset files. Open `assets` and check
   all 16 are there with the right endings.
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

## D. Klaviyo (15 min)

One list for everyone (P146): every form on both pages adds people to
**Email List**. What they signed up for is saved on their profile
(`bar_waitlist`, `result_time`, the plan), and the welcome email's top block
changes to match.

11. Klaviyo > Audience > Lists & segments > **Email List > Settings**. Copy
    the **List ID** (6 characters). Set **Opt-in process** to **Single opt-in**.
12. Online Store > Themes > `ERN final` > **Customize**. The **red bar** at
    the top is expected until the ID is in. Click **ERN Home**, paste the ID
    into **Email List ID**. Top dropdown > Pages > **the-bar** template, click
    **ERN Bar**, paste the same ID. **Save**.
13. Still in Customize: **App embeds** > **Klaviyo** on > **Save**.
14. Welcome flow > **Email 1** > Edit content (the HTML/code editor): select
    all, delete, paste all of `klaviyo/welcome-email.html` (Luke's design;
    the top changes with what the person did: their plan, the bar list, a
    result, or no goal yet). Subject:
    `Your marathon pace plan for {{ person|lookup:'race'|default:'your next marathon' }}`.
    Leave Klaviyo's preview-text box empty (the email has its own). Save,
    leave it Live.
15. Klaviyo **Sign-up forms**: set the old Live forms to Draft **at go-live**,
    not before (the old site still needs them).

## E. Test on your phone (10 min)

17. Online Store > Themes > `ERN v5` > **⋯ > Preview > Share preview** >
    copy the link and open it on your phone.
18. Run through it as a visitor, and check Klaviyo after each one:

| Do this | Check in Klaviyo (Profiles > search your email) |
|---|---|
| Drag to a goal, pick a race, enter your email, tap **Unlock my full plan** | On **Email List**; properties `race`, `goal_time`, `plan_10k` and the rest are filled in; the welcome email arrives with your plan in it |
| Tap **Save to lock screen** | The picture opens; press and hold saves it to Photos |
| Tap **Yes, add me** (race morning) | Property `bar_waitlist` = true |
| Fill in **Ran with our plan? Tell us your time** (new email) | On **Email List** with `result_time`; Email 1 thanks them for the result |
| Join on the bar page (new email; test it in Customize until the page has its template) | On **Email List** with `bar_waitlist`; Email 1 says they're on the bar list |

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

The Problems panel in the code editor (Shopify's theme check) should show 0 for the ERN files. Problems in the old theme's own files don't matter.


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
