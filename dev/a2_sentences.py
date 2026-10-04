# A2: zinnen met grammatica die nog niet behandeld is vervangen, en geleerde vormen laten terugkomen.
# In A2 komt de verleden tijd stap voor stap: indefinido regelmatig (unit 6), gebiedende wijs (unit 7),
# lo/la/le (unit 16), imperfecto (unit 32), onregelmatige indefinido (unit 34).
# Gebruik: python3 dev/a2_sentences.py   (idempotent)
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sentence_tools import replace_sentences, replace_text, move_intro

TE_VROEG = 'te vroeg'
HERHALING = 'herhaling'
FOUT = 'fout'

IRREG = 'Onregelmatige verleden tijd (fui, tuve, hice...) komt pas in unit 34; de voltooide tijd ken je al uit A1.'
INDEF = 'De verleden tijd (indefinido) komt pas in unit 6; de voltooide tijd ken je al uit A1.'
IMPERF = 'De imperfecto komt pas in unit 32.'
SE_ME = '"Se me ha..." (iets overkomt je) komt pas in B2.'

CHANGES = [
    # unit 2
    ('a2-u2-l3', 'Anoche soñé con mis vacaciones.',
        ['Esta noche he soñado con mis vacaciones.', 'Vannacht heb ik over mijn vakantie gedroomd.', 'Last night I dreamt about my holiday.', ['He soñado con mis vacaciones esta noche.']], (TE_VROEG, INDEF)),
    ('a2-u2-l3', 'Anoche tuve una pesadilla.',
        ['Esta noche he tenido una pesadilla.', 'Vannacht heb ik een nachtmerrie gehad.', 'Last night I had a nightmare.', ['He tenido una pesadilla esta noche.']], (TE_VROEG, IRREG)),
    ('a2-u2-l4', 'Ayer me acosté muy tarde.',
        ['Esta semana me he acostado muy tarde.', 'Deze week ben ik heel laat naar bed gegaan.', "This week I've gone to bed very late."], (TE_VROEG, INDEF)),
    # unit 4
    ('a2-u4-l2', 'Avísame si no puedes venir.',
        ['¿Me avisas si no puedes venir?', 'Laat je het me weten als je niet kunt komen?', "Will you let me know if you can't come?"], (TE_VROEG, 'Gebiedende wijs (avísame) komt pas in unit 7.')),
    ('a2-u4-l2', 'Perdona, se me ha olvidado.',
        ['Perdona, he olvidado la cita.', 'Sorry, ik ben de afspraak vergeten.', 'Sorry, I forgot the appointment.', ['Perdona, me he olvidado de la cita.']], (TE_VROEG, SE_ME)),
    ('a2-u4-l2', 'Tuve que posponer la reunión.',
        ['He tenido que posponer la reunión.', 'Ik heb de vergadering moeten uitstellen.', "I've had to postpone the meeting."], (TE_VROEG, IRREG)),
    ('a2-u4-l2', 'Ayer cancelé la cena con mis amigos.',
        ['Hoy he cancelado la cena con mis amigos.', 'Vandaag heb ik het etentje met mijn vrienden afgezegd.', 'Today I cancelled dinner with my friends.'], (TE_VROEG, INDEF)),
    ('a2-u4-l4', 'Ayer quedé con mi prima.',
        ['Hoy he quedado con mi prima.', 'Vandaag heb ik met mijn nicht afgesproken.', 'Today I met up with my cousin.'], (TE_VROEG, INDEF)),
    ('a2-u4-l4', '¿Con quién quedaste el sábado?',
        ['¿Con quién vas a quedar el sábado?', 'Met wie ga je zaterdag afspreken?', 'Who are you going to meet on Saturday?'], (TE_VROEG, INDEF + ' Nu met ir a (herhaling).')),
    ('a2-u4-l4', 'Mis amigos quedaron en el punto de encuentro de siempre.',
        ['Mis amigos han quedado en el punto de encuentro de siempre.', 'Mijn vrienden hebben afgesproken op de gebruikelijke ontmoetingsplek.', 'My friends have arranged to meet at the usual meeting point.'], (TE_VROEG, INDEF)),
    # unit 5
    ('a2-u5-l3', 'Vimos un relámpago enorme.',
        ['Hemos visto un relámpago enorme.', 'We hebben een enorme bliksemflits gezien.', "We've seen a huge flash of lightning."], (TE_VROEG, INDEF)),
    ('a2-u5-l3', 'Después de la lluvia salió el arcoíris.',
        ['Después de la lluvia sale el arcoíris.', 'Na de regen komt de regenboog.', 'After the rain the rainbow comes out.'], (TE_VROEG, INDEF)),
    ('a2-u5-l3', 'Ayer cayó granizo.',
        ['Hoy ha caído granizo.', 'Vandaag heeft het gehageld.', 'It has hailed today.'], (TE_VROEG, IRREG)),
    ('a2-u5-l3', 'Cayó un aguacero por la tarde.',
        ['Esta tarde ha caído un aguacero.', 'Vanmiddag is er een stortbui gevallen.', 'This afternoon there was a downpour.'], (TE_VROEG, IRREG)),
    ('a2-u5-l4', 'Cuando salí, llovía mucho.',
        ['Ayer por la tarde llovía mucho.', 'Gistermiddag regende het hard.', 'Yesterday afternoon it was raining a lot.'], (TE_VROEG, 'Hier oefen je het weer van vroeger (llovía). Salí (indefinido) komt pas in unit 6.')),
    ('a2-u5-l4', 'Cuando era pequeño, nevaba mucho.',
        ['De pequeño, nevaba mucho en invierno.', 'Toen ik klein was, sneeuwde het veel in de winter.', 'When I was little, it snowed a lot in winter.', ['De pequeña, nevaba mucho en invierno.']], (TE_VROEG, 'Era (van ser) komt pas in unit 32.')),
    ('a2-u5-l4', 'Estaba nublado cuando salimos.',
        ['Esta mañana estaba nublado.', 'Vanochtend was het bewolkt.', 'This morning it was cloudy.'], (TE_VROEG, INDEF)),
    ('a2-u5-l4', 'Había tormenta y no pudimos salir.',
        ['Ayer había tormenta y llovía mucho.', 'Gisteren was er onweer en regende het hard.', 'Yesterday there was a storm and it was raining hard.'], (TE_VROEG, IRREG)),
    ('a2-u5-l4', 'Llovía cuando llegué a casa.',
        ['El domingo hacía sol, pero hacía frío.', 'Zondag scheen de zon, maar het was koud.', 'On Sunday it was sunny, but it was cold.'], (TE_VROEG, INDEF)),
    ('a2-u5-l4', 'De pequeño, pasaba los veranos en el pueblo.',
        ['De pequeño, en verano hacía mucho calor en el pueblo.', 'Toen ik klein was, was het in de zomer heel warm in het dorp.', 'When I was little, it was very hot in the village in summer.', ['De pequeña, en verano hacía mucho calor en el pueblo.']], (TE_VROEG, 'Pasaba (imperfecto, niet over het weer) komt pas in unit 32.')),
    # unit 6
    ('a2-u6-l2', 'El estadio estaba lleno.',
        ['El estadio está lleno.', 'Het stadion zit vol.', 'The stadium is full.'], (TE_VROEG, IMPERF)),
    # unit 10
    ('a2-u10-l2', 'Lo hizo por amor.',
        ['Vivo en España por amor.', 'Ik woon in Spanje uit liefde.', 'I live in Spain for love.'], (TE_VROEG, 'Hizo (onregelmatig) en lo komen later.')),
    ('a2-u10-l2', 'No salimos por la lluvia.',
        ['No salimos por la lluvia.', 'We gaan niet naar buiten door de regen.', "We're not going out because of the rain."], (FOUT, 'De Nederlandse vertaling stond in de verleden tijd, de Spaanse zin niet.')),
    ('a2-u10-l2', 'Estaba cansado; por eso me fui a casa.',
        ['Estoy cansado; por eso me voy a casa.', 'Ik ben moe; daarom ga ik naar huis.', "I'm tired; that's why I'm going home.", ['Estoy cansada; por eso me voy a casa.']], (TE_VROEG, IMPERF + ' Fui komt pas in unit 34.')),
    ('a2-u10-l3', 'Para entonces ya estaré en casa.',
        ['Para entonces ya voy a estar en casa.', 'Tegen die tijd ben ik al thuis.', "By then I'll already be home."], (TE_VROEG, 'De futuro (estaré) komt pas in B1; ir a ken je al.')),
    ('a2-u10-l4', 'Te lo mando por correo.',
        ['Te mando las fotos por correo.', "Ik stuur je de foto's per mail.", "I'll send you the photos by email."], (TE_VROEG, 'Te lo komt pas in unit 16.')),
    # unit 11
    ('a2-u11-l1', 'Le confirmo la reserva por correo.',
        ['Confirmo la reserva por correo.', 'Ik bevestig de reservering per mail.', 'I confirm the booking by email.'], (TE_VROEG, 'Le komt pas in unit 16.')),
    ('a2-u11-l2', 'Fuimos a una agencia de viajes.',
        ['Hemos ido a una agencia de viajes.', 'We zijn naar een reisbureau gegaan.', "We've been to a travel agency."], (TE_VROEG, IRREG)),
    ('a2-u11-l3', 'El pago se hace al llegar.',
        ['Pagamos al llegar.', 'We betalen bij aankomst.', 'We pay on arrival.'], (TE_VROEG, 'Se hace (onpersoonlijk se) komt pas in B1.')),
    ('a2-u11-l3', 'Tuvimos que cancelar la reserva.',
        ['Hemos tenido que cancelar la reserva.', 'We hebben de reservering moeten annuleren.', "We've had to cancel the booking."], (TE_VROEG, IRREG)),
    # unit 12-15
    ('a2-u12-l3', 'La tripulación fue muy amable.',
        ['La tripulación es muy amable.', 'De bemanning is heel vriendelijk.', 'The crew is very friendly.'], (TE_VROEG, IRREG)),
    ('a2-u13-l1', 'Hicimos una excursión a la montaña.',
        ['Hemos hecho una excursión a la montaña.', 'We hebben een uitstapje naar de bergen gemaakt.', "We've been on a trip to the mountains."], (TE_VROEG, IRREG)),
    ('a2-u13-l3', 'Fue un viaje inolvidable.',
        ['Ha sido un viaje inolvidable.', 'Het was een onvergetelijke reis.', 'It has been an unforgettable trip.'], (TE_VROEG, IRREG)),
    ('a2-u13-l3', 'Fue una experiencia única.',
        ['Ha sido una experiencia única.', 'Het was een unieke ervaring.', 'It has been a unique experience.'], (TE_VROEG, IRREG)),
    ('a2-u14-l2', 'El examen no fue tan difícil como pensaba.',
        ['El examen no ha sido tan difícil como el otro.', 'Het examen was niet zo moeilijk als het andere.', "The exam wasn't as difficult as the other one."], (TE_VROEG, IRREG + ' Pensaba (imperfecto) komt pas in unit 32.')),
    ('a2-u14-l3', 'Fue el peor día de mi vida.',
        ['Hoy ha sido el peor día de mi vida.', 'Vandaag was de slechtste dag van mijn leven.', 'Today has been the worst day of my life.'], (TE_VROEG, IRREG)),
    ('a2-u15-l2', 'Guarde el tique para cambiarlo.',
        ['Guardo el tique para poder cambiar la camisa.', 'Ik bewaar de bon om het overhemd te kunnen ruilen.', 'I keep the receipt so I can exchange the shirt.'], (TE_VROEG, 'Lo achter het werkwoord (cambiarlo) komt pas in unit 16.')),
    # unit 20-27
    ('a2-u20-l2', 'El servicio fue excelente.',
        ['El servicio ha sido excelente.', 'De bediening was uitstekend.', 'The service has been excellent.'], (TE_VROEG, IRREG)),
    ('a2-u21-l1', 'Los sellos se venden en el estanco.',
        ['En el estanco venden sellos.', 'In de tabakswinkel verkopen ze postzegels.', "They sell stamps at the tobacconist's."], (TE_VROEG, 'Se venden (lijdende vorm met se) komt pas in B2.')),
    ('a2-u21-l3', 'Se me ha estropeado la lavadora.',
        ['La lavadora se ha estropeado.', 'De wasmachine is kapotgegaan.', 'The washing machine has broken down.'], (TE_VROEG, SE_ME)),
    ('a2-u25-l1', 'Se dio un golpe en el codo.',
        ['Se ha dado un golpe en el codo.', 'Hij heeft zijn elleboog gestoten.', 'He has banged his elbow.', ['Ella se ha dado un golpe en el codo.']], (TE_VROEG, IRREG)),
    ('a2-u25-l1', 'Me di un golpe en el pulgar.',
        ['Me he dado un golpe en el pulgar.', 'Ik heb mijn duim gestoten.', "I've banged my thumb."], (TE_VROEG, IRREG)),
    ('a2-u25-l4', 'Se dio un golpe en la barbilla.',
        ['Se ha dado un golpe en la barbilla.', 'Hij heeft zijn kin gestoten.', 'He has banged his chin.', ['Ella se ha dado un golpe en la barbilla.']], (TE_VROEG, IRREG)),
    ('a2-u26-l1', 'Me puse enfermo en las vacaciones.',
        ['Me he puesto enfermo en las vacaciones.', 'Ik ben ziek geworden tijdens de vakantie.', 'I got ill during the holidays.', ['Me he puesto enferma en las vacaciones.']], (TE_VROEG, IRREG)),
    ('a2-u26-l3', 'No tomes medicinas sin receta.',
        ['Nunca tomo medicinas sin receta.', 'Ik neem nooit medicijnen zonder recept.', 'I never take medicine without a prescription.'], (TE_VROEG, 'Ontkennende gebiedende wijs (no tomes) komt pas in B1.')),
    ('a2-u27-l1', 'Fuimos a urgencias por la noche.',
        ['Esta noche hemos ido a urgencias.', 'Vannacht zijn we naar de spoedeisende hulp gegaan.', 'Last night we went to A&E.', ['Hemos ido a urgencias esta noche.']], (TE_VROEG, IRREG)),
    ('a2-u27-l3', 'La operación fue un éxito.',
        ['La operación ha sido un éxito.', 'De operatie was een succes.', 'The operation has been a success.'], (TE_VROEG, IRREG)),
    # unit 29-35
    ('a2-u29-l2', 'Se me ha roto el paraguas.',
        ['He roto el paraguas.', 'Ik heb de paraplu kapotgemaakt.', "I've broken the umbrella."], (TE_VROEG, SE_ME)),
    ('a2-u31-l1', 'Aprobar el examen fue un gran logro.',
        ['Aprobar el examen ha sido un gran logro.', 'Slagen voor het examen was een grote prestatie.', 'Passing the exam has been a great achievement.'], (TE_VROEG, IRREG)),
    ('a2-u32-l1', 'Tuve una infancia muy feliz.',
        ['De niño era muy feliz.', 'Als kind was ik heel gelukkig.', 'As a child I was very happy.', ['De niña era muy feliz.']], (TE_VROEG, IRREG + ' Nu in de imperfecto van deze unit.')),
    ('a2-u33-l1', 'En esa época se usaba la máquina de escribir.',
        ['En esa época usábamos la máquina de escribir.', 'In die tijd gebruikten we de typemachine.', 'Back then we used the typewriter.'], (TE_VROEG, 'Se usaba (onpersoonlijk se) komt pas in B1.')),
    ('a2-u33-l3', 'Ya no se usan las cartas.',
        ['Ya no escribimos cartas.', 'We schrijven geen brieven meer.', "We don't write letters any more."], (TE_VROEG, 'Se usan (lijdende vorm met se) komt pas in B2.')),
    ('a2-u35-l1', 'Nunca olvidaré aquel día.',
        ['Nunca voy a olvidar aquel día.', 'Ik ga die dag nooit vergeten.', "I'm never going to forget that day."], (TE_VROEG, 'De futuro (olvidaré) komt pas in B1; ir a ken je al.')),
]

