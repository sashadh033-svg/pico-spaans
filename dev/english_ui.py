# App-teksten (knoppen, feedback, schermen) in het Engels voor wie Engels als basistaal heeft.
# In JS: L('nl','en'). In vaste HTML: data-en="..." (en data-en-ph voor placeholders), toegepast door applyStaticLang().
# Gebruik: python3 dev/english_ui.py   (idempotent)
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, 'index.html')

def L(nl, en):
    return "${L('" + nl.replace("'", "\\'") + "','" + en.replace("'", "\\'") + "')}"

def LJ(nl, en):
    # als JS-expressie (buiten een template)
    return "L('" + nl.replace("'", "\\'") + "','" + en.replace("'", "\\'") + "')"

R = []   # (oud, nieuw, aantal)
def r(old, new, n=1):
    R.append((old, new, n))

# ---------- hulpfuncties ----------
r("function go(screen){\n",
  "// Taal van de app-teksten: volgt de basistaal (Nederlands of Engels)\n"
  "function L(nl, en){ return (appState && appState.profile && appState.profile.baseLang==='en') ? en : nl; }\n"
  "function applyStaticLang(lang){\n"
  "  lang = lang || appState.profile.baseLang;\n"
  "  document.querySelectorAll('[data-en]').forEach(el=>{ if(el.dataset.nl===undefined) el.dataset.nl = el.innerHTML; el.innerHTML = lang==='en' ? el.dataset.en : el.dataset.nl; });\n"
  "  document.querySelectorAll('[data-en-ph]').forEach(el=>{ if(el.dataset.nlPh===undefined) el.dataset.nlPh = el.placeholder; el.placeholder = lang==='en' ? el.dataset.enPh : el.dataset.nlPh; });\n"
  "  document.documentElement.lang = lang==='en' ? 'en' : 'nl';\n"
  "}\n"
  "function go(screen){\n")
r("function pickBase(b){ tmpBase=b; ",
  "function pickBase(b){ tmpBase=b; applyStaticLang(b); buildLevelGrid(b); ")
r("function buildLevelGrid(){\n  const grid = document.getElementById('level-grid');\n  const LEVEL_LABELS = { A1:'Beginner', A2:'Basis', B1:'Gevorderd', B2:'Sterk', C1:'Vloeiend', C2:'Native-level' };",
  "function buildLevelGrid(lang){\n  const grid = document.getElementById('level-grid');\n  const LEVEL_LABELS = lang==='en' ? { A1:'Beginner', A2:'Elementary', B1:'Intermediate', B2:'Upper-intermediate', C1:'Fluent', C2:'Native-level' } : { A1:'Beginner', A2:'Basis', B1:'Gevorderd', B2:'Sterk', C1:'Vloeiend', C2:'Native-level' };")
r("  grid.innerHTML = LEVELS.map(l=>`\n    <div class=\"level-card\" data-level=\"${l}\"",
  "  grid.innerHTML = LEVELS.map(l=>`\n    <div class=\"level-card ${l===tmpLevel?'selected':''}\" data-level=\"${l}\"")
r("async function updateSetting(key, value){\n  appState.profile[key] = value;\n  await saveState();\n}",
  "async function updateSetting(key, value){\n  appState.profile[key] = value;\n  await saveState();\n  if(key==='baseLang') applyStaticLang();\n}")
r("  await loadState();\n  // Installeerbare app",
  "  await loadState();\n  applyStaticLang();\n  // Installeerbare app")

# ---------- vaste HTML ----------
def s(old_tag_text, en, n=1):
    # voegt data-en toe aan het eerste element in old_tag_text: '<h1>Lessen</h1>' -> '<h1 data-en="Lessons">Lessen</h1>'
    i = old_tag_text.index('>')
    new = old_tag_text[:i] + ' data-en="' + en.replace('"', '&quot;') + '"' + old_tag_text[i:]
    r(old_tag_text, new, n)

s('<p class="muted">Ik help je écht Spaans leren spreken &mdash; niet alleen herkennen. Even twee dingen instellen.</p>',
  "I'll help you really learn to speak Spanish &mdash; not just recognise it. Let's set up two things.")
s('<div class="setting-label" style="margin-bottom:10px;">Ik spreek al:</div>', 'I already speak:')
s('<div class="big-choice-label">Engels</div>', 'English')
s('<div class="big-choice-label">Nederlands</div>', 'Dutch')
s('<div class="setting-label" style="margin-bottom:10px;">Mijn niveau (CEFR):</div>', 'My level (CEFR):')
s('<button class="btn" style="margin-top:22px;" onclick="finishOnboarding()">Begin met les 1 &rarr;</button>', 'Start lesson 1 &rarr;')
s('<div style="font-size:11px; font-weight:800; color:#afafaf; letter-spacing:.3px;">JOUW LEERPAD</div>', 'YOUR LEARNING PATH')
s('<h1>Lessen</h1>', 'Lessons')
s('<span class="lb-text">NIVEAU</span>', 'LEVEL')
s('<h1>Gids</h1>', 'Guide')
s('<h2 class="section-title" style="margin-top:0;">💬 Vragen aan Pico</h2>', '💬 Ask Pico')
s('<p class="muted" style="margin-bottom:10px;">Snap je iets niet helemaal? Stel hier een vervolgvraag over deze uitleg.</p>',
  "Something not quite clear? Ask a follow-up question about this explanation here.")
