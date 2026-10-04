# Keuze-oefening 'Presente of estar + gerundio?' + betere uitleg wanneer je welke gebruikt.
# Gebruik: python3 dev/add_pres_prog_choice.py   (idempotent)
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from a1_intros import card, ex

def it(q, a, nl, en, alts=None):
    d = {"q": q, "a": a, "nl": nl, "en": en}
    if alts: d["alts"] = alts
    return d

POOL = [
 it("Normalmente ______ (trabajar, yo) en la oficina.", "trabajo", "Normaal werk ik op kantoor.", "Normally I work at the office."),
 it("Hoy no puedo hablar, ______ (trabajar, yo).", "estoy trabajando", "Ik kan vandaag niet praten, ik ben aan het werken.", "I can't talk today, I'm working."),
 it("¡Shh! El bebé ______ (dormir).", "está durmiendo", "Sst! De baby slaapt.", "Shh! The baby is sleeping."),
 it("Mi padre siempre ______ (dormir) la siesta.", "duerme", "Mijn vader doet altijd een middagdutje.", "My father always takes a nap."),
 it("Mañana ______ (salir, nosotros) a las ocho.", "salimos", "Morgen vertrekken we om acht uur.", "Tomorrow we're leaving at eight.", ["vamos a salir"]),
 it("¿Adónde vas? — ______ (ir, yo) al supermercado.", "voy", "Waar ga je heen? — Ik ga naar de supermarkt.", "Where are you going? — I'm going to the supermarket."),
 it("¡Un momento, ya ______ (ir, yo)!", "voy", "Momentje, ik kom eraan!", "One moment, I'm coming!"),
 it("______ (tener, yo) mucha hambre.", "tengo", "Ik heb veel honger.", "I'm very hungry."),
 it("Mi hermana ______ (querer) un perro.", "quiere", "Mijn zus wil een hond.", "My sister wants a dog."),
 it("Mira, ______ (llover) mucho.", "está lloviendo", "Kijk, het regent hard.", "Look, it's raining hard."),
 it("En Holanda ______ (llover) mucho en otoño.", "llueve", "In Nederland regent het veel in de herfst.", "In the Netherlands it rains a lot in autumn."),
 it("______ (vivir, yo) en Ámsterdam desde hace diez años.", "vivo", "Ik woon al tien jaar in Amsterdam.", "I've been living in Amsterdam for ten years."),
 it("Esta semana ______ (dormir, yo) en casa de mi tía.", "estoy durmiendo", "Deze week slaap ik bij mijn tante.", "This week I'm sleeping at my aunt's.", ["duermo"]),
 it("Los domingos ______ (comer, nosotros) con mis abuelos.", "comemos", "Op zondag eten we bij mijn opa en oma.", "On Sundays we eat with my grandparents."),
 it("No puedo abrir la puerta, ______ (ducharse, yo).", "me estoy duchando", "Ik kan de deur niet opendoen, ik sta onder de douche.", "I can't open the door, I'm in the shower.", ["estoy duchándome", "estoy duchandome"]),
 it("¿______ (conocer, tú) a Pedro?", "conoces", "Ken jij Pedro?", "Do you know Pedro?"),
 it("Ahora no, ______ (ver, yo) una película.", "estoy viendo", "Nu niet, ik zit een film te kijken.", "Not now, I'm watching a film."),
 it("¿Qué ______ (hacer, tú) los fines de semana?", "haces", "Wat doe je in het weekend?", "What do you do at weekends?"),
 it("El tren ______ (llegar) mañana a las nueve.", "llega", "De trein komt morgen om negen uur aan.", "The train arrives tomorrow at nine."),
 it("¡Mira, el tren ya ______ (llegar)!", "está llegando", "Kijk, de trein komt er al aan!", "Look, the train is arriving!"),
 it("Ana ______ (saber) hablar inglés.", "sabe", "Ana kan Engels spreken.", "Ana can speak English."),
 it("Son las diez y los niños todavía ______ (jugar).", "están jugando", "Het is tien uur en de kinderen zijn nog steeds aan het spelen.", "It's ten o'clock and the children are still playing."),
 it("Mis hijos ______ (jugar) al fútbol todos los sábados.", "juegan", "Mijn kinderen voetballen elke zaterdag.", "My children play football every Saturday."),
 it("Me ______ (gustar) mucho el chocolate.", "gusta", "Ik hou erg van chocolade.", "I really like chocolate."),
 it("Últimamente ______ (estudiar, yo) mucho para el examen.", "estoy estudiando", "De laatste tijd ben ik veel aan het leren voor het examen.", "Lately I've been studying a lot for the exam."),
 it("Siempre ______ (estudiar, yo) por la noche.", "estudio", "Ik studeer altijd 's avonds.", "I always study in the evening."),
 it("¿Dónde estás? — En la parada, te ______ (esperar, yo).", "estoy esperando", "Waar ben je? — Bij de halte, ik sta op je te wachten.", "Where are you? — At the stop, I'm waiting for you.", ["espero"]),
 it("El sábado ______ (cenar, nosotros) en casa de Luis.", "cenamos", "Zaterdag eten we bij Luis.", "On Saturday we're having dinner at Luis's.", ["vamos a cenar"]),
 it("Hoy ______ (llevar, yo) una camisa azul.", "llevo", "Ik heb vandaag een blauw overhemd aan.", "Today I'm wearing a blue shirt.", ["estoy llevando"]),
 it("¿Por qué no contestas? — Perdona, ______ (cocinar, yo).", "estoy cocinando", "Waarom neem je niet op? — Sorry, ik ben aan het koken.", "Why don't you answer? — Sorry, I'm cooking."),
]

