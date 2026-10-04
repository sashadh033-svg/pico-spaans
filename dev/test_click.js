const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:420,height:860},hasTouch:true,isMobile:true});const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.route(/workers\.dev|googleapis/,r=>r.abort());
await p.goto('file:///home/claude/spaans-leren.html');await p.waitForTimeout(400);
await p.evaluate(()=>{window.speakSpanish=()=>{};appState.profile.onboarded=true;appState.profile.level='A1';appState.progress={A1:{}};flattenPath('A1').filter(n=>n.unit.id==='a1-u1').forEach(n=>appState.progress.A1[n.lesson.id]={done:true});saveState();go('lessons');});
const log=[];
const nextOc=async()=>p.evaluate(()=>{const n=document.querySelector('.path-node.next');return n&&n.getAttribute('onclick');});
log.push('start next: '+await nextOc());
await p.locator('.path-node.next').scrollIntoViewIfNeeded();await p.locator('.path-node.next').tap();await p.waitForTimeout(200);
for(let step=0;step<80;step++){
  const st=await p.evaluate(()=>{const body=document.getElementById('exercise-body');const btns=[...body.querySelectorAll('button')].map(b=>b.textContent.trim());return {txt:body.innerText.slice(0,80),btns,screen:document.querySelector('.screen.active').id,type:exState&&exState.items[exState.index]?exState.items[exState.index].type:null,correct:exState&&exState.currentCorrect};});
  if(st.screen!=='screen-exercise'){log.push('left exercise at step '+step);break;}
  const has=t=>st.btns.find(b=>b.includes(t));
  if(has('Doorgaan')){await p.locator('#exercise-body button',{hasText:'Doorgaan'}).last().tap();continue;}
  if(has('Snap ik')){await p.locator('#exercise-body button',{hasText:'Snap ik'}).tap();continue;}
  if(has('Verder naar')){log.push('transition: '+st.txt.replace(/\n/g,' '));await p.locator('#exercise-body button',{hasText:'Verder naar'}).tap();continue;}
  if(has('Terug naar lessen')){log.push('end: '+st.txt.replace(/\n/g,' '));await p.locator('#exercise-body button',{hasText:'Terug naar lessen'}).first().tap();break;}
  if(st.type==='mc'||st.type==='listen'){await p.locator('.option',{hasText:st.correct}).first().tap();await p.locator('#check-btn').tap();continue;}
  if(st.type==='build'){const words=st.correct.split(' ');const used=[];for(const w of words){const i=await p.evaluate(([w,used])=>buildBank.findIndex((x,ix)=>x===w&&!used.includes(ix)&&!buildOrder.includes(ix)),[w,used]);used.push(i);await p.locator('#bank-'+i).tap();}await p.locator('#check-btn').tap();continue;}
  if(await p.locator('#type-answer').count()){await p.locator('#type-answer').fill(st.correct);await p.locator('#check-btn').tap();continue;}
  log.push('stuck: '+JSON.stringify(st));break;
}
await p.waitForTimeout(300);
log.push('progress b1: '+await p.evaluate(()=>JSON.stringify(appState.progress.A1['a1-u2-b1'])));
log.push('after next: '+await nextOc());
log.push('scrollY: '+await p.evaluate(()=>window.scrollY));
console.log(log.join('\n'),errs);await b.close();})();
