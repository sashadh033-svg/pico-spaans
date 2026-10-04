# Voornaamwoorden (lo, la, le, se...) duidelijker en vaker:
#  - spiekbriefje GUIDES['__pron__'] (te openen vanuit de Kluis en vanuit de gids van a2-u16, b1-u39, b2-u41)
#  - Kluis-knop "Voornaamwoorden oefenen": onbeperkt, met de oefenzinnen van alle niveaus tot waar je bent
#  - meer oefenzinnen in PRONOUN_POOL
#  - aanvullingen in de uitleg van a2-u16
# Gebruik: python3 dev/pronouns.py   (idempotent)
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sentence_tools import PATH, replace_text

def card(title, *paras):
    return ('<div class="card"><h2 class="section-title" style="margin-top:0;">' + title + '</h2>'
            + ''.join('<p class="muted">' + p + '</p>' for p in paras) + '</div>')

def ex(*lines):
    return '<br>'.join(lines)

TABLE_NL = ('<table style="width:100%; border-collapse:collapse; font-size:15px; margin:6px 0;">'
    '<tr><th></th><th style="text-align:left; padding:4px;">wat / wie? (lijdend)</th><th style="text-align:left; padding:4px;">aan wie? (meewerkend)</th></tr>'
    '<tr><td style="padding:4px;">hem / het (m)</td><td style="padding:4px;"><b>lo</b></td><td rowspan="2" style="padding:4px;"><b>le</b></td></tr>'
    '<tr><td style="padding:4px;">haar / het (v)</td><td style="padding:4px;"><b>la</b></td></tr>'
    '<tr><td style="padding:4px;">ze (m)</td><td style="padding:4px;"><b>los</b></td><td rowspan="2" style="padding:4px;"><b>les</b></td></tr>'
    '<tr><td style="padding:4px;">ze (v)</td><td style="padding:4px;"><b>las</b></td></tr>'
    '</table>')

