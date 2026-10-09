# Tikhulp voor vaste combinaties van werkwoord + voorzetsel die anders werken dan in het Nederlands/Engels
# (soñar con = dromen over, trabajar con el ordenador = op de computer werken, ir en coche = met de auto).
# Het hele stukje (bv. "soñado con") wordt onderstreept; tikken toont de uitleg.
# Werkt op alle zinnen (lessen en verhaaltjes) van A1-B2. Gebruik: python3 dev/prep_hints.py   (idempotent)
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sentence_tools import PATH
from a2_vocab import add_hints

V = r'[a-záéíóúñ]*'   # rest van een vervoegde vorm
VEH = r'(?:coche|tren|autobús|bus|bici|bicicleta|avión|metro|taxi|barco|moto|tranvía)'
RULES = [
    # (regex; groep 1 = het stukje dat onderstreept wordt), tip nl, tip en
    (r'\b((?:soñ|sueñ)' + V + r' con)\b', 'soñar con = dromen over', 'soñar con = to dream about'),
    (r'\b((?:pens|piens)' + V + r' en)\b', 'pensar en = denken aan', 'pensar en = to think about'),
    (r'\btrabaj' + V + r'(?: \w+){0,2}? (con el ordenador)\b', 'con el ordenador = op/met de computer', 'con el ordenador = on the computer'),
    (r'\b(naveg' + V + r' por internet)\b', 'navegar por internet = op internet surfen', 'navegar por internet = to surf the internet'),
    (r'\b(habl' + V + r' por teléfono)\b', 'hablar por teléfono = (met iemand) bellen', 'hablar por teléfono = to talk on the phone'),
    (r'\b(en ' + VEH + r')\b', 'en coche/tren… = met de auto/trein… (vervoer: en)', 'en coche/tren… = by car/train… (transport: en)'),
    (r'\b((?:jueg|jug)' + V + r' (?:al|a la|a los|a las))\b(?! (?:una|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce)\b)', 'jugar a(l) = een spel/sport spelen: jugar al fútbol', 'jugar a(l) = to play a game/sport: jugar al fútbol'),
    (r'\b(sub' + V + r' (?:al|a la) ' + VEH + r')\b', 'subir a(l) = instappen (in)', 'subir a(l) = to get on/into'),
    (r'\b(baj' + V + r' del? ' + VEH + r')\b', 'bajar de(l) = uitstappen (uit)', 'bajar de(l) = to get off/out of'),
    (r'(?<!\bme )(?<!\bte )(?<!\bse )(?<!\bnos )(?<!\bos )\b(qued(?:o|as|a|amos|áis|an|é|aste|ó|asteis|aron|ar|ado|ando) con)\b', 'quedar con alguien = met iemand afspreken', 'quedar con alguien = to meet up with someone'),
    (r'\b((?:(?:me|te|se|nos|os) (?:\w+ )?cas' + V + r'|casarse|casado|casada) con)\b', 'casarse con = trouwen met', 'casarse con = to marry'),
    (r'\b(enamor' + V + r' de)\b', 'enamorarse de = verliefd worden op', 'enamorarse de = to fall in love with'),
    (r'\b(depend(?:o|es|e|emos|éis|en|er|ía|ió|erá) de)\b', 'depender de = afhangen van', 'depender de = to depend on'),
    (r'\b((?:(?:me|te|se|nos|os) (?:\w+ )?(?:acord|acuerd)' + V + r'|acordarse) de)\b', 'acordarse de = zich herinneren', 'acordarse de = to remember'),
    (r'\b(olvid' + V + r' de)\b', 'olvidarse de = vergeten', 'olvidarse de = to forget'),
    (r'\b(tard(?:o|as|a|amos|áis|an|ar|é|aste|ó|aron|ado|ando) en)\b', 'tardar en = er (zo lang) over doen om', 'tardar en = to take (time) to'),
    (r'\b((?:confí(?:o|as|a|an)|confi(?:amos|áis|ar|ado|é|ó)) en)\b', 'confiar en = vertrouwen op', 'confiar en = to trust'),
    (r'\b(preocup' + V + r' por)\b', 'preocuparse por = zich zorgen maken om', 'preocuparse por = to worry about'),
    (r'\b(interes(?:o|as|a|amos|áis|an|ó|ado|ada|arse) por)\b', 'interesarse por = interesse hebben in', 'interesarse por = to be interested in'),
    (r'\b((?:me|te|se|nos|os) (?:río|ríes|ríe|reímos|reís|ríen|reí|rió|reímos) de)\b', 'reírse de = lachen om', 'reírse de = to laugh at'),
    (r'\b(despid' + V + r' de)\b', 'despedirse de = afscheid nemen van', 'despedirse de = to say goodbye to'),
    (r'\b((?:di|dio|doy|da|das|dado|dimos|dieron|dar|darse|daré) cuenta de)\b', 'darse cuenta de = merken, beseffen', 'darse cuenta de = to realise'),
    (r'\b(consist' + V + r' en)\b', 'consistir en = bestaan uit', 'consistir en = to consist of'),
    (r'\b((?:me|te|se|nos|os) fij' + V + r' en)\b', 'fijarse en = letten op', 'fijarse en = to notice'),
    (r'\b(dej' + V + r' de)\b(?= [a-záéíóú]+(?:ar|er|ir)\b)', 'dejar de + infinitief = stoppen met', 'dejar de + inf. = to stop doing'),
]

