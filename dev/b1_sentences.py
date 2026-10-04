# B1: zinnen met grammatica die nog niet behandeld is vervangen, en geleerde vormen (A1, A2 en B1) laten terugkomen.
# Volgorde B1: subjuntivo (unit 3), condicional (unit 12), se impersonal (unit 20), pluscuamperfecto (unit 22),
# estilo indirecto (unit 26/28), futuro (unit 33). Pluscuamperfecto de subjuntivo (hubiera), cuando + subjuntivo
# en "se me ha..." horen bij B2.
# Gebruik: python3 dev/b1_sentences.py   (idempotent)
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sentence_tools import replace_sentences

TE_VROEG = 'te vroeg'
HERHALING = 'herhaling'

FUT = 'De futuro komt pas in unit 33; ir a ken je al.'
COND = 'De condicional (deberíamos) komt pas in unit 12.'

CHANGES = [
    ('b1-u1-l1', 'Pienso que deberíamos viajar más.', ['Pienso que tenemos que viajar más.', 'Ik vind dat we meer moeten reizen.', 'I think we have to travel more.'], (TE_VROEG, COND)),
    ('b1-u1-l1', 'Opino que deberíamos esperar un poco.', ['Opino que es mejor esperar un poco.', 'Ik vind dat het beter is om even te wachten.', "I think it's better to wait a bit."], (TE_VROEG, COND)),
    ('b1-u8-l1', 'Personalmente, creo que deberíamos esperar un poco más.', ['Personalmente, creo que es mejor esperar un poco más.', 'Persoonlijk denk ik dat het beter is om nog even te wachten.', "Personally, I think it's better to wait a little longer."], (TE_VROEG, COND)),
    ('b1-u8-l2', 'No dijo que vendría, sino que llamaría.', ['No viene hoy, sino mañana.', 'Hij komt niet vandaag, maar morgen.', "He isn't coming today, but tomorrow."], (TE_VROEG, 'Indirecte rede met de condicional (dijo que vendría) komt pas in unit 26.')),
    ('b1-u2-l1', 'No seas tan vago y ayúdame.', ['Eres muy vago; ¡ayúdame un poco!', 'Je bent heel lui; help me eens een beetje!', "You're very lazy; help me a bit!"], (TE_VROEG, 'De ontkennende gebiedende wijs (no seas) is een subjuntivo-vorm; die komt pas in unit 3.')),
    ('b1-u13-l2', 'Te devolveré el dinero la semana que viene.', ['Te voy a devolver el dinero la semana que viene.', 'Ik geef je volgende week het geld terug.', "I'm going to pay you back next week.", ['Voy a devolverte el dinero la semana que viene.']], (TE_VROEG, FUT)),
    ('b1-u15-l3', 'No dudo que hará un buen trabajo.', ['No dudo que va a hacer un buen trabajo.', 'Ik twijfel er niet aan dat hij goed werk gaat leveren.', "I don't doubt he's going to do a good job."], (TE_VROEG, FUT)),
    ('b1-u15-l3', 'Me imagino que estará muy cansado.', ['Me imagino que está muy cansado.', 'Ik kan me voorstellen dat hij erg moe is.', 'I imagine he is very tired.'], (TE_VROEG, FUT)),
    ('b1-u15-l3', 'Supongo que vendrá con su familia.', ['Supongo que va a venir con su familia.', 'Ik neem aan dat hij met zijn familie komt.', "I suppose he's going to come with his family.", ['Supongo que viene con su familia.']], (TE_VROEG, FUT)),
    ('b1-u15-l4', 'No tengo ninguna duda de que ganará.', ['No tengo ninguna duda de que va a ganar.', 'Ik twijfel er niet aan dat hij gaat winnen.', "I have no doubt he's going to win."], (TE_VROEG, FUT)),
    ('b1-u39-l2', 'No sé si saldrá bien, pero lo voy a intentar.', ['No sé si va a salir bien, pero lo voy a intentar.', 'Ik weet niet of het goed gaat aflopen, maar ik ga het proberen.', "I don't know if it'll work out, but I'm going to try.", ['No sé si va a salir bien, pero voy a intentarlo.']], (TE_VROEG, FUT)),
    ('b1-u39-l4', 'Es una buena oferta, pero me lo pensaré.', ['Es una buena oferta, pero me lo voy a pensar.', 'Het is een goed aanbod, maar ik ga erover nadenken.', "It's a good offer, but I'm going to think about it.", ['Es una buena oferta, pero voy a pensármelo.']], (TE_VROEG, FUT)),
    ('b1-u27-l2', 'Circula el rumor de que dejará el equipo.', ['Circula el rumor de que va a dejar el equipo.', 'Het gerucht gaat dat hij het team gaat verlaten.', "There's a rumour he's going to leave the team."], (TE_VROEG, FUT)),
    ('b1-u18-l1', 'Se me ha roto la pantalla del móvil.', ['He roto la pantalla del móvil.', 'Ik heb het scherm van mijn telefoon gebroken.', "I've broken my phone screen."], (TE_VROEG, '"Se me ha roto" (iets overkomt je) komt pas in B2.')),
    ('b1-u17-l2', '¿Puedes corregirme cuando cometa un error?', ['¿Puedes corregirme si cometo un error?', 'Kun je me verbeteren als ik een fout maak?', 'Can you correct me if I make a mistake?'], (TE_VROEG, 'Cuando + subjuntivo komt pas in B2.')),
    ('b1-u20-l4', 'Apaga las luces cuando salgas de la habitación.', ['Apaga las luces al salir de la habitación.', 'Doe het licht uit als je de kamer verlaat.', 'Turn off the lights when you leave the room.'], (TE_VROEG, 'Cuando + subjuntivo komt pas in B2.')),
    ('b1-u31-l2', '¿Me prestas ese libro cuando lo termines?', ['¿Me prestas ese libro? Te lo devuelvo el lunes.', 'Leen je me dat boek? Ik geef het je maandag terug.', "Will you lend me that book? I'll give it back on Monday."], (TE_VROEG, 'Cuando + subjuntivo komt pas in B2. Nu met te lo (herhaling).')),
    ('b1-u22-l4', 'Siguió caminando como si nada hubiera pasado.', ['Siguió caminando como si nada.', 'Hij liep door alsof er niets aan de hand was.', 'He kept walking as if nothing had happened.'], (TE_VROEG, 'Hubiera (pluscuamperfecto de subjuntivo) komt pas in B2.')),
    ('b1-u26-l4', 'Negó que hubiera dicho eso alguna vez.', ['Negó haber dicho eso alguna vez.', 'Hij ontkende dat ooit gezegd te hebben.', 'He denied ever having said that.'], (TE_VROEG, 'Hubiera (pluscuamperfecto de subjuntivo) komt pas in B2.')),
]

