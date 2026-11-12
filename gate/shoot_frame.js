// G15: render a reel frame at full size (1080 x 1920) and at real phone size (390 x 693).
// Usage: node gate/shoot_frame.js <out.png> "t1=SAY THESE 10 WORDS&t2=IN YOUR NEXT MARATHON&tag=0:00 TO 0:03"
// Writes <out.png> and <out>-phone.png. Query keys: t1, t2, layout (full|half), pic (image path or label:text),
// subs, tag, who, ostTop, zones (0 to hide Instagram's overlay zones).
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [out, query = ''] = process.argv.slice(2);
  if (!out) { console.error('usage: node gate/shoot_frame.js <out.png> "<query>"'); process.exit(1); }
  const url = 'file://' + path.resolve(__dirname, 'frame.html') + '?' + query;
  const browser = await chromium.launch();
  for (const [w, h, file] of [[1080, 1920, out], [390, 693, out.replace(/\.png$/, '-phone.png')]]) {
    const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    await page.goto(url);
    await page.waitForTimeout(300);
    await page.screenshot({ path: file });
    const t = await page.title(); if (t.startsWith("fs=")) console.log(`title font ${t.slice(3)}vw (the 10% title was 6.1vw)`);
    console.log('wrote', file, w + 'x' + h);
  }
  await browser.close();
})();
