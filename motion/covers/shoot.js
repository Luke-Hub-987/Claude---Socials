// Renders cover variants (1080 x 1920) plus a grid-tile check of each.
// Usage: node motion/covers/shoot.js <page.html> <out dir> <variant...>
const path = require('path');
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const [page, out, ...variants] = process.argv.slice(2);
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('pageerror', e => console.log('ERR', e.message));
  for (const v of variants) {
    await p.goto('file://' + path.resolve(page) + '?v=' + v);
    await p.evaluate(() => Promise.all(['700 40px Barlow', '600 40px Barlow', '800 40px "Barlow Condensed"', '700 40px Caveat'].map(f => document.fonts.load(f))));
    await p.evaluate(() => document.fonts.ready);
    await p.waitForFunction(() => [...document.images].every(i => i.complete && i.naturalWidth > 0));
    const f = path.join(out, `${path.basename(page, '.html')}-cover-${v}.png`);
    await p.screenshot({ path: f }); console.log('saved', f);
  }
  await b.close();
})();
