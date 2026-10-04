# Hulpjes om zinnen in CURRICULUM (index.html) te vervangen zonder het aantal zinnen te veranderen.
# Elke wijziging: (les-id, oude Spaanse zin, nieuwe zin [es, nl, en, (alts)], reden).
# Idempotent: staat de nieuwe zin er al, dan wordt hij overgeslagen.
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, 'index.html')

def _lesson_span(c, lid):
    key = "{ id:'" + lid + "', "
    i = c.find(key)
    assert i >= 0, 'les niet gevonden: ' + lid
    assert c.find(key, i + 1) < 0, 'les dubbel: ' + lid
    return i, c.index('\n', i)

def _array_end(s, start):
    # einde van een JSON-array die op s[start] == '[' begint (houdt rekening met strings en geneste arrays)
    depth, i, instr = 0, start, False
    while True:
        ch = s[i]
        if instr:
            if ch == '\\': i += 1
            elif ch == '"': instr = False
        elif ch == '"': instr = True
        elif ch == '[': depth += 1
        elif ch == ']':
            depth -= 1
            if depth == 0: return i + 1
        i += 1

def fmt(item):
    return json.dumps(item, ensure_ascii=False, separators=(', ', ': '))

def replace_sentences(changes, path=PATH):
    c = open(path, encoding='utf-8').read()
    done = skipped = 0
    for lid, old, new, reason in changes:
        assert 3 <= len(new) <= 4 and all(isinstance(x, str) for x in new[:3]), (lid, new)
        a, b = _lesson_span(c, lid)
        line = c[a:b]
        new_lit = fmt(new)
        if ('[' + json.dumps(new[0], ensure_ascii=False) + ',') in line and ('[' + json.dumps(old, ensure_ascii=False) + ',') not in line:
            skipped += 1
            continue
        k = line.find('[' + json.dumps(old, ensure_ascii=False) + ',')
        assert k >= 0, 'zin niet gevonden in ' + lid + ': ' + old
        e = _array_end(line, k)
        line = line[:k] + new_lit + line[e:]
        c = c[:a] + line + c[b:]
        done += 1
    open(path, 'w', encoding='utf-8').write(c)
    print(done, 'zinnen vervangen,', skipped, 'stonden er al')

def replace_text(old, new, path=PATH):
    # kleine tekstfix (bv. in een intro); idempotent
    c = open(path, encoding='utf-8').read()
    if new in c and old not in c:
        return
    assert c.count(old) == 1, 'tekst niet (eenmalig) gevonden: ' + old[:60]
    open(path, 'w', encoding='utf-8').write(c.replace(old, new))