r('id="guide-question-input" class="type-input" placeholder="Typ je vraag..."',
  'id="guide-question-input" class="type-input" placeholder="Typ je vraag..." data-en-ph="Type your question..."')
s('<h1>Kluis</h1>', 'Vault')
r('<button class="btn leaf" id="vault-review-btn" onclick="startVaultReview()" style="margin-bottom:14px;">Herhalen starten (<span id="vault-due-count">0</span>)</button>',
  '<button class="btn leaf" id="vault-review-btn" onclick="startVaultReview()" style="margin-bottom:14px;"><span data-en="Start review">Herhalen starten</span> (<span id="vault-due-count">0</span>)</button>')
s('<button class="btn" id="vault-verb-btn" onclick="startVerbMix()" style="margin-bottom:6px; background:#ce82ff; border-color:#a568cc; box-shadow:0 4px 0 #a568cc;">🏋️ Werkwoorden oefenen</button>', '🏋️ Practise verbs')
s('<button class="btn" id="vault-pron-btn" onclick="startPronMix()" style="margin-bottom:6px; background:#1cb0f6; border-color:#1899d6; box-shadow:0 4px 0 #1899d6;">🔄 Voornaamwoorden oefenen</button>', '🔄 Practise pronouns')
s('<button class="btn secondary" onclick="showGuide(\'__pron__\',\'vault\')" style="margin-bottom:14px;">📖 Spiekbriefje: lo, la, le, se</button>', '📖 Cheat sheet: lo, la, le, se')
s('<h2 class="section-title">Alle woorden</h2>', 'All words')
s('<h1>Woord toevoegen</h1>', 'Add a word')
s('<div class="setting-label" style="margin-bottom:6px;">Spaans</div>', 'Spanish')
r('placeholder="bijv. la ventana"', 'placeholder="bijv. la ventana" data-en-ph="e.g. la ventana"')
s('<div class="setting-label" style="margin-bottom:6px;" id="add-trans-label">Vertaling</div>', 'Translation')
r('placeholder="bijv. het raam"', 'placeholder="bijv. het raam" data-en-ph="e.g. the window"')
s('<button class="btn" onclick="addManualWord()">Toevoegen aan kluis</button>', 'Add to vault')
s('<h1>Herhalen</h1>', 'Review')
s('<h1>Werkwoorden</h1>', 'Verbs')
r('placeholder="Zoek of typ een werkwoord (bijv. hablar)..."', 'placeholder="Zoek of typ een werkwoord (bijv. hablar)..." data-en-ph="Search or type a verb (e.g. hablar)..."')
s('<h1>Gesprek met Pico</h1>', 'Chat with Pico')
s('<p class="muted">Kies een scenario. Pico speelt een rol en het verhaal loopt door zolang je antwoordt &mdash; bij een foutje stuurt Pico je even bij.</p>',
  "Pick a scenario. Pico plays a role and the story keeps going as long as you reply &mdash; if you make a mistake, Pico will gently correct you.")
s('<h1 id="chat-title">Gesprek</h1>', 'Chat')
s('<h1>Instellingen</h1>', 'Settings')
s('<div class="setting-label">Basistaal</div>', 'Base language')
s('<div class="setting-sub">Taal van vertalingen &amp; uitleg</div>', 'Language of translations &amp; explanations')
s('<option value="nl">Nederlands</option>', 'Dutch')
s('<option value="en">Engels</option>', 'English')
s('<div class="setting-label">Niveau</div>', 'Level')
s('<div class="setting-sub">Bepaalt lesinhoud</div>', 'Sets the lesson content')
s('<div class="setting-label">Taal van uitleg</div>', 'Language of AI explanations')
s('<div class="setting-sub">Standaard schuift mee met je niveau</div>', 'By default it follows your level')
s('<option value="auto">Automatisch</option>', 'Automatic')
s('<option value="nl">Altijd Nederlands</option>', 'Always Dutch')
s('<option value="en">Altijd Engels</option>', 'Always English')
s('<option value="es">Altijd Spaans</option>', 'Always Spanish')
s('<p class="muted">Wijzigingen worden automatisch bewaard op dit toestel/account.</p>', 'Changes are saved automatically on this device/account.')
r('<p class="muted">Lesinhoud geladen uit: <b id="content-source">ingebakken</b></p>',
  '<p class="muted"><span data-en="Lesson content loaded from:">Lesinhoud geladen uit:</span> <b id="content-source">ingebakken</b></p>')
