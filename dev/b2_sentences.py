# B2: zinnen met grammatica die nog niet behandeld is vervangen, en geleerde vormen laten terugkomen.
# Volgorde B2: imperfecto de subjuntivo (unit 2), als-zinnen type 2/3 (unit 4/6), subjuntivo in tijdzinnen (unit 10),
# lo/le + se me olvidó (unit 41), lijdende vorm (unit 16), toegeven (unit 20), futuro perfecto (unit 34).
# Gebruik: python3 dev/b2_sentences.py   (idempotent)
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sentence_tools import replace_sentences

TE_VROEG = 'te vroeg'
HERHALING = 'herhaling'

CHANGES = [
    ('b2-u7-l1', 'Se nos rompió el coche en la autopista, pero podría haber sido peor.', ['El coche se averió en la autopista, pero podría haber sido peor.', 'De auto kreeg pech op de snelweg, maar het had erger kunnen zijn.', 'The car broke down on the motorway, but it could have been worse.'], (TE_VROEG, '"Se nos rompió" (iets overkomt je) komt pas in unit 41.')),
    ('b2-u14-l4', 'Prefiero un piso exterior, aunque haya más ruido.', ['Prefiero un piso exterior, aunque hay más ruido.', 'Ik heb liever een appartement aan de straatkant, ook al is er meer lawaai.', 'I prefer a flat facing the street, even though there is more noise.'], (TE_VROEG, 'Aunque + subjuntivo komt pas in unit 20.')),
]

PERF = 'Voltooide tijd laten terugkomen.'
IR_A = 'Ir a + infinitief laten terugkomen.'
IMPF = 'Imperfecto laten terugkomen.'
CONDH = 'Condicional laten terugkomen.'
IMPSUBJ = 'Imperfecto de subjuntivo (unit 2) laten terugkomen.'
SI2 = 'Als-zin type 2 (unit 4) laten terugkomen.'
PRON = 'Voornaamwoorden (lo/la, le/les, se lo, achteraan) laten terugkomen.'
SEME = '"Se me..." (unit 41) laten terugkomen.'

def R(lid, old, new, why):
    return (lid, old, new, (HERHALING, why))