GUIDE_NL = (
    '<h2 class="section-title">Voornaamwoorden: alles op een rij</h2>'
    '<p class="muted" style="margin-bottom:12px;">lo, la, le, se... Hier staat alles bij elkaar. Lees het stap voor stap; elke stap bouwt op de vorige.</p>'
    + card('1. Wat of aan wie?',
        '<b>lo, la, los, las</b> vervangen het ding of de persoon zelf (wat? wie?). <b>le, les</b> vervangen <b>aan wie</b> iets gegeven, gezegd of gevraagd wordt.',
        TABLE_NL,
        ex('<i>Compro <u>el pan</u>.</i> → <i><b>Lo</b> compro.</i> — ik koop het', '<i>Veo <u>a Ana</u>.</i> → <i><b>La</b> veo.</i> — ik zie haar',
           '<i>Escribo <u>a Ana</u>.</i> → <i><b>Le</b> escribo.</i> — ik schrijf (aan) haar', '<i>Doy un regalo <u>a mis padres</u>.</i> → <i><b>Les</b> doy un regalo.</i>'),
        '<b>Truc:</b> kun je er in het Nederlands "aan" voor zetten (ik geef het <i>aan</i> hem)? Dan is het <b>le/les</b>.',
        '<b>Let op, anders dan in het Nederlands:</b><br>met <b>lo/la</b>: <i>llamar, ayudar, esperar, invitar, ver, conocer</i> → <i>La llamo. Lo ayudo.</i><br>'
        'met <b>le</b>: <i>preguntar, pedir, decir, escribir, gustar, doler</i> → <i>Le pregunto. Le gusta.</i>',
        '<i>me, te, nos, os</i> doen allebei: <i>Me ve</i> (hij ziet mij) en <i>Me da el libro</i> (hij geeft het boek aan mij).')
    + card('2. Twee tegelijk: eerst aan wie, dan wat',
        'Staan er twee woordjes, dan komt <b>aan wie</b> altijd eerst:',
        ex('<i><b>Me lo</b> das.</i> — je geeft het (aan) mij', '<i><b>Te la</b> presto.</i> — ik leen hem je', '<i><b>Nos los</b> traen.</i> — ze brengen ze ons'))
    + card('3. Le + lo wordt <b>se lo</b>',
        'Je zegt <b>nooit</b> <i>le lo</i> of <i>les la</i>. Komen ze samen, dan wordt <b>le/les → se</b>:',
        ex('❌ <i>Le lo doy.</i> → ✅ <i><b>Se lo</b> doy.</i> — ik geef het aan hem/haar/u',
           '<i>Le doy <u>el libro</u> a María.</i> → <i><b>Se lo</b> doy.</i>',
           '<i>Les compro <u>las flores</u> a mis padres.</i> → <i><b>Se las</b> compro.</i>'),
        'Het tweede woordje past zich aan het <b>ding</b> aan: <i>el libro → lo</i>, <i>las flores → las</i>.',
        'Is niet duidelijk aan wie? Zet het er gewoon bij: <i>Se lo doy <b>a ella</b>.</i> · <i>Se lo explico <b>a usted</b>.</i>')
    + card('4. Waar staat het? Vóór of achteraan',
        '<b>Vervoegd werkwoord</b> (<i>doy, compré, he dicho</i>): <b>ervóór</b>, los geschreven.<br><i>Lo compro. · Se lo he dicho.</i>',
        '<b>Heel werkwoord</b> (<i>-ar, -er, -ir</i>): ervóór <b>óf</b> er achteraan vast. Allebei goed:<br><i>Lo voy a comprar = Voy a comprar<b>lo</b>.</i><br><i>Te lo quiero decir = Quiero decír<b>telo</b>.</i>',
        '<b>-ndo-vorm</b> (<i>-ando, -iendo</i>): ervóór <b>óf</b> achteraan:<br><i>Lo estoy haciendo = Estoy haciéndo<b>lo</b>.</i>',
        '<b>Bevel</b> (doe het!): <b>altijd achteraan</b> vast:<br><i>¡Cómpra<b>lo</b>! · ¡Dá<b>melo</b>! · ¡Dí<b>selo</b>! · ¡Siénta<b>te</b>!</i>',
        '<b>Bevel met no</b> (doe het niet!): <b>altijd ervóór</b>:<br><i>¡No <b>lo</b> compres! · ¡No <b>me lo</b> des! · ¡No <b>se lo</b> digas!</i>',
        '<b>Nooit twee keer:</b> ❌ <i>Lo voy a comprarlo.</i>',
        '<b>Accent:</b> plak je er iets achter, dan blijft de klemtoon op dezelfde plek. Daarom komt er vaak een accent bij: '
        '<i>compra → cómpralo</i>, <i>haciendo → haciéndolo</i>, <i>da → dámelo</i>, <i>decir → decírselo</i>. Met één woordje achter een heel werkwoord hoeft het niet: <i>comprarlo, decirte</i>.')
    + card('5. Alle betekenissen van se',
        '<b>a) Zichzelf</b> (A1): <i><b>Se</b> ducha. <b>Se</b> llama Ana.</i> — net als <i>me lavo, te lavas</i>.',
        '<b>b) In plaats van le/les</b> (A2): <i><b>Se</b> lo doy.</i> — zie stap 3.',
        '<b>c) Elkaar</b>: <i><b>Se</b> quieren mucho. <b>Se</b> escriben cada semana.</i>',
        '<b>d) Andere betekenis van het werkwoord</b>: <i>ir → ir<b>se</b></i> (weggaan), <i>dormir → dormir<b>se</b></i> (in slaap vallen), <i>quedar → quedar<b>se</b></i> (blijven): <i>Me voy. <b>Se</b> durmió.</i>',
        '<b>e) "Men"</b> (B1): <i>Aquí <b>se</b> habla español. ¿Cómo <b>se</b> dice...? <b>Se</b> venden pisos.</i>',
        '<b>f) Per ongeluk</b> (B2): <i><b>Se me</b> olvidó la llave. <b>Se le</b> cayó el móvil.</i> — het ding is het onderwerp.',
        '<b>Welke is het?</b> Kijk wat erna komt:<br>se + <i>lo/la/los/las</i> → b (aan hem/haar/u/hen)<br>se + <i>me/te/le/nos/les</i> + werkwoord → f (per ongeluk)<br>'
        'se + werkwoord over de persoon zelf → a, c of d<br>se + werkwoord zonder iemand die het doet → e')
    + card('6. Veelgemaakte fouten',
        ex('❌ <i>Le lo doy</i> → ✅ <i>Se lo doy</i>', '❌ <i>Doy lo</i> → ✅ <i>Lo doy</i>', '❌ <i>Dame lo</i> → ✅ <i>Dámelo</i>',
           '❌ <i>No dámelo</i> → ✅ <i>No me lo des</i>', '❌ <i>La gusta</i> → ✅ <i>Le gusta</i>', '❌ <i>Le llamo a Ana</i> → ✅ <i>La llamo</i>',
           '❌ <i>Lo voy a comprarlo</i> → ✅ <i>Voy a comprarlo</i> of <i>Lo voy a comprar</i>'))
)

