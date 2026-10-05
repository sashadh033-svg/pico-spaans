# Engelse uitleg (intro's vóór de bolletjes) en Engelse begripsvragen bij de verhaaltjes.
# Bron: dev/en/intros_en.json {les-id: html} en dev/en/story_questions_en.json [{question, options, question_en, options_en, answer_en}] -> tabel STORY_Q_EN
# Gebruik: python3 dev/english_content.py   (idempotent; na een gewijzigde vertaling opnieuw draaien)
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, 'index.html')
EN = os.path.join(ROOT, 'dev', 'en')

def main():
    c = open(PATH, encoding='utf-8').read()

    # 1) INTRO_EN als losse tabel (vóór STORY_CHARACTERS), elke keer opnieuw geschreven
    intros = json.load(open(os.path.join(EN, 'intros_en.json'), encoding='utf-8'))
    for k, v in intros.items():
        assert '`' not in v and '${' not in v, k
    line = 'const INTRO_EN = ' + json.dumps(intros, ensure_ascii=False) + ';\n'
    m = re.search(r'const INTRO_EN = .*;\n', c)
    if m:
        c = c[:m.start()] + line + c[m.end():]
    else:
        i = c.index('const STORY_CHARACTERS =')
        c = c[:i] + '// Engelse versie van de uitleg vóór een bolletje (les-id -> html); zie dev/english_content.py\n' + line + c[i:]

    # 2) weergave: Engelse uitleg als de basistaal Engels is
    rep = [
        ("    if(intros.length) virtual.intro = intros.map(l=>l.intro).join('<hr style=\"border:none;border-top:1px solid rgba(0,0,0,.1);margin:14px 0;\">');",
         "    if(intros.length) virtual.intro = intros.map(l=>l.intro).join('<hr style=\"border:none;border-top:1px solid rgba(0,0,0,.1);margin:14px 0;\">');\n"
         "    if(intros.length) virtual.introEn = intros.map(l=>INTRO_EN[l.id] || l.intro).join('<hr style=\"border:none;border-top:1px solid rgba(0,0,0,.1);margin:14px 0;\">');"),
        ('<div class="card" style="margin-bottom:16px;">${lesson.intro}</div>',
         '<div class="card" style="margin-bottom:16px;">${(appState.profile.baseLang===\'en\' && (lesson.introEn || INTRO_EN[lesson.id])) || lesson.intro}</div>'),
        # verhaalvragen
        ("function selectStoryOption(el, val){",
         "// begripsvraag in de basistaal (Engelse vertaling uit STORY_Q_EN als die er is)\n"
         "function storyQ(q){\n"
         "  if(appState.profile.baseLang!=='en') return q;\n"
         "  const t = STORY_Q_EN[q.question + '\\u0001' + (q.options||[]).join('\\u0001')];\n"
         "  return t ? { q:q.q, question:t.q, options:(q.options&&q.options.length) ? t.o : q.options, answer:(q.options&&q.options.length) ? t.a : q.answer } : q;\n"
         "}\n"
         "function selectStoryOption(el, val){"),
        ("  const current = story.lines[idx];\n  if(!current){ return finishStory(); }",
         "  const current = story.lines[idx] && story.lines[idx].speaker === undefined ? storyQ(story.lines[idx]) : story.lines[idx];\n  if(!current){ return finishStory(); }"),
        ("  const current = storyState.story.lines[storyState.idx];\n  const given = current.q==='mc'",
         "  const current = storyQ(storyState.story.lines[storyState.idx]);\n  const given = current.q==='mc'"),
    ]
    for old, new in rep:
        if new in c:
            continue
        assert c.count(old) == 1, old[:70]
        c = c.replace(old, new)

    # 3) Engelse begripsvragen als tabel: sleutel = Nederlandse vraag + opties (zelfde vraag kan andere opties hebben)
    qs = {}
    for t in json.load(open(os.path.join(EN, 'story_questions_en.json'), encoding='utf-8')):
        if t['options']:
            assert len(t['options_en']) == len(t['options']), t['question']
        qs[t['question'] + '\u0001' + '\u0001'.join(t['options'])] = {'q': t['question_en'], 'o': t['options_en'], 'a': t['answer_en']}
    line = 'const STORY_Q_EN = ' + json.dumps(qs, ensure_ascii=False) + ';\n'
    m = re.search(r'const STORY_Q_EN = .*;\n', c)
    if m:
        c = c[:m.start()] + line + c[m.end():]
    else:
        i = c.index('const STORY_CHARACTERS =')
        c = c[:i] + '// Engelse begripsvragen bij de verhaaltjes (NL-vraag + opties -> {q, o, a}); zie dev/english_content.py\n' + line + c[i:]
    n = len(qs)
    open(PATH, 'w', encoding='utf-8').write(c)
    print(len(intros), 'intro\'s,', n, 'begripsvragen')

if __name__ == '__main__':
    main()