# Herhaling: geleerde vormen (ir a, voltooide tijd, estar + gerundio, verleden tijd, lo/la, imperfecto)
# laten terugkomen. Bestaande zinnen worden omgezet; de woorden van de les blijven erin.
IR_A = 'Ir a + infinitief (A1 unit 22) laten terugkomen.'
PERF = 'Voltooide tijd (A1 unit 23) laten terugkomen.'
PROG = 'Estar + gerundio (A1) laten terugkomen.'
PRET = 'Verleden tijd (indefinido, unit 6) laten terugkomen.'
LOLA = 'Lo/la (unit 16) laten terugkomen.'
IMPF = 'Imperfecto (unit 32) laten terugkomen.'

REUSE = [
    ('a2-u1-l1', 'Necesito comprar champú.', ['Voy a comprar champú.', 'Ik ga shampoo kopen.', "I'm going to buy shampoo."], (HERHALING, IR_A)),
    ('a2-u2-l2', 'Leo una revista en el sofá.', ['Voy a leer una revista en el sofá.', 'Ik ga een tijdschrift lezen op de bank.', "I'm going to read a magazine on the sofa."], (HERHALING, IR_A)),
    ('a2-u3-l2', 'Hago fotos de paisajes.', ['Este verano voy a hacer fotos de paisajes.', "Deze zomer ga ik foto's van landschappen maken.", "This summer I'm going to take photos of landscapes.", ['Voy a hacer fotos de paisajes este verano.']], (HERHALING, IR_A)),
    ('a2-u4-l3', 'Tengo un hueco el miércoles.', ['Estoy mirando la agenda y tengo un hueco el miércoles.', 'Ik kijk in mijn agenda en ik heb woensdag nog een gaatje.', "I'm looking at my diary and I have a gap on Wednesday."], (HERHALING, PROG)),
    ('a2-u6-l1', 'Voy al gimnasio por la mañana.', ['Esta mañana he ido al gimnasio.', 'Vanochtend ben ik naar de sportschool gegaan.', 'This morning I went to the gym.', ['He ido al gimnasio esta mañana.']], (HERHALING, PERF)),
    ('a2-u7-l3', 'Tengo un plano de la ciudad en el móvil.', ['Estoy mirando el plano de la ciudad en el móvil.', 'Ik kijk op de plattegrond van de stad op mijn telefoon.', "I'm looking at the city map on my phone."], (HERHALING, PROG)),
    ('a2-u7-l4', 'Pago el peaje y sigo por la circunvalación.', ['Ayer pagué el peaje y seguí por la circunvalación.', 'Gisteren betaalde ik de tol en bleef ik op de ringweg.', 'Yesterday I paid the toll and stayed on the ring road.'], (HERHALING, PRET)),
    ('a2-u8-l1', 'Cojo el tranvía para ir al centro.', ['Voy a coger el tranvía para ir al centro.', 'Ik ga de tram nemen naar het centrum.', "I'm going to take the tram to the centre."], (HERHALING, IR_A)),
    ('a2-u9-l2', 'Visito el jardín botánico los domingos.', ['Hoy he visitado el jardín botánico.', 'Vandaag heb ik de botanische tuin bezocht.', "Today I've visited the botanical garden."], (HERHALING, PERF)),
    ('a2-u9-l2', 'Voy a la biblioteca a estudiar.', ['Voy a estudiar en la biblioteca.', 'Ik ga in de bibliotheek studeren.', "I'm going to study in the library."], (HERHALING, IR_A)),
    ('a2-u9-l1', 'Compro el periódico en el quiosco.', ['Estoy comprando el periódico en el quiosco.', 'Ik ben de krant aan het kopen bij de kiosk.', "I'm buying the newspaper at the kiosk."], (HERHALING, PROG)),
    ('a2-u9-l4', 'Conocemos el acueducto de Segovia.', ['El año pasado conocimos el acueducto de Segovia.', 'Vorig jaar leerden we het aquaduct van Segovia kennen.', 'Last year we got to know the aqueduct of Segovia.'], (HERHALING, PRET)),
    ('a2-u10-l4', 'Compro los billetes por internet.', ['He comprado los billetes por internet.', 'Ik heb de kaartjes via internet gekocht.', "I've bought the tickets online."], (HERHALING, PERF)),
    ('a2-u10-l1', 'Camino por la ciudad.', ['Estoy caminando por la ciudad.', 'Ik ben door de stad aan het lopen.', "I'm walking through the city."], (HERHALING, PROG)),
    ('a2-u10-l1', 'Paseamos por el parque.', ['Ayer paseamos por el parque.', 'Gisteren wandelden we door het park.', 'Yesterday we walked through the park.'], (HERHALING, PRET)),
    ('a2-u11-l2', 'Viajamos en temporada baja.', ['Vamos a viajar en temporada baja.', 'We gaan in het laagseizoen reizen.', "We're going to travel in the low season."], (HERHALING, IR_A)),
    ('a2-u12-l1', 'Pongo la ropa en la bolsa de viaje.', ['Voy a poner la ropa en la bolsa de viaje.', 'Ik ga de kleren in de reistas doen.', "I'm going to put the clothes in the travel bag."], (HERHALING, IR_A)),
    ('a2-u12-l2', 'Pasamos por el control de seguridad.', ['Estamos pasando por el control de seguridad.', 'We gaan nu door de beveiligingscontrole.', "We're going through security."], (HERHALING, PROG)),
    ('a2-u13-l3', 'Seguimos un sendero entre los árboles.', ['Vamos a seguir un sendero entre los árboles.', 'We gaan een wandelpad tussen de bomen volgen.', "We're going to follow a path through the trees."], (HERHALING, IR_A)),
    ('a2-u13-l2', 'Sacamos fotos del castillo.', ['Estamos sacando fotos del castillo.', "We zijn foto's van het kasteel aan het maken.", "We're taking photos of the castle."], (HERHALING, PROG)),
    ('a2-u14-l3', 'Este es el mejor restaurante.', ['Vamos a cenar en el mejor restaurante de la ciudad.', 'We gaan eten in het beste restaurant van de stad.', "We're going to have dinner at the best restaurant in town."], (HERHALING, IR_A)),
    ('a2-u14-l1', 'Esta película es menos interesante que la otra.', ['Estoy viendo una película menos interesante que la otra.', 'Ik kijk een film die minder interessant is dan de andere.', "I'm watching a film that is less interesting than the other one."], (HERHALING, PROG)),
    ('a2-u14-l3', 'Es el hotel más caro de la zona.', ['El año pasado dormimos en el hotel más caro de la zona.', 'Vorig jaar sliepen we in het duurste hotel van de omgeving.', 'Last year we slept in the most expensive hotel in the area.'], (HERHALING, PRET)),
    ('a2-u15-l1', 'Me gusta ese vestido del escaparate.', ['Estoy mirando ese vestido del escaparate.', 'Ik kijk naar die jurk in de etalage.', "I'm looking at that dress in the shop window."], (HERHALING, PROG)),
    ('a2-u16-l1', 'Me gusta este bolso; lo compro.', ['Me gusta este bolso; lo voy a comprar.', 'Ik vind deze tas mooi; ik ga hem kopen.', "I like this bag; I'm going to buy it.", ['Me gusta este bolso; voy a comprarlo.']], (HERHALING, IR_A + ' Lo kan voor voy of achter comprar.')),
    ('a2-u16-l3', 'Le regalo flores a mi abuela.', ['Ayer le regalé flores a mi abuela.', 'Gisteren gaf ik mijn oma bloemen.', 'Yesterday I gave my grandmother flowers.'], (HERHALING, PRET)),
    ('a2-u17-l1', 'Guardo el tique de compra.', ['He guardado el tique de compra.', 'Ik heb de kassabon bewaard.', "I've kept the receipt."], (HERHALING, PERF)),
    ('a2-u17-l3', 'Compro un litro de leche.', ['Voy a comprar un litro de leche.', 'Ik ga een liter melk kopen.', "I'm going to buy a litre of milk."], (HERHALING, IR_A)),
    ('a2-u17-l3', 'Traigo mi bolsa reutilizable.', ['Traigo mi bolsa reutilizable; la uso siempre.', 'Ik neem mijn herbruikbare tas mee; ik gebruik hem altijd.', 'I bring my reusable bag; I always use it.'], (HERHALING, LOLA)),
    ('a2-u18-l2', 'Compro verduras frescas.', ['He comprado verduras frescas.', 'Ik heb verse groenten gekocht.', "I've bought fresh vegetables."], (HERHALING, PERF)),
    ('a2-u18-l2', 'Compro una sandía para la playa.', ['Voy a comprar una sandía para la playa.', 'Ik ga een watermeloen kopen voor het strand.', "I'm going to buy a watermelon for the beach."], (HERHALING, IR_A)),
    ('a2-u18-l1', 'El vendedor es muy simpático.', ['El vendedor está pesando las naranjas.', 'De verkoper is de sinaasappels aan het wegen.', 'The seller is weighing the oranges.'], (HERHALING, PROG)),
    ('a2-u18-l3', 'Compro chorizo para el bocadillo.', ['Este chorizo es muy bueno; lo compro para el bocadillo.', 'Deze chorizo is heel lekker; ik koop hem voor op het broodje.', "This chorizo is very good; I'm buying it for the sandwich."], (HERHALING, LOLA)),
    ('a2-u19-l1', 'El camarero recomienda el pescado.', ['El camarero nos ha recomendado el pescado.', 'De ober heeft ons de vis aangeraden.', 'The waiter has recommended the fish to us.'], (HERHALING, PERF)),
    ('a2-u19-l2', 'Quiero el pescado a la plancha.', ['Voy a pedir el pescado a la plancha.', 'Ik ga de gegrilde vis bestellen.', "I'm going to order the grilled fish."], (HERHALING, IR_A)),
    ('a2-u19-l1', 'El camarero nos trae la carta.', ['El camarero nos está trayendo la carta.', 'De ober is de kaart aan het brengen.', 'The waiter is bringing us the menu.'], (HERHALING, PROG)),
    ('a2-u19-l2', 'De postre, flan casero.', ['El flan es casero; lo pido de postre.', 'De flan is huisgemaakt; ik bestel hem als toetje.', "The flan is homemade; I'm ordering it for dessert."], (HERHALING, LOLA)),
    ('a2-u20-l2', 'Llevo los billetes en el billetero.', ['Estoy buscando los billetes en el billetero.', 'Ik zoek de biljetten in mijn portefeuille.', "I'm looking for the notes in my wallet."], (HERHALING, PROG)),
    ('a2-u20-l4', 'Guarda el comprobante de pago.', ['Guarda el comprobante de pago; lo vas a necesitar.', 'Bewaar het betaalbewijs; je gaat het nodig hebben.', "Keep the proof of payment; you're going to need it.", ['Guarda el comprobante de pago; vas a necesitarlo.']], (HERHALING, LOLA + ' En ir a.')),
    ('a2-u21-l3', 'El zapatero arregla mis botas.', ['El zapatero está arreglando mis botas.', 'De schoenmaker is mijn laarzen aan het repareren.', 'The shoemaker is repairing my boots.'], (HERHALING, PROG)),
    ('a2-u21-l2', 'Envío el paquete certificado.', ['El paquete es importante; lo envío certificado.', 'Het pakket is belangrijk; ik verstuur het aangetekend.', "The parcel is important; I'm sending it by registered mail."], (HERHALING, LOLA)),
    ('a2-u21-l1', 'Compro flores en la floristería.', ['Ayer compré flores en la floristería.', 'Gisteren kocht ik bloemen bij de bloemenwinkel.', 'Yesterday I bought flowers at the florist.'], (HERHALING, PRET)),
    ('a2-u22-l3', 'Alquilamos un piso en el centro.', ['Hemos alquilado un piso en el centro.', 'We hebben een appartement in het centrum gehuurd.', "We've rented a flat in the centre."], (HERHALING, PERF)),
    ('a2-u22-l1', 'Guardamos las bicis en el trastero.', ['Vamos a guardar las bicis en el trastero.', 'We gaan de fietsen in de berging zetten.', "We're going to put the bikes in the storage room."], (HERHALING, IR_A)),
    ('a2-u22-l2', 'Tendemos la ropa en la azotea.', ['Estamos tendiendo la ropa en la azotea.', 'We zijn de was aan het ophangen op het dakterras.', "We're hanging the washing on the roof terrace."], (HERHALING, PROG)),
    ('a2-u22-l4', 'Cierro la persiana por la noche.', ['Cierro la persiana por la noche y la abro por la mañana.', "'s Avonds doe ik het rolluik dicht en 's ochtends doe ik het open.", 'I close the blind at night and open it in the morning.'], (HERHALING, LOLA)),
    ('a2-u23-l2', 'Necesito un colchón nuevo.', ['He comprado un colchón nuevo.', 'Ik heb een nieuw matras gekocht.', "I've bought a new mattress."], (HERHALING, PERF)),
    ('a2-u23-l3', 'Me gusta decorar mi casa.', ['Estoy decorando mi casa.', 'Ik ben mijn huis aan het inrichten.', "I'm decorating my house."], (HERHALING, PROG)),
    ('a2-u23-l4', '¿Dónde pongo este cuadro?', ['Este cuadro es precioso; ¿dónde lo pongo?', 'Dit schilderij is prachtig; waar zet ik het neer?', 'This painting is beautiful; where shall I put it?'], (HERHALING, LOLA)),
    ('a2-u23-l1', 'Compramos muebles nuevos.', ['La semana pasada compramos muebles nuevos.', 'Vorige week kochten we nieuwe meubels.', 'Last week we bought new furniture.'], (HERHALING, PRET)),
    ('a2-u24-l1', 'Paso la aspiradora los sábados.', ['Mañana voy a pasar la aspiradora.', 'Morgen ga ik stofzuigen.', "Tomorrow I'm going to vacuum.", ['Voy a pasar la aspiradora mañana.']], (HERHALING, IR_A)),
    ('a2-u24-l2', 'Guardo la ropa en el armario.', ['Doblo la ropa y la guardo en el armario.', 'Ik vouw de kleren en berg ze op in de kast.', 'I fold the clothes and put them away in the wardrobe.'], (HERHALING, LOLA)),
    ('a2-u25-l3', 'Tengo el párpado rojo.', ['Tengo el párpado rojo; voy a ir al médico.', 'Mijn ooglid is rood; ik ga naar de dokter.', "My eyelid is red; I'm going to the doctor."], (HERHALING, IR_A)),
    ('a2-u26-l2', 'Hoy me quedo en cama.', ['Hoy me voy a quedar en cama.', 'Vandaag blijf ik in bed.', "Today I'm going to stay in bed.", ['Hoy voy a quedarme en cama.']], (HERHALING, IR_A)),
    ('a2-u26-l3', 'Tomo paracetamol para el dolor de cabeza.', ['Estoy tomando paracetamol para el dolor de cabeza.', 'Ik neem paracetamol tegen de hoofdpijn.', "I'm taking paracetamol for the headache."], (HERHALING, PROG)),
    ('a2-u27-l1', 'Espero en la sala de espera.', ['Estoy esperando en la sala de espera.', 'Ik zit in de wachtkamer te wachten.', "I'm waiting in the waiting room."], (HERHALING, PROG)),
    ('a2-u32-l3', 'Miro fotos antiguas de mi familia.', ['Estoy mirando fotos antiguas de mi familia.', "Ik ben oude foto's van mijn familie aan het bekijken.", "I'm looking at old photos of my family."], (HERHALING, PROG)),
    ('a2-u34-l3', 'Es un escritor muy conocido.', ['Era un escritor muy conocido.', 'Hij was een heel bekende schrijver.', 'He was a very well-known writer.'], (HERHALING, IMPF)),
    ('a2-u34-l3', 'Leí la biografía de un músico famoso.', ['He leído la biografía de un músico famoso.', 'Ik heb de biografie van een beroemde muzikant gelezen.', "I've read the biography of a famous musician."], (HERHALING, PERF)),
]

