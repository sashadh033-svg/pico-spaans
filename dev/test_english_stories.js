const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.route(/workers\.dev|googleapis/,r=>r.abort());await p.goto('file:///home/claude/spaans-leren.html');await p.waitForTimeout(500);
const r=await p.evaluate(()=>{appState.profile.baseLang='en';let n=0,bad=[];for(const k in STORIES){(STORIES[k].lines||[]).forEach(l=>{ if(l.speaker===undefined && l.question){ n++; const e=storyQ(l); if(e.question===l.question) bad.push('niet vertaald: '+k+' '+l.question); if(l.options&&l.options.length&&!e.options.includes(e.answer)) bad.push('antwoord: '+k+' '+e.question); if(l.q==='type'&&e.answer!==l.answer) bad.push('type: '+k);} });}return [n,bad];});
console.log(r[0],r[1].length,r[1].slice(0,5));await b.close();})();