TABLE_EN = TABLE_NL.replace('wat / wie? (lijdend)', 'what / who? (direct)').replace('aan wie? (meewerkend)', 'to whom? (indirect)') \
    .replace('hem / het (m)', 'him / it (m)').replace('haar / het (v)', 'her / it (f)').replace('ze (m)', 'them (m)').replace('ze (v)', 'them (f)')

GUIDE_EN = (
    '<h2 class="section-title">Pronouns: everything in one place</h2>'
    '<p class="muted" style="margin-bottom:12px;">lo, la, le, se... Read it step by step; each step builds on the one before.</p>'
    + card('1. What, or to whom?',
        '<b>lo, la, los, las</b> replace the thing or person itself (what? who?). <b>le, les</b> replace <b>to whom</b> something is given, said or asked.',
        TABLE_EN,
        ex('<i>Compro <u>el pan</u>.</i> → <i><b>Lo</b> compro.</i> — I buy it', '<i>Veo <u>a Ana</u>.</i> → <i><b>La</b> veo.</i> — I see her',
           '<i>Escribo <u>a Ana</u>.</i> → <i><b>Le</b> escribo.</i> — I write to her', '<i>Doy un regalo <u>a mis padres</u>.</i> → <i><b>Les</b> doy un regalo.</i>'),
        '<b>Tip:</b> can you put "to" in front (I give it <i>to</i> him)? Then it is <b>le/les</b>.',
        '<b>Different from English:</b> <i>llamar, ayudar, esperar, invitar</i> take <b>lo/la</b>; <i>preguntar, pedir, gustar, doler</i> take <b>le</b>.')
    + card('2. Two at once: to whom first, then what',
        ex('<i><b>Me lo</b> das.</i> — you give it to me', '<i><b>Te la</b> presto.</i>', '<i><b>Nos los</b> traen.</i>'))
    + card('3. Le + lo becomes <b>se lo</b>',
        'You <b>never</b> say <i>le lo</i>. When they meet, <b>le/les → se</b>:',
        ex('❌ <i>Le lo doy.</i> → ✅ <i><b>Se lo</b> doy.</i>', '<i>Les compro <u>las flores</u> a mis padres.</i> → <i><b>Se las</b> compro.</i>'),
        'Unclear who? Add it: <i>Se lo doy <b>a ella</b>.</i>')
    + card('4. Where does it go? Before or attached',
        '<b>Conjugated verb</b>: <b>before</b>, separate. <i>Lo compro. Se lo he dicho.</i>',
        '<b>Infinitive</b> and <b>-ndo form</b>: before <b>or</b> attached. <i>Lo voy a comprar = Voy a comprarlo. Lo estoy haciendo = Estoy haciéndolo.</i>',
        '<b>Command</b>: <b>always attached</b>. <i>¡Cómpralo! ¡Dámelo! ¡Díselo!</i>',
        '<b>Negative command</b>: <b>always before</b>. <i>¡No lo compres! ¡No se lo digas!</i>',
        '<b>Accent</b>: attaching keeps the stress in place, so an accent is often added: <i>compra → cómpralo, haciendo → haciéndolo</i>.')
    + card('5. All the meanings of se',
        '<b>a) oneself</b> (A1): <i>Se ducha.</i> · <b>b) instead of le/les</b> (A2): <i>Se lo doy.</i> · <b>c) each other</b>: <i>Se quieren.</i>',
        '<b>d) different meaning</b>: <i>irse</i> (to leave), <i>dormirse</i> (to fall asleep) · <b>e) "one / people"</b> (B1): <i>Aquí se habla español.</i> · <b>f) by accident</b> (B2): <i>Se me olvidó la llave.</i>')
    + card('6. Common mistakes',
        ex('❌ <i>Le lo doy</i> → ✅ <i>Se lo doy</i>', '❌ <i>Dame lo</i> → ✅ <i>Dámelo</i>', '❌ <i>No dámelo</i> → ✅ <i>No me lo des</i>', '❌ <i>La gusta</i> → ✅ <i>Le gusta</i>'))
)

