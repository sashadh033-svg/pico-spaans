const { chromium } = require('playwright');
const LANG = process.argv[2] || 'en';
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:400,height:850}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.route(/workers\.dev|googleapis/,r=>r.abort());await p.goto('file:///home/claude/spaans-leren.html?open=1');await p.waitForTimeout(600);
const NL=/\b(je|jij|jouw|het|een|niet|van|voor|met|naar|nog|deze|alle|wordt|klaar|oefenen|woorden|zinnen|uitleg|opnieuw|terug|verder|goed|fout|bijna|kies|typ|luister|vertaling|wat|hoe|waar|geen|maak|vul|juiste|antwoord|lessen|kluis|instellingen|doorgaan|controleren|woordenschat|herhalen|lastige|keuzes|verhaal|toets|ik|zijn|ben|heb|hebt|heeft|dat|dit|als|ook|maar|wel|bij|uit|om|te|er|zo|dan|nu|wij|jullie|zij|hij|haar|hem|ons|mijn|meer|eerst|zelf|kun|kan|mag|moet|zal)\b/i;
const out = await p.evaluate(async (args)=>{
  const [LANG, NLsrc] = args; const NL = new RegExp(NLsrc,'i');
  appState.profile.baseLang=LANG; appState.profile.onboarded=true; appState.profile.level='A1'; applyStaticLang();
  document.getElementById('bottomnav').style.display='flex';
  const res=[];
  const grab=(name)=>{ const el=document.querySelector('.screen.active'); const txt=(el?el.innerText:'')+'\n'+document.getElementById('bottomnav').innerText;
    const bad=txt.split('\n').map(s=>s.trim()).filter(s=>s && NL.test(s.replace(/[¡¿][^!?]*[!?]/g,'')));
    res.push([name, bad.slice(0,12)]); };
  const sleep=ms=>new Promise(r=>setTimeout(r,ms));
  go('lessons'); grab('lessons');
  go('vault'); grab('vault'); go('vault-add'); grab('vault-add'); go('verbs'); grab('verbs'); go('chat-menu'); grab('chat-menu'); go('settings'); grab('settings');
  showGuide('a1-u3'); grab('guide a1-u3');
  // les met intro
  for(const [lv,uid] of [['A1','a1-u3'],['B1','b1-u3'],['B2','b2-u10']]){
    appState.profile.level=lv; const unit=unitsForLevel(lv).find(u=>u.id===uid); const g=buildNodeGroups(unit).find(g=>g.lessons.some(l=>l.intro)) || buildNodeGroups(unit)[0];
    startLessonGroup(lv,uid,g.id); grab('intro '+uid);
    exSkipIntro=true; startLessonGroup(lv,uid,g.id); exSkipIntro=false;
    for(let i=0;i<6;i++){ grab('oefening '+uid+' '+(exState.items[exState.index]||{}).type); exState.index++; if(exState.index>=exState.items.length) break; renderExercise(); }
  }
  appState.profile.level='A1';
  startStory('A1','a1-u2'); for(let i=0;i<30;i++){ const cur=storyState.story.lines[storyState.idx]; if(!cur) break; if(cur.speaker===undefined){ grab('verhaalvraag'); break;} advanceStory(); }

  appState.profile.level='A2';
  startTrainer('A2','a2-u10'); for(let i=0;i<3;i++){ grab('trainer'); const inp=document.getElementById('type-answer'); if(inp){inp.value='xx'; checkAnswer(); grab('trainer fout');} exState.index++; renderExercise(); }
  startVerbPractice('a2-u29'); grab('werkwoord-oefenen'); const vi=document.getElementById('type-answer'); if(vi){vi.value='xx'; checkAnswer(); grab('werkwoord fout');}
  startWordPractice('a2-u5'); grab('woordentraining');
  startPronMix(); grab('pron-mix'); startVerbMix(); grab('verb-mix');
  startCheckpoint('A2','a2-u5'); for(let i=0;i<5;i++){ grab('checkpoint '+exState.items[exState.index].type); exState.index++; renderExercise(); }
  // uitslagschermen
  const unit=unitsForLevel('A2').find(u=>u.id==='a2-u5'); const g=buildNodeGroups(unit)[0];
  exSkipIntro=true; startLessonGroup('A2','a2-u5',g.id); exSkipIntro=false; exState.correct=3; exState.index=exState.items.length; try{ await finishExercise(); }catch(e){} grab('uitslag slecht');
  exSkipIntro=true; startLessonGroup('A2','a2-u5',g.id); exSkipIntro=false; exState.correct=exState.items.length; exState.index=exState.items.length; try{ await finishExercise(); }catch(e){} grab('uitslag goed');
  startStory('A2','a2-u5'); for(let i=0;i<40;i++){ const cur=storyState.story.lines[storyState.idx]; if(!cur){ break;} advanceStory(); } await sleep(50); grab('verhaal klaar');
  startVaultReview(); grab('vault-review');
  return res; }, [LANG, NL.source]);
for(const [n,bad] of out) console.log(n, bad.length? '\n   '+bad.join('\n   '):'OK');
console.log('errors',errs);
await p.goto('file:///home/claude/spaans-leren.html?open=1');await b.close();})();
