const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.route(/workers\.dev|googleapis/,r=>r.abort());await p.goto('file:///home/claude/spaans-leren.html');await p.waitForTimeout(400);
const r=await p.evaluate(()=>{const out=[];window.addToVault=()=>{};let fb;window.showFeedback=(c,it,ty)=>{fb=c?'goed':(ty?'oranje':'fout')};
 const bt=(ans,given)=>{exState={items:[],index:0,correct:0,source:'x',currentItem:{type:'build',es:ans,trans:'x'},currentCorrect:ans};buildBank=given.split(' ');buildOrder=buildBank.map((_,i)=>i);checkAnswer();out.push(['build',given,fb]);};
 const ty=(ans,given)=>{document.body.insertAdjacentHTML('beforeend','<input id="type-answer">');document.getElementById('type-answer').value=given;exState={items:[],index:0,correct:0,source:'x',currentItem:{type:'type-sentence',es:ans,trans:'x'},currentCorrect:ans};checkAnswer();document.getElementById('type-answer').remove();out.push(['type',given,fb]);};
 bt('¿A qué te dedicas tú?','¿A qué te dedicas?'); bt('¿A qué te dedicas tú?','¿A qué te dedicas tú?'); bt('Soy Carlos, ¿y tú?','Soy Carlos, ¿y?');
 ty('¿A qué te dedicas tú?','en que trabajas'); ty('Soy Carlos, ¿y tú?','soy carlos y'); ty('Vivo en Madrid.','Yo vivo en Madrid'); ty('¿Y tú?','y');
 return out;});console.log(r,errs);await b.close();})();
