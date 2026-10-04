# Verhaaltjes (STORIES): zinnen met grammatica die op dat moment nog niet behandeld is vervangen.
# Zelfde regels als dev/a1_sentences.py, a2_sentences.py en b1_sentences.py.
# Gebruik: python3 dev/story_fixes.py   (idempotent)
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sentence_tools import PATH, replace_text

# (unit, oude es, nieuwe es, nieuwe nl, nieuwe en, reden)
FIXES = [
    ('a1-u11', 'De nada. ¡Que tengas un buen día!', 'De nada. ¡Hasta luego!', 'Graag gedaan. Tot ziens!', "You're welcome. See you!", '"Que tengas" is subjuntivo (B1).'),
    ('a1-u19', 'Perfecto. ¿Qué vas a pedir?', 'Perfecto. ¿Qué quieres pedir?', 'Perfect. Wat wil je bestellen?', 'Perfect. What do you want to order?', 'Ir a komt pas in unit 22.'),
    ('a1-u19', 'Sí, y voy a dejar propina.', 'Sí, y dejo propina.', 'Ja, en ik geef een fooi.', "Yes, and I'll leave a tip.", 'Ir a komt pas in unit 22.'),
    ('a1-u19', 'Buena idea, el camarero fue muy amable.', 'Buena idea, el camarero es muy amable.', 'Goed idee, de ober is heel vriendelijk.', 'Good idea, the waiter is very kind.', 'Fue (verleden tijd) komt pas in A2.'),
    ('a1-u20', '¿Cómo vas a viajar, en tren o en avión?', '¿Cómo viajas, en tren o en avión?', 'Hoe reis je, met de trein of met het vliegtuig?', 'How are you travelling, by train or by plane?', 'Ir a komt pas in unit 22.'),
    ('a1-u21', 'Sí, voy a comprar algo después.', 'Sí, después compro algo.', 'Ja, ik koop straks iets.', "Yes, I'll buy something later.", 'Ir a komt pas in unit 22.'),
    ('a1-u22', '¡Qué aburrido! Deberías descansar también.', '¡Qué aburrido! Tienes que descansar también.', 'Wat saai! Je moet ook rusten.', 'How boring! You have to rest too.', 'Deberías (condicional) komt pas in B1.'),
    ('a1-u22', '¡Me encantaría! ¿Adónde vamos a ir?', '¡Sí, me encanta la idea! ¿Adónde vamos a ir?', 'Ja, leuk idee! Waar gaan we naartoe?', 'Yes, I love the idea! Where are we going to go?', 'Me encantaría (condicional) komt pas in B1.'),
    ('a2-u6', 'Sí, ganamos. ¡El entrenador estaba muy contento!', 'Sí, ganamos. ¡El entrenador está muy contento!', 'Ja, we hebben gewonnen. De trainer is heel blij!', 'Yes, we won. The coach is very happy!', 'De imperfecto komt pas in unit 32.'),
    ('a2-u8', 'Sí, una vez tuve que transbordar y perdí la conexión.', 'Sí, una vez perdí la conexión al transbordar.', 'Ja, een keer miste ik de aansluiting bij het overstappen.', 'Yes, once I missed the connection when changing.', 'Tuve (onregelmatig) komt pas in unit 34.'),
    ('a2-u13', 'Una vez me perdí allí, pero fue una aventura.', 'Una vez me perdí allí. ¡Qué aventura!', 'Een keer verdwaalde ik daar. Wat een avontuur!', 'Once I got lost there. What an adventure!', 'Fue (onregelmatig) komt pas in unit 34.'),
    ('a2-u13', '¿Fue un viaje inolvidable entonces?', '¿Ha sido un viaje inolvidable entonces?', 'Was het dan een onvergetelijke reis?', 'So has it been an unforgettable trip?', 'Fue (onregelmatig) komt pas in unit 34.'),
    ('a2-u14', 'Mi hermano es mayor que yo, le encantaría esto.', 'Mi hermano es mayor que yo, y le encanta esto.', 'Mijn broer is ouder dan ik, en hij vindt dit geweldig.', 'My brother is older than me, and he loves this.', 'Encantaría (condicional) komt pas in B1.'),
    ('a2-u20', 'El camarero fue muy amable, dejemos buena propina.', 'El camarero ha sido muy amable; vamos a dejar buena propina.', 'De ober was heel aardig; laten we een flinke fooi geven.', "The waiter has been very kind; let's leave a good tip.", 'Fue (onregelmatig) en dejemos (subjuntivo) komen later.'),
    ('a2-u25', 'Deberías ir al médico.', 'Tienes que ir al médico.', 'Je moet naar de dokter.', 'You have to go to the doctor.', 'Deberías (condicional) komt pas in B1.'),
    ('a2-u26', 'Deberías tomar medicina y descansar.', 'Tienes que tomar medicina y descansar.', 'Je moet medicijnen nemen en rusten.', 'You have to take medicine and rest.', 'Deberías (condicional) komt pas in B1.'),
    ('a2-u31', 'Deberíamos celebrar este éxito.', 'Tenemos que celebrar este éxito.', 'We moeten dit succes vieren.', 'We have to celebrate this success.', 'Deberíamos (condicional) komt pas in B1.'),
    ('b1-u1', 'Es verdad, sin embargo, no creo que sea tan sencillo.', 'Es verdad, sin embargo, creo que no es tan sencillo.', 'Dat is waar, maar ik denk dat het niet zo simpel is.', "That's true, but I think it isn't that simple.", 'No creo que + subjuntivo komt pas in unit 3/15.'),
    ('b1-u1', 'Además, es posible que algunas personas se sientan solas.', 'Además, algunas personas se sienten solas.', 'Bovendien voelen sommige mensen zich eenzaam.', 'Moreover, some people feel lonely.', 'Es posible que + subjuntivo komt pas in unit 3.'),
    ('b1-u1', 'Por eso creo que cada empresa debería decidir por su cuenta.', 'Por eso creo que cada empresa tiene que decidir por su cuenta.', 'Daarom vind ik dat elk bedrijf het zelf moet beslissen.', 'That is why I think each company has to decide for itself.', 'Debería (condicional) komt pas in unit 12.'),
    ('b1-u4', 'Y si no sale bien, no pasa nada. Habrá otras oportunidades.', 'Y si no sale bien, no pasa nada. Va a haber otras oportunidades.', 'En als het niet lukt, is het niet erg. Er komen nog andere kansen.', "And if it doesn't work out, it's fine. There are going to be other chances.", 'De futuro komt pas in unit 33.'),
    ('b1-u7', 'Sí, y mis cuñados con los niños. Seremos quince.', 'Sí, y mis cuñados con los niños. Vamos a ser quince.', 'Ja, en mijn zwagers met de kinderen. We worden met z’n vijftienen.', "Yes, and my in-laws with the kids. We're going to be fifteen.", 'De futuro komt pas in unit 33.'),
    ('b1-u8', 'Creo que deberíamos prohibir los coches en el centro.', 'Creo que hay que prohibir los coches en el centro.', 'Ik vind dat auto’s in het centrum verboden moeten worden.', 'I think cars should be banned in the centre.', 'Deberíamos (condicional) komt pas in unit 12.'),
    ('b1-u10', 'Clásico. ¿Cuándo te darán una respuesta?', 'Clásico. ¿Cuándo te van a dar una respuesta?', 'Klassiek. Wanneer krijg je antwoord?', 'Classic. When are they going to give you an answer?', 'De futuro komt pas in unit 33.'),
    ('b1-u18', 'Buena idea. Aunque me quedaré sin saber qué pasa en el grupo.', 'Buena idea. Aunque me voy a quedar sin saber qué pasa en el grupo.', 'Goed idee. Al weet ik dan niet wat er in de groep gebeurt.', "Good idea. Although I'm not going to know what's happening in the group.", 'De futuro komt pas in unit 33.'),
    ('b1-u23', 'Tranquila, por fin terminaremos. Paso a paso.', 'Tranquila, por fin vamos a terminar. Paso a paso.', 'Rustig maar, uiteindelijk worden we klaar. Stap voor stap.', "Relax, we're going to finish in the end. Step by step.", 'De futuro komt pas in unit 33.'),
]

