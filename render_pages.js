// render_pages.js -- NEEC Session 80: renders the Compassionism Simulation's findings and study pages (their figures
// are filled in by script) to text for outside_kit.py --fetch. Run from a static server over the simulation at its pin:
//   (cd compassionism-simulation && python3 -m http.server 8765) &
//   NODE_PATH=$(npm root -g) node render_pages.js
// Writes outside_kit_sources/rendered/<page>.txt (the page's innerText). Needs Playwright's Chromium.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  for (const page of ['findings.html', 'study.html']) {
    await p.goto('http://localhost:8765/' + page, { waitUntil: 'networkidle', timeout: 120000 });
    await p.waitForTimeout(3000);
    const t = await p.evaluate(() => document.body.innerText);
    const out = path.join(__dirname, 'outside_kit_sources', 'rendered', page + '.txt');
    fs.writeFileSync(out, t);
    console.log(out, t.length);
  }
  await b.close();
})();
