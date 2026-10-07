# A2-woordenschat lichter maken (okt 2026): zeldzame woorden en zware combinaties (B1+) uit de A2-woordenlijst,
# zinnen die zo'n woord gebruikten vervangen door zinnen met gewone, al geleerde woorden (zelfde aantal zinnen,
# dus zelfde bolletjes), en tikhulp (HINTS) waar zo'n woord nog in een verhaaltje of B1/B2-zin staat.
# Bronnen: dev/a2_vocab_remove.json (woorden), dev/a2_vocab_sentences.json (zinnen), dev/a2_vocab_hints.json (tikhulp)
# Gebruik: python3 dev/a2_vocab.py   (idempotent)
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sentence_tools import PATH, replace_sentences

D = os.path.dirname(os.path.abspath(__file__))

def remove_words(c, words):
    lo = c.index("id:'a2-u1', icon"); hi = c.index("id:'b1-u1', icon")
    seg = c[lo:hi]; n = 0
    for es in words:
        pat = re.compile(r'(, )?\[' + re.escape(json.dumps(es, ensure_ascii=False)) + r', "(?:[^"\\]|\\.)*", "(?:[^"\\]|\\.)*"\](, )?')
        m = pat.search(seg)
        while m:
            seg = seg[:m.start()] + (', ' if (m.group(1) and m.group(2)) else '') + seg[m.end():]
            n += 1; m = pat.search(seg)
    print(n, 'woorden weggehaald')
    return c[:lo] + seg + c[hi:]

def add_hints(c, H):
    i = c.index('const HINTS = ') + len('const HINTS = '); j = c.index('\n', i)
    raw = c[i:j].rstrip(); semi = raw.endswith(';')
    hints = json.loads(raw.rstrip(';')); added = 0
    for sent, hs in H.items():
        if sent not in c:
            continue
        cur = hints.setdefault(sent, [])
        for h in hs:
            if not any(x[0] == h[0] for x in cur):
                cur.append(h); added += 1
    print(added, 'tikhulp-woorden toegevoegd')
    return c[:i] + json.dumps(hints, ensure_ascii=False) + (';' if semi else '') + c[j:]

def main():
    sents = json.load(open(os.path.join(D, 'a2_vocab_sentences.json'), encoding='utf-8'))
    replace_sentences([(s['lesson'], s['old'], s['new'], 'a2-woordenschat') for s in sents])
    c = open(PATH, encoding='utf-8').read()
    c = remove_words(c, [x['es'] for x in json.load(open(os.path.join(D, 'a2_vocab_remove.json'), encoding='utf-8'))])
    c = add_hints(c, json.load(open(os.path.join(D, 'a2_vocab_hints.json'), encoding='utf-8')))
    open(PATH, 'w', encoding='utf-8').write(c)

if __name__ == '__main__':
    main()