def sentences(c):
    i, j = c.index('const CURRICULUM'), c.index('const STORY_CHARACTERS')
    out = set(json.loads('"' + m.group(1) + '"') for m in re.finditer(r'\["((?:[^"\\]|\\.)+)", "', c[i:j]))
    k = c.index('const STORIES'); l = c.index('\nconst ', k + 10)
    out |= set(json.loads('"' + m.group(1) + '"') for m in re.finditer(r'"es": "((?:[^"\\]|\\.)+)"', c[k:l]))
    out |= set(m.group(1) for m in re.finditer(r"es:'((?:[^'\\]|\\.)+)'", c[k:]))
    return out

# De uitleg ook tonen onder het juiste antwoord (bij 'bouw de zin' zie je de Spaanse zin pas na het nakijken)
CODE = [
    ("  .hint-tip{", "  .sent-tips{ margin-top:8px; font-size:14px; line-height:1.4; }\n  .hint-tip{"),
    ("function hintify(text, sentEs, lang){",
     "function sentenceTips(es){\n"
     "  const hs = HINTS[es]; if(!hs || !hs.length) return '';\n"
     "  const en = appState.profile.baseLang==='en';\n"
     "  return '<div class=\"sent-tips\">' + hs.slice(0,3).map(h=> '💡 ' + escHtml(en ? h[4] : h[3])).join('<br>') + '</div>';\n"
     "}\n"
     "function hintify(text, sentEs, lang){"),
    ("${showTranslation ? '<br>'+it.translation : ''}</div>",
     "${showTranslation ? '<br>'+it.translation : ''}${it.es ? sentenceTips(it.es) : ''}</div>"),
]

def main():
    c = open(PATH, encoding='utf-8').read()
    for old, new in CODE:
        if new in c:
            continue
        assert c.count(old) == 1, old
        c = c.replace(old, new)
    H = {}
    for s in sentences(c):
        # alleen echte zinnen (geen woordenlijst-items); 'el pienso' = diervoer
        if ' ' not in s or not re.search(r'[.?!…]$', s) or 'pienso en sacos' in s:
            continue
        for rx, nl, en in RULES:
            m = re.search(rx, s, re.I)
            if m:
                H.setdefault(s, []).append([m.group(1), '', '', nl, en])
    c = add_hints(c, H)
    open(PATH, 'w', encoding='utf-8').write(c)
    print(len(H), 'zinnen met een voorzetsel-combinatie')

if __name__ == '__main__':
    main()
