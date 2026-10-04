# Extra's voor estar + gerundio: werkwoordoefening (🏋️), gids (📖), en herhaling in latere units.
# Gebruik: python3 dev/add_progresivo_extras.py   (idempotent)
import json, re, sys

J = lambda x: json.dumps(x, ensure_ascii=False)

GERUND_JS = r"""
// Gerundio (-ando/-iendo) met de onregelmatige vormen; gebruikt door de tijd 'progresivo' (estar + gerundio)
const GERUNDIO_IRREGULAR = { leer:'leyendo', traer:'trayendo', oír:'oyendo', ir:'yendo', caer:'cayendo', creer:'creyendo', construir:'construyendo', huir:'huyendo',
  dormir:'durmiendo', morir:'muriendo', poder:'pudiendo', decir:'diciendo', pedir:'pidiendo', venir:'viniendo', vestir:'vistiendo', sentir:'sintiendo',
  servir:'sirviendo', seguir:'siguiendo', repetir:'repitiendo', preferir:'prefiriendo', divertir:'divirtiendo', mentir:'mintiendo', reír:'riendo', freír:'friendo', elegir:'eligiendo', corregir:'corrigiendo' };
function gerundio(verb){
  const v = String(verb).replace(/se$/,'');
  if(GERUNDIO_IRREGULAR[v]) return GERUNDIO_IRREGULAR[v];
  if(/ar$/.test(v)) return v.slice(0,-2)+'ando';
  if(/(er|ir|ír)$/.test(v)) return v.slice(0,-2)+'iendo';
  return v;
}
"""

VERB_PRACTICE_ENTRY = """  'a1-u17p': { tense:'progresivo', verbs:[
    { verb:'hablar', reflexive:false, infNl:'hablar', trNl:'praten', trEn:'to talk', templates:[
      '{suj} ______ por teléfono.', '¿{suj} ______ con el profesor?' ] },
    { verb:'comer', reflexive:false, infNl:'comer', trNl:'eten', trEn:'to eat', templates:[
      '{suj} ______ en el restaurante.', '{suj} ______ una manzana.' ] },
    { verb:'escribir', reflexive:false, infNl:'escribir', trNl:'schrijven', trEn:'to write', templates:[
      '{suj} ______ un correo.', '{suj} ______ en el cuaderno.' ] },
    { verb:'trabajar', reflexive:false, infNl:'trabajar', trNl:'werken', trEn:'to work', templates:[
      'Hoy {suj} ______ en casa.', '{suj} ______ mucho esta semana.' ] },
    { verb:'hacer', reflexive:false, infNl:'hacer', trNl:'doen/maken', trEn:'to do/make', templates:[
      '{suj} ______ la cena.', '{suj} ______ los deberes.' ] },
    { verb:'leer', reflexive:false, infNl:'leer', trNl:'lezen', trEn:'to read', templates:[
      '{suj} ______ un libro muy bueno.', '{suj} ______ el periódico.' ] },
    { verb:'dormir', reflexive:false, infNl:'dormir', trNl:'slapen', trEn:'to sleep', templates:[
      'No hagas ruido, {suj} ______.', '{suj} ______ la siesta.' ] },
    { verb:'duchar', reflexive:true, infNl:'ducharse', trNl:'douchen', trEn:'to shower', templates:[
      '{suj} ______ ahora mismo.', 'Un momento, {suj} ______.' ] } ] },

"""