PERF = 'Voltooide tijd laten terugkomen.'
IR_A = 'Ir a + infinitief laten terugkomen.'
PROG = 'Estar + gerundio laten terugkomen.'
PRET = 'Verleden tijd (indefinido) laten terugkomen.'
IMPF = 'Imperfecto laten terugkomen.'
SUBJ = 'Subjuntivo (unit 3) laten terugkomen.'
CONDH = 'Condicional (unit 12) laten terugkomen.'
PLUS = 'Pluscuamperfecto (unit 22) laten terugkomen.'
PRON = 'Voornaamwoorden (lo/la, le/les, se lo, achteraan) laten terugkomen.'

def R(lid, old, new, why):
    return (lid, old, new, (HERHALING, why))

REUSE = [
    R('b1-u1-l3', 'Me interesa mucho la historia de España.', ['Siempre me ha interesado la historia de España.', 'De geschiedenis van Spanje heeft me altijd geïnteresseerd.', "I've always been interested in Spanish history."], PERF),
    R('b1-u1-l1', 'Tengo claro que quiero vivir en España.', ['Tengo claro que voy a vivir en España.', 'Het is voor mij duidelijk dat ik in Spanje ga wonen.', "I'm sure I'm going to live in Spain."], IR_A),
    R('b1-u1-l1', 'A mi parecer, esta película es aburrida.', ['A mi parecer, la película de ayer fue aburrida.', 'Naar mijn mening was de film van gisteren saai.', "In my opinion, yesterday's film was boring."], PRET),
    R('b1-u2-l3', 'Me llevo bien con mis compañeros.', ['Siempre me he llevado bien con mis compañeros.', 'Ik heb altijd goed met mijn collega’s kunnen opschieten.', "I've always got on well with my colleagues."], PERF),
    R('b1-u2-l2', 'La película no es nada aburrida.', ['La película no fue nada aburrida.', 'De film was helemaal niet saai.', "The film wasn't boring at all."], PRET),
    R('b1-u2-l3', 'Tu primo es muy buena gente.', ['Tu primo es muy buena gente; lo conozco bien.', 'Je neef is een heel goed mens; ik ken hem goed.', 'Your cousin is a really good person; I know him well.'], PRON),
    R('b1-u2-l3', 'Tu abuela es un encanto.', ['Tu abuela es un encanto; le voy a llevar flores.', 'Je oma is een schat; ik ga haar bloemen brengen.', "Your grandmother is a sweetheart; I'm going to take her flowers.", ['Tu abuela es un encanto; voy a llevarle flores.']], PRON + ' En ir a.'),
    R('b1-u4-l3', 'Estoy aliviada porque ya terminé.', ['Estoy aliviada porque ya he terminado.', 'Ik ben opgelucht omdat ik al klaar ben.', "I'm relieved because I've already finished."], PERF),
    R('b1-u4-l3', 'Se siente melancólico cuando llueve.', ['De niño se sentía melancólico cuando llovía.', 'Als kind voelde hij zich melancholisch als het regende.', 'As a child he felt melancholy when it rained.'], IMPF),
    R('b1-u5-l3', 'Tengo una cita el viernes por la noche.', ['El viernes por la noche voy a tener una cita.', 'Vrijdagavond heb ik een date.', "On Friday night I'm going to have a date."], IR_A),
    R('b1-u5-l2', 'Pienso mucho en ti.', ['Estoy pensando mucho en ti.', 'Ik denk veel aan je.', "I'm thinking about you a lot."], PROG),
    R('b1-u5-l1', 'Es una persona muy leal.', ['Es una persona muy leal; la quiero mucho.', 'Ze is heel loyaal; ik hou veel van haar.', "She's a very loyal person; I love her very much."], PRON),
    R('b1-u6-l4', 'El director concedió el permiso.', ['El director nos ha concedido el permiso.', 'De directeur heeft ons toestemming gegeven.', 'The director has given us permission.'], PERF),
    R('b1-u6-l1', 'Te recomiendo que leas ese libro.', ['Es un libro genial; te recomiendo que lo leas.', 'Het is een geweldig boek; ik raad je aan het te lezen.', "It's a great book; I recommend you read it."], PRON),
    R('b1-u7-l3', 'Mi tía hizo el árbol genealógico de la familia.', ['Mi tía ha hecho el árbol genealógico de la familia.', 'Mijn tante heeft de stamboom van de familie gemaakt.', 'My aunt has made the family tree.'], PERF),
    R('b1-u7-l2', 'Mañana me despido de mis abuelos en el aeropuerto.', ['Mañana me voy a despedir de mis abuelos en el aeropuerto.', 'Morgen neem ik afscheid van mijn grootouders op het vliegveld.', "Tomorrow I'm going to say goodbye to my grandparents at the airport.", ['Mañana voy a despedirme de mis abuelos en el aeropuerto.']], IR_A),
    R('b1-u7-l4', 'Tengo nostalgia de las vacaciones en casa de mis abuelos.', ['Tengo nostalgia de las vacaciones que pasábamos en casa de mis abuelos.', 'Ik verlang terug naar de vakanties die we bij mijn grootouders doorbrachten.', 'I miss the holidays we used to spend at my grandparents’ house.'], IMPF),
    R('b1-u7-l1', 'Mi suegra cocina muy bien.', ['Mi suegra cocina muy bien; la visito cada domingo.', 'Mijn schoonmoeder kookt heel goed; ik bezoek haar elke zondag.', 'My mother-in-law cooks very well; I visit her every Sunday.'], PRON),
    R('b1-u7-l1', 'Mi ahijado me llama todas las semanas.', ['A mi ahijado le compro un regalo cada año.', 'Ik koop elk jaar een cadeau voor mijn petekind.', 'I buy my godson a present every year.'], PRON),
    R('b1-u7-l4', 'Cuido de mi abuela todos los fines de semana.', ['Mi abuela quiere que la cuide los fines de semana.', 'Mijn oma wil dat ik in het weekend voor haar zorg.', 'My grandmother wants me to look after her at weekends.'], SUBJ + ' En la.'),
    R('b1-u8-l4', 'Por fin llegamos a un acuerdo.', ['Por fin hemos llegado a un acuerdo.', 'Eindelijk zijn we het eens geworden.', "We've finally reached an agreement."], PERF),
    R('b1-u8-l3', 'Defiende su postura con firmeza.', ['Está defendiendo su postura con firmeza.', 'Hij verdedigt zijn standpunt vastberaden.', "He's firmly defending his position."], PROG),
    R('b1-u9-l4', 'Contraté a un asesor financiero.', ['He contratado a un asesor financiero.', 'Ik heb een financieel adviseur in de arm genomen.', "I've hired a financial adviser."], PERF),
    R('b1-u9-l3', 'Siempre me da buenos consejos.', ['De pequeña, mi abuela siempre me daba buenos consejos.', 'Toen ik klein was, gaf mijn oma me altijd goede adviezen.', 'When I was little, my grandmother always gave me good advice.', ['De pequeño, mi abuela siempre me daba buenos consejos.']], IMPF),
    R('b1-u10-l1', 'Envié mi currículum a varias empresas.', ['He enviado mi currículum a varias empresas.', 'Ik heb mijn cv naar verschillende bedrijven gestuurd.', "I've sent my CV to several companies."], PERF),
    R('b1-u10-l1', 'Escribí una carta de presentación breve.', ['Escribí una carta de presentación y se la mandé a la empresa.', 'Ik schreef een sollicitatiebrief en stuurde hem naar het bedrijf.', 'I wrote a cover letter and sent it to the company.'], PRON),
    R('b1-u10-l3', 'Ofrecen un horario flexible.', ['Espero que me ofrezcan un horario flexible.', 'Ik hoop dat ze me flexibele werktijden aanbieden.', 'I hope they offer me flexible hours.'], SUBJ),
    R('b1-u11-l2', 'Colaboramos en varios proyectos juntos.', ['Hemos colaborado en varios proyectos juntos.', 'We hebben samen aan verschillende projecten gewerkt.', "We've worked together on several projects."], PERF),
    R('b1-u11-l1', 'El gerente quiere hablar con todos.', ['El gerente quiere que todos vayamos a la reunión.', 'De manager wil dat we allemaal naar de vergadering gaan.', 'The manager wants us all to go to the meeting.'], SUBJ),
    R('b1-u11-l1', 'Te envié un correo electrónico ayer.', ['Le envié un correo electrónico al cliente ayer.', 'Ik stuurde de klant gisteren een e-mail.', 'I sent the client an email yesterday.'], PRON),
    R('b1-u11-l1', 'Tengo que entregar el informe hoy.', ['El informe está listo; tengo que entregárselo al jefe hoy.', 'Het rapport is klaar; ik moet het vandaag aan de baas geven.', 'The report is ready; I have to hand it to the boss today.', ['El informe está listo; se lo tengo que entregar al jefe hoy.']], PRON),
    R('b1-u13-l3', 'El sueldo mínimo subió este año.', ['El sueldo mínimo ha subido este año.', 'Het minimumloon is dit jaar gestegen.', 'The minimum wage has gone up this year.'], PERF),
    R('b1-u13-l3', 'El coste de vida aquí es muy alto.', ['Antes el coste de vida aquí era más bajo.', 'Vroeger waren de kosten van levensonderhoud hier lager.', 'The cost of living here used to be lower.'], IMPF),
    R('b1-u13-l2', 'No quiero malgastar mi dinero.', ['No quiero que malgastes nuestro dinero.', 'Ik wil niet dat je ons geld verspilt.', "I don't want you to waste our money."], SUBJ),
    R('b1-u13-l4', 'Hice una transferencia a mi hermana.', ['Mi hermana necesitaba dinero y se lo transferí ayer.', 'Mijn zus had geld nodig en ik heb het haar gisteren overgemaakt.', 'My sister needed money and I transferred it to her yesterday.'], PRON),
    R('b1-u14-l1', 'Mi meta financiera es comprar una casa.', ['Vamos a comprar una casa; es nuestra meta financiera.', 'We gaan een huis kopen; dat is ons financiële doel.', "We're going to buy a house; it's our financial goal."], IR_A),
    R('b1-u14-l1', 'Tiene mucha deuda por la universidad.', ['Tenía mucha deuda por la universidad.', 'Hij had veel schulden door de universiteit.', 'He had a lot of debt from university.'], IMPF),
    R('b1-u14-l2', 'Es importante diversificar tus inversiones.', ['Es importante que diversifiques tus inversiones.', 'Het is belangrijk dat je je beleggingen spreidt.', "It's important that you diversify your investments."], SUBJ),
    R('b1-u14-l2', 'Consulté a un asesor financiero antes de invertir.', ['Le pregunté a un asesor financiero antes de invertir.', 'Ik vroeg het een financieel adviseur voordat ik ging beleggen.', 'I asked a financial adviser before investing.'], PRON),
    R('b1-u14-l3', 'Hice la lista de compras antes de salir.', ['Hice la lista de compras y se la di a mi marido.', 'Ik maakte de boodschappenlijst en gaf hem aan mijn man.', 'I made the shopping list and gave it to my husband.'], PRON),
    R('b1-u15-l4', 'Todavía tengo mis dudas sobre el plan.', ['Al principio tenía mis dudas sobre el plan.', 'In het begin had ik mijn twijfels over het plan.', 'At first I had my doubts about the plan.'], IMPF),
    R('b1-u16-l1', 'Tengo que pagar la matrícula antes de septiembre.', ['Es necesario que pague la matrícula antes de septiembre.', 'Ik moet het inschrijfgeld vóór september betalen.', 'I need to pay the enrolment fee before September.'], SUBJ),
    R('b1-u16-l1', 'Quiero hacer un doctorado en biología.', ['Me gustaría hacer un doctorado en biología.', 'Ik zou graag promoveren in de biologie.', "I'd like to do a PhD in biology."], CONDH),
    R('b1-u16-l4', 'Quiero convalidar mi título en España.', ['Tengo un título holandés y quiero convalidarlo en España.', 'Ik heb een Nederlands diploma en wil het in Spanje laten erkennen.', 'I have a Dutch degree and want to get it recognised in Spain.', ['Tengo un título holandés y lo quiero convalidar en España.']], PRON),
    R('b1-u16-l3', 'Mi compañero de clase me ayudó con los apuntes.', ['Mi compañero de clase no tenía los apuntes y se los presté.', 'Mijn klasgenoot had de aantekeningen niet en ik heb ze hem geleend.', "My classmate didn't have the notes and I lent them to him."], PRON),
    R('b1-u17-l1', 'Necesito ampliar mi vocabulario en español.', ['Mi profesora quiere que amplíe mi vocabulario en español.', 'Mijn lerares wil dat ik mijn Spaanse woordenschat uitbreid.', 'My teacher wants me to expand my Spanish vocabulary.'], SUBJ),
    R('b1-u17-l1', 'Con este certificado de idiomas puedo trabajar en España.', ['Con este certificado de idiomas podría trabajar en España.', 'Met dit taalcertificaat zou ik in Spanje kunnen werken.', 'With this language certificate I could work in Spain.'], CONDH),
    R('b1-u17-l2', 'Repaso las palabras nuevas antes de dormir.', ['Apunto las palabras nuevas y las repaso antes de dormir.', 'Ik schrijf de nieuwe woorden op en herhaal ze voor het slapengaan.', 'I write down the new words and review them before bed.'], PRON),
    R('b1-u17-l3', 'No entendí ese modismo, ¿qué significa?', ['No entendí ese modismo, así que le pregunté a la profesora.', 'Ik begreep die uitdrukking niet, dus ik vroeg het aan de lerares.', "I didn't understand that idiom, so I asked the teacher."], PRON),
    R('b1-u18-l1', 'Este dispositivo ya tiene cinco años.', ['Este dispositivo tiene cinco años; es raro que todavía funcione.', 'Dit apparaat is vijf jaar oud; het is vreemd dat het nog werkt.', "This device is five years old; it's strange that it still works."], SUBJ),
    R('b1-u18-l3', 'Necesito desconectarme del móvil los fines de semana.', ['Debería desconectarme del móvil los fines de semana.', 'Ik zou in het weekend mijn telefoon moeten wegleggen.', 'I should disconnect from my phone at weekends.'], CONDH),
    R('b1-u18-l2', 'Descargué la aplicación para aprender vocabulario.', ['Vi la aplicación y la descargué para aprender vocabulario.', 'Ik zag de app en downloadde hem om woordjes te leren.', 'I saw the app and downloaded it to learn vocabulary.'], PRON),
    R('b1-u18-l4', 'Le reenvié el mensaje a mi jefe.', ['Recibí un mensaje importante y se lo reenvié a mi jefe.', 'Ik kreeg een belangrijk bericht en stuurde het door naar mijn baas.', 'I got an important message and forwarded it to my boss.'], PRON),
    R('b1-u19-l2', 'Le encanta observar aves con sus prismáticos.', ['Está observando aves con sus prismáticos.', 'Hij is met zijn verrekijker vogels aan het kijken.', "He's watching birds with his binoculars."], PROG),
    R('b1-u19-l2', 'Escalar esa montaña requiere mucha experiencia.', ['Me encantaría escalar esa montaña, pero requiere mucha experiencia.', 'Ik zou die berg graag beklimmen, maar daar is veel ervaring voor nodig.', "I'd love to climb that mountain, but it takes a lot of experience."], CONDH),
    R('b1-u19-l3', 'Vimos animales salvajes durante la excursión.', ['Vimos animales salvajes y los fotografiamos durante la excursión.', 'We zagen wilde dieren en fotografeerden ze tijdens de tocht.', 'We saw wild animals and photographed them during the trip.'], PRON),
    R('b1-u19-l4', 'Intentamos no dejar huella en el bosque.', ['Es importante que no dejemos huella en el bosque.', 'Het is belangrijk dat we geen sporen achterlaten in het bos.', "It's important that we leave no trace in the forest."], SUBJ),
    R('b1-u20-l3', 'Intento reducir mi huella de carbono cada año.', ['Este año voy a reducir mi huella de carbono.', 'Dit jaar ga ik mijn CO2-voetafdruk verkleinen.', "This year I'm going to reduce my carbon footprint.", ['Voy a reducir mi huella de carbono este año.']], IR_A),
    R('b1-u20-l2', 'En casa reutilizamos las bolsas de plástico.', ['Antes no reutilizábamos las bolsas de plástico.', 'Vroeger hergebruikten we de plastic tassen niet.', "We didn't use to reuse plastic bags."], IMPF),
    R('b1-u20-l3', 'Llevamos el vidrio al punto verde del barrio.', ['Separamos el vidrio y lo llevamos al punto verde del barrio.', 'We scheiden het glas en brengen het naar het milieupunt in de buurt.', 'We separate the glass and take it to the local recycling point.'], PRON),
    R('b1-u21-l3', 'Encontraron mi objeto perdido en la estación.', ['Han encontrado mi objeto perdido en la estación.', 'Ze hebben mijn verloren voorwerp op het station gevonden.', "They've found my lost item at the station."], PERF),
    R('b1-u21-l2', 'Tenemos que facturar la maleta antes de las seis.', ['Vamos a facturar la maleta antes de las seis.', 'We gaan de koffer vóór zes uur inchecken.', "We're going to check in the suitcase before six."], IR_A),
    R('b1-u21-l2', 'Pedimos ayuda a un policía para llegar al hotel.', ['Le pedimos ayuda a un policía para llegar al hotel.', 'We vroegen een agent om hulp om bij het hotel te komen.', 'We asked a police officer for help getting to the hotel.'], PRON),
    R('b1-u21-l4', 'Lleva siempre una copia del pasaporte por si acaso.', ['Haz una copia del pasaporte y llévala siempre por si acaso.', 'Maak een kopie van je paspoort en neem hem altijd mee voor het geval dat.', 'Make a copy of your passport and always carry it just in case.'], PRON),
    R('b1-u22-l2', 'Nos encanta contar esa historia de nuestro viaje.', ['Hemos contado esa historia de nuestro viaje mil veces.', 'We hebben dat verhaal van onze reis al duizend keer verteld.', "We've told that story about our trip a thousand times."], PERF),
    R('b1-u22-l3', 'Nos pasó algo muy curioso en el mercado.', ['A mi hermano le pasó algo muy curioso en el mercado.', 'Mijn broer overkwam iets heel vreemds op de markt.', 'Something very odd happened to my brother at the market.'], PRON),
    R('b1-u23-l3', 'Nos preparamos para el examen todo el fin de semana.', ['Vamos a prepararnos para el examen todo el fin de semana.', 'We gaan ons het hele weekend op het examen voorbereiden.', "We're going to prepare for the exam all weekend.", ['Nos vamos a preparar para el examen todo el fin de semana.']], IR_A),
    R('b1-u23-l1', 'Le organizamos una fiesta por sorpresa.', ['Le organizamos una fiesta por sorpresa; nadie se lo había dicho.', 'We organiseerden een verrassingsfeest voor hem; niemand had het hem verteld.', 'We threw him a surprise party; nobody had told him.'], PLUS + ' En se lo.'),
    R('b1-u24-l1', 'Quiero terminar lo más pronto posible.', ['Voy a terminar lo más pronto posible.', 'Ik ga zo snel mogelijk klaar zijn.', "I'm going to finish as soon as possible."], IR_A),
    R('b1-u24-l2', 'Aprender chino me parece dificilísimo.', ['Para mí sería dificilísimo aprender chino.', 'Voor mij zou het superlastig zijn om Chinees te leren.', 'For me it would be really hard to learn Chinese.'], CONDH),
    R('b1-u24-l2', 'La paella de mi abuela está riquísima.', ['La paella de mi abuela está riquísima; siempre le pido la receta.', 'De paella van mijn oma is overheerlijk; ik vraag haar altijd om het recept.', "My grandmother's paella is delicious; I always ask her for the recipe."], PRON),
    R('b1-u25-l2', 'El periodista reveló un secreto importante.', ['El periodista ha revelado un secreto importante.', 'De journalist heeft een belangrijk geheim onthuld.', 'The journalist has revealed an important secret.'], PERF),
    R('b1-u25-l2', 'El periodista entrevistó al ministro esta tarde.', ['El periodista entrevistó al ministro y le preguntó por el escándalo.', 'De journalist interviewde de minister en vroeg hem naar het schandaal.', 'The journalist interviewed the minister and asked him about the scandal.'], PRON),
    R('b1-u25-l1', 'Hay que verificar siempre la fuente de la noticia.', ['Habría que verificar siempre la fuente de la noticia.', 'Je zou altijd de bron van het nieuws moeten controleren.', 'You should always check the source of the news.'], CONDH),
    R('b1-u27-l1', 'Siempre cotillean sobre los vecinos nuevos.', ['Siempre están cotilleando sobre los vecinos nuevos.', 'Ze zitten altijd te roddelen over de nieuwe buren.', "They're always gossiping about the new neighbours."], PROG),
    R('b1-u29-l1', 'Las elecciones son en noviembre este año.', ['Las elecciones son en noviembre y voy a votar.', 'De verkiezingen zijn in november en ik ga stemmen.', "The elections are in November and I'm going to vote."], IR_A),
    R('b1-u29-l3', 'La campaña electoral duró casi dos meses.', ['Durante la campaña electoral había carteles por todas partes.', 'Tijdens de verkiezingscampagne hingen er overal affiches.', 'During the election campaign there were posters everywhere.'], IMPF),
    R('b1-u29-l3', 'El sistema sanitario necesita más inversión.', ['Es necesario que el sistema sanitario reciba más inversión.', 'Het is nodig dat de gezondheidszorg meer investeringen krijgt.', 'The health system needs to receive more investment.'], SUBJ),
    R('b1-u29-l4', 'Prefiero no tomar partido en discusiones así.', ['Preferiría no tomar partido en discusiones así.', 'Ik zou liever geen partij kiezen in zulke discussies.', "I'd rather not take sides in discussions like that."], CONDH),
    R('b1-u29-l2', 'El parlamento aprobó la nueva ley por mayoría.', ['El parlamento debatió la nueva ley y la aprobó por mayoría.', 'Het parlement besprak de nieuwe wet en nam hem met meerderheid aan.', 'Parliament debated the new law and passed it by a majority.'], PRON),
    R('b1-u29-l2', 'Prometieron reformar el sistema educativo.', ['Los votantes pidieron una reforma y el gobierno se la prometió.', 'De kiezers vroegen om een hervorming en de regering beloofde die hun.', 'Voters asked for a reform and the government promised it to them.'], PRON),
    R('b1-u30-l2', 'Esa serie es muy recomendable para el fin de semana.', ['Esa serie es muy recomendable; voy a verla este fin de semana.', 'Die serie is een aanrader; ik ga hem dit weekend kijken.', "That series is highly recommended; I'm going to watch it this weekend.", ['Esa serie es muy recomendable; la voy a ver este fin de semana.']], IR_A + ' En la achteraan.'),
    R('b1-u30-l3', 'No puedo ver películas de miedo solo.', ['De niño no podía ver películas de miedo solo.', 'Als kind kon ik niet alleen naar enge films kijken.', "As a child I couldn't watch horror films alone."], IMPF),
    R('b1-u30-l2', 'Prefiero ver las películas en versión original, no dobladas.', ['Prefiero que no doblen las películas.', 'Ik heb liever dat ze films niet nasynchroniseren.', "I'd rather they didn't dub films."], SUBJ),
    R('b1-u30-l1', 'Me encantan todas las películas de ese director.', ['Me encantan las películas de ese director; me encantaría conocerlo.', 'Ik ben dol op de films van die regisseur; ik zou hem graag ontmoeten.', "I love that director's films; I'd love to meet him."], CONDH + ' En lo achteraan.'),
    R('b1-u31-l1', 'Una editorial pequeña publicó su primer libro.', ['Una editorial pequeña ha publicado su primer libro.', 'Een kleine uitgeverij heeft haar eerste boek uitgegeven.', 'A small publisher has published her first book.'], PERF),
    R('b1-u31-l4', 'Ese libro está muy de moda este verano.', ['Ese libro está muy de moda; voy a comprarlo este verano.', 'Dat boek is erg in; ik ga het deze zomer kopen.', "That book is very popular; I'm going to buy it this summer.", ['Ese libro está muy de moda; lo voy a comprar este verano.']], IR_A + ' En lo achteraan.'),
    R('b1-u31-l1', 'Mi sueño es ser escritora algún día.', ['Ojalá sea escritora algún día.', 'Hopelijk word ik ooit schrijfster.', 'I hope I become a writer one day.', ['Ojalá sea escritor algún día.']], SUBJ),
    R('b1-u32-l1', 'Vimos el desfile desde el balcón.', ['Hemos visto el desfile desde el balcón.', 'We hebben de optocht vanaf het balkon gezien.', "We've watched the parade from the balcony."], PERF),
    R('b1-u32-l2', 'Engalanamos la plaza para la fiesta.', ['Estamos engalanando la plaza para la fiesta.', 'We zijn het plein aan het versieren voor het feest.', "We're decorating the square for the festival."], PROG),
    R('b1-u32-l2', 'En la cena homenajeamos a mis abuelos.', ['En la cena homenajeamos a mis abuelos y les dimos un regalo.', 'Tijdens het diner eerden we mijn grootouders en gaven we ze een cadeau.', 'At dinner we paid tribute to my grandparents and gave them a present.'], PRON),
    R('b1-u32-l3', 'Había más de doscientos invitados en la boda.', ['Nunca había estado en una boda con doscientos invitados.', 'Ik was nog nooit op een bruiloft met tweehonderd gasten geweest.', 'I had never been to a wedding with two hundred guests.'], PLUS),
    R('b1-u34-l3', 'Es obvio que está cansado.', ['Era obvio que estaba cansado.', 'Het was duidelijk dat hij moe was.', 'It was obvious he was tired.'], IMPF),
    R('b1-u34-l2', 'Es urgente que hables con el médico.', ['Es urgente que le digas al médico lo que te duele.', 'Het is dringend dat je de dokter vertelt wat er pijn doet.', "It's urgent that you tell the doctor what hurts."], PRON),
    R('b1-u35-l1', 'Me siento un poco inseguro con esta decisión.', ['Me sentía un poco inseguro con esta decisión.', 'Ik voelde me een beetje onzeker over deze beslissing.', 'I felt a bit unsure about this decision.'], IMPF),
    R('b1-u36-l1', 'La casa que compraron tiene jardín.', ['La casa que vamos a comprar tiene jardín.', 'Het huis dat we gaan kopen heeft een tuin.', "The house we're going to buy has a garden."], IR_A),
    R('b1-u36-l1', 'Los amigos que conocí en Madrid me escriben a menudo.', ['Los amigos que conocí en Madrid me escriben y yo siempre les contesto.', 'De vrienden die ik in Madrid leerde kennen schrijven me en ik antwoord ze altijd.', 'The friends I met in Madrid write to me and I always answer them.'], PRON),
    R('b1-u37-l3', 'El responsable del proyecto está de viaje.', ['El responsable del proyecto estaba de viaje cuando empezó la obra.', 'De projectleider was op reis toen het werk begon.', 'The project manager was away when the work started.'], IMPF),
    R('b1-u37-l3', 'Pedimos una prórroga de una semana.', ['Pedimos que nos den una prórroga de una semana.', 'We vragen of ze ons een week uitstel geven.', "We're asking them to give us a week's extension."], SUBJ),
    R('b1-u37-l4', 'Es difícil cumplir el plazo con tan poca gente.', ['Sería difícil cumplir el plazo con tan poca gente.', 'Het zou moeilijk zijn de deadline te halen met zo weinig mensen.', 'It would be hard to meet the deadline with so few people.'], CONDH),
    R('b1-u37-l3', 'El plazo para entregar el informe es el viernes.', ['El informe es para el viernes; se lo entrego al cliente ese día.', 'Het rapport is voor vrijdag; ik geef het die dag aan de klant.', "The report is due on Friday; I'll hand it to the client that day."], PRON),
    R('b1-u38-l2', 'Te deseo mucho éxito en tu nuevo trabajo.', ['A mi hermana le deseo mucho éxito en su nuevo trabajo.', 'Ik wens mijn zus veel succes met haar nieuwe baan.', 'I wish my sister every success in her new job.'], PRON),
    R('b1-u38-l3', 'Ella persigue su sueño de ser actriz.', ['Ella está persiguiendo su sueño de ser actriz.', 'Ze is haar droom aan het najagen om actrice te worden.', 'She is chasing her dream of becoming an actress.'], PROG),
]

if __name__ == '__main__':
    replace_sentences(CHANGES)
    replace_sentences(REUSE)
