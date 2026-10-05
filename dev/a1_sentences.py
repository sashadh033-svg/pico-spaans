# A1: zinnen met grammatica die nog niet behandeld is vervangen, en geleerde vormen laten terugkomen.
# Gebruik: python3 dev/a1_sentences.py   (idempotent)
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sentence_tools import replace_sentences, replace_text

TE_VROEG = 'te vroeg'      # grammatica die nog niet behandeld is
HERHALING = 'herhaling'    # eerder geleerde vorm laten terugkomen
DUBBEL = 'dubbel'          # zin stond al in een eerdere unit

CHANGES = [
    ('a1-u11-l2', 'Sigue todo recto.',
        ['Sigues todo recto.', 'Je gaat rechtdoor.', 'You go straight on.', ['Sigue todo recto.']],
        (TE_VROEG, 'De gebiedende wijs (sigue) komt pas in A2. Bij de weg wijzen is de tegenwoordige tijd heel gewoon.')),
    ('a1-u11-l2', 'Cruza la plaza y gira a la izquierda.',
        ['Cruzas la plaza y giras a la izquierda.', 'Je steekt het plein over en slaat linksaf.', 'You cross the square and turn left.', ['Cruza la plaza y gira a la izquierda.']],
        (TE_VROEG, 'Gebiedende wijs → tegenwoordige tijd.')),
    ('a1-u19-l4', '¿Qué vas a pedir?',
        ['¿Qué quieres pedir?', 'Wat wil je bestellen?', 'What do you want to order?'],
        (TE_VROEG, 'Ir a + infinitief komt pas in unit 22.')),
    ('a1-u20-l3', 'Voy a hacer la maleta esta noche.',
        ['Esta noche hago la maleta.', 'Vanavond pak ik mijn koffer.', 'Tonight I pack my suitcase.', ['Hago la maleta esta noche.']],
        (TE_VROEG, 'Ir a + infinitief komt pas in unit 22.')),
    ('a1-u21-l1', 'Me lavo las manos.',
        ['Tengo las manos frías.', 'Ik heb koude handen.', 'My hands are cold.'],
        (DUBBEL, 'Deze zin stond al in unit 16.')),
    ('a1-u23-l1', 'Todavía no he comido.',
        ['Todavía no he comido, voy a comer ahora.', 'Ik heb nog niet gegeten, ik ga nu eten.', "I haven't eaten yet, I'm going to eat now.", ['Aún no he comido, voy a comer ahora.', 'Todavía no he comido, ahora voy a comer.', 'Aún no he comido, ahora voy a comer.']],
        (HERHALING, 'Voltooide tijd + ir a (unit 22).')),
    ('a1-u23-l3', 'Nunca he estado en España.',
        ['Nunca he estado en España, pero voy a ir este verano.', 'Ik ben nog nooit in Spanje geweest, maar ik ga deze zomer.', "I've never been to Spain, but I'm going this summer."],
        (HERHALING, 'Voltooide tijd + ir a (unit 22).')),
    ('a1-u23-l4', 'Hemos comido ya.',
        ['Hemos preparado la cena y ahora vamos a comer.', 'We hebben het avondeten klaargemaakt en nu gaan we eten.', "We've made dinner and now we're going to eat."],
        (HERHALING, 'Voltooide tijd + ir a (unit 22).')),
    # Engelse vertaling in de voltooide tijd, anders lokt "I called" uit dat je "he" weglaat
    ('a1-u23-l1', 'Hace un rato he llamado a Ana.',
        ['Hace un rato he llamado a Ana.', 'Ik heb Ana net gebeld.', "I've just called Ana.", ['He llamado a Ana hace un rato.']],
        (HERHALING, 'Engels in de voltooide tijd.')),
    ('a1-u23-l2', 'He vuelto a casa muy tarde.',
        ['He vuelto a casa muy tarde.', 'Ik ben heel laat thuisgekomen.', "I've come home very late."],
        (HERHALING, 'Engels in de voltooide tijd.')),
]

# 'Nací en...' wordt in a1-u3 als woord geleerd: uitleggen dat het een vaste uitdrukking is.
NACI_OLD = '<p class="muted"><i>Vivo <b>en</b> Ámsterdam</i>: wonen <b>in</b> een plaats is altijd <b>en</b>.</p>`'
NACI_NEW = ('<p class="muted"><i>Vivo <b>en</b> Ámsterdam</i>: wonen <b>in</b> een plaats is altijd <b>en</b>.</p>'
            '<p class="muted"><i><b>Nací</b> en Holanda</i> — ik ben geboren in Nederland. Leer <i>nací</i> voor nu als vaste uitdrukking; de verleden tijd komt later.</p>`')

if __name__ == '__main__':
    replace_sentences([(l, o, n, r) for l, o, n, r in CHANGES])
    replace_text(NACI_OLD, NACI_NEW)
