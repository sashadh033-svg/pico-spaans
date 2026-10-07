# A2 unit 1: wederkerende werkwoorden in de voltooide tijd (me he levantado, me he quedado dormido,
# me he dado un madrugón) werden nergens uitgelegd. Uitleg vóór het eerste bolletje.
# (darse un madrugón is later uit de A2-lijst gehaald, zie dev/a2_vocab.py).
# Gebruik: python3 dev/a2u1_reflexive.py && python3 dev/english_content.py   (idempotent)
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sentence_tools import PATH, replace_text

INTRO_NL = ('<h2 class="section-title" style="margin-top:0;">Me he levantado — wederkerend in de voltooide tijd</h2>'
            '<p class="muted">Bij een wederkerend werkwoord (<i>levantarse, ducharse, quedarse</i>) staat <b>me/te/se</b> vóór <b>he/has/ha</b>:</p>'
            '<p class="muted"><i>Me levanto</i> → <i><b>Me he</b> levantado</i> — ik ben opgestaan<br>'
            '<i>¿<b>Te has</b> duchado?</i> — heb je gedoucht?<br>'
            '<i>Ana <b>se ha</b> vestido.</i> — Ana heeft zich aangekleed</p>'
            '<p class="muted">Vaste uitdrukking uit deze unit: <i><b>quedarse dormido</b></i> = zich verslapen '
            '(<i>Hoy me he quedado dormido</i>).</p>')
OLD_NL_END = ('<p class="muted">Twee vaste uitdrukkingen uit deze unit: <i><b>quedarse dormido</b></i> = zich verslapen '
            '(<i>Hoy me he quedado dormido</i>) en <i><b>darse un madrugón</b></i> = heel vroeg opstaan '
            '(<i>Hoy me he dado un madrugón</i>).</p>')
INTRO_EN = ('<h2 class="section-title" style="margin-top:0;">Me he levantado — reflexive verbs in the perfect</h2>'
            '<p class="muted">With a reflexive verb (<i>levantarse, ducharse, quedarse</i>), <b>me/te/se</b> goes before <b>he/has/ha</b>:</p>'
            '<p class="muted"><i>Me levanto</i> → <i><b>Me he</b> levantado</i> — I\'ve got up<br>'
            '<i>¿<b>Te has</b> duchado?</i> — have you showered?<br>'
            '<i>Ana <b>se ha</b> vestido.</i> — Ana has got dressed</p>'
            '<p class="muted">A set phrase from this unit: <i><b>quedarse dormido</b></i> = to oversleep '
            '(<i>Hoy me he quedado dormido</i>).</p>')

def main():
    # eerdere versie noemde ook 'darse un madrugón' (inmiddels uit de A2-lijst): bijwerken
    c = open(PATH, encoding='utf-8').read()
    if OLD_NL_END in c:
        open(PATH, 'w', encoding='utf-8').write(c.replace(OLD_NL_END, INTRO_NL[INTRO_NL.index('<p class="muted">Vaste'):]))
    # uitleg vóór het eerste bolletje van A2 unit 1
    replace_text("{ id:'a2-u1-l1', kind:'new', topic:'Mijn ochtendroutine', words:",
                 "{ id:'a2-u1-l1', kind:'new', topic:'Mijn ochtendroutine', intro:`" + INTRO_NL + "`, words:")
    # woord = de uitdrukking zoals hij in de zin staat
    # (woord 'el madrugón'/'darse un madrugón' is later uit de A2-lijst gehaald: dev/a2_vocab.py)
    # Engelse uitleg
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'en', 'intros_en.json')
    d = json.load(open(p, encoding='utf-8'))
    d['a2-u1-l1'] = INTRO_EN
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('klaar; draai nu dev/english_content.py')

if __name__ == '__main__':
    main()