r('<span class="navicon">🏠</span>Lessen</button>', '<span class="navicon">🏠</span><span data-en="Lessons">Lessen</span></button>')
r('<span class="navicon">📚</span>Werkw.</button>', '<span class="navicon">📚</span><span data-en="Verbs">Werkw.</span></button>')
r('<span class="navicon">🗂️</span>Kluis</button>', '<span class="navicon">🗂️</span><span data-en="Vault">Kluis</span></button>')

# ---------- leerpad ----------
r("const PATH_TIPS = [\n  '¡Vamos! Volg het pad stap voor stap. Rond een les af om de volgende te openen.',\n  'Elke fout woord komt automatisch in je Kluis terecht om te herhalen.',\n  '¿Listo? Kies de volgende les op het pad om verder te gaan.'\n];",
  "const PATH_TIPS = [\n  '¡Vamos! Volg het pad stap voor stap. Rond een les af om de volgende te openen.',\n  'Elke fout woord komt automatisch in je Kluis terecht om te herhalen.',\n  '¿Listo? Kies de volgende les op het pad om verder te gaan.'\n];\n"
  "const PATH_TIPS_EN = [\n  '¡Vamos! Follow the path step by step. Finish a lesson to unlock the next one.',\n  'Every word you get wrong goes straight into your Vault so you can review it.',\n  '¿Listo? Pick the next lesson on the path to keep going.'\n];")
r("Nog geen gids voor deze unit.", L('Nog geen gids voor deze unit.', 'No guide for this unit yet.'))
r("${level} gaat open als je ${levelLock} hebt afgerond", "${L(`${level} gaat open als je ${levelLock} hebt afgerond`, `${level} unlocks when you have finished ${levelLock}`)}")
r("Je bent bij ${levelLock} op ${done} van de ${total} onderdelen.", "${L(`Je bent bij ${levelLock} op ${done} van de ${total} onderdelen.`, `You have done ${done} of the ${total} parts of ${levelLock}.`)}")
r(">Verder met ${levelLock}</button>", ">${L('Verder met','Continue with')} ${levelLock}</button>")
r("(levelLock ? 'Eerst '+levelLock+' afronden' : 'Op slot') : (unit.ai ? 'AI-thema' : 'Woordenschat') + ' &middot; Unit ' + (uIdx+1)",
  "(levelLock ? L('Eerst '+levelLock+' afronden', 'Finish '+levelLock+' first') : L('Op slot','Locked')) : (unit.ai ? L('AI-thema','AI topic') : L('Woordenschat','Vocabulary')) + ' &middot; Unit ' + (uIdx+1)")
r("🔓 Toets doen om te ontgrendelen</button>", "🔓 ${L('Toets doen om te ontgrendelen','Take a test to unlock')}</button>")
r('<span class="badge" style="margin-bottom:0;">Verhaal</span>', '<span class="badge" style="margin-bottom:0;">${L(\'Verhaal\',\'Story\')}</span>')
r('<span class="badge" style="margin-bottom:0;">Unit-toets</span>', '<span class="badge" style="margin-bottom:0;">${L(\'Unit-toets\',\'Unit test\')}</span>')
r("  return TRAINER_LABEL[k] || 'Oefenen';", "  return (appState.profile.baseLang==='en' ? TRAINER_LABEL_EN[k] : TRAINER_LABEL[k]) || L('Oefenen','Practice');")
r('const TRAINER_LABEL = {',
  'const TRAINER_LABEL_EN = {"pres_prog": "Presente or estar + gerundio", "ser_estar": "Ser or estar", "por_para": "Por or para", "pret_imp": "Indefinido or imperfecto", "subj": "Subjuntivo or not", "subj2": "Subjuntivo or not", "saber_conocer": "Saber or conocer", "pedir_preguntar": "Pedir or preguntar", "perif": "Verb constructions", "pron": "Pronouns"};\nconst TRAINER_LABEL = {')

r('<span>${PATH_TIPS[0]}</span>', '<span>${L(PATH_TIPS[0], PATH_TIPS_EN[0])}</span>')

