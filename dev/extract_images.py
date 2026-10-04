# Haalt de plaatjes (base64 PNG's en SVG-achtergronden) uit index.html en zet ze
# als losse bestanden in img/. In index.html komt dan een relatief pad te staan.
# Gebruik: python3 dev/extract_images.py   (idempotent)
import base64, hashlib, os, re, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, 'index.html')

def slug(s):
    s = s.lower()
    m = re.search(r'\((a\d|b\d|c\d)\.(\d)\)', s)  # 'De Eerste Ontmoeting (A1.1)' -> fase-a1-1
    if m:
        return 'fase-' + m.group(1) + '-' + m.group(2)
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

def write(rel, data):
    full = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    if os.path.exists(full) and open(full, 'rb').read() != data:
        raise SystemExit('bestaat al met andere inhoud: ' + rel)
    open(full, 'wb').write(data)

c = open(PATH, encoding='utf-8').read()
n = 0

# 1. Het voorbeeld-personage in het commentaarblok (wordt niet gebruikt, wel bewaard).
def ex_png(m):
    global n
    write('img/characters/voorbeeld.png', base64.b64decode(m.group(1)))
    n += 1
    return "character: 'img/characters/voorbeeld.png'"
c = re.sub(r"character: 'data:image/png;base64,([A-Za-z0-9+/=]+)'", ex_png, c, count=1)
c = c.replace("Voorbeeld zodra je een ontwerp hebt:\n     'De Eerste Ontmoeting (A1.1)': { background: 'assets/fases/a1-fase1-bg.jpg', character: 'img/characters/voorbeeld.png'",
              "Voorbeeld zodra je een ontwerp hebt:\n     'De Eerste Ontmoeting (A1.1)': { background: 'img/backgrounds/fase-a1-1.svg', character: 'img/characters/voorbeeld.png'")
c = c.replace('in een map "assets/fases/"\n   (of "assets/units/" voor de losse uitzonderingen)',
              'in de map "img/" (img/backgrounds/ en\n   img/characters/)')

# 2. Achtergronden (SVG) en personages (PNG) in FASE_ASSETS / UNIT_ASSETS.
start = c.index('const FASE_ASSETS =')
end = c.index('function getUnitAsset(')
block = c[start:end]
out = []
for line in block.split('\n'):
    km = re.match(r"\s*'([^']+)':", line)
    if km:
        key = slug(km.group(1))
        def svg(m):
            global n
            write('img/backgrounds/' + key + '.svg', urllib.parse.unquote(m.group(1)).encode('utf-8'))
            n += 1
            return "background: 'img/backgrounds/" + key + ".svg'"
        line = re.sub(r"background: 'data:image/svg\+xml,([^']+)'", svg, line)
        def png(m):
            global n
            data = base64.b64decode(m.group(1))
            name = 'lucia' if 'characterLayered: \'lucia\'' in line else key
            write('img/characters/' + name + '.png', data)
            n += 1
            return "character: 'img/characters/" + name + ".png'"
        line = re.sub(r"character: 'data:image/png;base64,([A-Za-z0-9+/=]+)'", png, line)
    out.append(line)
c = c[:start] + '\n'.join(out) + c[end:]

assert 'base64,' not in c[start - 3000:c.index('function getUnitAsset(')], 'nog base64 over'
open(PATH, 'w', encoding='utf-8').write(c)
print('plaatjes verplaatst:', n)
