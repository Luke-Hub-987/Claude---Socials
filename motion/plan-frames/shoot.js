// Screenshots each frame of a plan-frames page to a 1920 x 1080 PNG.
// Usage: node motion/plan-frames/shoot.js <page.html> <out dir> <name prefix> <frame names, in order...>
const path = require('path');
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const [page, out, prefix, ...names] = process.argv.slice(2);
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto('file://' + path.resolve(page));
  await p.evaluate(() => Promise.all(['800 30px Barlow', '700 30px Barlow', '60px "DM Serif Display"', 'italic 60px "DM Serif Display"'].map(f => document.fonts.load(f))));
  for (const [i, name] of names.entries()) {
    await p.evaluate(n => window.render(n), i + 1);
    await p.evaluate(() => document.fonts.ready);
    await p.waitForFunction(() => [...document.images].every(im => im.complete && im.naturalWidth > 0));
    const f = path.join(out, `${prefix}-${i + 1}-${name}.png`);
    await p.screenshot({ path: f }); console.log('saved', f);
  }
  await b.close();
})();