# ---------- lege schermen / laden ----------
r('<h2 class="section-title" style="text-align:center;">Nog geen content voor deze unit</h2>', '<h2 class="section-title" style="text-align:center;">' + L('Nog geen content voor deze unit', 'No content for this unit yet') + '</h2>')
r('<p class="muted">De lessen van deze unit zijn nog leeg, dus er is nog geen toets mogelijk.</p>', '<p class="muted">' + L('De lessen van deze unit zijn nog leeg, dus er is nog geen toets mogelijk.', "This unit's lessons are still empty, so there's no test yet.") + '</p>')
r('<h2 class="section-title" style="text-align:center;">Nog geen content voor deze les</h2>', '<h2 class="section-title" style="text-align:center;">' + L('Nog geen content voor deze les', 'No content for this lesson yet') + '</h2>')
r('<p class="muted">Onderwerp: <b>', '<p class="muted">${L(\'Onderwerp\',\'Topic\')}: <b>')
r('<br>Grammatica: <b>', '<br>${L(\'Grammatica\',\'Grammar\')}: <b>')
r(">Terug naar lessen</button>", ">" + L('Terug naar lessen', 'Back to lessons') + "</button>", None)
r(">Terug naar kluis</button>", ">" + L('Terug naar kluis', 'Back to vault') + "</button>", None)
r(">Terug</button>", ">" + L('Terug', 'Back') + "</button>", None)
r(">Doorgaan</button>", ">" + L('Doorgaan', 'Continue') + "</button>", None)
r(">Controleren</button>", ">" + L('Controleren', 'Check') + "</button>", None)
r("Pico stelt een pittige toets samen...", L('Pico stelt een pittige toets samen...', 'Pico is putting together a tough test...'))
r("Kon de toets niet laden. Probeer het nog eens.", L('Kon de toets niet laden. Probeer het nog eens.', "Couldn't load the test. Please try again."))
r("Pico bedenkt oefeningen...", L('Pico bedenkt oefeningen...', 'Pico is coming up with exercises...'))
r("Kon geen oefeningen laden. Probeer het nog eens.", L('Kon geen oefeningen laden. Probeer het nog eens.', "Couldn't load exercises. Please try again."))
r(">Snap ik, beginnen &rarr;</button>", ">" + L('Snap ik, beginnen', 'Got it, start') + " &rarr;</button>")
r("hint.textContent = '🔇 Geluid werkt niet in deze weergave — probeer het bestand rechtstreeks in Chrome.';",
  "hint.textContent = " + LJ('🔇 Geluid werkt niet in deze weergave — probeer het bestand rechtstreeks in Chrome.', "🔇 Sound doesn't work in this view — try opening the file directly in Chrome.") + ";")

# ---------- verhaaltjes ----------
r("🌐 ${revealed?'verberg':'vertaling'}</button>", "🌐 ${revealed?L('verberg','hide'):L('vertaling','translation')}</button>", 2)
r('<span class="badge">❓ Begripsvraag</span>', '<span class="badge">❓ ${L(\'Begripsvraag\',\'Comprehension question\')}</span>')
r('placeholder="Typ hier..."', 'placeholder="${L(\'Typ hier...\',\'Type here...\')}"', None)
r('<h2 class="section-title" style="text-align:center;">Verhaal afgerond!</h2>', '<h2 class="section-title" style="text-align:center;">' + L('Verhaal afgerond!', 'Story finished!') + '</h2>')
r("`${storyState.correct} / ${storyState.total} begripsvragen goed` : 'Goed gedaan!'",
  "`${storyState.correct} / ${storyState.total} ${L('begripsvragen goed','questions correct')}` : L('Goed gedaan!','Well done!')")

# ---------- oefeningen ----------
r("'✏️ Kies het juiste antwoord' : (forward ? '🧠 Wat betekent dit?' : '🇪🇸 Vertaal naar het Spaans')",
  "L('✏️ Kies het juiste antwoord','✏️ Choose the right answer') : (forward ? L('🧠 Wat betekent dit?','🧠 What does this mean?') : L('🇪🇸 Vertaal naar het Spaans','🇪🇸 Translate into Spanish'))")
r("'⌨️ Typ het antwoord' : '⌨️ Typ de Spaanse vertaling'", "L('⌨️ Typ het antwoord','⌨️ Type the answer') : L('⌨️ Typ de Spaanse vertaling','⌨️ Type it in Spanish')")
r("badgeText = '✍️ Vrije tekstinvoer: typ de Spaanse vertaling';", "badgeText = " + LJ('✍️ Vrije tekstinvoer: typ de Spaanse vertaling', '✍️ Free writing: type it in Spanish') + ";")
r("it.badge || '📝 Vul het werkwoord in de juiste vorm in'", "it.badge || " + LJ('📝 Vul het werkwoord in de juiste vorm in', '📝 Fill in the verb in the right form'))
r('<span class="badge">🎧 Audio-dictee: typ precies wat je hoort</span>', '<span class="badge">🎧 ' + L('Audio-dictee: typ precies wat je hoort', 'Dictation: type exactly what you hear') + '</span>')
r('placeholder="Typ hier wat je hoort..."', 'placeholder="${L(\'Typ hier wat je hoort...\',\'Type what you hear...\')}"')
r('<span class="badge">🎧 Luister en kies de vertaling</span>', '<span class="badge">🎧 ' + L('Luister en kies de vertaling', 'Listen and choose the translation') + '</span>')
r('<div class="speaker-hint">Tik om het woord te horen</div>', '<div class="speaker-hint">' + L('Tik om het woord te horen', 'Tap to hear the word') + '</div>')
r("🏋️ Onbeperkt oefenen &middot; ${verbPracticeState.correct}/${verbPracticeState.count} goed &middot; <span style=\"cursor:pointer; text-decoration:underline;\" onclick=\"go('lessons')\">stoppen</span>",
  "🏋️ ${L('Onbeperkt oefenen','Unlimited practice')} &middot; ${verbPracticeState.correct}/${verbPracticeState.count} ${L('goed','correct')} &middot; <span style=\"cursor:pointer; text-decoration:underline;\" onclick=\"go('lessons')\">${L('stoppen','stop')}</span>")
