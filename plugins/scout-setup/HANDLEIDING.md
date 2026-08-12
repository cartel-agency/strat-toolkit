# Root Scout: korte handleiding

## Wat is Root Scout?

Root Scout is een agent die **volledig automatisch** in de cloud draait. Elke dag speurt hij het web
af naar verse, inspirerende campagnes per klant. Elke maandag kiest hij daaruit de sterkste tegen het
merkplatform van die klant en mailt hij een gestyled rapport naar het strategieteam. Niemand hoeft iets
te installeren; je ontvangt gewoon het wekelijkse rapport.

Alles wat per klant instelbaar is, leeft in **Notion → Scout Config**: één rij per klant, met de
keywords, de rationale en de ontvangers. De code hoef je daar niet voor aan te raken. Een wijziging is
dezelfde avond al actief: de scout leest de rij bij elke run opnieuw uit Notion, er hoeft niets gepusht
te worden.

## Een nieuwe klant toevoegen met de setup-skill

1. Zorg dat de **Notion-connector** aanstaat en dat je bij de Scout Config-database kunt.
2. Start de skill **scout-setup** (typ `/` of klik **+** in een gesprek en kies ze).
3. Beantwoord de vragen. De skill vraagt naar: klantnaam, sector, merkplatform, rationale (wat een
   campagne wél en niet relevant maakt), wat een goed **marktsignaal** is, keywords, de ontvangers
   (e-mailadressen) en optioneel een korte voedingsbodem.
4. De skill vat samen en vraagt bevestiging. Klopt het? Dan zet hij de klant als één rij in Scout Config
   en vinkt hem op **Actief**.
5. Zit de klant **buiten food/retail**? Dan waarschuwt de skill dat de gedeelde zoekbronnen in de code
   (`config.yaml`) nog food/retail-gericht zijn en door Tomas bijgesteld moeten worden voor die sector.
   De klant-eigen keywords werken wel al.

## Hoe het daarna loopt

- De klant draait mee vanaf de eerstvolgende run: **scout** elke dag rond **17:20**, **rapport** elke
  maandag rond **08:47** (Belgische tijd).
- **De vakpersrondes draaien alleen op woensdag en zondag.** Op de andere dagen loopt enkel de brede
  oogst. Dat is een creditkeuze, geen fout: zondag is de dragende dag voor het maandagrapport, woensdag
  is het vangnet.
- Meteen testen? Ga in GitHub naar **Actions → Root Scout → Run workflow**. Kies **scout-vakpers** voor
  een volledige oogst (dat wil je bij een eerste test, want gewone `scout` slaat op de meeste dagen de
  vakpers over), en daarna **strategist** voor het rapport.
- Het rapport gaat in fase 1 **eerst intern** ter review; pas bij bewezen kwaliteit richting de klant.

## Iets aanpassen achteraf

Rechtstreeks in de rij in **Scout Config**, zonder skill en zonder code:

| Ik wil… | Waar |
|---|---|
| keywords toevoegen | kolom **Keywords** (één per regel, **geen komma's binnen een term**) |
| de rationale/criteria bijstellen | kolom **Rationale** |
| bijsturen wat een signaal is | kolom **Rationale**, onder het kopje SIGNALEN |
| wie het rapport ontvangt | kolom **Ontvangers** (één adres per regel) |
| de scout pauzeren | vink **Actief** uit |
| goedkoper draaien | kolom **Model** = `claude-haiku-4-5-20251001` |

De zoekbronnen zelf (globale zoekopdrachten en vakpers-feeds) en de rapport-opmaak zitten in de code
(`config/config.yaml` en `src/report_template.py`). Die aanpassen loopt via GitHub Desktop.

> **Twee kolommen die je kan negeren.** In Scout Config staan ook **Landen** en **Klantfiche**. Geen van
> beide wordt vandaag door de code gelezen. De markten volgen uit de zoekopdrachten in `config.yaml`, en
> merkcontext hoort in de body van de rij (zie hieronder), niet in een gekoppelde klantfiche.

## Let op het creditbudget

De scout zoekt via Tavily, en dat kost credits. Het gratis plan geeft er **1000 per maand**. Eén actieve
klant kost er ongeveer **530**, plus zo'n 30 per keywordterm. De volledige set zoekopdrachten wordt
vandaag **per klant opnieuw** gedraaid, dus een tweede klant verdubbelt het verbruik.

**Met twee actieve klanten loopt het budget dus leeg vóór het einde van de maand.** Dat gebeurt stil: de
zoekopdrachten mislukken zonder foutmelding en het rapport wordt gewoon mager. Zet een tweede klant dus
niet op Actief zonder dat daar eerst een oplossing voor gekozen is.

## Nieuwe keywords: waar je op let

Een keyword wordt **letterlijk** als zoekopdracht doorgegeven. Drie regels:

- **Eén term per regel, en nooit een komma binnen een term.** Het veld wordt ook op komma's gesplitst,
  dus `campagne rond eten, gezin en tafelen` wordt twee zoekopdrachten waarvan de tweede niets waard is.
- **Zet vaktaal uit de reclamewereld in de term**, niet enkel het thema. De zoekmachine matcht op de
  zelfstandige naamwoorden. `korte keten teler` levert landbouwnieuws; `campagne korte keten teler`
  levert campagnes.
- **Elke term kost ongeveer dertig credits per maand.** Drie tot vijf termen is de bandbreedte.

## Rationale en Voedingsbodem: twee velden, twee rollen

Dit is het meest gemaakte misverstand, dus lees het één keer goed. Op de klantpagina staan twee plekken
met merkcontext, en ze worden **niet door dezelfde agent gelezen**.

| | Waar | Wie leest het | Wanneer |
|---|---|---|---|
| **Rationale** | de kolom Rationale in de rij | de scout **én** de strategist | elke dag bij het filteren, en elke maandag bij het schrijven |
| **Voedingsbodem** | de tekst in de body van de rij zelf | **alleen** de strategist | enkel maandag, bij het schrijven van het rapport |

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

> **Let op, twee plekken waar de tekst niet gelezen wordt.** Zet merkmateriaal niet op een **subpagina**
> van de rij: subpagina's worden overgeslagen. En zet het ook niet enkel op de **klantfiche in de
> Klanten-database**: die pagina wordt door geen enkel script uitgelezen, ook niet als je ze via de
> kolom Klantfiche koppelt. Alleen de tekst in de body van de Scout Config-rij zelf telt, en niets
> waarschuwt je daarvoor.
