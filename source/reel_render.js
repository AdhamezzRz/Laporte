// node reel_render.js <reel.html> <framesDir> [fps] [onlyTimes,comma-separated]
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
(async () => {
  const [inp, dir, fpsArg, only] = process.argv.slice(2);
  const fps = +(fpsArg || 30);
  fs.mkdirSync(dir, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.resolve(inp));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  const dur = await p.evaluate(() => window.DUR);
  const times = only ? only.split(',').map(Number) : [...Array(Math.round(dur * fps)).keys()].map(i => i / fps);
  for (let i = 0; i < times.length; i++) {
    await p.evaluate(([t, f]) => window.setTime(t, f), [times[i], i]);
    const name = only ? `t_${times[i].toFixed(2)}.png` : `f_${String(i).padStart(4, '0')}.jpg`;
    await p.screenshot({ path: path.join(dir, name), type: only ? 'png' : 'jpeg', quality: only ? undefined : 95 });
  }
  await b.close();
})();