# Voornaamwoorden (unit 16) door de rest van A2 laten terugkomen: per unit lo/la, le/les en se lo/me lo of achteraan.
PRON = 'Voornaamwoorden (lo/la, le/les, se lo, achteraan) laten terugkomen.'
PRON_REUSE = [
    ('a2-u17-l2', 'Tengo un cupón de descuento.', ['Tengo un cupón de descuento; se lo doy al cajero.', 'Ik heb een kortingsbon; ik geef hem aan de caissier.', 'I have a discount coupon; I give it to the cashier.'], (HERHALING, PRON)),
    ('a2-u17-l1', 'El cajero es muy simpático.', ['El cajero me da el tique y le doy las gracias.', 'De caissier geeft me de bon en ik bedank hem.', 'The cashier gives me the receipt and I thank him.'], (HERHALING, PRON)),
    ('a2-u18-l1', 'El tendero es muy amable.', ['Le pregunto al tendero el precio de las cerezas.', 'Ik vraag de winkelier de prijs van de kersen.', 'I ask the shopkeeper the price of the cherries.', ['Le pregunto el precio de las cerezas al tendero.']], (HERHALING, PRON)),
    ('a2-u19-l4', 'Pido una cucharilla y una jarra de agua.', ['Necesito una cucharilla; ¿me la trae, por favor?', 'Ik heb een lepeltje nodig; kunt u het me brengen?', 'I need a teaspoon; could you bring it to me, please?'], (HERHALING, PRON)),
    ('a2-u20-l3', 'Hay un error en la cuenta.', ['Hay un error en la cuenta; voy a decírselo al camarero.', 'Er zit een fout in de rekening; ik ga het tegen de ober zeggen.', "There's a mistake in the bill; I'm going to tell the waiter.", ['Hay un error en la cuenta; se lo voy a decir al camarero.']], (HERHALING, PRON)),
    ('a2-u21-l3', 'El técnico viene mañana.', ['Le explico el problema al técnico.', 'Ik leg de monteur het probleem uit.', 'I explain the problem to the technician.'], (HERHALING, PRON)),
    ('a2-u21-l3', 'Tengo que arreglar la bicicleta.', ['La bicicleta está rota; tengo que arreglarla.', 'De fiets is kapot; ik moet hem repareren.', 'The bike is broken; I have to fix it.', ['La bicicleta está rota; la tengo que arreglar.']], (HERHALING, PRON)),
    ('a2-u22-l2', 'Mi vecino es muy amable.', ['Mi vecino es muy amable; le doy una llave de casa.', 'Mijn buurman is heel aardig; ik geef hem een huissleutel.', "My neighbour is very kind; I give him a key to the house."], (HERHALING, PRON)),
    ('a2-u22-l3', 'La calefacción no funciona.', ['La calefacción no funciona; hay que repararla.', 'De verwarming doet het niet; die moet gerepareerd worden.', "The heating doesn't work; it needs fixing."], (HERHALING, PRON)),
    ('a2-u23-l1', 'Mi abuela lee en la mecedora.', ['Mi abuela lee en la mecedora; le traigo un cojín.', 'Mijn oma leest in de schommelstoel; ik breng haar een kussen.', 'My grandmother reads in the rocking chair; I bring her a cushion.'], (HERHALING, PRON)),
    ('a2-u23-l4', 'Cuelgo las fotos en la pared.', ['Tengo fotos nuevas; voy a colgarlas en la pared.', "Ik heb nieuwe foto's; ik ga ze aan de muur hangen.", "I have new photos; I'm going to hang them on the wall.", ['Tengo fotos nuevas; las voy a colgar en la pared.']], (HERHALING, PRON)),
    ('a2-u24-l3', 'Mi hijo saca la basura.', ['Mi hijo saca la basura y le doy las gracias.', 'Mijn zoon brengt het afval weg en ik bedank hem.', 'My son takes out the rubbish and I thank him.'], (HERHALING, PRON)),
    ('a2-u24-l3', '¿Dónde está la escoba?', ['¿Dónde está la escoba? ¿Me la pasas?', 'Waar is de bezem? Geef je hem even aan?', "Where's the broom? Can you pass it to me?"], (HERHALING, PRON)),
    ('a2-u25-l1', 'Tengo el hombro muy tenso.', ['Tengo el hombro muy tenso; lo muevo despacio.', 'Mijn schouder zit heel vast; ik beweeg hem langzaam.', 'My shoulder is very tense; I move it slowly.'], (HERHALING, PRON)),
    ('a2-u25-l2', 'Me duele el cuello de mirar el ordenador.', ['Me duele el cuello de mirar el ordenador; voy a apagarlo.', 'Mijn nek doet pijn van het kijken naar de computer; ik ga hem uitzetten.', "My neck hurts from looking at the computer; I'm going to switch it off.", ['Me duele el cuello de mirar el ordenador; lo voy a apagar.']], (HERHALING, PRON)),
    ('a2-u26-l3', 'El jarabe ayuda con la tos.', ['El jarabe ayuda con la tos; lo tomo cada noche.', 'De siroop helpt tegen het hoesten; ik neem hem elke avond.', 'The syrup helps with the cough; I take it every night.'], (HERHALING, PRON)),
    ('a2-u26-l2', '¿Tienes un pañuelo?', ['Mi hermano estornuda; le doy un pañuelo.', 'Mijn broer niest; ik geef hem een zakdoekje.', 'My brother sneezes; I give him a tissue.'], (HERHALING, PRON)),
    ('a2-u26-l3', 'Esta crema es para las quemaduras.', ['Esta crema es para las quemaduras; tienes que ponértela dos veces al día.', 'Deze crème is voor brandwonden; je moet hem twee keer per dag opdoen.', 'This cream is for burns; you have to put it on twice a day.', ['Esta crema es para las quemaduras; te la tienes que poner dos veces al día.']], (HERHALING, PRON)),
    ('a2-u27-l3', 'Necesito un análisis de sangre.', ['El médico me pide un análisis de sangre y lo hago mañana.', 'De dokter vraagt om een bloedonderzoek en ik laat het morgen doen.', "The doctor asks for a blood test and I'm doing it tomorrow."], (HERHALING, PRON)),
    ('a2-u28-l4', '¿Habéis visto a Pedro?', ['¿Habéis visto a Pedro? No, no lo hemos visto.', 'Hebben jullie Pedro gezien? Nee, we hebben hem niet gezien.', "Have you seen Pedro? No, we haven't seen him.", ['¿Habéis visto a Pedro? No, no le hemos visto.']], (HERHALING, PRON)),
    ('a2-u28-l1', '¿Has oído la noticia?', ['¿Le has contado la noticia a tu madre?', 'Heb je je moeder het nieuws verteld?', 'Have you told your mother the news?'], (HERHALING, PRON)),
    ('a2-u28-l3', 'Acabo de terminar el informe.', ['Acabo de terminar el informe y te lo he mandado.', 'Ik heb net het rapport afgemaakt en ik heb het je gestuurd.', "I've just finished the report and I've sent it to you."], (HERHALING, PRON)),
    ('a2-u29-l1', '¿Has impreso los billetes?', ['¿Has impreso los billetes? Sí, los he impreso.', 'Heb je de kaartjes geprint? Ja, ik heb ze geprint.', "Have you printed the tickets? Yes, I've printed them."], (HERHALING, PRON)),
    ('a2-u29-l4', '¿Qué han dicho los médicos?', ['¿Qué le han dicho los médicos a tu padre?', 'Wat hebben de artsen tegen je vader gezegd?', 'What have the doctors told your father?'], (HERHALING, PRON)),
    ('a2-u29-l1', 'He hecho la tarea.', ['He hecho la tarea; ¿quieres verla?', 'Ik heb het huiswerk gemaakt; wil je het zien?', "I've done the homework; do you want to see it?", ['He hecho la tarea; ¿la quieres ver?']], (HERHALING, PRON)),
    ('a2-u30-l4', 'He terminado el informe esta mañana.', ['He terminado el informe y lo he enviado esta mañana.', 'Ik heb het rapport afgemaakt en het vanochtend verstuurd.', "I've finished the report and sent it this morning."], (HERHALING, PRON)),
    ('a2-u30-l1', 'A la hora de comer he llamado a mi madre.', ['A la hora de comer le he mandado un mensaje a mi madre.', 'Rond etenstijd heb ik mijn moeder een bericht gestuurd.', 'At lunchtime I sent my mother a message.'], (HERHALING, PRON)),
    ('a2-u30-l3', 'He leído el mensaje de nuevo.', ['No entiendo el mensaje; voy a leerlo de nuevo.', 'Ik begrijp het bericht niet; ik ga het opnieuw lezen.', "I don't understand the message; I'm going to read it again.", ['No entiendo el mensaje; lo voy a leer de nuevo.']], (HERHALING, PRON)),
    ('a2-u31-l2', 'Brindamos por su éxito.', ['Le damos un regalo y brindamos por su éxito.', 'We geven hem een cadeau en proosten op zijn succes.', 'We give him a present and toast to his success.'], (HERHALING, PRON)),
    ('a2-u32-l3', 'Mi madre guarda un álbum de fotos.', ['Mi madre tiene un álbum de fotos y lo guarda en el salón.', 'Mijn moeder heeft een fotoalbum en ze bewaart het in de woonkamer.', 'My mother has a photo album and keeps it in the living room.'], (HERHALING, PRON)),
    ('a2-u32-l3', 'Mi abuelo nos contaba historias.', ['Mi abuelo les contaba historias a mis primos.', 'Mijn opa vertelde mijn neven verhalen.', 'My grandfather used to tell my cousins stories.'], (HERHALING, PRON)),
    ('a2-u32-l4', 'Teníamos una cometa roja.', ['Teníamos una cometa roja; nos la regaló mi tío.', 'We hadden een rode vlieger; die hadden we van mijn oom gekregen.', 'We had a red kite; my uncle gave it to us.'], (HERHALING, PRON)),
    ('a2-u33-l1', 'Mis abuelos escuchaban música en un tocadiscos.', ['Mis abuelos tenían un tocadiscos y lo usaban cada día.', 'Mijn grootouders hadden een platenspeler en gebruikten hem elke dag.', 'My grandparents had a record player and used it every day.'], (HERHALING, PRON)),
    ('a2-u33-l4', 'Mi abuela sabía cocinar muy bien.', ['Mi abuela sabía cocinar muy bien y le enseñaba recetas a mi madre.', 'Mijn oma kon heel goed koken en leerde mijn moeder recepten.', 'My grandmother could cook very well and taught my mother recipes.'], (HERHALING, PRON)),
    ('a2-u33-l3', 'He empezado a hacer yoga.', ['He empezado a hacer yoga; intento practicarlo cada día.', 'Ik ben begonnen met yoga; ik probeer het elke dag te doen.', "I've started doing yoga; I try to practise it every day."], (HERHALING, PRON)),
    ('a2-u34-l3', 'Su obra más famosa es una novela.', ['Su obra más famosa es una novela; la escribió en 1990.', 'Zijn beroemdste werk is een roman; hij schreef hem in 1990.', 'His most famous work is a novel; he wrote it in 1990.'], (HERHALING, PRON)),
    ('a2-u34-l3', 'Recibió un galardón muy importante.', ['Le dieron un galardón muy importante.', 'Ze kreeg een heel belangrijke onderscheiding.', 'She was given a very important award.'], (HERHALING, PRON)),
    ('a2-u34-l3', 'Su biografía es muy interesante.', ['Su biografía es muy interesante; te la presto.', 'Zijn biografie is heel interessant; ik leen hem je.', "His biography is very interesting; I'll lend it to you."], (HERHALING, PRON)),
    ('a2-u35-l1', 'Me organizaron una fiesta sorpresa.', ['Le organizamos una fiesta sorpresa a mi madre.', 'We organiseerden een verrassingsfeest voor mijn moeder.', 'We organised a surprise party for my mother.'], (HERHALING, PRON)),
    ('a2-u35-l2', 'Recuerdo mi primer día de trabajo.', ['Recuerdo mi primer día de trabajo; nunca voy a olvidarlo.', 'Ik herinner me mijn eerste werkdag; ik ga hem nooit vergeten.', "I remember my first day at work; I'm never going to forget it.", ['Recuerdo mi primer día de trabajo; nunca lo voy a olvidar.']], (HERHALING, PRON)),
    ('a2-u36-l1', 'Anteayer vi a una amiga en el centro.', ['Anteayer vi a una amiga en el centro y la invité a un café.', 'Eergisteren zag ik een vriendin in het centrum en ik trakteerde haar op een koffie.', 'The day before yesterday I saw a friend in the centre and bought her a coffee.'], (HERHALING, PRON)),
    ('a2-u36-l2', 'Con frecuencia visitábamos a mis tíos.', ['Con frecuencia les escribíamos cartas a mis tíos.', 'We schreven mijn oom en tante vaak brieven.', 'We often wrote letters to my aunt and uncle.'], (HERHALING, PRON)),
    ('a2-u36-l1', 'Hace dos días compré un coche.', ['Hace dos días compré un coche; me lo vendió mi vecino.', 'Twee dagen geleden kocht ik een auto; mijn buurman verkocht hem aan mij.', 'Two days ago I bought a car; my neighbour sold it to me.'], (HERHALING, PRON)),
]

