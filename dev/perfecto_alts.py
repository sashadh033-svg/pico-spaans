# Zinnen met pretérito perfecto waarvan de Engelse vertaling in de gewone verleden tijd staat.
# - Vóór A2 unit 6 (nog geen indefinido): Engels in de voltooide tijd, zodat het niet uitlokt dat je "he" weglaat.
# - Daarna: de indefinido-versie telt ook als goed (alts), want beide zijn correct Spaans.
# Gebruik: python3 dev/perfecto_alts.py   (idempotent)
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sentence_tools import _array_end, fmt, PATH

EN = {
    'Hoy me he quedado dormido.': "I've overslept today.",
    'Hoy he cancelado la cena con mis amigos.': "I've cancelled dinner with my friends today.",
    'Hoy he quedado con mi prima.': "I've met up with my cousin today.",
    'Perdona, he olvidado la cita.': "Sorry, I've forgotten the appointment.",
    'Mis padres han vuelto de viaje.': 'My parents have come back from their trip.',
}
ALTS = {
    'El examen no ha sido tan difícil como el otro.': ['El examen no fue tan difícil como el otro.'],
    'Hoy he llegado más tarde que ayer.': ['Hoy llegué más tarde que ayer.'],
    'Mi amigo se ha equivocado, pero lo perdono.': ['Mi amigo se equivocó, pero lo perdono.'],
    'Me he puesto enfermo en las vacaciones.': ['Me puse enfermo en las vacaciones.'],
    'Hace unos días he visto a tu hermano.': ['Hace unos días vi a tu hermano.'],
    'Hace unos minutos he hablado con Ana.': ['Hace unos minutos hablé con Ana.'],
    'Mis padres han vuelto de viaje.': ['Mis padres volvieron de viaje.'],
    'Su abuelo ha muerto este año.': ['Su abuelo murió este año.'],
    'A la hora de comer le he mandado un mensaje a mi madre.': ['A la hora de comer le mandé un mensaje a mi madre.'],
    'Al amanecer he salido a correr.': ['Al amanecer salí a correr.'],
    'Al anochecer hemos vuelto a casa.': ['Al anochecer volvimos a casa.'],
    'Al final no hemos salido.': ['Al final no salimos.'],
    'Antes he pasado por el banco.': ['Antes pasé por el banco.'],
    'Este lunes he empezado un curso.': ['Este lunes empecé un curso.'],
    'Hace poco he hablado con él.': ['Hace poco hablé con él.'],
    'Hace un momento ha llamado Laura.': ['Hace un momento llamó Laura.'],
    'He llegado justo a tiempo.': ['Llegué justo a tiempo.'],
    '¿Habéis ganado el partido?': ['¿Ganasteis el partido?'],
    'Me han dado una beca para estudiar en Chile.': ['Me dieron una beca para estudiar en Chile.'],
    'He descargado una aplicación nueva para estudiar español.': ['Descargué una aplicación nueva para estudiar español.'],
    'He olvidado mi contraseña otra vez.': ['Olvidé mi contraseña otra vez.'],
    'A lo mejor tienes razón y me he equivocado.': ['A lo mejor tienes razón y me equivoqué.'],
    '¡Adivina quién me ha llamado!': ['¡Adivina quién me llamó!'],
    'Perdona, no te he entendido. ¿Me lo puedes repetir?': ['Perdona, no te entendí. ¿Me lo puedes repetir?'],
    '¡Qué collar tan bonito! ¿Quién te lo ha dado?': ['¡Qué collar tan bonito! ¿Quién te lo dio?'],
    'Mi cuñada se ha quedado embarazada.': ['Mi cuñada se quedó embarazada.', 'Mi cuñada está embarazada.'],
    '¡Qué cara tiene! Se ha comido mi bocadillo sin preguntar.': ['¡Qué cara tiene! Se comió mi bocadillo sin preguntar.'],
    'Hoy me he dado un capricho: unos zapatos preciosos.': ['Hoy me di un capricho: unos zapatos preciosos.'],
    '¿Para eso me has llamado?': ['¿Para eso me llamaste?'],
    '¿Qué nota has sacado en el examen?': ['¿Qué nota sacaste en el examen?'],
    'Tranquila, lo peor ya ha pasado.': ['Tranquila, lo peor ya pasó.'],
    'Tienes mala cara, ¿has dormido bien?': ['Tienes mala cara, ¿dormiste bien?'],
    'Ha llovido todo el fin de semana, pero al mal tiempo, buena cara.': ['Llovió todo el fin de semana, pero al mal tiempo, buena cara.'],
}

def main():
    c = open(PATH, encoding='utf-8').read()
    lo, hi = c.index('const CURRICULUM'), c.index('const STORY_CHARACTERS')
    changed = 0
    for es in sorted(set(EN) | set(ALTS)):
        key = '[' + json.dumps(es, ensure_ascii=False) + ', "'
        pos, found = lo, 0
        while True:
            k = c.find(key, pos, hi)
            if k < 0:
                break
            e = _array_end(c, k)
            item = json.loads(c[k:e])
            found += 1
            if es in EN:
                item[2] = EN[es]
            if es in ALTS:
                if len(item) < 4:
                    item.append([])
                for a in ALTS[es]:
                    if a not in item[3]:
                        item[3].append(a)
            new = fmt(item)
            if new != c[k:e]:
                c = c[:k] + new + c[e:]
                hi += len(new) - (e - k)
                changed += 1
            pos = k + len(new)
        assert found, 'zin niet gevonden: ' + es
    open(PATH, 'w', encoding='utf-8').write(c)
    print(changed, 'zinnen bijgewerkt')

if __name__ == '__main__':
    main()