r("🎯 Woordentraining &middot; ${wordPracticeState.correct}/${wordPracticeState.count} goed &middot; <span style=\"cursor:pointer; text-decoration:underline;\" onclick=\"go('lessons')\">stoppen</span>",
  "🎯 ${L('Woordentraining','Word training')} &middot; ${wordPracticeState.correct}/${wordPracticeState.count} ${L('goed','correct')} &middot; <span style=\"cursor:pointer; text-decoration:underline;\" onclick=\"go('lessons')\">${L('stoppen','stop')}</span>")

# ---------- feedback ----------
r("exState.lastTitle = accentMiss && markMiss ? 'Bijna goed! Let op accenten en ¿ ¡ ✏️' : (accentMiss ? 'Bijna goed! Let op de accenten ✏️' : 'Bijna goed! Let op ¿ en ¡ ✏️');",
  "exState.lastTitle = accentMiss && markMiss ? L('Bijna goed! Let op accenten en ¿ ¡ ✏️','Almost! Watch the accents and ¿ ¡ ✏️') : (accentMiss ? L('Bijna goed! Let op de accenten ✏️','Almost! Watch the accents ✏️') : L('Bijna goed! Let op ¿ en ¡ ✏️','Almost! Watch the ¿ and ¡ ✏️'));")
r("exState.lastTip = 'Spaanse vragen en uitroepen beginnen met <b>¿</b> of <b>¡</b>.';",
  "exState.lastTip = " + LJ('Spaanse vragen en uitroepen beginnen met <b>¿</b> of <b>¡</b>.', 'Spanish questions and exclamations start with <b>¿</b> or <b>¡</b>.') + ";")
r("exState.lastTip = 'Bij een beroep na <i>ser</i> laat je <i>un/una</i> weg: <i>Soy médico</i>, <i>Él es cocinero</i> (niet <i>es un cocinero</i>).';",
  "exState.lastTip = " + LJ('Bij een beroep na <i>ser</i> laat je <i>un/una</i> weg: <i>Soy médico</i>, <i>Él es cocinero</i> (niet <i>es un cocinero</i>).', 'With a job after <i>ser</i>, leave out <i>un/una</i>: <i>Soy médico</i>, <i>Él es cocinero</i> (not <i>es un cocinero</i>).') + ";")
r("exState.lastTip ? 'Bijna goed! Kleine grammaticatip 💡' : 'Bijna goed! Let op de spelling ✏️') : 'Niet helemaal')",
  "exState.lastTip ? L('Bijna goed! Kleine grammaticatip 💡','Almost! Small grammar tip 💡') : L('Bijna goed! Let op de spelling ✏️','Almost! Watch the spelling ✏️')) : L('Niet helemaal','Not quite'))")
r("`Telt als goed, maar zo is het: <b>${answerShown}</b>", "`${L('Telt als goed, maar zo is het:','Counts as correct, but this is how it goes:')} <b>${answerShown}</b>")
r("`Juiste antwoord: <b>", "`${L('Juiste antwoord:','Correct answer:')} <b>", None)
r("'¡Correcto! 🎉' : 'Niet helemaal'}", "'¡Correcto! 🎉' : L('Niet helemaal','Not quite')}", None)
r('onclick="appealAnswer(this)">Mijn antwoord is ook goed</button>', 'onclick="appealAnswer(this)">${L(\'Mijn antwoord is ook goed\',\'My answer is also correct\')}</button>')
r('onclick="requestExplanation(this)">Leg uit</button>', 'onclick="requestExplanation(this)">${L(\'Leg uit\',\'Explain\')}</button>')
r("box.textContent = 'Pico kon dit nu niet controleren (geen verbinding?). Probeer het later nog eens.';",
  "box.textContent = " + LJ('Pico kon dit nu niet controleren (geen verbinding?). Probeer het later nog eens.', "Pico couldn't check this right now (no connection?). Please try again later.") + ";")
r("t.textContent = '¡Correcto! Jouw antwoord telt ook 🎉';", "t.textContent = " + LJ('¡Correcto! Jouw antwoord telt ook 🎉', '¡Correcto! Your answer counts too 🎉') + ";")
r("box.textContent = res.reden || 'Jouw antwoord is ook goed.';", "box.textContent = res.reden || " + LJ('Jouw antwoord is ook goed.', 'Your answer is also correct.') + ";")
r("box.textContent = '❌ ' + (res.reden || 'Toch niet helemaal goed.');", "box.textContent = '❌ ' + (res.reden || " + LJ('Toch niet helemaal goed.', 'Not quite right after all.') + ");")