# Onregelmatige indefinido: uitleg kwam pas aan het eind van unit 35, terwijl unit 34 er al vol mee staat.
U34_OLD = 'Jaartallen lees je als gewoon getal: <i>mil novecientos noventa</i>.</p>`'
U34_NEW = ('Jaartallen lees je als gewoon getal: <i>mil novecientos noventa</i>.</p>'
           '<p class="muted">Een paar veelgebruikte werkwoorden zijn <b>onregelmatig</b> (en hebben géén accent):</p>'
           '<p class="muted"><i>ser / ir → <b>fue</b></i> — was / ging<br><i>tener → <b>tuvo</b></i><br><i>hacer → <b>hizo</b></i><br><i>dar → <b>dio</b></i></p>`')
U35_OLD = ('<h2 class="section-title" style="margin-top:0;">Onregelmatige verleden tijd</h2><p class="muted">Veel gebruikte werkwoorden zijn onregelmatig in de indefinido (en hebben géén accent):</p>'
           '<p class="muted"><i>ser / ir → <b>fue</b></i> — was / ging<br><i>tener → <b>tuvo</b></i><br><i>estar → <b>estuvo</b></i><br><i>hacer → <b>hizo</b></i><br><i>poder → <b>pudo</b></i><br><i>decir → <b>dijo</b></i></p><p class="muted"><i>Tuvo lugar</i> = vond plaats.</p>')
U35_NEW = ('<h2 class="section-title" style="margin-top:0;">Onregelmatig: ik en hij/zij</h2><p class="muted">Bij de onregelmatige werkwoorden eindigt de ik-vorm op <b>-e</b> en de hij/zij-vorm op <b>-o</b>, zonder accent:</p>'
           '<p class="muted"><i>tener → <b>tuve</b>, tuvo</i><br><i>estar → <b>estuve</b>, estuvo</i><br><i>hacer → <b>hice</b>, hizo</i><br><i>poder → <b>pude</b>, pudo</i><br><i>decir → <b>dije</b>, dijo</i></p>'
           '<p class="muted">Ser en ir zijn gelijk: <i><b>fui</b>, fue</i>. <i>Tuvo lugar</i> = vond plaats.</p>')

if __name__ == '__main__':
    replace_sentences(CHANGES)
    replace_sentences(REUSE)
    replace_sentences(PRON_REUSE)
    move_intro('a2-u7-l2', 'a2-u7-l1')   # unit 7 les 1 gebruikt de gebiedende wijs al
    replace_text(U34_OLD, U34_NEW)
    replace_text(U35_OLD, U35_NEW)
