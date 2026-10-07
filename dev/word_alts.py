# Woordenlijst: extra goede Spaanse antwoorden (EXTRA_ALTS) en duidelijkere vertalingen.
# Bron: dev/word_fixes.json  [{es, alts?, en_new?, nl_new?, alts_en?, alts_nl?, why}]
# alts = goede Spaanse antwoorden; alts_en/alts_nl = goede vertalingen bij Spaans -> Engels/Nederlands
# Gebruik: python3 dev/word_alts.py   (idempotent)
import json, os, re, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, 'index.html')
FIXES = os.path.join(ROOT, 'dev', 'word_fixes.json')

def normalize_lenient(s):
    # zelfde als normalizeLenient() in index.html
    s = str(s).lower()
    s = re.sub(r'\.{2,}|…', ' ', s)
    s = re.sub(r'[¿?¡!.,]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return ''.join(ch for ch in unicodedata.normalize('NFD', s) if unicodedata.category(ch) != 'Mn')

def j(s):
    return json.dumps(s, ensure_ascii=False)

def main():
    c = open(PATH, encoding='utf-8').read()
    fixes = json.load(open(FIXES, encoding='utf-8'))
    head = 'const EXTRA_ALTS = '
    a = c.index(head) + len(head)
    b = c.index(';\n', a)
    alts = json.loads(c[a:b])
    c = c[:a] + '@@EXTRA_ALTS@@' + c[b:]
    n_alt = n_gloss = 0
    for f in fixes:
        es = f['es']
        # vertaling verduidelijken in elke woordregel met dit Spaanse woord
        for lang, idx in (('nl_new', 1), ('en_new', 2)):
            new = f.get(lang)
            if not new:
                continue
            pat = re.compile(r'\[' + re.escape(j(es)) + r', ("(?:[^"\\]|\\.)*"), ("(?:[^"\\]|\\.)*")\]')
            def rep(m):
                nonlocal n_gloss
                parts = [json.loads(m.group(1)), json.loads(m.group(2))]
                old = parts[idx - 1]
                if old == new:
                    return m.group(0)
                parts[idx - 1] = new
                n_gloss += 1
                # alternatieven voor de oude vertaling (andere richting) gelden ook voor de nieuwe
                ko, kn = normalize_lenient(old), normalize_lenient(new)
                if ko in alts and kn not in alts:
                    alts[kn] = list(alts[ko])
                return '[' + j(es) + ', ' + j(parts[0]) + ', ' + j(parts[1]) + ']'
            c, k = pat.subn(rep, c)
            assert k > 0, 'woord niet gevonden: ' + es
        # extra goede vertalingen in je eigen taal (richting Spaans -> NL/EN); sleutel = de huidige vertaling
        for lang, idx in (('alts_nl', 1), ('alts_en', 2)):
            if not f.get(lang):
                continue
            m = re.search(r'\[' + re.escape(j(es)) + r', ("(?:[^"\\]|\\.)*"), ("(?:[^"\\]|\\.)*")\]', c)
            assert m, 'woord niet gevonden: ' + es
            gk = normalize_lenient(json.loads(m.group(idx)))
            cur = alts.setdefault(gk, [])
            for x in f[lang]:
                if x not in cur and normalize_lenient(x) != gk:
                    cur.append(x); n_alt += 1
        # extra goede Spaanse antwoorden
        key = normalize_lenient(es)
        cur = alts.setdefault(key, [])
        for x in f.get('alts', []):
            if x not in cur and normalize_lenient(x) != key:
                cur.append(x)
                n_alt += 1
        if not cur:
            del alts[key]
    c = c.replace('@@EXTRA_ALTS@@', json.dumps(alts, ensure_ascii=False, separators=(',', ':')))
    open(PATH, 'w', encoding='utf-8').write(c)
    print(n_alt, 'alts toegevoegd,', n_gloss, 'vertalingen aangepast')

if __name__ == '__main__':
    main()
