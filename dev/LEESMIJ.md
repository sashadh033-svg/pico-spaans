# Pico Spaans – overdracht
- index.html = app (v25). Hosting: Cloudflare Worker pico-spaans gekoppeld aan GitHub repo sashadh033-svg/pico-spaans (bestanden in root).
- AI-proxy + D1: worker fancy-surf-0c04, D1 database pico-spaans-db (id 2113ba3c-1467-42cd-98f9-951890311648). D1 bevat ALLEEN tekstverbeteringen (tabellen units/lessons); de app legt lessen uit D1 over de ingebouwde lessen (zelfde les-id). Lege D1 = ingebouwde tekst.
- Tekstfix live zetten zonder upload: les in index.html aanpassen én die les via push_lesson.py als SQL in D1 zetten.
- Tests: test_prog.js (pad/toetsen), test_checker.js LEVEL, test_stories_lv.js LEVEL, test_click.js, test_typo.js, test_you.js, test_build.js, test_gender.js, test_marks.js (oranje bij vergeten accenten/¿¡).
- A1/A2-grammatica-uitleg vóór bolletjes: dev/a1_intros.py en dev/a2_intros.py (teksten aanpassen en opnieuw draaien voegt alleen ontbrekende toe).
