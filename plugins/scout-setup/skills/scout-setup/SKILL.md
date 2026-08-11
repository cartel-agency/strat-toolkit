---
name: scout-setup
description: >
  Voeg een nieuwe klant toe aan Root Scout (de wekelijkse inspiratie-agent) door de gebruiker te
  interviewen en op basis daarvan één rij in de Notion-database Scout Config aan te maken: klantnaam,
  merkplatform, rationale, keywords, landen en ontvangers. Gebruik dit wanneer iemand een nieuwe scout
  voor een klant wil opzetten, of de instellingen van een bestaande klant wil herzien. De agent schrijft
  zelf niets naar de code; hij vult enkel Notion in en signaleert wanneer de zoekbronnen (config.yaml)
  bijgesteld moeten worden voor een klant buiten de food/retail-sector.
versie: v1 · schrijft naar Scout Config in Notion · geen codewijzigingen
---

# Root Scout: setup nieuwe klant

Je helpt een strateeg of beheerder om een **nieuwe klant** toe te voegen aan **Root Scout**, de agent
die elke week per klant inspiratiecampagnes verzamelt en als rapport mailt. Je doet dat door te
**interviewen** en daarna **één rij** aan te maken in de Notion-database **Scout Config**. Meer is niet
nodig: Root Scout draait met één gedeelde Scout Inbox en één gedeeld Archief die op de kolom `Klant`
filteren, dus je hoeft geen databases aan te maken.

- **Scout Config-database:** https://app.notion.com/p/1fca38368720425ca86a2be8cd92b0d0
- **Data source (voor create-pages):** `collection://59a5eb43-db30-44c1-b390-e5ba92ea5fd1`

## Vooraf

Zet de **Notion-connector** aan en zorg dat de Scout Config-database gedeeld is. Kun je de database niet
bereiken? Meld dat en stop; verzin geen rij die je niet echt kunt wegschrijven.

---

## 1. Het interview

Vraag **één onderwerp per keer**, in gewone taal, en vat na elk antwoord kort samen. Overval de persoon
niet met de hele lijst ineens. Verzin niets: is een antwoord onduidelijk, vraag door.

Verzamel deze velden:

1. **Klant**: de naam van de klant (wordt de titel van de rij).
2. **Sector**: in welke sector zit de klant? (Dit heb je nodig voor de bronnen-check in §3.)
3. **Merkplatform**: waar het merk voor staat, in enkele woorden of één zin. *Voorbeeld (BelOrta):
   "Verbonden door Smaak".*
4. **Rationale**: het belangrijkste veld. Wat maakt een campagne **relevant** voor deze klant, en wat
   **niet**? Help de persoon dit scherp te krijgen. Een goede rationale bevat:
   - waar het merk voor staat en welke emotionele of strategische kern het heeft;
   - **KERN:** de thema's waar het zwaartepunt hoort te liggen;
   - **OOK RELEVANT:** wat erbij mag als aanvulling, met de voorwaarde erbij. Schrijf hier nooit dat
     iets "uitdrukkelijk relevant" is zonder afbakening, en vermijd een slotzin als "liever een sterke
     internationale case dan niets". Zulke zinnen verbreden het net zo ver dat één soort case het
     rapport gaat overheersen;
   - **NIET relevant:** wat eruit moet (bv. pure prijsacties, bedrijfsnieuws, overnames, personeelsnieuws,
     media- en bureaunieuws, productlanceringen zonder campagne-idee, content zonder creatieve of
     strategische inhoud).

   Gebruik de BelOrta-rationale als model voor de vorm, niet voor de inhoud.

   **Belangrijk om te weten en door te geven:** dit veld is het enige dat de **dagelijkse filter** ziet.
   Elke dag beoordeelt de scout tientallen artikels op basis van de Rationale alleen. De voedingsbodem
   op de klantpagina (zie hieronder) wordt daar niet gelezen. Merkcontext die alleen daar staat, stuurt
   dus niet wat er binnenkomt.
5. **Keywords**: zoektermen, **één per regel**. Leid ze samen met de persoon af uit de sector, de
   concurrenten en de internationale spelers in die sector. Denk aan: het type campagnes, de sector, de
   naaste concurrenten, en bredere thema's. Stel een lijst voor en laat de persoon bijsturen.
6. **Landen**: kies uit exact deze opties: **Belgie, Nederland, Frankrijk, Duitsland, Italie**.
   (Alleen deze; andere landen kunnen niet zonder de code aan te passen.)
7. **Ontvangers**: e-mailadressen, **één per regel**. Begin **intern** (het rapport gaat in fase 1
   eerst langs strategie ter review, pas bij bewezen kwaliteit naar de klant).
8. **Model**: laat leeg voor de standaard (Claude Sonnet), of kies `claude-haiku-4-5-20251001` om
   goedkoper te draaien. Bij twijfel: leeg laten.
