// Test: Kluis-knop "Voornaamwoorden oefenen" gaat mee met de voortgang, en alle oefenzinnen worden goed nagekeken.
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport:{width:420,height:900} });
  const errs = []; p.on('pageerror', e => errs.push(e.message)); await p.route(/workers\.dev|googleapis/, r => r.abort());
  await p.goto('file:///home/claude/spaans-leren.html'); await p.waitForTimeout(500);
  const r = await p.evaluate(async () => {
    const out = {};
    appState.profile.baseLang = 'nl';
    // 1. voortgang: A1 -> niets, B1 (begin) -> A2, B2 (begin) -> A2+B1
    for (const L of ['A1','A2','B1','B2']) { appState.profile.level = L; out['pools_'+L] = reachedPronPools(); }
    // 2. Kluis-info en knop
    appState.profile.level = 'B1'; go('vault'); renderVault && renderVault();
    out.info = document.getElementById('vault-pron-info').textContent;
    // 3. elke oefenzin: het eigen antwoord (en de alts) moet goed zijn
    const bad = [];
    for (const k of Object.keys(PRONOUN_POOL)) for (const it of PRONOUN_POOL[k]) {
      for (const ans of [it.a, ...(it.alts||[])]) {
        startPronMix(); const item = buildPronounItem(k, it);
        exState = { items:[item], index:0, correct:0, level:'B1', lessonId:null, unitId:'__pron__', source:'verbPractice' };
        renderExercise();
        const inp = document.getElementById('type-answer'); if (!inp) { bad.push(k+' geen invoer: '+it.q); continue; }
        inp.value = ans; checkAnswer && checkAnswer();
        await new Promise(r=>setTimeout(r,10));
        const fb = document.querySelector('.feedback-bar'); const txt = fb ? fb.textContent : '';
        if (!/Correct|Bijna/i.test(txt)) bad.push(k+': '+ans+' => '+txt.slice(0,60));
      }
    }
    out.bad = bad;
    // 4. spiekbriefje
    showGuide('__pron__','vault'); out.guide = document.getElementById('guide-content').textContent.slice(0,80);
    showGuide('a2-u16'); out.link = !!Array.from(document.querySelectorAll('#guide-content button')).find(x=>/lo, la, le en se/.test(x.textContent));
    return out;
  });
  console.log(JSON.stringify(r, null, 1)); console.log('errors', errs); await b.close();
})();