GUIDE_JS = "GUIDES['__pron__'] = { nl:`" + GUIDE_NL + "`, en:`" + GUIDE_EN + "` };\n"

# ---------- extra oefenzinnen ----------
def P(q, a, nl, en, alts=None):
    d = {'q': q, 'a': a, 'nl': nl, 'en': en}
    if alts: d['alts'] = alts
    return d

EXTRA_POOL = {
 'A2': [
  P('Visito <b>a mis abuelos</b> los domingos.', 'Los visito los domingos.', 'Ik bezoek ze op zondag.', 'I visit them on Sundays.'),
  P('Ayudo <b>a mi hermana</b> con los deberes.', 'La ayudo con los deberes.', 'Ik help haar met het huiswerk.', 'I help her with her homework.'),
  P('Espero <b>a Pedro</b> en la parada.', 'Lo espero en la parada.', 'Ik wacht op hem bij de halte.', 'I wait for him at the stop.', ['Le espero en la parada.']),
  P('Invito <b>a mis amigas</b> a cenar.', 'Las invito a cenar.', 'Ik nodig ze uit voor het eten.', 'I invite them to dinner.'),
  P('Conozco <b>a Marta</b> muy bien.', 'La conozco muy bien.', 'Ik ken haar heel goed.', 'I know her very well.'),
  P('Pregunto la hora <b>a la profesora</b>.', 'Le pregunto la hora.', 'Ik vraag haar hoe laat het is.', 'I ask her the time.'),
  P('Digo la verdad <b>a mis padres</b>.', 'Les digo la verdad.', 'Ik vertel hun de waarheid.', 'I tell them the truth.'),
  P('Explico el ejercicio <b>a Juan</b>.', 'Le explico el ejercicio.', 'Ik leg hem de oefening uit.', 'I explain the exercise to him.'),
  P('Pido la cuenta <b>al camarero</b>.', 'Le pido la cuenta.', 'Ik vraag hem om de rekening.', 'I ask him for the bill.'),
  P('Escribo una postal <b>a mis abuelos</b>.', 'Les escribo una postal.', 'Ik schrijf hun een ansichtkaart.', 'I write them a postcard.'),
  P('Voy a comprar <b>la fruta</b>.', 'Voy a comprarla.', 'Ik ga het kopen.', "I'm going to buy it.", ['La voy a comprar.']),
  P('Vamos a ver <b>la película</b> esta noche.', 'Vamos a verla esta noche.', 'We gaan hem vanavond kijken.', "We're going to watch it tonight.", ['La vamos a ver esta noche.']),
  P('Quiero ver <b>las fotos</b>.', 'Quiero verlas.', 'Ik wil ze zien.', 'I want to see them.', ['Las quiero ver.']),
  P('Tengo que llamar <b>a Laura</b>.', 'Tengo que llamarla.', 'Ik moet haar bellen.', 'I have to call her.', ['La tengo que llamar.']),
  P('Estoy leyendo <b>el libro</b>.', 'Estoy leyéndolo.', 'Ik ben het aan het lezen.', "I'm reading it.", ['Lo estoy leyendo.']),
  P('Estamos preparando <b>la cena</b>.', 'Estamos preparándola.', 'We zijn het aan het klaarmaken.', "We're making it.", ['La estamos preparando.']),
  P('Compra <b>el pan</b>, por favor.', 'Cómpralo, por favor.', 'Koop het, alsjeblieft.', 'Buy it, please.'),
  P('Cierra <b>la puerta</b>.', 'Ciérrala.', 'Doe hem dicht.', 'Close it.'),
  P('Llama <b>a tu madre</b>.', 'Llámala.', 'Bel haar.', 'Call her.'),
  P('He visto <b>a tus primos</b>.', 'Los he visto.', 'Ik heb ze gezien.', "I've seen them."),
  P('He perdido <b>las llaves</b>.', 'Las he perdido.', 'Ik ben ze kwijt.', "I've lost them."),
  P('He escrito un correo <b>al jefe</b>.', 'Le he escrito un correo.', 'Ik heb hem een mail geschreven.', "I've written him an email."),
  P('Mi madre me da <b>el dinero</b>.', 'Mi madre me lo da.', 'Mijn moeder geeft het mij.', 'My mother gives it to me.'),
  P('Te presto <b>el coche</b>.', 'Te lo presto.', 'Ik leen hem je.', "I'll lend it to you."),
  P('Le doy <b>el regalo</b> <b>a Ana</b>.', 'Se lo doy.', 'Ik geef het haar.', 'I give it to her.', ['Se lo doy a Ana.']),
  P('Les mando <b>las fotos</b> <b>a mis amigos</b>.', 'Se las mando.', 'Ik stuur ze hun.', 'I send them to them.', ['Se las mando a mis amigos.']),
  P('Nos traen <b>los platos</b>.', 'Nos los traen.', 'Ze brengen ze ons.', 'They bring them to us.'),
  P('Me lavo <b>las manos</b>.', 'Me las lavo.', 'Ik was ze.', 'I wash them.'),
 ],
 'B1': [
  P('Me pongo <b>el abrigo</b>.', 'Me lo pongo.', 'Ik trek hem aan.', 'I put it on.'),
  P('Mi hermano se pone <b>las gafas</b>.', 'Mi hermano se las pone.', 'Mijn broer zet hem op.', 'My brother puts them on.'),
  P('Me lavo <b>el pelo</b> cada día.', 'Me lo lavo cada día.', 'Ik was het elke dag.', 'I wash it every day.'),
  P('Quiero contar <b>el secreto</b> <b>a Ana</b>.', 'Quiero contárselo.', 'Ik wil het haar vertellen.', 'I want to tell it to her.', ['Se lo quiero contar.', 'Quiero contárselo a Ana.']),
  P('Estoy explicando <b>la regla</b> <b>a los alumnos</b>.', 'Estoy explicándosela.', 'Ik ben het hun aan het uitleggen.', "I'm explaining it to them.", ['Se la estoy explicando.']),
  P('Voy a devolver <b>el dinero</b> <b>a mi hermano</b>.', 'Voy a devolvérselo.', 'Ik ga het hem teruggeven.', "I'm going to give it back to him.", ['Se lo voy a devolver.']),
  P('Está escribiendo <b>la carta</b> <b>a su novia</b>.', 'Está escribiéndosela.', 'Hij is hem haar aan het schrijven.', "He's writing it to her.", ['Se la está escribiendo.']),
  P('Te voy a enseñar <b>la casa</b>.', 'Te la voy a enseñar.', 'Ik ga het je laten zien.', "I'm going to show it to you.", ['Voy a enseñártela.']),
  P('¿Me puedes enviar <b>los documentos</b>?', '¿Me los puedes enviar?', 'Kun je ze me sturen?', 'Can you send them to me?', ['¿Puedes enviármelos?']),
  P('Da <b>las llaves</b> <b>a tu padre</b>.', 'Dáselas.', 'Geef ze aan hem.', 'Give them to him.'),
  P('No des <b>las llaves</b> <b>a tu padre</b>.', 'No se las des.', 'Geef ze hem niet.', "Don't give them to him."),
  P('Pásame <b>la sal</b>.', 'Pásamela.', 'Geef hem eens door.', 'Pass it to me.'),
  P('No me pases <b>la sal</b> todavía.', 'No me la pases todavía.', 'Geef hem nog niet door.', "Don't pass it to me yet."),
  P('Explícanos <b>el problema</b>.', 'Explícanoslo.', 'Leg het ons uit.', 'Explain it to us.'),
  P('Pide perdón <b>a tu hermana</b>.', 'Pídele perdón.', 'Bied haar je excuses aan.', 'Apologise to her.'),
  P('Le he regalado <b>una bufanda</b> <b>a mi abuela</b>.', 'Se la he regalado.', 'Ik heb hem haar cadeau gegeven.', "I've given it to her as a present."),
  P('Les vendimos <b>el coche</b> <b>a los vecinos</b>.', 'Se lo vendimos.', 'We verkochten hem aan hen.', 'We sold it to them.'),
  P('Mi madre nos prepara <b>la comida</b>.', 'Mi madre nos la prepara.', 'Mijn moeder maakt het voor ons klaar.', 'My mother makes it for us.'),
  P('Pregunté la dirección <b>a Luis</b>.', 'Le pregunté la dirección.', 'Ik vroeg hem het adres.', 'I asked him the address.'),
  P('Os enviamos <b>la invitación</b> ayer.', 'Os la enviamos ayer.', 'We stuurden hem jullie gisteren.', 'We sent it to you yesterday.'),
 ],
 'B2': [
  P('Le comuniqué <b>la decisión</b> <b>al director</b>.', 'Se la comuniqué.', 'Ik deelde het hem mee.', 'I told him about it.'),
  P('Dígale <b>la verdad</b> <b>al cliente</b>.', 'Dígasela.', 'Zegt u het hem.', 'Tell it to him.'),
  P('No le diga <b>la verdad</b> <b>al cliente</b>.', 'No se la diga.', 'Zegt u het hem niet.', "Don't tell it to him."),
  P('Tráiganos <b>la cuenta</b>, por favor.', 'Tráiganosla, por favor.', 'Brengt u hem ons, alstublieft.', 'Bring it to us, please.'),
  P('Habría que explicar <b>las normas</b> <b>a los nuevos</b>.', 'Habría que explicárselas.', 'We zouden ze hun moeten uitleggen.', 'We should explain them to them.'),
  P('Quisiera pedir <b>un favor</b> <b>a usted</b>.', 'Quisiera pedírselo.', 'Ik zou het u willen vragen.', "I'd like to ask you for it.", ['Se lo quisiera pedir.']),
  P('Ya había contado <b>la noticia</b> <b>a sus padres</b>.', 'Ya se la había contado.', 'Hij had het hun al verteld.', 'He had already told them.'),
  P('Te devolveré <b>los apuntes</b> mañana.', 'Te los devolveré mañana.', 'Ik geef ze je morgen terug.', "I'll give them back to you tomorrow."),
  P('Están arreglando <b>la calefacción</b> <b>a los vecinos</b>.', 'Se la están arreglando.', 'Ze zijn hem voor hen aan het repareren.', "They're fixing it for them.", ['Están arreglándosela.']),
  P('<b>Olvidaste</b> el móvil. <i>(per ongeluk: se te...)</i>', 'Se te olvidó el móvil.', 'Je bent je telefoon vergeten.', 'You forgot your phone.'),
  P('Nosotros <b>rompimos</b> la ventana. <i>(per ongeluk)</i>', 'Se nos rompió la ventana.', 'Het raam ging per ongeluk kapot.', 'The window broke on us.'),
  P('Mis hijos <b>perdieron</b> el balón. <i>(per ongeluk)</i>', 'A mis hijos se les perdió el balón.', 'Mijn kinderen zijn de bal kwijtgeraakt.', 'My children lost the ball.', ['Se les perdió el balón.']),
  P('Escribí <b>la carta</b> yo. <i>(begin met \'La carta\')</i>', 'La carta la escribí yo.', 'De brief heb ík geschreven.', 'I was the one who wrote the letter.'),
  P('Hemos visto <b>a tus padres</b> en el centro.', 'Los hemos visto en el centro.', 'We hebben ze in het centrum gezien.', "We've seen them in the centre."),
  P('Sé <b>que tienes razón</b>.', 'Lo sé.', 'Ik weet het.', 'I know.'),
 ],
}

