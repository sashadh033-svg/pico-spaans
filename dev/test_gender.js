const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.route(/workers\.dev|googleapis/,r=>r.abort());await p.goto('file:///home/claude/spaans-leren.html');await p.waitForTimeout(400);
const r=await p.evaluate(()=>{const out=[];window.addToVault=()=>{};let fb;window.showFeedback=(c,it,ty)=>{fb=c?'goed':(ty?'oranje':'fout')};
 const ty=(ans,given,type='type-sentence')=>{document.body.insertAdjacentHTML('beforeend','<input id="type-answer">');document.getElementById('type-answer').value=given;exState={items:[],index:0,correct:0,source:'x',currentItem:{type,es:ans,trans:'x'},currentCorrect:ans};checkAnswer();document.getElementById('type-answer').remove();out.push([given,fb]);};
 ty('Soy médica, no profesora.','Soy médico no profesor'); ty('Soy médica, no profesora.','Soy médica no profesor'); ty('Es una enfermera muy simpática.','Es un enfermero muy simpático');
 ty('El chico es alto.','La chica es alta'); ty('Mi hermano es alto.','Mi hermana es alta'); ty('el/la médico/a','médico','type');
 return [out, Object.keys(genderFlex()).length];});console.log(JSON.stringify(r),errs);await b.close();})();