# Typvraag in het verhaaltje van b1-u1 vroeg om 'Dudo que ... sea' (subjuntivo, unit 15).
Q_OLD = "{ q:'type', question:\"Vul aan met de juiste twijfel-uitdrukking: '______ que el trabajo remoto sea la solución para todos.' (ik betwijfel)\", answer:'Dudo' }"
Q_NEW = "{ q:'type', question:\"Vul aan: 'En mi ______, el trabajo remoto no es la solución para todos.' (mening)\", answer:'opinión' }"

STR = r"""(?P<q>['"])(?:\\.|(?!(?P=q)).)*(?P=q)"""

def _q(s, quote):
    return s.replace('\\', '\\\\').replace(quote, '\\' + quote)

def run():
    c = open(PATH, encoding='utf-8').read()
    a = c.index('const STORIES =')
    b = c.index('\n};', a)
    blk = c[a:b]
    done = 0
    for uid, old, new, nl, en, why in FIXES:
        hit = None
        for quote in ("'", '"'):
            for es in (old, new):
                lit = quote + _q(es, quote) + quote
                k = blk.find(lit)
                if k >= 0:
                    hit = (k, lit, quote, es == new)
                    break
            if hit: break
        assert hit, 'verhaalzin niet gevonden: ' + old
        k, lit, quote, already = hit
        end = blk.index('}', blk.index('trans', k)) + 1
        seg = blk[k:end]
        seg = seg.replace(lit, quote + _q(new, quote) + quote, 1)
        seg = re.sub(r'(nl"?\s*:\s*)' + STR, lambda m: m.group(1) + quote + _q(nl, quote) + quote, seg, count=1)
        seg = re.sub(r'(en"?\s*:\s*)' + STR, lambda m: m.group(1) + quote + _q(en, quote) + quote, seg, count=1)
        blk = blk[:k] + seg + blk[end:]
        done += 1
    c = c[:a] + blk + c[b:]
    open(PATH, 'w', encoding='utf-8').write(c)
    replace_text(Q_OLD, Q_NEW)
    print(done, 'verhaalzinnen gecontroleerd/aangepast')

if __name__ == '__main__':
    run()