KLUIS_OLD = '<div class="muted" id="vault-verb-info" style="font-size:13px; margin:0 0 14px; text-align:center;"></div>'
KLUIS_NEW = (KLUIS_OLD +
    '\n      <button class="btn" id="vault-pron-btn" onclick="startPronMix()" style="margin-bottom:6px; background:#1cb0f6; border-color:#1899d6; box-shadow:0 4px 0 #1899d6;">🔄 Voornaamwoorden oefenen</button>'
    '\n      <div class="muted" id="vault-pron-info" style="font-size:13px; margin:0 0 8px; text-align:center;"></div>'
    '\n      <button class="btn secondary" onclick="showGuide(\'__pron__\',\'vault\')" style="margin-bottom:14px;">📖 Spiekbriefje: lo, la, le, se</button>')

GUIDE_BACK_OLD = '''      <button class="icon-btn" onclick="go('lessons')">←</button>
      <h1>Gids</h1>'''
GUIDE_BACK_NEW = '''      <button class="icon-btn" onclick="go(guideBack||'lessons')">←</button>
      <h1>Gids</h1>'''

SHOWGUIDE_OLD = '''function showGuide(unitId){
  currentGuideUnitId = unitId;'''
SHOWGUIDE_NEW = '''let guideBack = 'lessons';
// Units waar voornaamwoorden behandeld worden: hun gids linkt naar het spiekbriefje GUIDES['__pron__']
const PRON_GUIDE_UNITS = ['a2-u16','b1-u39','b2-u41'];
function showGuide(unitId, back){
  guideBack = back || 'lessons';
  currentGuideUnitId = unitId;'''

