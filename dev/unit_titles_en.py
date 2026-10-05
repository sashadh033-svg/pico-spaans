# Engelse unit-titels voor A1/A2 (stonden er als kopie van de Nederlandse titel).
# Gebruik: python3 dev/unit_titles_en.py   (idempotent)
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, 'index.html')

EN = {
    'a1-u1': 'Greetings, goodbyes & introducing yourself',
    'a1-u2': 'Articles & gender (el/la)',
    'a1-u3': 'Origin & nationalities',
    'a1-u4': 'Jobs & work',
    'a1-u5': 'Numbers (1-30) & age',
    'a1-u6': 'Family & relationships',
    'a1-u7': 'Possessives (mi, tu, su)',
    'a1-u8': 'Describing people & personality',
    'a1-u9': 'Weather & seasons',
    'a1-u10': 'Food & drink: basics & groceries',
    'a1-u11': 'In town & asking for directions',
    'a1-u12': 'Ser vs. Estar',
    'a1-u13': 'Home & furniture',
    'a1-u14': 'Time & telling the time',
    'a1-u15': 'Days, months & dates',
    'a1-u16': 'Daily habits (reflexive verbs)',
    'a1-u17': "Free time, hobbies & sport",
    'a1-u17p': 'What are you doing? (estar + gerundio)',
    'a1-u18': 'Shopping, clothes & sizes',
    'a1-u19': 'At the restaurant & ordering',
    'a1-u20': 'Travel & transport',
    'a1-u21': 'Body & health',
    'a1-u22': 'Making plans & the future (ir a + infinitive)',
    'a1-u23': 'Intro to the past (pretérito perfecto)',
    'a2-u1': 'My morning routine',
    'a2-u2': 'My evening routine',
    'a2-u4': 'Making appointments',
    'a2-u5': 'Weather & seasons',
    'a2-u6': 'Sports & activities',
    'a2-u7': 'Asking the way',
    'a2-u8': 'Public transport',
    'a2-u9': 'In town',
    'a2-u10': 'Por vs. Para',
    'a2-u11': 'Booking a holiday',
    'a2-u12': 'Travel & luggage',
    'a2-u13': 'Discovering new places',
    'a2-u14': 'Comparisons (más...que, tan...como)',
    'a2-u15': 'Buying clothes',
    'a2-u16': 'Direct/indirect pronouns (lo, la, le)',
    'a2-u17': 'At the supermarket',
    'a2-u18': 'At the market',
    'a2-u19': 'At the restaurant',
    'a2-u20': 'Paying the bill',
    'a2-u21': 'Services & shops',
    'a2-u22': 'My home & rooms',
    'a2-u23': 'Furniture & decor',
    'a2-u24': 'Household chores',
    'a2-u25': 'Parts of the body',
    'a2-u26': 'Health & pain',
    'a2-u27': 'At the doctor',
    'a2-u28': 'My recent experiences',
    'a2-u29': 'Irregular past participles',
    'a2-u30': 'Today & this week',
    'a2-u31': 'Achievements & successes',
    'a2-u32': 'My childhood',
    'a2-u33': 'Then vs. now',
    'a2-u34': 'Biographies',
    'a2-u35': 'Important events',
    'a2-u36': 'Pretérito Indefinido vs. Imperfecto',
}

def main():
    c = open(PATH, encoding='utf-8').read()
    n = 0
    for uid, en in EN.items():
        m = re.search(r"id:'" + re.escape(uid) + r"', icon:[^\n]*\n\s*title: \{ nl:'((?:[^'\\]|\\.)*)', en:'((?:[^'\\]|\\.)*)' \}", c)
        assert m, uid
        lit = en.replace("'", "\\'")
        if m.group(2) == lit:
            continue
        c = c[:m.start(2)] + lit + c[m.end(2):]
        n += 1
    open(PATH, 'w', encoding='utf-8').write(c)
    print(n, 'titels vertaald')

if __name__ == '__main__':
    main()
