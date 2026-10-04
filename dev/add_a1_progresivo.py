# Voegt A1-unit 'a1-u17p' (estar + gerundio) toe na a1-u17, plus slot-logica voor later toegevoegde units.
# Gebruik: python3 dev/add_a1_progresivo.py   (idempotent)
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from a1_intros import card, ex

J = lambda x: json.dumps(x, ensure_ascii=False)

L1 = dict(
 intro=card('Wat ben je aan het doen?',
   'Wat je <b>nu, op dit moment</b> aan het doen bent, zeg je met <b>estar</b> + het gerundio (de -end-vorm):',
   '<b>-ar → -ando</b>: <i>hablar → habl<b>ando</b></i>. <b>-er/-ir → -iendo</b>: <i>comer → com<b>iendo</b>, escribir → escrib<b>iendo</b></i>.',
   ex('<i><b>Estoy</b> trabaj<b>ando</b>.</i> — Ik ben aan het werken.', '<i>¿Qué <b>estás</b> hac<b>iendo</b>?</i> — Wat ben je aan het doen?'),
   'Alleen <i>estar</i> verandert (estoy, estás, está...). Het gerundio blijft altijd hetzelfde.'),
 words=[["estoy trabajando","ik ben aan het werken","I am working"],["estás hablando","jij bent aan het praten","you are talking"],["está cocinando","hij/zij is aan het koken","he/she is cooking"],["estamos estudiando","wij zijn aan het studeren","we are studying"],["están escuchando","zij zijn aan het luisteren","they are listening"],["estoy comiendo","ik ben aan het eten","I am eating"],["estás bebiendo","jij bent aan het drinken","you are drinking"],["está escribiendo","hij/zij is aan het schrijven","he/she is writing"],["¿Qué estás haciendo?","Wat ben je aan het doen?","What are you doing?"]],
 sentences=[["Estoy trabajando en casa.","Ik ben thuis aan het werken.","I am working at home."],["¿Qué estás haciendo?","Wat ben je aan het doen?","What are you doing?"],["Estoy cocinando la cena.","Ik ben het avondeten aan het koken.","I am cooking dinner."],["Mi madre está hablando por teléfono.","Mijn moeder is aan het bellen.","My mother is talking on the phone."],["Estamos comiendo en el restaurante.","We zijn in het restaurant aan het eten.","We are eating at the restaurant."],["Ella está escribiendo un correo.","Zij is een e-mail aan het schrijven.","She is writing an email."],["¿Estás estudiando español?","Ben je Spaans aan het studeren?","Are you studying Spanish?"],["Los niños están jugando en el parque.","De kinderen zijn in het park aan het spelen.","The children are playing in the park."],["Estoy bebiendo un café.","Ik ben een koffie aan het drinken.","I am drinking a coffee."],["Mis amigos están escuchando música.","Mijn vrienden zijn naar muziek aan het luisteren.","My friends are listening to music."]])

L2 = dict(
 intro=card('Onregelmatige gerundios',
   'Een paar werkwoorden doen het net anders:',
   ex('<i>leer → le<b>y</b>endo</i> — lezend (y in plaats van i)', '<i>traer → tra<b>y</b>endo</i>', '<i>dormir → d<b>u</b>rmiendo</i> — o wordt u', '<i>decir → d<b>i</b>ciendo</i>, <i>pedir → p<b>i</b>diendo</i>, <i>venir → v<b>i</b>niendo</i> — e wordt i'),
   'Weer kan ook: <i><b>Está lloviendo.</b></i> — Het regent (nu). <i>Está nevando.</i> — Het sneeuwt.'),
 words=[["estoy leyendo","ik ben aan het lezen","I am reading"],["está durmiendo","hij/zij is aan het slapen","he/she is sleeping"],["está lloviendo","het regent (nu)","it is raining"],["está nevando","het sneeuwt (nu)","it is snowing"],["estamos pidiendo","wij zijn aan het bestellen","we are ordering"],["está viniendo","hij/zij komt eraan","he/she is coming"],["están trayendo","zij zijn aan het brengen","they are bringing"],["¿Qué estás diciendo?","Wat zeg je nou?","What are you saying?"],["estoy durmiendo","ik ben aan het slapen","I am sleeping"]],
 sentences=[["Estoy leyendo un libro muy bueno.","Ik ben een heel goed boek aan het lezen.","I am reading a very good book."],["El bebé está durmiendo.","De baby is aan het slapen.","The baby is sleeping."],["Está lloviendo mucho hoy.","Het regent vandaag heel hard.","It is raining a lot today."],["¿Qué estás diciendo?","Wat zeg je nou?","What are you saying?"],["Estamos pidiendo la cena.","We zijn het avondeten aan het bestellen.","We are ordering dinner."],["Mi hermano está viniendo a casa.","Mijn broer is onderweg naar huis.","My brother is coming home."],["Los camareros están trayendo la comida.","De obers zijn het eten aan het brengen.","The waiters are bringing the food."],["Está nevando en la montaña.","Het sneeuwt in de bergen.","It is snowing in the mountains."],["Mis padres están durmiendo la siesta.","Mijn ouders doen een middagdutje.","My parents are taking a nap."],["Ella está leyendo el periódico.","Zij is de krant aan het lezen.","She is reading the newspaper."]])

