// node shoot.js <in.html> <outDir> <selector> [scale] [omitBackground]
// Screenshots every element matching selector to <outDir>/<id>.png
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [inp, outDir, sel, scale, omit] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1400 }, deviceScaleFactor: +(scale || 1) });
  await p.goto('file://' + path.resolve(inp));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  const els = await p.locator(sel).all();
  for (const e of els) {
    const id = await e.getAttribute('id');
    await e.screenshot({ path: path.join(outDir, id + '.png'), omitBackground: omit === '1' });
  }
  await b.close();
})();