GUIDE = r"""GUIDES['a1-u17p'] = { nl:`
      <div class="card">
        <h2 class="section-title" style="margin-top:0;">Estar + gerundio</h2>
        <table class="conj-table">
          <tr><th>yo</th><td>estoy hablando</td></tr><tr><th>tú</th><td>estás hablando</td></tr><tr><th>él/ella/usted</th><td>está hablando</td></tr>
          <tr><th>nosotros</th><td>estamos hablando</td></tr><tr><th>vosotros</th><td>estáis hablando</td></tr><tr><th>ellos/ustedes</th><td>están hablando</td></tr>
        </table>
        <p class="muted" style="margin-top:10px;">Alleen <i>estar</i> verandert. Het gerundio maak je zo: <b>-ar → -ando</b> (<i>hablando</i>), <b>-er/-ir → -iendo</b> (<i>comiendo, viviendo</i>).</p>
      </div>
      <div class="card">
        <h2 class="section-title" style="margin-top:0;">Onregelmatig</h2>
        <div class="muted" style="line-height:1.55;"><b>y</b> in plaats van i: <i>leer → leyendo, traer → trayendo, oír → oyendo, ir → yendo</i>.<br><b>o → u</b>: <i>dormir → durmiendo, morir → muriendo</i>.<br><b>e → i</b>: <i>decir → diciendo, pedir → pidiendo, venir → viniendo, vestir → vistiendo, sentir → sintiendo</i>.</div>
      </div>
      <div class="card">
        <h2 class="section-title" style="margin-top:0;">Wanneer gebruik je het?</h2>
        <div class="muted" style="line-height:1.55;">Voor wat er <b>nu</b> of <b>deze dagen</b> gebeurt: <i>Ahora estoy comiendo. Esta semana estoy trabajando mucho.</i><br>Voor gewoontes en feiten gebruik je de gewone tegenwoordige tijd: <i>Normalmente como a las dos. Vivo en Madrid.</i><br>Let op: Spaans gebruikt het minder vaak dan Engels. <i>¿Qué haces?</i> kan ook "wat ben je aan het doen?" betekenen.</div>
      </div>
      <div class="card">
        <h2 class="section-title" style="margin-top:0;">Me, te, se</h2>
        <div class="muted" style="line-height:1.55;">Twee plekken mogelijk: <i><b>Me</b> estoy duchando</i> of <i>Estoy duchándo<b>me</b></i> (dan krijgt het gerundio een accent). Hetzelfde met lo/la: <i><b>Lo</b> estoy leyendo</i> = <i>Estoy leyéndo<b>lo</b></i>.</div>
      </div>
      <div class="card">
        <h2 class="section-title" style="margin-top:0;">Handige zinnen</h2>
        <div class="muted" style="line-height:1.55;"><i>¿Qué estás haciendo?</i> — Wat ben je aan het doen?<br><i>Estoy ocupado/a.</i> — Ik heb het druk.<br><i>Está lloviendo.</i> — Het regent.<br><i>Te estoy esperando.</i> — Ik wacht op je.</div>
      </div>` };
"""