GUIDE_LINK_OLD = '''  document.getElementById('guide-chat-log').innerHTML = '';
  go('guide');'''
GUIDE_LINK_NEW = '''  if(PRON_GUIDE_UNITS.includes(unitId)){
    content.innerHTML += `<button class="btn secondary" style="margin:6px 0 14px;" onclick="showGuide('__pron__')">${appState.profile.baseLang==='en' ? '📖 Everything about lo, la, le and se' : '📖 Alles over lo, la, le en se'}</button>`;
  }
  document.getElementById('guide-chat-log').innerHTML = '';
  go('guide');'''

TITLE_OLD = '''function findUnitTitleById(unitId){
  for(const lvl of LEVELS){'''
TITLE_NEW = '''function findUnitTitleById(unitId){
  if(unitId==='__pron__') return appState.profile.baseLang==='en' ? 'Pronouns (lo, la, le, se)' : 'Voornaamwoorden (lo, la, le, se)';
  for(const lvl of LEVELS){'''

MIX_OLD = '''function startVerbMix(){'''
MIX_NEW = '''// Alle units die je bereikt hebt (afgerond, of de unit waar je nu in bezig bent)
function reachedUnitIds(){
  const cur = appState.profile.level, ci = LEVELS.indexOf(cur), out = [];
  LEVELS.forEach((L,li)=>{
    if(li > ci) return;
    const units = unitsForLevel(L);
    if(li < ci){ units.forEach(u=> out.push(u.id)); return; }
    const ns = flattenPath(L);
    const fi = ns.findIndex((n,i)=> !progressKeyDone(L, n.lesson.id) && !skippableLater(L, ns, i));
    const lastIdx = fi === -1 ? units.length-1 : units.indexOf(ns[fi].unit);
    const started = fi !== -1 && ns.some(n=> n.unit === ns[fi].unit && progressKeyDone(L, n.lesson.id));
    units.forEach((u,i)=>{ if(i < lastIdx || (i === lastIdx && (fi === -1 || started))) out.push(u.id); });
  });
  return out;
}
// Voornaamwoorden oefenen (Kluis): elk niveau komt vrij zodra je bij de unit bent waar het behandeld wordt
const PRON_GATES = [['A2','a2-u16'],['B1','b1-u39'],['B2','b2-u41']];
function reachedPronPools(){
  const r = new Set(reachedUnitIds());
  return PRON_GATES.filter(g=> r.has(g[1]) && (PRONOUN_POOL[g[0]]||[]).length).map(g=>g[0]);
}
function startPronMix(){
  const pools = reachedPronPools();
  verbPracticeState = { unitId:'__pron__', pool:null, pronPools:pools, count:0, correct:0 };
  go('exercise');
  if(!pools.length){
    document.getElementById('exercise-body').innerHTML = `<div class="empty-state"><div class="e-icon">🔄</div>Voornaamwoorden (lo, la, le...) leer je in A2 unit 16. Daarna kun je hier onbeperkt oefenen.<br><br><button class="btn secondary" onclick="showGuide('__pron__','vault')">📖 Spiekbriefje bekijken</button><br><button class="btn secondary" onclick="go('vault')">Terug</button></div>`;
    return;
  }
  renderVerbPracticeItem();
}
function startVerbMix(){'''

