# Kleine losse fixes naar aanleiding van screenshots (zinnen en woorden). Idempotent.
# Gebruik: python3 dev/misc_fixes.py
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sentence_tools import replace_sentences, replace_text

SENTENCES = [
    # "wakes me up" lokte despertar uit; despejar = je hoofd helder maken. Beide goed rekenen.
    ('a2-u1-l4', 'Un café solo me despeja por la mañana.',
        ['Un café solo me despeja por la mañana.', "Een zwarte koffie maakt mijn hoofd 's ochtends helder.",
         'A black coffee clears my head in the morning.',
         ['Un café solo me despierta por la mañana.', 'Por la mañana un café solo me despeja.']],
        'despejar ≠ despertar'),
    # "esta noche" met perfecto = afgelopen nacht: verwarrend; en soñar CON (niet a)
    ('a2-u2-l3', 'Esta noche he soñado con mis vacaciones.',
        ['He soñado con mis vacaciones.', 'Ik heb over mijn vakantie gedroomd.', "I've dreamt about my holiday.",
         ['Esta noche he soñado con mis vacaciones.']],
        'esta noche = vanavond verwarrend'),
]
# tikhulp bij vervangen zinnen: {nieuwe zin: [[es, nl, en, tip_nl, tip_en], ...]}
HINTS = {
    'He soñado con mis vacaciones.': [['soñado', 'gedroomd', 'dreamt', 'gedroomd (soñar)', 'dreamt (soñar)'],
                                      ['con', 'over', 'about', 'soñar con = dromen over', 'soñar con = dream about']],
}
WORDS = [
    ('["despejarse", "helder worden / wakker worden", "to clear one\'s head"]',
     '["despejarse", "helder worden (in je hoofd)", "to clear one\'s head"]'),
]

if __name__ == '__main__':
    replace_sentences(SENTENCES)
    for old, new in WORDS:
        replace_text(old, new)
    from a2_vocab import add_hints
    from sentence_tools import PATH
    c = open(PATH, encoding='utf-8').read()
    open(PATH, 'w', encoding='utf-8').write(add_hints(c, HINTS))
