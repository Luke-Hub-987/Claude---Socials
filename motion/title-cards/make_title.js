// One command for the title graphics (Luke, 18 Nov: one chat, not three).
// Usage: node motion/title-cards/make_title.js <out prefix> "LINE 1 / LINE 2 / (LINE 3)" --red WORD [--blue WORD]
// Writes <prefix>-title-16x9.png (also the text-only cover), <prefix>-overlay-9x16.png (frame one, transparent).
const path = require('path'); const { chromium } = require('playwright');
const a = process.argv.slice(2); const out = a[0], title = a[1];
const opt = k => { const i = a.indexOf('--' + k); return i > 0 ? a[i + 1] : '' };
if (!out || !title) { console.error('usage: node motion/title-cards/make_title.js <out prefix> "L1 / L2 / (L3)" --red WORD [--blue WORD]'); process.exit(1); }
const l = title.split('/').map(s => s.trim()).join('|');
(async () => {
  const b = await chromium.launch();
  for (const [mode, w, h, suffix] of [['card', 1920, 1080, '-title-16x9.png'], ['overlay', 1080, 1920, '-overlay-9x16.png']]) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    const q = new URLSearchParams({ l, red: opt('red'), blue: opt('blue'), mode }).toString();
    await p.goto('file://' + path.resolve(__dirname, 'white.html') + '?' + q);
    await p.waitForFunction(() => document.title === 'ready');
    await p.screenshot({ path: out + suffix, omitBackground: mode === 'overlay' }); console.log('wrote', out + suffix);
  }
  await b.close();
})();
