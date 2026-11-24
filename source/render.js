// node render.js <in.html> <out.pdf> [pngDir] [pngWidth]
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
(async () => {
  const [inp, out, pngDir, pngW] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file://' + path.resolve(inp));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  if (out && out !== '-') {
    await p.pdf({ path: out, width: '1920px', height: '1080px', printBackground: true, preferCSSPageSize: true });
  }
  if (pngDir) {
    fs.mkdirSync(pngDir, { recursive: true });
    const n = await p.locator('section.page').count();
    for (let i = 0; i < n; i++) {
      await p.locator('section.page').nth(i).screenshot({ path: path.join(pngDir, `page_${String(i + 1).padStart(2, '0')}.png`) });
    }
  }
  await b.close();
})();