L3 = dict(
 intro=card('Nu of altijd?',
   '<b>Gewone tegenwoordige tijd</b> = wat je normaal/altijd doet: <i>Trabajo en la oficina.</i> (Ik werk op kantoor.)',
   '<b>Estar + gerundio</b> = wat er <b>nu</b> (of deze week) gebeurt: <i>Hoy <b>estoy trabajando</b> en casa.</i>',
   'Signaalwoorden voor nu: <i>ahora, ahora mismo, en este momento, esta semana</i>. Voor gewoontes: <i>normalmente, siempre, a veces, los lunes</i>.'),
 words=[["ahora mismo","nu meteen / op dit moment","right now"],["en este momento","op dit moment","at the moment"],["normalmente","normaal gesproken","normally"],["esta semana","deze week","this week"],["¿Qué haces?","Wat doe je? (meestal)","What do you do?"],["siempre","altijd","always"],["a veces","soms","sometimes"],["estar ocupado/a","het druk hebben","to be busy"],["descansar","uitrusten","to rest"]],
 sentences=[["Normalmente trabajo en la oficina, pero hoy estoy trabajando en casa.","Normaal werk ik op kantoor, maar vandaag werk ik thuis.","Normally I work at the office, but today I'm working at home."],["¿Qué haces los sábados?","Wat doe je op zaterdag?","What do you do on Saturdays?"],["¿Qué estás haciendo ahora?","Wat ben je nu aan het doen?","What are you doing now?"],["Ahora mismo estoy comiendo.","Ik ben nu aan het eten.","I'm eating right now.",["Estoy comiendo ahora mismo."]],["En este momento estoy ocupado.","Op dit moment heb ik het druk.","At the moment I'm busy.",["Estoy ocupado en este momento."]],["Siempre bebo café por la mañana.","Ik drink 's ochtends altijd koffie.","I always drink coffee in the morning."],["Esta semana estoy estudiando mucho.","Deze week ben ik veel aan het studeren.","This week I'm studying a lot."],["Mi hermana vive en Madrid.","Mijn zus woont in Madrid.","My sister lives in Madrid."],["Juego al tenis los lunes, pero hoy estoy descansando.","Ik tennis op maandag, maar vandaag rust ik uit.","I play tennis on Mondays, but today I'm resting."],["Ana está ocupada, está hablando con su jefe.","Ana heeft het druk, ze is met haar baas aan het praten.","Ana is busy, she's talking to her boss."]])