# ---------- Kluis / oefenen ----------
r("Voornaamwoorden (lo, la, le...) leer je in A2 unit 16. Daarna kun je hier onbeperkt oefenen.",
  L('Voornaamwoorden (lo, la, le...) leer je in A2 unit 16. Daarna kun je hier onbeperkt oefenen.', "You learn pronouns (lo, la, le...) in A2 unit 16. After that you can practise them here as much as you like."))
r(">📖 Spiekbriefje bekijken</button>", ">📖 " + L('Spiekbriefje bekijken', 'View cheat sheet') + "</button>")
r("Je hebt nog geen werkwoorden geleerd. Maak eerst een paar units af!", L('Je hebt nog geen werkwoorden geleerd. Maak eerst een paar units af!', "You haven't learned any verbs yet. Finish a few units first!"))
r("Nog geen oefenstof voor deze unit.", L('Nog geen oefenstof voor deze unit.', 'No practice material for this unit yet.'))
r("Nog geen woorden om te oefenen in deze unit.", L('Nog geen woorden om te oefenen in deze unit.', 'No words to practise in this unit yet.'))
r("'Mix uit ' + vu.length + ' units, tot waar je nu bent' : 'Komt vrij zodra je je eerste werkwoorden hebt geleerd'",
  "L('Mix uit ' + vu.length + ' units, tot waar je nu bent', 'Mix from ' + vu.length + ' units, up to where you are now') : L('Komt vrij zodra je je eerste werkwoorden hebt geleerd', 'Unlocks once you have learned your first verbs')")
r("'Tot waar je nu bent: ' + pp.map(k=>PRON_INFO[k]).join(' ') : 'Komt vrij in A2 unit 16 (lo, la, le)'",
  "L('Tot waar je nu bent: ','Up to where you are now: ') + pp.map(k=>PRON_INFO[k]).join(' ') : L('Komt vrij in A2 unit 16 (lo, la, le)','Unlocks in A2 unit 16 (lo, la, le)')")
r("Nog geen woorden. Voeg er handmatig een toe of maak fouten tijdens het oefenen — dat werkt ook!",
  L('Nog geen woorden. Voeg er handmatig een toe of maak fouten tijdens het oefenen — dat werkt ook!', 'No words yet. Add one yourself, or make mistakes while practising — that works too!'))
r("Klaar met herhalen voor nu!", L('Klaar met herhalen voor nu!', 'Done reviewing for now!'))
r('<span class="badge">⌨️ Typ de vertaling</span>', '<span class="badge">⌨️ ' + L('Typ de vertaling', 'Type the translation') + '</span>')

# ---------- resultaatschermen ----------
r("${score} / ${total} goed (minimaal ${need} nodig).</p>", "${score} / ${total} ${L('goed','correct')} (${L('minimaal','at least')} ${need} ${L('nodig','needed')}).</p>")
r('<h2 class="section-title" style="text-align:center;">Nog even oefenen</h2>', '<h2 class="section-title" style="text-align:center;">' + L('Nog even oefenen', 'A bit more practice') + '</h2>')
r("${score} / ${total} goed &mdash; je hebt minimaal ${need} nodig. Lees de uitleg na in de gids (📖) en probeer het opnieuw met nieuwe zinnen.",
  "${score} / ${total} ${L(`goed &mdash; je hebt minimaal ${need} nodig. Lees de uitleg na in de gids (📖) en probeer het opnieuw met nieuwe zinnen.`, `correct &mdash; you need at least ${need}. Read the explanation in the guide (📖) and try again with new sentences.`)}")
r('<h2 class="section-title" style="text-align:center;">De woorden zitten nog niet</h2>', '<h2 class="section-title" style="text-align:center;">' + L('De woorden zitten nog niet', "The words haven't stuck yet") + '</h2>')
r("${scoreA} / ${totalA} goed &mdash; je hebt minimaal ${ROUND_A_THRESHOLD} nodig voordat je met zinnen verder mag. Probeer de woorden nog een keer met een nieuwe set vragen.",
  "${scoreA} / ${totalA} ${L(`goed &mdash; je hebt minimaal ${ROUND_A_THRESHOLD} nodig voordat je met zinnen verder mag. Probeer de woorden nog een keer met een nieuwe set vragen.`, `correct &mdash; you need at least ${ROUND_A_THRESHOLD} before moving on to sentences. Try the words again with a new set of questions.`)}")
r('<h2 class="section-title" style="text-align:center;">Deel 1 van 2 klaar: woorden geleerd!</h2>', '<h2 class="section-title" style="text-align:center;">' + L('Deel 1 van 2 klaar: woorden geleerd!', 'Part 1 of 2 done: words learned!') + '</h2>')
r("${scoreA} / ${totalA} goed. Nu nog deel 2: de zinnen. Pas daarna is dit bolletje af en gaat het volgende open.",
  "${scoreA} / ${totalA} ${L('goed. Nu nog deel 2: de zinnen. Pas daarna is dit bolletje af en gaat het volgende open.', 'correct. Now part 2: the sentences. After that this lesson is done and the next one unlocks.')}")