RENDER_OLD = '''function renderVerbPracticeItem(){
  let item = null, uid = verbPracticeState.unitId;'''
RENDER_NEW = '''function renderVerbPracticeItem(){
  if(verbPracticeState.pronPools){
    // het nieuwste niveau vaker, de eerdere blijven terugkomen
    const ps = verbPracticeState.pronPools;
    const key = (ps.length===1 || Math.random()<0.5) ? ps[ps.length-1] : ps[Math.floor(Math.random()*(ps.length-1))];
    const pitem = buildPronounItem(key);
    exState = { items:[pitem], index:0, correct:0, level:appState.profile.level, lessonId:null, unitId:'__pron__', source:'verbPractice' };
    renderExercise();
    return;
  }
  let item = null, uid = verbPracticeState.unitId;'''

INFO_OLD = '''  document.getElementById('vault-verb-info').textContent = vu.length ? 'Mix uit ' + vu.length + ' units, tot waar je nu bent' : 'Komt vrij zodra je je eerste werkwoorden hebt geleerd';'''
INFO_NEW = INFO_OLD + '''
  const pp = reachedPronPools();
  const PRON_INFO = { A2:'lo, la, le, se lo', B1:'+ achteraan en ontkennend', B2:'+ se me olvidó en usted' };
  document.getElementById('vault-pron-info').textContent = pp.length ? 'Tot waar je nu bent: ' + pp.map(k=>PRON_INFO[k]).join(' ') : 'Komt vrij in A2 unit 16 (lo, la, le)';'''