RULES_HTML = card('Nu of altijd?',
   'Spaans gebruikt <b>estar + gerundio</b> alleen als je wilt benadrukken dat iets <b>nu bezig</b> is (of tijdelijk): <i>Hoy <b>estoy trabajando</b> en casa.</i>',
   'In alle andere gevallen gebruik je gewoon de <b>presente</b>, ook waar je in het Engels -ing zegt:',
   ex('gewoontes: <i>Normalmente <b>trabajo</b> en la oficina.</i>',
      'plannen/toekomst: <i>Mañana <b>salgo</b> a las ocho.</i> (niet <s>estoy saliendo</s>)',
      'ir en venir: <i>¡Ya <b>voy</b>!</i> — Ik kom eraan!',
      'toestanden: <i><b>Tengo</b> hambre. <b>Quiero</b> un café. <b>Sé</b> nadar.</i>'),
   'Twijfel je? De presente is bijna nooit fout. <i>¿Qué haces?</i> kan ook "wat ben je aan het doen?" betekenen.')

OLD_GUIDE_CARD_START = '<h2 class="section-title" style="margin-top:0;">Wanneer gebruik je het?</h2>'
NEW_GUIDE_CARD = ('<h2 class="section-title" style="margin-top:0;">Wanneer gebruik je het? (en wanneer niet)</h2>\n'
 '        <div class="muted" style="line-height:1.55;"><b>Wel</b>: iets is <b>nu</b> bezig of tijdelijk: <i>Ahora estoy comiendo. Esta semana estoy trabajando mucho.</i><br>'
 '<b>Niet</b> bij gewoontes en feiten: <i>Normalmente como a las dos. Vivo en Madrid.</i><br>'
 '<b>Niet</b> voor de toekomst (in het Engels wel!): <i>I\'m leaving tomorrow</i> = <i>Me voy mañana / Salgo mañana</i>.<br>'
 '<b>Niet</b> met <i>ir</i> en <i>venir</i>: <i>¡Ya voy!</i> (I\'m coming!), <i>Voy al trabajo</i> (I\'m going to work).<br>'
 '<b>Niet</b> met toestandswerkwoorden: <i>tener, querer, saber, conocer, gustar, ser, parecer</i>: <i>Tengo frío</i>, niet <s>estoy teniendo frío</s>.<br>'
 'Spaans gebruikt het dus veel minder dan Engels. Twijfel je, kies dan de presente: die is bijna nooit fout.</div>')

# Recurrence: keuze-oefening wordt bijgemengd in de 🏋️-oefening van latere units
MIX_UNITS = ['a1-u17p','a1-u18','a1-u19','a1-u20','a1-u21','a1-u22','a1-u23','a2-u2','a2-u3','a2-u4','a2-u6','a2-u15','a2-u26']

def rep(c, old, new):
    assert c.count(old) == 1, old[:80]
    return c.replace(old, new)

def main(path='index.html'):
    c = open(path, encoding='utf-8').read()
    if '"pres_prog"' in c:
        print('al aanwezig'); return
    J = lambda x: json.dumps(x, ensure_ascii=False)
    c = rep(c, 'const CHOICE_POOL = {', 'const CHOICE_POOL = {"pres_prog": ' + J(POOL) + ', ')
    c = rep(c, 'const CHOICE_BADGE = {', 'const CHOICE_BADGE = {"pres_prog": ["🤔 Presente of estar + gerundio? Vul de juiste vorm in", "🤔 Present or estar + gerund? Fill in the right form"], ')
    c = rep(c, 'const TRAINER_LABEL = {', 'const TRAINER_LABEL = {"pres_prog": "Presente of estar + gerundio", ')
    c = rep(c, 'const TRAINER_NODES = {', 'const TRAINER_NODES = {"a1-u17p": ["pres_prog"], ')
    # bijmengen in 🏋️ van deze en latere units
    c = rep(c, 'function buildVerbPracticeItem(unitId){',
        '// estar + gerundio blijft terugkomen: keuze presente/progresivo bijmengen in de werkwoordoefening van latere units\n'
        + J(MIX_UNITS) + ".forEach(id=>{ const v = VERB_PRACTICE[id]; if(!v || v.mode==='keuze' || v.mode==='pronombres') return;\n"
        "  v.mix = v.mix ? { pools:[...v.mix.pools, 'pres_prog'], rate: v.mix.rate } : { pools:['pres_prog'], rate: id==='a1-u17p' ? 0.4 : 0.25 }; });\n"
        'function buildVerbPracticeItem(unitId){')
    # uitleg les 3 + gids
    i = c.index("id:'a1-u17p-l3', kind:'new', topic:'Estar + gerundio', intro:`") + len("id:'a1-u17p-l3', kind:'new', topic:'Estar + gerundio', intro:`")
    j = c.index('`', i)
    c = c[:i] + RULES_HTML + c[j:]
    gi = c.index(OLD_GUIDE_CARD_START, c.index("GUIDES['a1-u17p']"))
    ge = c.index('</div>', c.index('<div class="muted"', gi)) + len('</div>')
    c = c[:gi] + NEW_GUIDE_CARD + c[ge:]
    open(path, 'w', encoding='utf-8').write(c)
    print('klaar:', len(POOL), 'keuze-zinnen')

if __name__ == '__main__':
    main(*(sys.argv[1:2]))
