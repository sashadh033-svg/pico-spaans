const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch(); const page = await browser.newPage();
  const errors = []; page.on('pageerror', e => errors.push(e.message));
  await page.route(/workers\.dev/, r => r.abort());
  await page.goto('file:///home/claude/spaans-leren.html'); await page.waitForTimeout(400);
  const LV = process.argv[2]||'B1'; const r = await page.evaluate(async (LV) => {
    appState.profile = appState.profile||{}; appState.profile.baseLang='nl'; appState.profile.level=LV;
    const out = { missing:[], fails:[], done:0, pathStoryNodes:0 };
    const nodes = flattenPath(LV);
    out.pathStoryNodes = (nodes||[]).filter(n=>n.isStory).length;
    for (const u of CURRICULUM[LV]) {
      if (!STORIES[u.id]) { out.missing.push(u.id); continue; }
      startStory(LV, u.id);
      let guard = 0;
      while (storyState.idx < storyState.story.lines.length && guard++ < 50) {
        const cur = storyState.story.lines[storyState.idx];
        if (cur.speaker !== undefined) { advanceStory(); continue; }
        const el = [...document.querySelectorAll('.option')].find(o => o.textContent === cur.answer);
        if (!el) { out.fails.push(u.id+' option not found: '+cur.answer); break; }
        el.click(); checkStoryAnswer();
        const btn = [...document.querySelectorAll('.feedback-bar button.btn, button.btn')].reverse().find(b => /Doorgaan|Verder/.test(b.textContent));
        if (btn) btn.click(); else { out.fails.push(u.id+' no continue btn'); break; }
      }
      if (storyState.correct !== storyState.total) out.fails.push(`${u.id} score ${storyState.correct}/${storyState.total}`);
      out.done++;
    }
    return out;
  }, LV);
  console.log(JSON.stringify(r)); console.log('errors:', errors.length?errors.slice(0,5):'none');
  await browser.close();
})();