r(">Verder naar deel 2: zinnen &rarr;</button>", ">" + L('Verder naar deel 2: zinnen', 'On to part 2: sentences') + " &rarr;</button>")
r("${totalCorrect} / ${totalQuestions} goed (minimaal ${MASTERY_THRESHOLD} nodig).",
  "${totalCorrect} / ${totalQuestions} ${L('goed','correct')} (${L('minimaal','at least')} ${MASTERY_THRESHOLD} ${L('nodig','needed')}).")
r('<h2 class="section-title" style="text-align:center;">Nog niet onder de knie</h2>', '<h2 class="section-title" style="text-align:center;">' + L('Nog niet onder de knie', 'Not mastered yet') + '</h2>')
r("${totalCorrect} / ${totalQuestions} goed &mdash; je hebt minimaal ${MASTERY_THRESHOLD} nodig (max ${ALLOWED_WRONG} fout). Het volgende bolletje gaat pas open als je dit haalt. Probeer het nog een keer met nieuwe vragen over dezelfde stof.",
  "${totalCorrect} / ${totalQuestions} ${L(`goed &mdash; je hebt minimaal ${MASTERY_THRESHOLD} nodig (max ${ALLOWED_WRONG} fout). Het volgende bolletje gaat pas open als je dit haalt. Probeer het nog een keer met nieuwe vragen over dezelfde stof.`, `correct &mdash; you need at least ${MASTERY_THRESHOLD} (max ${ALLOWED_WRONG} wrong). The next lesson only unlocks once you pass this. Try again with new questions on the same material.`)}")
r('<h2 class="section-title" style="text-align:center;">Leerdeel klaar!</h2>', '<h2 class="section-title" style="text-align:center;">' + L('Leerdeel klaar!', 'Learning part done!') + '</h2>')
r("${exState.correct} / ${exState.items.length} goed. Nu volgt een toets van 15 vragen (max 2 fout) om te kijken of het beklijft.",
  "${exState.correct} / ${exState.items.length} ${L('goed. Nu volgt een toets van 15 vragen (max 2 fout) om te kijken of het beklijft.', 'correct. Now a 15-question test follows (max 2 wrong) to check that it sticks.')}")
r("${exState.correct} / ${exState.items.length} goed (max 2 fout toegestaan).</p>", "${exState.correct} / ${exState.items.length} ${L('goed (max 2 fout toegestaan).','correct (max 2 wrong allowed).')}</p>")
r('<h2 class="section-title" style="text-align:center;">Nog niet gehaald</h2>', '<h2 class="section-title" style="text-align:center;">' + L('Nog niet gehaald', 'Not passed yet') + '</h2>', None)
r("${exState.correct} / ${exState.items.length} goed &mdash; ${wrong} fout, max 2 mag. Je krijgt nu een nieuw setje vragen over hetzelfde onderwerp.",
  "${exState.correct} / ${exState.items.length} ${L(`goed &mdash; ${wrong} fout, max 2 mag. Je krijgt nu een nieuw setje vragen over hetzelfde onderwerp.`, `correct &mdash; ${wrong} wrong, max 2 allowed. You'll now get a new set of questions on the same topic.`)}")
r("${exState.correct} / ${exState.items.length} goed (max 2 fout toegestaan) &mdash; volgende unit is open!",
  "${exState.correct} / ${exState.items.length} ${L('goed (max 2 fout toegestaan) &mdash; volgende unit is open!', 'correct (max 2 wrong allowed) &mdash; the next unit is unlocked!')}")
r("${exState.correct} / ${exState.items.length} goed &mdash; ${wrong} fout, max 2 mag. Geen zorgen, gewoon nog een keer proberen!",
  "${exState.correct} / ${exState.items.length} ${L(`goed &mdash; ${wrong} fout, max 2 mag. Geen zorgen, gewoon nog een keer proberen!`, `correct &mdash; ${wrong} wrong, max 2 allowed. No worries, just try again!`)}")
r("${exState.correct} / ${exState.items.length} goed (max 3 fout toegestaan) &mdash; alles ervoor staat op voltooid, deze unit is nu open.",
  "${exState.correct} / ${exState.items.length} ${L('goed (max 3 fout toegestaan) &mdash; alles ervoor staat op voltooid, deze unit is nu open.', 'correct (max 3 wrong allowed) &mdash; everything before it is marked as done, and this unit is now unlocked.')}")
r("${exState.correct} / ${exState.items.length} goed &mdash; ${wrong} fout, max 3 mag. Je kan het opnieuw proberen, of gewoon de units in volgorde doen.",
  "${exState.correct} / ${exState.items.length} ${L(`goed &mdash; ${wrong} fout, max 3 mag. Je kan het opnieuw proberen, of gewoon de units in volgorde doen.`, `correct &mdash; ${wrong} wrong, max 3 allowed. You can try again, or just do the units in order.`)}")