9. **Voedingsbodem**: optioneel, en bewust kort. Dit is de tekst op de klantpagina zelf, onder het
   kopje Voedingsbodem. Alleen de **wekelijkse strategist** leest dit mee, bij het schrijven van de
   insteken. Vraag ernaar, maar waarschuw voor de valkuil: hoe meer tekst, hoe moeilijker het voor de
   agent wordt om gericht te kiezen. Een lang merkdocument verdunt de aandacht over context die niet
   helpt om te oordelen.

   **Vuistregel:** wat je een nieuwe collega zou vertellen vlak voor hij vijftig artikels moet
   doornemen. Richtlijn ongeveer 400 woorden.

   Wel erin: de doelen achter elke campagne, de spanning waar het merk op speelt, de emoties of criteria
   waarop je een case beoordeelt, wat het merk onderscheidt, het concurrentieveld en vooral **wat de
   klant bewust niét doet** (dat is het bruikbaarste afwijssignaal), distinctive assets, en wat er nu
   loopt of gevraagd is.

   Eruit: de geschiedenis van vorige merkplatformen (één zin volstaat), interne wervingstekst over
   medewerkers en partners, uitrolplannen en mediaschema's, en passages die een eerder punt herhalen.

   Zet merkmateriaal **niet op een subpagina** van de klantpagina. De agent leest alleen de tekst op de
   klantpagina zelf; subpagina's worden overgeslagen en niets waarschuwt daarvoor.

---

## 2. Toon de samenvatting en vraag bevestiging

Vat alle velden overzichtelijk samen en vraag: *"Klopt dit? Dan zet ik de klant in Scout Config."*
Wacht op akkoord vóór je schrijft.

---

## 3. Bronnen-check (de kanttekening), vóór je bevestigt

Root Scout heeft een **gedeelde, food/retail-gerichte zoekbasis** in `config.yaml` (de globale
`zoekopdrachten` en de RSS-`feeds`). De klant-eigen keywords en rationale werken voor elke sector, maar
die brede basis en de vakpers-feeds zijn op food/retail afgestemd.

- **Klant in food of retail?** Alles werkt meteen, niets extra nodig.
- **Klant in een andere sector** (bv. bank, mode, energie, tech)? Meld dit **expliciet**:
  > "Deze klant zit buiten food/retail. De klant-eigen keywords werken, maar de gedeelde zoekbronnen en
  > vakpers-feeds in `config.yaml` zijn nog food/retail-gericht. Voor scherpe resultaten laat je Tomas
  > die bronnen bijstellen naar deze sector. Dat is een code-aanpassing (config.yaml aanpassen en pushen
  > via GitHub Desktop), geen Notion-stap."
  Bied aan om alvast een setje **sector-passende keywords en zoekopdrachten** voor te stellen die Tomas
  in `config.yaml` kan overnemen. Schrijf die zelf **niet** naar de code.

---

## 4. Schrijf de rij naar Scout Config

Na akkoord, maak één pagina aan in de data source `collection://59a5eb43-db30-44c1-b390-e5ba92ea5fd1`
met de verzamelde waarden:

- **Klant** (titel)
- **Merkplatform** (tekst)
- **Rationale** (tekst)
- **Keywords** (tekst, één term per regel)
- **Landen** (multi-select, enkel uit: Belgie, Nederland, Frankrijk, Duitsland, Italie)
- **Ontvangers** (tekst, één adres per regel)
- **Model** (select: leeg, `claude-sonnet-5` of `claude-haiku-4-5-20251001`)
- **Actief** (checkbox): zet op **aan** zodra de rij volledig is. Twijfel je of iets nog ontbreekt, laat
  Actief dan uit en zeg dat de klant nog niet meedraait tot hij aangevinkt wordt.

Optioneel: als er een klantfiche-pagina bestaat in de Klanten-database, koppel die via het veld
**Klantfiche** zodat Root Scout ze als extra bronmateriaal meeleest.

---

## 5. Bevestig en leg uit hoe het verder loopt

Sluit af met een korte bevestiging:

- De klant staat nu in Scout Config en draait mee vanaf de eerstvolgende geplande run (scout elke dag
  ~06:00, rapport elke maandag ~09:00 Belgische tijd).
- Wil je meteen testen zonder tot maandag te wachten: draai in GitHub, tabblad **Actions** →
  **Root Scout** → **Run workflow**, eerst **scout** (vult de inbox), daarna **strategist** (maakt het
  rapport).
- Het rapport gaat in fase 1 **eerst intern**; pas bij bewezen kwaliteit richting de klant.
- Later iets aanpassen (keywords, ontvangers, rationale, pauzeren)? Dat kan rechtstreeks in de rij in
  Scout Config, zonder deze skill en zonder code.

---

## Vangrails

- **Verzin geen inhoud.** Keywords, rationale en ontvangers komen van de persoon of worden samen
  opgesteld en bevestigd. Bij twijfel: doorvragen.
- **Schrijf nooit naar de code.** Deze skill vult enkel Notion in. Bronnen of zoekopdrachten in
  `config.yaml` aanpassen is werk voor Tomas, via GitHub Desktop.
- **Landen enkel uit de vaste lijst.** Een land dat er niet in staat, vereist een codewijziging; meld
  dat in plaats van het stil te laten vallen.
- **Actief pas aan als de rij compleet is.** Een halve rij die al meedraait, levert een zwak of leeg
  rapport op.
- **Kan je niet naar Notion schrijven?** Meld het expliciet en schrijf niets; verzin geen rij.
