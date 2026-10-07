# Pico Spaans — instructies voor Claude

Pico is Sasha's zelfgebouwde Spaans-leer-app (Duolingo-achtig), bedoeld om later ook aan anderen te geven.
Communiceer met Sasha in **informeel Nederlands**. Beantwoord eerst eventuele vragen en bouw daarna.
Ga zuinig om met usage: bij grote klussen eerst de omvang schatten en kort voorleggen.

## Hoe het in elkaar zit
- **`index.html`** (~5 MB) is de hele app: code + alle lessen (`CURRICULUM` A1–B2) + plaatjes (base64). Er is geen build-stap.
- **`sw.js`**: network-first service worker, dus na een push krijgen gebruikers meteen de nieuwe versie. Er is geen cache-bump nodig.
- **Hosting**: Cloudflare Worker `pico-spaans` deployt automatisch vanaf `main` van GitHub `sashadh033-svg/pico-spaans`. Een push naar main gaat binnen een paar minuten live.
- **AI-features** (AI Chat, "Leg uit", "Mijn antwoord is ook goed") lopen via Cloudflare Worker-proxy `fancy-surf-0c04`.
- **D1-database** `pico-spaans-db` (id 2113ba3c-1467-42cd-98f9-951890311648) is **leeg en wordt niet meer gebruikt**. Een les in D1 zou de les in index.html overschrijven. Afspraak: alles staat in GitHub, D1 blijft leeg.
- **`dev/`**: testjes, scripts en `dev/LEESMIJ.md` (technische overdracht met alle recente wijzigingen). Lees die eerst.

## Belangrijke structuren in index.html
- `CURRICULUM[L]` → units `{id, icon, colors, title, fase, lessons}` → lessons `{id, kind:'new'|'review', intro?, words:[[es,nl,en]], sentences:[[es,nl,en,(alts[])]]}`.
- Lessen worden per unit herverdeeld in "bolletjes" (`buildNodeGroups`). Een `intro` (HTML) toont Pico vóór het eerste bolletje van die les.
- Per unit (allemaal optioneel): `UNIT_ASSETS`, `VERB_PRACTICE` (🏋️), `GUIDES` (📖), `GUIDE_MORE`, `STORIES`, `TRAINER_NODES` (bolletje "lastige keuzes" met `CHOICE_POOL`/`CHOICE_BADGE`/`TRAINER_LABEL`).
- Nakijken: `checkAnswer()`, `normalize`/`normalizeLenient`, `answerVariants`, `isTypo` (oranje = bijna goed, telt mee).
- **Een unit tussenvoegen?** Geef hem `addedLater: true`. Anders gaat de voortgang op slot voor gebruikers die er al voorbij zijn (`skippableLater`). Voeg **nooit** nieuwe bolletjes of trainers toe aan bestaande units, om dezelfde reden.

## Werkwijze
1. `git pull`, en lees `dev/LEESMIJ.md`.
2. Grote/herhaalbare inhoudswijzigingen doe je via een idempotent Python-script in `dev/` (zie de voorbeelden daar). Kleine fixes bewerk je direct met Python-replace. Het bestand is te groot voor gewone editors.
3. Test met Playwright (Chromium). De tests verwijzen naar `/home/claude/spaans-leren.html`, dus kopieer ze en vervang dat pad door het pad van `index.html`. Altijd draaien:
   - `test_prog.js` (moet voor A1–B2 `problems: []` geven)
   - de testjes die bij je wijziging horen (`test_typo`, `test_marks`, `test_review`, `test_build`, `test_alts`, `test_you`, `test_gender`)
4. Commit (auteur `Sasha <sasha99@live.nl>`) en push naar `main`. Vertel Sasha kort wat er veranderd is.

## Inhoudelijke afspraken
- Volgorde van grammatica zoals Instituto Cervantes. A1: presente, estar + gerundio (unit `a1-u17p`), ir a, pretérito perfecto. A2: indefinido/imperfecto, por/para, lo/le enz.
- Geen grammatica in zinnen die nog niet behandeld is (bv. "se ha roto" hoort niet in A1).
- Alternatieve goede antwoorden zet je als 4e element (alts) bij de zin.
- Oranje (telt als goed): vergeten accenten of ¿¡, tikfouten, een spatie vergeten. Hoofdletters/punten/komma's tellen niet.
- Toon van uitlegkaartjes: kort, Nederlands, met 2–3 voorbeeldzinnen.

## Open ideeën / mogelijke volgende stappen
- Gedaan (okt 2026): B1/B2-uitleg in thema-units, verhaaltje a1-u17p, A1–B2 nagelopen op te vroege grammatica (zinnen én verhaaltjes), geleerde vormen laten terugkomen door de hele cursus, plaatjes naar `img/`, voornaamwoorden (spiekbriefje, Kluis-knop, meer oefenzinnen). Zie `dev/LEESMIJ.md`.
- Bij nieuwe inhoud: houd de volgorde aan (zie LEESMIJ) en laat geleerde vormen terugkomen; vervang zinnen in plaats van toevoegen.
- A2 is in okt 2026 lichter gemaakt (982 i.p.v. 1.386 woorden). De zware versie is bewaard op branch `archief/a2-zware-versie`; gebruik die als bron als Sasha de extra woorden/zinnen later terug wil (bv. in B1 of als extra oefenstof).
- Mogelijk: nieuwe personages/achtergronden in `img/` voor A2 en verder (nu alleen A1).