L4 = dict(
 intro=card('Me estoy duchando',
   'Bij wederkerende werkwoorden (ducharse, vestirse...) mag het kleine woordje op twee plekken:',
   ex('<i><b>Me</b> estoy duchando.</i> — vóór estar', '<i>Estoy duchándo<b>me</b>.</i> — vast achter het gerundio (met accent!)'),
   'Allebei goed en betekenen hetzelfde: ik sta onder de douche. Vooraan is het makkelijkst.'),
 words=[["me estoy duchando","ik sta onder de douche","I'm taking a shower"],["te estás vistiendo","jij bent je aan het aankleden","you're getting dressed"],["se está lavando","hij/zij is zich aan het wassen","he/she is washing"],["nos estamos preparando","wij maken ons klaar","we're getting ready"],["estoy esperando","ik ben aan het wachten","I'm waiting"],["está llegando","hij/zij komt nu aan","he/she is arriving"],["estoy buscando","ik ben aan het zoeken","I'm looking for"],["estoy pensando","ik ben aan het nadenken","I'm thinking"],["están viendo la tele","zij zitten tv te kijken","they're watching TV"]],
 sentences=[["Me estoy duchando, ¡un momento!","Ik sta onder de douche, momentje!","I'm in the shower, one moment!",["Estoy duchándome, ¡un momento!"]],["Los niños se están vistiendo.","De kinderen zijn zich aan het aankleden.","The children are getting dressed.",["Los niños están vistiéndose."]],["Estoy esperando el autobús.","Ik sta op de bus te wachten.","I'm waiting for the bus."],["¿Qué estás buscando?","Wat ben je aan het zoeken?","What are you looking for?"],["Estoy buscando mis llaves.","Ik ben mijn sleutels aan het zoeken.","I'm looking for my keys."],["Mis padres están viendo la tele.","Mijn ouders zitten tv te kijken.","My parents are watching TV."],["Nos estamos preparando para la fiesta.","We maken ons klaar voor het feest.","We're getting ready for the party.",["Estamos preparándonos para la fiesta."]],["El tren está llegando a la estación.","De trein komt nu het station binnen.","The train is arriving at the station."],["Estoy pensando en mis vacaciones.","Ik denk aan mijn vakantie.","I'm thinking about my holidays."],["¿Te estás lavando las manos?","Ben je je handen aan het wassen?","Are you washing your hands?",["¿Estás lavándote las manos?"]]])

def lesson(i, d):
    assert '`' not in d['intro'] and '${' not in d['intro']
    return "        { id:'a1-u17p-l%d', kind:'new', topic:'Estar + gerundio', intro:`%s`, words: %s, sentences: %s }," % (i, d['intro'], J(d['words']), J(d['sentences']))

UNIT = """    {
      id:'a1-u17p', icon: '🎬', colors: ['#ce82ff','#a568cc'], addedLater: true,
      title: { nl:'Wat ben je aan het doen? (estar + gerundio)', en:'Wat ben je aan het doen? (estar + gerundio)' },
      fase: 'Dagelijkse Routines & Vrije Tijd (A1.3)',
      lessons: [
%s
        { id:'a1-u17p-l5', kind:'review' },
        { id:'a1-u17p-l6', kind:'review' },
        { id:'a1-u17p-l7', kind:'review' },
        { id:'a1-u17p-l8', kind:'review' }
      ]
    },
""" % '\n'.join(lesson(i+1, d) for i, d in enumerate([L1, L2, L3, L4]))

def rep(c, old, new):
    assert c.count(old) == 1, old[:80]
    return c.replace(old, new)

def main(path='index.html'):
    c = open(path, encoding='utf-8').read()
    if "id:'a1-u17p'" in c:
        print('al aanwezig'); return
    anchor = "    {\n      id:'a1-u18',"
    c = rep(c, anchor, UNIT + anchor)
    # Later toegevoegde units (addedLater) blokkeren je voortgang niet als je er al voorbij bent
    c = rep(c, "  let firstIncomplete = nodes.findIndex(n => !progressKeyDone(level, n.lesson.id));",
               "  let firstIncomplete = nodes.findIndex((n,i) => !progressKeyDone(level, n.lesson.id) && !skippableLater(level, nodes, i));")
    c = rep(c, "function levelComplete(L){\n  const ns = flattenPath(L);\n  return ns.length>0 && ns.every(n=>progressKeyDone(L, n.lesson.id));\n}",
               "function levelComplete(L){\n  const ns = flattenPath(L);\n  return ns.length>0 && ns.every((n,i)=>progressKeyDone(L, n.lesson.id) || skippableLater(L, ns, i));\n}\n"
               "// Een unit die later aan de cursus is toegevoegd (addedLater) telt niet als 'nog te doen' voor wie er al voorbij is:\n"
               "// zo gaan latere units en het volgende niveau niet ineens op slot. Je kunt hem gewoon alsnog doen.\n"
               "function skippableLater(L, ns, i){\n  if(!ns[i].unit || !ns[i].unit.addedLater) return false;\n  for(let k=ns.length-1;k>i;k--){ if(!(ns[k].unit && ns[k].unit.addedLater) && progressKeyDone(L, ns[k].lesson.id)) return true; }\n  return false;\n}")
    open(path, 'w', encoding='utf-8').write(c)
    print('unit toegevoegd')

if __name__ == '__main__':
    main(*(sys.argv[1:2]))