REUSE = [
    R('b2-u1-l1', 'Soy tan despistado que siempre pierdo las llaves.', ['Soy tan despistado que siempre pierdo las llaves; mi madre me las guarda.', 'Ik ben zo verstrooid dat ik altijd mijn sleutels kwijtraak; mijn moeder bewaart ze voor me.', "I'm so absent-minded that I always lose my keys; my mother keeps them for me."], PRON),
    R('b2-u3-l1', 'Ligaron en una discoteca y ahora viven juntos.', ['Ligaron en una discoteca y ahora se van a casar.', 'Ze kregen iets in een discotheek en nu gaan ze trouwen.', "They hooked up at a club and now they're going to get married."], IR_A),
    R('b2-u3-l4', 'Si te ignora, no le escribas más.', ['Si te ignora, yo no le escribiría más.', 'Als hij je negeert, zou ik hem niet meer schrijven.', "If he ignores you, I wouldn't write to him any more."], CONDH),
    R('b2-u5-l3', 'Quiero ponerme en forma antes del verano.', ['Me gustaría ponerme en forma antes del verano.', 'Ik zou graag in vorm komen voor de zomer.', "I'd like to get in shape before summer."], CONDH),
    R('b2-u5-l3', 'Los expertos recomiendan hacer ejercicio al menos tres veces por semana.', ['El médico me recomendó que hiciera ejercicio al menos tres veces por semana.', 'De dokter raadde me aan minstens drie keer per week te sporten.', 'The doctor recommended I exercise at least three times a week.'], IMPSUBJ),
    R('b2-u7-l4', 'Esta vez quiero hacer las cosas bien desde el principio.', ['Esta vez voy a hacer las cosas bien desde el principio.', 'Deze keer ga ik het vanaf het begin goed doen.', "This time I'm going to do things right from the start."], IR_A),
    R('b2-u8-l4', 'Si quieres aprobar, tienes que ponerte las pilas.', ['Si quisieras aprobar, tendrías que ponerte las pilas.', 'Als je zou willen slagen, zou je aan de slag moeten.', "If you wanted to pass, you'd have to get your act together."], SI2),
    R('b2-u8-l1', 'Mi abuelo siempre cuenta el mismo chiste en Navidad.', ['Seguro que mi abuelo va a contar el mismo chiste en Navidad.', 'Mijn opa gaat vast weer dezelfde mop vertellen met Kerst.', "My grandfather is sure to tell the same joke at Christmas."], IR_A),
    R('b2-u9-l2', 'Trabaja en una empresa emergente de energía solar.', ['Va a trabajar en una empresa emergente de energía solar.', 'Hij gaat werken bij een start-up in zonne-energie.', "He's going to work at a solar energy start-up."], IR_A),
    R('b2-u9-l3', 'Busca un trabajo de media jornada para poder estudiar.', ['Le gustaría un trabajo de media jornada para poder estudiar.', 'Hij zou graag een parttimebaan hebben om te kunnen studeren.', "He'd like a part-time job so he can study."], CONDH),
    R('b2-u9-l1', 'Piden al menos tres años de experiencia laboral.', ['Pedían que tuviera al menos tres años de experiencia laboral.', 'Ze vroegen dat ik minstens drie jaar werkervaring had.', 'They asked that I have at least three years of work experience.'], IMPSUBJ),
    R('b2-u9-l3', 'Por fin me han hecho un contrato indefinido.', ['Por fin me han ofrecido un contrato indefinido y lo he firmado.', 'Eindelijk hebben ze me een vast contract aangeboden en ik heb het getekend.', "They've finally offered me a permanent contract and I've signed it."], PRON),
    R('b2-u11-l3', 'Hacemos una videollamada con el equipo de México cada lunes.', ['Vamos a hacer una videollamada con el equipo de México.', 'We gaan videobellen met het team in Mexico.', "We're going to have a video call with the team in Mexico."], IR_A),
    R('b2-u11-l1', 'Le envío el archivo adjunto con el presupuesto.', ['Le envío el presupuesto; se lo mando como archivo adjunto.', 'Ik stuur u de offerte; ik stuur hem als bijlage mee.', "I'm sending you the quote; I'm sending it as an attachment."], PRON),
    R('b2-u12-l2', 'Esta semana el aceite está de oferta.', ['Esta semana el aceite está de oferta; voy a comprar dos botellas.', 'Deze week is de olie in de aanbieding; ik ga twee flessen kopen.', "This week the oil is on offer; I'm going to buy two bottles."], IR_A),
    R('b2-u12-l1', 'El coste de la vida es cada vez más alto en las grandes ciudades.', ['Antes el coste de la vida era más bajo en las grandes ciudades.', 'Vroeger waren de kosten van levensonderhoud in de grote steden lager.', 'The cost of living used to be lower in big cities.'], IMPF),
    R('b2-u12-l3', 'Invertir en bolsa tiene sus riesgos.', ['Yo no invertiría en bolsa; tiene sus riesgos.', 'Ik zou niet in aandelen beleggen; dat heeft zijn risico’s.', "I wouldn't invest in the stock market; it has its risks."], CONDH),
    R('b2-u12-l2', 'Guarda el ticket de compra por si quieres cambiarlo.', ['Guarda el ticket de compra; a mí siempre se me pierde.', 'Bewaar de kassabon; ik raak hem altijd kwijt.', 'Keep the receipt; I always lose mine.'], SEME),
    R('b2-u13-l4', 'No ha estudiado nada; por lo tanto, no aprobará.', ['No ha estudiado nada; por lo tanto, no va a aprobar.', 'Hij heeft niets gestudeerd; hij gaat dus niet slagen.', "He hasn't studied at all; therefore, he isn't going to pass."], IR_A),
    R('b2-u14-l3', 'Hay que empaquetar los platos con mucho cuidado.', ['Vamos a empaquetar los platos con mucho cuidado.', 'We gaan de borden heel voorzichtig inpakken.', "We're going to pack the plates very carefully."], IR_A),
    R('b2-u14-l2', 'Todas las mañanas hay un atasco enorme en la entrada de la ciudad.', ['Antes había un atasco enorme todas las mañanas en la entrada de la ciudad.', 'Vroeger stond er elke ochtend een enorme file bij de ingang van de stad.', 'There used to be a huge traffic jam every morning at the entrance to the city.'], IMPF),
    R('b2-u14-l1', 'El casero no quiere arreglar la caldera.', ['Le pedimos al casero que arreglara la caldera, pero no quiso.', 'We vroegen de huisbaas om de cv-ketel te repareren, maar hij wilde niet.', 'We asked the landlord to fix the boiler, but he refused.'], IMPSUBJ + ' En le.'),
    R('b2-u14-l3', 'El portero recoge los paquetes cuando no estamos.', ['El portero recoge los paquetes y nos los sube cuando no estamos.', 'De conciërge neemt de pakketjes aan en brengt ze naar boven als we er niet zijn.', "The porter takes in the parcels and brings them up when we're out."], PRON),
    R('b2-u15-l4', 'Tengo que renovar el carné de conducir.', ['Voy a renovar el carné de conducir.', 'Ik ga mijn rijbewijs verlengen.', "I'm going to renew my driving licence."], IR_A),
    R('b2-u15-l3', 'Hace voluntariado en un banco de alimentos.', ['De joven hacía voluntariado en un banco de alimentos.', 'Toen hij jong was, deed hij vrijwilligerswerk bij een voedselbank.', 'When he was young he volunteered at a food bank.'], IMPF),
    R('b2-u17-l1', 'Después del bachillerato quiere estudiar Medicina.', ['Después del bachillerato va a estudiar Medicina.', 'Na de middelbare school gaat ze geneeskunde studeren.', "After sixth form she's going to study medicine."], IR_A),
    R('b2-u17-l4', 'Los colegios privados son muy caros.', ['No podríamos pagar un colegio privado; son muy caros.', 'We zouden een privéschool niet kunnen betalen; die zijn erg duur.', "We couldn't afford a private school; they're very expensive."], CONDH),
    R('b2-u17-l2', 'Mis padres firmaron el boletín de notas.', ['Mis padres querían que les enseñara el boletín de notas.', 'Mijn ouders wilden dat ik ze mijn rapport liet zien.', 'My parents wanted me to show them my school report.'], IMPSUBJ + ' En les.'),
    R('b2-u18-l2', 'Añoro la comida de mi madre y el mar.', ['Añoro la comida de mi madre; este verano voy a volver a casa.', 'Ik mis het eten van mijn moeder; deze zomer ga ik terug naar huis.', "I miss my mother's cooking; this summer I'm going back home."], IR_A),
    R('b2-u18-l3', 'Hay que respetar las creencias de los demás.', ['Habría que respetar más las creencias de los demás.', 'We zouden de overtuigingen van anderen meer moeten respecteren.', "We ought to respect other people's beliefs more."], CONDH),
    R('b2-u18-l2', 'Al principio me costó adaptarme al horario español.', ['Al principio me costaba que la gente cenara tan tarde.', 'In het begin vond ik het moeilijk dat mensen zo laat aten.', 'At first I found it hard that people ate dinner so late.'], IMPSUBJ),
    R('b2-u19-l1', 'Analizaron una muestra de mil personas.', ['Van a analizar una muestra de mil personas.', 'Ze gaan een steekproef van duizend mensen analyseren.', "They're going to analyse a sample of a thousand people."], IR_A),
    R('b2-u19-l1', 'La investigación científica necesita más financiación.', ['La investigación científica necesitaría más financiación.', 'Wetenschappelijk onderzoek zou meer geld nodig hebben.', 'Scientific research would need more funding.'], CONDH),
    R('b2-u19-l1', 'Su teoría fue muy criticada al principio.', ['Al principio nadie creía que su teoría fuera correcta.', 'Aanvankelijk geloofde niemand dat zijn theorie klopte.', 'At first nobody believed his theory was correct.'], IMPSUBJ),
    R('b2-u21-l1', 'Tienes que actualizar el sistema operativo.', ['Voy a actualizar el sistema operativo.', 'Ik ga het besturingssysteem bijwerken.', "I'm going to update the operating system."], IR_A),
    R('b2-u21-l4', 'Veo series en streaming casi todas las noches.', ['Antes veía series en streaming casi todas las noches.', 'Vroeger keek ik bijna elke avond series via streaming.', 'I used to watch series on streaming almost every night.'], IMPF),
    R('b2-u21-l2', 'Siempre rechazo las cookies de las páginas web.', ['Yo que tú rechazaría las cookies de las páginas web.', 'Als ik jou was, zou ik de cookies van websites weigeren.', "If I were you, I'd reject cookies on websites."], CONDH),
    R('b2-u22-l1', 'Es columnista y publica un artículo cada domingo.', ['Es columnista y ha publicado más de cien artículos.', 'Ze is columnist en heeft meer dan honderd artikelen gepubliceerd.', "She's a columnist and has published more than a hundred articles."], PERF),
    R('b2-u22-l3', 'Convocaron una rueda de prensa a las doce.', ['Van a convocar una rueda de prensa a las doce.', 'Ze gaan om twaalf uur een persconferentie houden.', "They're going to call a press conference at twelve."], IR_A),
    R('b2-u22-l3', 'Alguien filtró el documento a la prensa.', ['Alguien filtró el documento y se lo dio a la prensa.', 'Iemand lekte het document en gaf het aan de pers.', 'Someone leaked the document and gave it to the press.'], PRON),
    R('b2-u24-l3', 'Intentamos reducir el consumo de carne.', ['Este año vamos a reducir el consumo de carne.', 'Dit jaar gaan we minder vlees eten.', "This year we're going to cut down on meat."], IR_A),
    R('b2-u24-l1', 'Los incendios forestales son cada vez más frecuentes.', ['Antes los incendios forestales eran menos frecuentes.', 'Vroeger waren bosbranden minder vaak.', 'Forest fires used to be less frequent.'], IMPF),
    R('b2-u24-l2', 'Tenemos que dejar de depender de los combustibles fósiles.', ['Deberíamos dejar de depender de los combustibles fósiles.', 'We zouden niet langer afhankelijk moeten zijn van fossiele brandstoffen.', 'We should stop depending on fossil fuels.'], CONDH),
    R('b2-u24-l3', 'Me he comprado un coche eléctrico de segunda mano.', ['Me he comprado un coche eléctrico de segunda mano y lo cargo en casa.', 'Ik heb een tweedehands elektrische auto gekocht en ik laad hem thuis op.', "I've bought a second-hand electric car and I charge it at home."], PRON),
    R('b2-u25-l3', 'Saco a pasear al perro tres veces al día.', ['Ahora voy a sacar a pasear al perro.', 'Ik ga nu de hond uitlaten.', "I'm going to take the dog for a walk now."], IR_A),
    R('b2-u25-l1', 'El lobo es el gran depredador de la península.', ['Antes el lobo vivía en casi toda la península.', 'Vroeger leefde de wolf op bijna het hele schiereiland.', 'The wolf used to live almost all over the peninsula.'], IMPF),
    R('b2-u27-l3', 'Alquilamos una casa rural en la sierra de Gredos.', ['Vamos a alquilar una casa rural en la sierra de Gredos.', 'We gaan een vakantiehuisje huren in de Sierra de Gredos.', "We're going to rent a country house in the Sierra de Gredos."], IR_A),
    R('b2-u27-l1', 'Prefiero viajar en temporada baja, hay menos gente.', ['Preferiría viajar en temporada baja; hay menos gente.', 'Ik zou liever in het laagseizoen reizen; dan is het minder druk.', "I'd rather travel in the low season; there are fewer people."], CONDH),
    R('b2-u27-l1', 'Ya casi nadie reserva en una agencia de viajes.', ['Antes todo el mundo reservaba en una agencia de viajes.', 'Vroeger boekte iedereen bij een reisbureau.', 'Everyone used to book through a travel agency.'], IMPF),
    R('b2-u27-l4', 'Lleva la tarjeta de embarque en el móvil.', ['¿La tarjeta de embarque? Llévala en el móvil.', 'De instapkaart? Neem hem mee op je telefoon.', 'The boarding pass? Keep it on your phone.'], PRON),
    R('b2-u28-l1', 'Fuimos a una cata de vinos en La Rioja.', ['Hemos ido a una cata de vinos en La Rioja.', 'We zijn naar een wijnproeverij in La Rioja geweest.', "We've been to a wine tasting in La Rioja."], PERF),
    R('b2-u28-l4', 'Comemos fuera una vez a la semana.', ['Esta noche vamos a comer fuera.', 'Vanavond gaan we uit eten.', "Tonight we're going to eat out."], IR_A),
    R('b2-u28-l3', 'Este postre es demasiado empalagoso.', ['Yo no repetiría este postre; es demasiado empalagoso.', 'Ik zou dit toetje niet nog eens nemen; het is te zoet.', "I wouldn't have this dessert again; it's too sickly sweet."], CONDH),
    R('b2-u28-l2', 'Deja que el guiso se haga a fuego lento.', ['Deja que el guiso se haga a fuego lento; a mí siempre se me quema.', 'Laat de stoofpot op een laag vuur garen; bij mij brandt hij altijd aan.', 'Let the stew cook slowly; mine always burns.'], SEME),
    R('b2-u29-l1', 'Hizo un boceto antes de empezar el cuadro.', ['Ha hecho un boceto antes de empezar el cuadro.', 'Hij heeft een schets gemaakt voordat hij aan het schilderij begon.', "He's made a sketch before starting the painting."], PERF),
    R('b2-u29-l4', 'Leí una reseña muy elogiosa de la exposición.', ['Leí una reseña muy elogiosa y voy a ir a la exposición.', 'Ik las een lovende recensie en ik ga naar de tentoonstelling.', "I read a glowing review and I'm going to go to the exhibition."], IR_A),
    R('b2-u29-l2', 'No entiendo mucho el arte abstracto.', ['Me gustaría que alguien me explicara el arte abstracto.', 'Ik zou willen dat iemand me abstracte kunst uitlegde.', "I'd like someone to explain abstract art to me."], IMPSUBJ),
    R('b2-u30-l3', 'Vimos una obra de teatro de Lorca.', ['Hemos visto una obra de teatro de Lorca.', 'We hebben een toneelstuk van Lorca gezien.', "We've seen a play by Lorca."], PERF),
    R('b2-u30-l3', 'Recoge las entradas en la taquilla.', ['Voy a recoger las entradas en la taquilla.', 'Ik ga de kaartjes bij de kassa ophalen.', "I'm going to pick up the tickets at the box office."], IR_A),
    R('b2-u30-l3', 'Subir al escenario me pone muy nervioso.', ['Nunca subiría al escenario; me pondría muy nervioso.', 'Ik zou nooit het podium op gaan; ik zou heel zenuwachtig worden.', "I'd never go on stage; I'd get very nervous."], CONDH),
    R('b2-u30-l1', 'La letra de esta canción es muy triste.', ['La letra de esta canción es muy triste, pero te la canto.', 'De tekst van dit liedje is heel verdrietig, maar ik zing het voor je.', "The lyrics of this song are very sad, but I'll sing it for you."], PRON),
    R('b2-u32-l1', 'Cojo el autobús a las ocho.', ['Cuando vivía en Madrid, cogía el autobús a las ocho.', 'Toen ik in Madrid woonde, nam ik de bus om acht uur.', 'When I lived in Madrid, I took the bus at eight.'], IMPF),
    R('b2-u32-l1', '¿Has visto mis gafas?', ['¿Has visto mis gafas? No las encuentro.', 'Heb je mijn bril gezien? Ik kan hem niet vinden.', "Have you seen my glasses? I can't find them."], PRON),
    R('b2-u33-l3', 'Rindieron homenaje a los fallecidos.', ['Les rindieron homenaje a los fallecidos.', 'Ze brachten hulde aan de overledenen.', 'They paid tribute to the dead.'], PRON),
    R('b2-u35-l4', 'El debate de anoche fue muy tenso.', ['El debate de anoche fue muy tenso; nadie escuchaba a nadie.', 'Het debat van gisteravond was heel gespannen; niemand luisterde naar elkaar.', "Last night's debate was very tense; nobody was listening to anyone."], IMPF),
    R('b2-u37-l2', 'Hago musculación tres veces por semana en el gimnasio.', ['Voy a hacer musculación tres veces por semana en el gimnasio.', 'Ik ga drie keer per week aan krachttraining doen in de sportschool.', "I'm going to do weight training three times a week at the gym."], IR_A),
    R('b2-u37-l4', 'Las jugadoras reclaman igualdad salarial.', ['Las jugadoras reclamaban que les pagaran lo mismo.', 'De speelsters eisten dat ze hetzelfde betaald kregen.', 'The players demanded that they be paid the same.'], IMPSUBJ + ' En les.'),
    R('b2-u38-l1', 'La despoblación afecta a muchas zonas del interior.', ['La despoblación ha afectado a muchas zonas del interior.', 'De ontvolking heeft veel gebieden in het binnenland getroffen.', 'Depopulation has affected many inland areas.'], PERF),
    R('b2-u38-l3', 'Prefiero ser optimista sobre el futuro.', ['Voy a ser optimista sobre el futuro.', 'Ik ga optimistisch zijn over de toekomst.', "I'm going to be optimistic about the future."], IR_A),
    R('b2-u38-l4', 'Una sociedad sin pobreza parece una utopía.', ['Hace cien años, una sociedad sin pobreza parecía una utopía.', 'Honderd jaar geleden leek een samenleving zonder armoede een utopie.', 'A hundred years ago, a society without poverty seemed a utopia.'], IMPF),
    R('b2-u40-l3', 'Lo pasamos bomba en la fiesta.', ['Lo hemos pasado bomba en la fiesta.', 'We hebben het superleuk gehad op het feest.', "We've had a blast at the party."], PERF),
    R('b2-u40-l3', '¿Qué haces este finde?', ['¿Qué vas a hacer este finde?', 'Wat ga je dit weekend doen?', 'What are you going to do this weekend?'], IR_A),
    R('b2-u40-l3', 'Me piro, que es tarde.', ['Me piro, que se me ha hecho tarde.', 'Ik smeer ’m, het is laat geworden.', "I'm off, it's got late."], SEME),
]

if __name__ == '__main__':
    replace_sentences(CHANGES)
    replace_sentences(REUSE)
