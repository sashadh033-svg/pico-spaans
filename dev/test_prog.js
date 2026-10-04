const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:420,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.route(/workers\.dev|googleapis/,r=>r.abort());await p.goto('file:///home/claude/spaans-leren.html');await p.waitForTimeout(500);
for(const L of ['A1','A2','B1','B2']){
const r=await p.evaluate(async(L)=>{const o={L,steps:0,problems:[],cp:0,skip:0};appState.profile.onboarded=true;appState.profile.level=L;const fillPrev=()=>{LEVELS.slice(0,LEVELS.indexOf(L)).forEach(P=>{appState.progress[P]={};flattenPath(P).forEach(n=>appState.progress[P][n.lesson.id]={done:true});});};appState.progress={};fillPrev();
 window.saveState=async()=>{};
 const nodes=flattenPath(L);
 for(let k=0;k<nodes.length;k++){
   go('lessons');renderLessons();
   const nx=[...document.querySelectorAll('.path-node.next')];
   const n=nodes[k];
   if(nx.length!==1){o.problems.push(k+' '+n.lesson.id+' next='+nx.length);if(o.problems.length>5)break;}
   else{const oc=nx[0].getAttribute('onclick')||'';
     if(!oc.includes(n.unit.id)) o.problems.push(k+' '+n.lesson.id+' onclick '+oc);}
   if(n.isCheckpoint){
     try{startCheckpoint(L,n.unit.id); if(!exState||exState.source!=='checkpoint'||!exState.items.length) o.problems.push('cp empty '+n.unit.id);
       exState.correct=exState.items.length;exState.index=exState.items.length;await finishExercise();o.cp++;}catch(e){o.problems.push('cp err '+n.unit.id+' '+e.message);}
     if(!progressKeyDone(L,n.lesson.id)){o.problems.push('cp not done '+n.unit.id);appState.progress[L][n.lesson.id]={done:true};}
   } else { appState.progress[L]=appState.progress[L]||{}; appState.progress[L][n.lesson.id]={done:true}; }
   o.steps++;
 }
 // skip test per unit
 const units=unitsForLevel(L);
 for(const u of units.slice(1)){
   appState.progress={};fillPrev();
   try{ for(let t=0;t<15;t++){ await startSkipTest(L,u.id); if(exState.source!=='skiptest'||!exState.items.length) throw new Error('empty'); }
     exState.correct=exState.items.length;exState.index=exState.items.length;await finishExercise();
     const ns=flattenPath(L); const fi=ns.findIndex(n=>!progressKeyDone(L,n.lesson.id));
     if(!ns[fi]||ns[fi].unit.id!==u.id) o.problems.push('skip '+u.id+' -> first incomplete '+(ns[fi]&&ns[fi].lesson.id));
     o.skip++;
   }catch(e){o.problems.push('skip err '+u.id+' '+e.message);}
 }
 return o;},L);
console.log(JSON.stringify(r));}
console.log(errs.slice(0,5));await b.close();})();
