// usage: node test_checker.js A1 a1-u1 a1-u2 ...   (no units = all units of that level)
const { chromium } = require('playwright');
(async () => {
  const level = process.argv[2]; const units = process.argv.slice(3);
  const browser = await chromium.launch(); const page = await browser.newPage();
  const errors = []; page.on('pageerror', e => errors.push(e.message));
  await page.route(/workers\.dev/, r => r.abort());
  await page.goto('file:///home/claude/spaans-leren.html'); await page.waitForTimeout(400);
  const r = await page.evaluate(async ({level, units}) => {
    const out = { fail: [], items: 0, rounds: 0, passed: 0, counts: [] };
    appState.profile = appState.profile || {}; appState.profile.baseLang='nl'; appState.profile.level=level;
    flattenPath(level);
    const list = CURRICULUM[level].filter(u => !u.ai && (!units.length || units.includes(u.id)));
    for (const u of list) {
      const groups = u.nodeGroups || buildNodeGroups(u);
      for (const g of groups) {
        const lesson = g.lessons[0];
        if (lesson.kind === 'new') out.counts.push(`${lesson.id}:${(lesson.words||[]).length}/${(lesson.sentences||[]).length}`);
        for (const round of ['A','B']) {
          exState = null; exSkipIntro = true; startLessonGroup(level, u.id, g.id); exSkipIntro = false;
          if (!exState) { out.fail.push(g.id+' no exState'); continue; }
          if (round === 'B' && lesson.kind !== 'new') continue;
          if (lesson.kind === 'new') { exState.items = buildFixed15Sequence(level, u.id, g.id, round); exState.round = round; }
          exState.correct = 0;
          for (let i=0;i<exState.items.length;i++){
            exState.index = i; renderExercise();
            const it = exState.currentItem;
            if (['mc','listen','ai-mc'].includes(it.type)) { selectedOptionVal = exState.currentCorrect; }
            else if (['build','ai-build'].includes(it.type)) { buildBank = exState.currentCorrect.split(' '); buildOrder = buildBank.map((_,j)=>j); }
            else { const inp = document.getElementById('type-answer'); if (!inp) { out.fail.push(g.id+' no input '+it.type); continue; } inp.value = exState.currentCorrect; }
            const before = exState.correct; checkAnswer(); out.items++;
            if (exState.correct === before) out.fail.push(`${g.id} ${round}${i} ${it.type} rejected "${exState.currentCorrect}"`);
          }
          out.rounds++;
        }
        // full flow to "Les afgerond"
        exState = null; exSkipIntro = true; startLessonGroup(level, u.id, g.id); exSkipIntro = false;
        exState.correct = exState.items.length; exState.index = exState.items.length; await finishExercise();
        const b = [...document.querySelectorAll('button')].find(x => x.textContent.includes('zinnen')); if (b) b.click();
        if (exState && exState.round === 'B') { exState.correct = exState.items.length; exState.index = exState.items.length; await finishExercise(); }
        if (document.body.innerHTML.includes('Les afgerond') || document.body.innerHTML.includes('afgerond')) out.passed++; else out.fail.push(g.id+' no Les afgerond');
      }
    }
    return out;
  }, {level, units});
  console.log(`${level}: rounds ${r.rounds}, items ${r.items}, groups passed ${r.passed}`);
  const thin = r.counts.filter(c => { const [w,s] = c.split(':')[1].split('/').map(Number); return w<10||s<10; });
  console.log('lessons under 10/10:', thin.length ? thin.join(' ') : 'none');
  console.log('failures:', r.fail.length ? r.fail.slice(0,15) : 'none', r.fail.length);
  console.log('page errors:', errors.length ? errors.slice(0,5) : 'none');
  await browser.close();
})();
