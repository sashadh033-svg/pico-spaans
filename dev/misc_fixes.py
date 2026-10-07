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
]
WORDS = [
    ('["despejarse", "helder worden / wakker worden", "to clear one\'s head"]',
     '["despejarse", "helder worden (in je hoofd)", "to clear one\'s head"]'),
]

if __name__ == '__main__':
    replace_sentences(SENTENCES)
    for old, new in WORDS:
        replace_text(old, new)