# aanvullingen in de uitleg van a2-u16
U16L1_OLD = 'Bij een heel werkwoord mag het er ook achter vast: <i>Quiero comprar<b>lo</b>.</i></p>'
U16L1_NEW = ('Bij een heel werkwoord of een -ndo-vorm mag het er ook achter vast: <i>Quiero comprar<b>lo</b></i>, <i>Estoy leyéndo<b>lo</b></i>. '
             'Bij een bevel staat het er altijd achter: <i>¡Cómpra<b>lo</b>!</i></p>')
U16L4_OLD = '<i><s>le lo doy</s></i> → <i><b>se lo</b> doy</i> — ik geef het aan hem/haar</p>`'
U16L4_NEW = '<i><s>le lo doy</s></i> → <i><b>se lo</b> doy</i> — ik geef het aan hem/haar. Je zegt dus nooit <i>le lo</i>.</p>`'

def run():
    c = open(PATH, encoding='utf-8').read()
    if "GUIDES['__pron__']" not in c:
        anchor = c.index("GUIDES['a1-u17p'] = {")
        c = c[:anchor] + GUIDE_JS + c[anchor:]
    # oefenzinnen toevoegen (zonder dubbele)
    i = c.index('const PRONOUN_POOL = ') + len('const PRONOUN_POOL = ')
    j = c.index('\n', i)
    raw = c[i:j].rstrip()
    semi = raw.endswith(';')
    pool = json.loads(raw.rstrip(';'))
    added = 0
    for k, items in EXTRA_POOL.items():
        have = {x['q'] for x in pool[k]}
        for it in items:
            if it['q'] not in have:
                pool[k].append(it); added += 1
    c = c[:i] + json.dumps(pool, ensure_ascii=False) + (';' if semi else '') + c[j:]
    open(PATH, 'w', encoding='utf-8').write(c)
    for old, new in [(KLUIS_OLD, KLUIS_NEW), (GUIDE_BACK_OLD, GUIDE_BACK_NEW), (SHOWGUIDE_OLD, SHOWGUIDE_NEW), (GUIDE_LINK_OLD, GUIDE_LINK_NEW),
                     (TITLE_OLD, TITLE_NEW), (MIX_OLD, MIX_NEW), (RENDER_OLD, RENDER_NEW), (INFO_OLD, INFO_NEW),
                     (U16L1_OLD, U16L1_NEW), (U16L4_OLD, U16L4_NEW)]:
        replace_text(old, new)
    print('oefenzinnen toegevoegd:', added, '| pools:', {k: len(v) for k, v in pool.items()})

if __name__ == '__main__':
    run()
