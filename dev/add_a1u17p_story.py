# Voegt een verhaaltje (STORIES) toe aan unit a1-u17p (estar + gerundio).
# Alleen presente en estar + gerundio, woorden uit de unit. Gebruik: python3 dev/add_a1u17p_story.py (idempotent)
import os
PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'index.html')

STORY = r"""  'a1-u17p': {
    lines: [
      { speaker:1, es:'¡Hola, Ana! ¿Qué estás haciendo?', trans:{nl:'Hoi Ana! Wat ben je aan het doen?', en:'Hi Ana! What are you doing?'} },
      { speaker:0, es:'Estoy cocinando. Mi hermana está viniendo a cenar.', trans:{nl:'Ik ben aan het koken. Mijn zus komt eten.', en:'I\'m cooking. My sister is coming for dinner.'} },
      { speaker:1, es:'¡Qué bien! Yo estoy trabajando en la oficina.', trans:{nl:'Wat leuk! Ik ben op kantoor aan het werk.', en:'How nice! I\'m working at the office.'} },
      { q:'mc', question:'Wat is Ana aan het doen?', options:['Koken', 'Werken', 'Slapen'], answer:'Koken' },
      { speaker:0, es:'¿Ahora? Normalmente terminas a las cinco.', trans:{nl:'Nu nog? Normaal ben je om vijf uur klaar.', en:'Now? You normally finish at five.'} },
      { speaker:1, es:'Sí, pero esta semana estoy trabajando mucho.', trans:{nl:'Ja, maar deze week ben ik veel aan het werk.', en:'Yes, but this week I\'m working a lot.'} },
      { speaker:0, es:'¿Y qué tiempo hace allí? Aquí está lloviendo mucho.', trans:{nl:'En wat voor weer is het daar? Hier regent het hard.', en:'And what\'s the weather like there? It\'s raining a lot here.'} },
      { speaker:1, es:'Aquí también. ¿Y tu perro? ¿Está durmiendo?', trans:{nl:'Hier ook. En je hond? Ligt hij te slapen?', en:'Here too. And your dog? Is he sleeping?'} },
      { q:'mc', question:'Waarom is Carlos nog aan het werk?', options:['Hij werkt deze week veel', 'Hij heeft vrij', 'Het regent'], answer:'Hij werkt deze week veel' },
      { speaker:0, es:'No, está comiendo mi pan. ¡Hasta luego!', trans:{nl:'Nee, hij zit mijn brood op te eten. Tot later!', en:'No, he\'s eating my bread. See you later!'} },
      { q:'mc', question:'Wat doet Ana\'s hond?', options:['Hij eet haar brood op', 'Hij slaapt', 'Hij is buiten'], answer:'Hij eet haar brood op' }
    ]
  },
"""

c = open(PATH, encoding='utf-8').read()
start = c.index('const STORIES =')
if "  'a1-u17p': {\n    lines:" in c[start:]:
    print('al aanwezig')
else:
    anchor = c.index("  'a1-u18': {\n    lines:", start)
    c = c[:anchor] + STORY + c[anchor:]
    open(PATH, 'w', encoding='utf-8').write(c)
    print('verhaaltje toegevoegd')
