// Screenshots each New York frame to a 1920 x 1080 PNG.
// Usage: node motion/nyc-maps/tools/shoot.js <frames dir> [frame numbers...]
const path = require('path'), fs = require('fs');
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const [dir, ...only] = process.argv.slice(2);
const NAMES = { 1: 'opening', 2: 'miles-0-2-the-bridge', 3: 'miles-2-13-brooklyn', 4: 'miles-15-20-quiet-bridge-loud-avenue', 5: 'mile-20-to-the-line-fifth-avenue', 6: 'the-whole-plan' };
(async () => {
  const geo = JSON.parse(fs.readFileSync(path.join(dir, 'geo.json'), 'utf8'));
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto('file://' + path.resolve(dir, 'frames.html'));
  await p.evaluate(() => Promise.all(['800 30px Barlow', '700 30px Barlow', '600 30px Barlow', '92px "DM Serif Display"', 'italic 92px "DM Serif Display"', '600 40px Inter'].map(f => document.fonts.load(f))));
  for (const n of Object.keys(NAMES)) {
    if (only.length && !only.includes(n)) continue;
    await p.evaluate(([g, n]) => window.render(g, +n), [geo, n]);
    await p.evaluate(() => document.fonts.ready);
    await p.waitForFunction(() => { const i = document.getElementById('map'); return i.complete && i.naturalWidth > 0; });
    const out = path.join(dir, `nyc-${n}-${NAMES[n]}.png`);
    await p.screenshot({ path: out }); console.log('saved', out);
  }
  await b.close();
})();
