// Renders the scoreboard frames to PNG, plus phone-size checks.
// Usage: node motion/scoreboard/shoot.js <out dir> [r p m]
const path = require('path');
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const [out, r = '16', p = '10', m = '2'] = process.argv.slice(2);
const page = 'file://' + path.resolve(__dirname, 'scoreboard.html');
(async () => {
  const b = await chromium.launch();
  for (const [f, w, h] of [['wide', 1920, 1080], ['cover', 1080, 1920]]) {
    const pg = await b.newPage({ viewport: { width: w, height: h } });
    pg.on('pageerror', e => console.log('ERR', e.message));
    await pg.goto(`${page}?f=${f}&r=${r}&p=${p}&m=${m}`);
    await pg.evaluate(() => Promise.all(['400 100px "DM Serif Display"', '600 40px Barlow', '700 40px Barlow'].map(x => document.fonts.load(x))));
    await pg.evaluate(() => document.fonts.ready);
    await pg.waitForFunction(() => [...document.images].every(i => i.complete && i.naturalWidth > 0));
    const ok = await pg.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight));
    console.log(f, 'fonts loaded:', ok.join(', '));
    const file = path.join(out, `scoreboard-${r}-${p}-${m}-${f}.png`);
    await pg.screenshot({ path: file }); console.log('saved', file);
    await pg.close();
  }
  await b.close();
})();
