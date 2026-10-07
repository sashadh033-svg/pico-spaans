# Tikhulp (HINTS) voor woorden in vervangen zinnen die op dat moment nog niet behandeld zijn.
# Gevonden met een woordenlijst-check (dev/a1..b2_sentences.py); vormen van bekende werkwoorden krijgen geen hulp.
# Formaat per woord: [es in de zin, nl in de vertaling, en in de vertaling, uitleg nl, uitleg en]
# Gebruik: python3 dev/new_word_hints.py   (idempotent)
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sentence_tools import PATH

H = {
 'Esta noche he soñado con mis vacaciones.': [['soñado', 'gedroomd', 'dreamt', 'gedroomd (soñar)', 'dreamt (soñar)']],
 'Este verano voy a hacer fotos de paisajes.': [['paisajes', 'landschappen', 'landscapes', 'landschappen', 'landscapes']],
 'Hoy he quedado con mi prima.': [['prima', 'nicht', 'cousin', 'nicht (dochter van oom/tante)', 'cousin']],
 'Hemos visto un relámpago enorme.': [['enorme', 'enorme', 'huge', 'enorm, heel groot', 'huge']],
 'Ayer por la tarde llovía mucho.': [['Ayer', 'Gistermiddag', 'Yesterday', 'gisteren', 'yesterday']],
 'Ayer había tormenta y llovía mucho.': [['Ayer', 'Gisteren', 'Yesterday', 'gisteren', 'yesterday']],
 'El estadio está lleno.': [['lleno', 'vol', 'full', 'vol', 'full']],
 'Ha sido una experiencia única.': [['experiencia', 'ervaring', 'experience', 'ervaring', 'experience']],
 'He guardado el tique de compra.': [['guardado', 'bewaard', 'kept', 'bewaard (guardar)', 'kept (guardar)']],
 'Le pregunto al tendero el precio de las cerezas.': [['tendero', 'winkelier', 'shopkeeper', 'winkelier', 'shopkeeper']],
 'El flan es casero; lo pido de postre.': [['casero', 'huisgemaakt', 'homemade', 'huisgemaakt', 'homemade']],
 'El servicio ha sido excelente.': [['excelente', 'uitstekend', 'excellent', 'uitstekend', 'excellent']],
 'En el estanco venden sellos.': [['venden', 'verkopen', 'sell', 'ze verkopen (vender)', 'they sell (vender)']],
 'La lavadora se ha estropeado.': [['estropeado', 'kapotgegaan', 'broken down', 'kapotgegaan (estropearse)', 'broken down']],
 'Estamos tendiendo la ropa en la azotea.': [['tendiendo', 'ophangen', 'hanging', 'aan het ophangen (tender la ropa)', 'hanging out (tender)']],
 'La calefacción no funciona; hay que repararla.': [['funciona', 'doet het', 'work', 'werkt (funcionar)', 'works'], ['repararla', 'gerepareerd', 'fixing', 'hem repareren (reparar)', 'to fix it']],
 'Tengo fotos nuevas; voy a colgarlas en la pared.': [['colgarlas', 'hangen', 'hang', 'ze ophangen (colgar)', 'to hang them']],
 'Se ha dado un golpe en el codo.': [['golpe', 'gestoten', 'banged', 'klap, stoot (darse un golpe = zich stoten)', 'knock']],
 'Me he dado un golpe en el pulgar.': [['golpe', 'gestoten', 'banged', 'klap, stoot (darse un golpe = zich stoten)', 'knock']],
 'Tengo el hombro muy tenso; lo muevo despacio.': [['tenso', 'vast', 'tense', 'gespannen, stijf', 'tense'], ['muevo', 'beweeg', 'move', 'ik beweeg (mover)', 'I move']],
 'Me duele el cuello de mirar el ordenador; voy a apagarlo.': [['apagarlo', 'uitzetten', 'switch it off', 'hem uitzetten (apagar)', 'to switch it off']],
 'Mi hermano estornuda; le doy un pañuelo.': [['estornuda', 'niest', 'sneezes', 'niest (estornudar)', 'sneezes']],
 'Esta crema es para las quemaduras; tienes que ponértela dos veces al día.': [['quemaduras', 'brandwonden', 'burns', 'brandwonden', 'burns']],
 'La operación ha sido un éxito.': [['éxito', 'succes', 'success', 'succes', 'success']],
 'De niño era muy feliz.': [['feliz', 'gelukkig', 'happy', 'gelukkig, blij', 'happy']],
 'He empezado a hacer yoga; intento practicarlo cada día.': [['intento', 'probeer', 'try', 'ik probeer (intentar)', 'I try']],
 'Mi abuela sabía cocinar muy bien y le enseñaba recetas a mi madre.': [['enseñaba', 'leerde', 'taught', 'leerde (enseñar = onderwijzen)', 'taught']],
 'He leído la biografía de un músico famoso.': [['músico', 'muzikant', 'musician', 'muzikant', 'musician']],
 'Recuerdo mi primer día de trabajo; nunca voy a olvidarlo.': [['olvidarlo', 'vergeten', 'forget', 'het vergeten (olvidar)', 'to forget it']],
 'Anteayer vi a una amiga en el centro y la invité a un café.': [['invité', 'trakteerde', 'bought', 'ik trakteerde (invitar)', 'I treated (invitar)']],
 'Es un libro genial; te recomiendo que lo leas.': [['genial', 'geweldig', 'great', 'geweldig', 'great']],
 'El director nos ha concedido el permiso.': [['permiso', 'toestemming', 'permission', 'toestemming', 'permission']],
 'Mañana me voy a despedir de mis abuelos en el aeropuerto.': [['despedir', 'afscheid', 'say goodbye', 'afscheid nemen (despedirse)', 'to say goodbye']],
 'Mi abuela quiere que la cuide los fines de semana.': [['cuide', 'zorg', 'look after', 'zorgen voor (cuidar)', 'look after']],
 'Está defendiendo su postura con firmeza.': [['firmeza', 'vastberaden', 'firmly', 'vastberadenheid', 'firmness']],
 'He contratado a un asesor financiero.': [['contratado', 'in de arm genomen', 'hired', 'aangenomen, ingehuurd (contratar)', 'hired'], ['financiero', 'financieel', 'financial', 'financieel', 'financial']],
 'No quiero que malgastes nuestro dinero.': [['malgastes', 'verspilt', 'waste', 'verspillen (malgastar)', 'to waste']],
 'Mi hermana necesitaba dinero y se lo transferí ayer.': [['transferí', 'overgemaakt', 'transferred', 'ik maakte over (transferir)', 'I transferred']],
 'Es importante que diversifiques tus inversiones.': [['diversifiques', 'spreidt', 'diversify', 'spreiden (diversificar)', 'diversify']],
 'Me gustaría hacer un doctorado en biología.': [['biología', 'biologie', 'biology', 'biologie', 'biology']],
 'Mi compañero de clase no tenía los apuntes y se los presté.': [['apuntes', 'aantekeningen', 'notes', 'aantekeningen', 'notes'], ['presté', 'geleend', 'lent', 'ik leende uit (prestar)', 'I lent']],
 'Tengo un título holandés y quiero convalidarlo en España.': [['convalidarlo', 'laten erkennen', 'recognised', 'het laten erkennen (convalidar)', 'to get it recognised']],
 'Mi profesora quiere que amplíe mi vocabulario en español.': [['amplíe', 'uitbreid', 'expand', 'uitbreiden (ampliar)', 'expand']],
 '¿Puedes corregirme si cometo un error?': [['corregirme', 'verbeteren', 'correct me', 'mij verbeteren (corregir)', 'correct me'], ['cometo', 'maak', 'make', 'ik maak (cometer un error = een fout maken)', 'I make']],
 'Apunto las palabras nuevas y las repaso antes de dormir.': [['palabras', 'woorden', 'words', 'woorden', 'words'], ['repaso', 'herhaal', 'review', 'ik herhaal (repasar)', 'I review']],
 'Vi la aplicación y la descargué para aprender vocabulario.': [['descargué', 'downloadde', 'downloaded', 'ik downloadde (descargar)', 'I downloaded']],
 'Debería desconectarme del móvil los fines de semana.': [['desconectarme', 'wegleggen', 'disconnect', 'loskomen van, afsluiten (desconectarse)', 'to disconnect']],
 'Recibí un mensaje importante y se lo reenvié a mi jefe.': [['reenvié', 'stuurde', 'forwarded', 'ik stuurde door (reenviar)', 'I forwarded']],
 'Está observando aves con sus prismáticos.': [['prismáticos', 'verrekijker', 'binoculars', 'verrekijker', 'binoculars']],
 'Me encantaría escalar esa montaña, pero requiere mucha experiencia.': [['requiere', 'nodig', 'takes', 'vereist (requerir)', 'requires']],
 'Vimos animales salvajes y los fotografiamos durante la excursión.': [['fotografiamos', 'fotografeerden', 'photographed', 'we fotografeerden (fotografiar)', 'we photographed']],
 'Separamos el vidrio y lo llevamos al punto verde del barrio.': [['Separamos', 'scheiden', 'separate', 'we scheiden (separar)', 'we separate']],
 'Haz una copia del pasaporte y llévala siempre por si acaso.': [['copia', 'kopie', 'copy', 'kopie', 'copy']],
 'Le organizamos una fiesta por sorpresa; nadie se lo había dicho.': [['nadie', 'niemand', 'nobody', 'niemand', 'nobody']],
 'Para mí sería dificilísimo aprender chino.': [['chino', 'Chinees', 'Chinese', 'Chinees', 'Chinese']],
 'Habría que verificar siempre la fuente de la noticia.': [['verificar', 'controleren', 'check', 'controleren', 'to check']],
 'El periodista ha revelado un secreto importante.': [['secreto', 'geheim', 'secret', 'geheim', 'secret']],
 'El periodista entrevistó al ministro y le preguntó por el escándalo.': [['ministro', 'minister', 'minister', 'minister', 'minister']],
 'Los votantes pidieron una reforma y el gobierno se la prometió.': [['reforma', 'hervorming', 'reform', 'hervorming', 'reform']],
 'Durante la campaña electoral había carteles por todas partes.': [['carteles', 'affiches', 'posters', 'affiches', 'posters']],
 'Preferiría no tomar partido en discusiones así.': [['discusiones', 'discussies', 'discussions', 'discussies', 'discussions']],
 'Ojalá sea escritora algún día.': [['escritora', 'schrijfster', 'writer', 'schrijfster', 'writer']],
 'Ligaron en una discoteca y ahora se van a casar.': [['discoteca', 'discotheek', 'club', 'discotheek', 'nightclub']],
 'Le pedimos al casero que arreglara la caldera, pero no quiso.': [['caldera', 'cv-ketel', 'boiler', 'cv-ketel', 'boiler']],
 'Habría que respetar más las creencias de los demás.': [['creencias', 'overtuigingen', 'beliefs', 'overtuigingen', 'beliefs']],
 'Voy a actualizar el sistema operativo.': [['operativo', 'besturingssysteem', 'operating system', 'sistema operativo = besturingssysteem', 'operating system']],
 'Vamos a alquilar una casa rural en la sierra de Gredos.': [['sierra', 'Sierra', 'Sierra', 'bergketen', 'mountain range']],
 'Deja que el guiso se haga a fuego lento; a mí siempre se me quema.': [['guiso', 'stoofpot', 'stew', 'stoofpot', 'stew']],
 'Leí una reseña muy elogiosa y voy a ir a la exposición.': [['elogiosa', 'lovende', 'glowing', 'lovend', 'glowing']],
 'La letra de esta canción es muy triste, pero te la canto.': [['canción', 'liedje', 'song', 'lied, liedje', 'song']],
 'Les rindieron homenaje a los fallecidos.': [['rindieron', 'brachten hulde', 'paid tribute', 'rendir homenaje = eer bewijzen', 'paid tribute'], ['fallecidos', 'overledenen', 'dead', 'overledenen', 'the deceased']],
 'Las jugadoras reclamaban que les pagaran lo mismo.': [['jugadoras', 'speelsters', 'players', 'speelsters', 'players']],
 'Hace cien años, una sociedad sin pobreza parecía una utopía.': [['pobreza', 'armoede', 'poverty', 'armoede', 'poverty']],
 'Me piro, que se me ha hecho tarde.': [['piro', 'smeer', 'off', 'ik ga ervandoor (pirarse, spreektaal)', "I'm off (slang)"]],
}

def run():
    c = open(PATH, encoding='utf-8').read()
    i = c.index('const HINTS = ') + len('const HINTS = ')
    j = c.index('\n', i)
    raw = c[i:j].rstrip()
    semi = raw.endswith(';')
    hints = json.loads(raw.rstrip(';'))
    added = 0
    for sent, hs in H.items():
        if sent not in c:
            continue  # zin is later vervangen (bv. dev/a2_vocab.py)
        cur = hints.setdefault(sent, [])
        for h in hs:
            if not any(x[0] == h[0] for x in cur):
                cur.append(h); added += 1
    c = c[:i] + json.dumps(hints, ensure_ascii=False) + (';' if semi else '') + c[j:]
    open(PATH, 'w', encoding='utf-8').write(c)
    print(added, 'woorden tikhulp toegevoegd in', len(H), 'zinnen')

if __name__ == '__main__':
    run()
