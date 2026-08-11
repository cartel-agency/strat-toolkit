# Root Scout: korte handleiding

## Wat is Root Scout?

Root Scout is een agent die **volledig automatisch** in de cloud draait. Elke werkdag speurt hij het web
af naar verse, inspirerende campagnes per klant. Elke maandag kiest hij daaruit de sterkste tegen het
merkplatform van die klant en mailt hij een gestyled rapport naar het strategieteam. Niemand hoeft iets
te installeren; je ontvangt gewoon het wekelijkse rapport.

Alles wat per klant instelbaar is, leeft in **Notion → Scout Config**: één rij per klant, met de
keywords, de rationale, de landen en de ontvangers. De code hoef je daar niet voor aan te raken.

## Een nieuwe klant toevoegen met de setup-skill

1. Zorg dat de **Notion-connector** aanstaat en dat je bij de Scout Config-database kunt.
2. Start de skill **root-scout-setup** (typ `/` of klik **+** in een gesprek en kies ze).
3. Beantwoord de vragen. De skill vraagt naar: klantnaam, sector, merkplatform, rationale (wat een
   campagne wél en niet relevant maakt), keywords, landen en de ontvangers (e-mailadressen).
4. De skill vat samen en vraagt bevestiging. Klopt het? Dan zet hij de klant als één rij in Scout Config
   en vinkt hem op **Actief**.
5. Zit de klant **buiten food/retail**? Dan waarschuwt de skill dat de gedeelde zoekbronnen in de code
   (`config.yaml`) nog food/retail-gericht zijn en door Tomas bijgesteld moeten worden voor die sector.
   De klant-eigen keywords werken wel al.

## Hoe het daarna loopt

- De klant draait mee vanaf de eerstvolgende run: **scout** elke dag ~06:00, **rapport** elke maandag
  ~09:00 (Belgische tijd).
- Meteen testen? Ga in GitHub naar **Actions → Root Scout → Run workflow**, eerst **scout**, dan
  **strategist**.
- Het rapport gaat in fase 1 **eerst intern** ter review; pas bij bewezen kwaliteit richting de klant.

## Iets aanpassen achteraf

Rechtstreeks in de rij in **Scout Config**, zonder skill en zonder code:

| Ik wil… | Waar |
|---|---|
| keywords toevoegen | kolom **Keywords** (één per regel) |
| de rationale/criteria bijstellen | kolom **Rationale** |
| een land toevoegen | kolom **Landen** (enkel Belgie, Nederland, Frankrijk, Duitsland, Italie) |
| wie het rapport ontvangt | kolom **Ontvangers** (één adres per regel) |
| de scout pauzeren | vink **Actief** uit |
| goedkoper draaien | kolom **Model** = `claude-haiku-4-5-20251001` |

De zoekbronnen zelf (globale zoekopdrachten en vakpers-feeds) en de rapport-opmaak zitten in de code
(`config/config.yaml` en `src/report_template.py`). Die aanpassen loopt via GitHub Desktop.

## Rationale en Voedingsbodem: twee velden, twee rollen

Dit is het meest gemaakte misverstand, dus lees het één keer goed. Op de klantpagina staan twee plekken
met merkcontext, en ze worden **niet door dezelfde agent gelezen**.

| | Waar | Wie leest het | Wanneer |
|---|---|---|---|
| **Rationale** | de kolom Rationale in de rij | de scout **én** de strategist | elke dag bij het filteren, en elke maandag bij het schrijven |
| **Voedingsbodem** | de tekst op de klantpagina zelf | **alleen** de strategist | enkel maandag, bij het schrijven van het rapport |

De gevolgen daarvan:

- **De dagelijkse filter ziet alleen de Rationale.** Elke dag beoordeelt de agent tientallen artikels op
  basis van dat ene veld. Zet je merkcontext uitsluitend in de voedingsbodem, dan stuurt die dus niet
  wat er binnenkomt, en filter je op een half beeld.
- **Zet in de Rationale wat een artikel wél en niet relevant maakt.** Concreet en afbakenend: waar ligt
  het zwaartepunt, wat mag erbij als aanvulling, en wat valt altijd af.
- **Zet in de Voedingsbodem wat nodig is om een goede insteek te schrijven.** De merkemoties, het
  onderscheidende, wat de klant juist niet doet, en waar het merk nu mee bezig is.

## Houd de voedingsbodem kort

Hoe meer tekst, hoe moeilijker het voor de agent wordt om gericht te kiezen. Dat is geen bezuiniging
maar een kwaliteitsregel: een lang merkdocument verdunt de aandacht over veel context die niet helpt om
te oordelen.

**Vuistregel:** zet in de voedingsbodem wat je een nieuwe collega zou vertellen vlak voor hij vijftig
artikels moet doornemen. Niet meer. Voor BelOrta is dat ongeveer 400 woorden.

Wat er wél in hoort:

- De doelen achter elke campagne, in één of twee zinnen
- De spanning of het probleem waar het merk op speelt
- De merkemoties of criteria waarop je een case beoordeelt
- Wat het merk onderscheidt en geloofwaardig maakt
- Het concurrentieveld, en vooral: **wat de klant bewust niét doet**. Dat is het bruikbaarste
  afwijssignaal dat je de agent kan geven
- Distinctive assets
- Wat er nu loopt, en wat de klant gevraagd heeft

Wat eruit mag:

- De geschiedenis van vorige merkplatformen. Eén zin volstaat
- Interne wervingstekst over medewerkers, partners en trots
- Uitrolplannen, mediaschema's en productiedetails
- Passages die een eerder punt herhalen in andere woorden

Het volledige merkdocument mag gerust bestaan, maar bewaar het ergens anders.

> **Let op:** zet merkmateriaal niet op een **subpagina** van de klantpagina. De agent leest alleen de
> tekst op de klantpagina zelf; subpagina's worden overgeslagen, en niets waarschuwt je daarvoor.