# Herhaling: estar + gerundio komt terug in latere lessen (lesson-id -> extra zinnen)
REPEAT = {
 'a1-u18-l1': [["Estoy buscando una chaqueta para el invierno.","Ik ben op zoek naar een jas voor de winter.","I'm looking for a jacket for winter."]],
 'a1-u18-l3': [["Mi hermana se está probando un vestido.","Mijn zus is een jurk aan het passen.","My sister is trying on a dress.",["Mi hermana está probándose un vestido."]]],
 'a1-u19-l2': [["Estamos esperando el postre.","We zitten op het toetje te wachten.","We're waiting for dessert."]],
 'a1-u19-l4': [["El camarero está trayendo la cuenta.","De ober is de rekening aan het brengen.","The waiter is bringing the bill."]],
 'a1-u20-l3': [["Estoy haciendo la maleta.","Ik ben mijn koffer aan het pakken.","I'm packing my suitcase."]],
 'a1-u20-l4': [["El autobús está llegando.","De bus komt eraan.","The bus is arriving."]],
 'a1-u21-l3': [["Estoy descansando en la cama.","Ik lig in bed uit te rusten.","I'm resting in bed."]],
 'a1-u22-l1': [["Estoy pensando en el plan para mañana.","Ik ben aan het nadenken over het plan voor morgen.","I'm thinking about the plan for tomorrow."]],
 'a1-u22-l3': [["Ahora mismo estoy trabajando, te llamo luego.","Ik ben nu aan het werken, ik bel je straks.","I'm working right now, I'll call you later."]],
 'a1-u23-l1': [["Ya he comido y ahora estoy leyendo.","Ik heb al gegeten en nu ben ik aan het lezen.","I've already eaten and now I'm reading."]],
 'a1-u23-l3': [["Estoy aprendiendo español y nunca he estado en España.","Ik ben Spaans aan het leren en ik ben nog nooit in Spanje geweest.","I'm learning Spanish and I've never been to Spain."]],
 'a2-u1-l1': [["Mi hermano se está duchando y yo estoy desayunando.","Mijn broer staat onder de douche en ik ben aan het ontbijten.","My brother is showering and I'm having breakfast.",["Mi hermano está duchándose y yo estoy desayunando."]]],
 'a2-u2-l2': [["Estoy viendo una serie muy buena.","Ik ben een heel goede serie aan het kijken.","I'm watching a really good series."]],
 'a2-u3-l1': [["Estoy aprendiendo a tocar el piano.","Ik ben piano aan het leren spelen.","I'm learning to play the piano."]],
 'a2-u5-l1': [["Está lloviendo, pero hace calor.","Het regent, maar het is warm.","It's raining, but it's warm."]],
 'a2-u6-l3': [["Estoy entrenando para una carrera.","Ik ben aan het trainen voor een hardloopwedstrijd.","I'm training for a race."]],
 'a2-u8-l3': [["Estamos esperando el tren, que viene con retraso.","We wachten op de trein, die vertraging heeft.","We're waiting for the train, which is delayed."]],
 'a2-u11-l2': [["Estoy buscando un vuelo barato.","Ik ben op zoek naar een goedkope vlucht.","I'm looking for a cheap flight."]],
 'a2-u17-l1': [["Estoy haciendo la compra en el supermercado.","Ik ben boodschappen aan het doen in de supermarkt.","I'm doing the shopping at the supermarket."]],
 'a2-u24-l1': [["Mi madre está pasando la aspiradora.","Mijn moeder is aan het stofzuigen.","My mother is vacuuming."]],
 'a2-u30-l4': [["Esta semana estoy trabajando mucho.","Deze week werk ik veel.","This week I'm working a lot."]],
}

def rep(c, old, new):
    assert c.count(old) == 1, old[:80]
    return c.replace(old, new)

def main(path='index.html'):
    c = open(path, encoding='utf-8').read()
    if 'function gerundio(' in c:
        print('al aanwezig'); return
    # 1) tijd 'progresivo' in conjugate + gerundio-helper
    c = rep(c, "function conjugate(verb, tense){\n",
               GERUND_JS.lstrip('\n') + "function conjugate(verb, tense){\n"
               "  if(tense==='progresivo'){ const g = gerundio(verb); return ['estoy','estás','está','estamos','estáis','están'].map(e=>e+' '+g); }\n")
    c = rep(c, "TENSE_LABEL = { presente:'Presente', ", "TENSE_LABEL = { presente:'Presente', progresivo:'Estar + gerundio', ")
    # 2) werkwoordoefening
    c = rep(c, "  'a1-u18': { tense:'presente', verbs:[", VERB_PRACTICE_ENTRY + "  'a1-u18': { tense:'presente', verbs:[")
    # 3) gids
    c = rep(c, "GUIDES['a2-u5'] = {", GUIDE + "GUIDES['a2-u5'] = {")
    # 4) herhaling in latere lessen
    dec = json.JSONDecoder()
    for lid, sents in REPEAT.items():
        m = re.search(r"\{ id:['\"]" + re.escape(lid) + r"['\"], kind:'new', ", c); assert m, lid
        s0 = c.index('[', c.index('sentences:', c.index('words:', m.start())))
        arr, end = dec.raw_decode(c, s0)
        new = arr + [x for x in sents if x[0] not in [a[0] for a in arr]]
        c = c[:s0] + J(new) + c[end:]
    open(path, 'w', encoding='utf-8').write(c)
    print('klaar:', len(REPEAT), 'lessen met herhaling')

if __name__ == '__main__':
    main(*(sys.argv[1:2]))
