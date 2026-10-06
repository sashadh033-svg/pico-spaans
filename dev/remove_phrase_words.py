# Woordenlijst A2: "woorden" die eigenlijk gewone zinnetjes zijn (alle delen al bekend, letterlijke betekenis,
# bv. "tomar café", "salir de casa") eruit halen. Vaste uitdrukkingen (poner la mesa, echar de menos) en
# grammatica-voorbeelden in grammatica-units blijven staan. Het aantal bolletjes per unit blijft gelijk
# (in deze units bepalen de zinnen het aantal). tomar/coger stonden nergens los: die worden het losse werkwoord.
# Bron: dev/phrase_words_a2.json   Gebruik: python3 dev/remove_phrase_words.py   (idempotent)
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, 'index.html')
REPLACE = {
    'tomar café': ['tomar', 'nemen / drinken (eten, drinken, vervoer)', 'to take / to have (food, drink, transport)'],
    'coger el autobús': ['coger', 'nemen / pakken', 'to take / to catch'],
}

def main():
    c = open(PATH, encoding='utf-8').read()
    lo = c.index("id:'a2-u1', icon"); hi = c.index("id:'b1-u1'") if "id:'b1-u1'" in c else c.index('id:"b1-u1"')
    words = json.load(open(os.path.join(ROOT, 'dev', 'phrase_words_a2.json'), encoding='utf-8'))
    removed = replaced = 0
    for es in words:
        pat = re.compile(r'(, )?\[' + re.escape(json.dumps(es, ensure_ascii=False)) + r', "(?:[^"\\]|\\.)*", "(?:[^"\\]|\\.)*"\](, )?')
        seg = c[lo:hi]
        m = pat.search(seg)
        if not m:
            continue
        if es in REPLACE:
            new = json.dumps(REPLACE[es], ensure_ascii=False, separators=(', ', ': '))
            rep = (m.group(1) or '') + new + (m.group(2) or '')
            replaced += 1
        else:
            # komma's netjes houden: midden in de lijst één ", " laten staan
            rep = ', ' if (m.group(1) and m.group(2)) else ''
            removed += 1
        seg = seg[:m.start()] + rep + seg[m.end():]
        assert not pat.search(seg), 'dubbel: ' + es
        c = c[:lo] + seg + c[hi:]
        hi = lo + len(seg)
    open(PATH, 'w', encoding='utf-8').write(c)
    print(removed, 'weggehaald,', replaced, 'vervangen door los werkwoord')

if __name__ == '__main__':
    main()