r('<p class="muted">${exState.correct} / ${exState.items.length} goed</p>', '<p class="muted">${exState.correct} / ${exState.items.length} ${L(\'goed\',\'correct\')}</p>')

# ---------- werkwoorden ----------
r('<p class="muted">Niet in de kernlijst.</p>', '<p class="muted">${L(\'Niet in de kernlijst.\',\'Not in the core list.\')}</p>')
r(">Vraag Pico naar \"${document.getElementById('verb-search').value}\"</button>", ">${L('Vraag Pico naar','Ask Pico about')} \"${document.getElementById('verb-search').value}\"</button>")
r("'<span class=\"muted\">— (geen vorm)</span>'", "'<span class=\"muted\">— ('+L('geen vorm','no form')+')</span>'")
r("'<tr><td>Kon deze vorm niet bepalen.</td></tr>'", "'<tr><td>'+L('Kon deze vorm niet bepalen.','Could not work out this form.')+'</td></tr>'")
r('Kon "${verb}" niet vinden. Check de spelling.', '${L(`Kon "${verb}" niet vinden. Check de spelling.`, `Couldn\'t find "${verb}". Check the spelling.`)}')

# ---------- AI-chat ----------
r("addBubble('npc','(Pico is er even niet — probeer opnieuw)')", "addBubble('npc', " + LJ('(Pico is er even niet — probeer opnieuw)', "(Pico isn't available right now — try again)") + ")")
r("addBubble(null, '🎉 Gesprek afgerond! Ga terug voor een nieuw scenario.', null, true)", "addBubble(null, " + LJ('🎉 Gesprek afgerond! Ga terug voor een nieuw scenario.', '🎉 Conversation finished! Go back for a new scenario.') + ", null, true)")
r("return wantJson ? null : '(Pico kon nu even niet antwoorden — probeer het zo nog eens.)';",
  "return wantJson ? null : " + LJ('(Pico kon nu even niet antwoorden — probeer het zo nog eens.)', "(Pico couldn't answer just now — try again in a moment.)") + ";", 2)

def main():
    c = open(PATH, encoding='utf-8').read()
    if 'function applyStaticLang(' in c:
        print('al gedaan'); return
    for old, new, n in R:
        k = c.count(old)
        if n is None:
            assert k > 0, 'niet gevonden: ' + old[:80]
        else:
            assert k == n, f'{k}x gevonden (verwacht {n}): ' + old[:80]
        c = c.replace(old, new)
    open(PATH, 'w', encoding='utf-8').write(c)
    print(len(R), 'vervangingen')

# ---------- tweede ronde (per regel idempotent) ----------
R2 = []
def r2(old, new, n=1):
    R2.append((old, new, n))
r2('>✨ NIEUW WOORD</span>', ">${L('✨ NIEUW WOORD','✨ NEW WORD')}</span>")
r2("badgeText = '🧩 Bouw de zin';", "badgeText = " + LJ('🧩 Bouw de zin', '🧩 Build the sentence') + ";")
for nl, en in [('Goed gekozen!', 'Well chosen!'), ('Les afgerond!', 'Lesson complete!'), ('Toets gehaald!', 'Test passed!'),
               ('Unit-toets gehaald!', 'Unit test passed!'), ('Toets gehaald, unit overgeslagen!', 'Test passed, unit skipped!'), ('Klaar!', 'Done!')]:
    r2('<h2 class="section-title" style="text-align:center;">' + nl + '</h2>', '<h2 class="section-title" style="text-align:center;">' + L(nl, en) + '</h2>')
r2('>Opnieuw proberen (nieuwe vragen)</button>', '>' + L('Opnieuw proberen (nieuwe vragen)', 'Try again (new questions)') + '</button>')
r2('>Opnieuw proberen</button>', '>' + L('Opnieuw proberen', 'Try again') + '</button>', None)
r2('>Start de toets</button>', '>' + L('Start de toets', 'Start the test') + '</button>')
r2('"reden": "één korte zin in het Nederlands"}`;', '"reden": "één korte zin in het ${baseLangName(appState.profile.baseLang)}"}`;')
r2("btn.textContent = 'Pico kijkt mee...';", "btn.textContent = " + LJ('Pico kijkt mee...', 'Pico is checking...') + ";")
r2("btn.textContent = 'Pico denkt na...';", "btn.textContent = " + LJ('Pico denkt na...', 'Pico is thinking...') + ";")

def main2():
    c = open(PATH, encoding='utf-8').read()
    done = 0
    for old, new, n in R2:
        k = c.count(old)
        if k == 0:
            assert new in c, 'niet gevonden: ' + old[:80]
            continue
        assert n is None or k == n, f'{k}x gevonden (verwacht {n}): ' + old[:80]
        c = c.replace(old, new); done += 1
    open(PATH, 'w', encoding='utf-8').write(c)
    print(done, 'extra vervangingen')

if __name__ == '__main__':
    main()
    main2()
