---
name: scout-setup
description: >
  Voeg een nieuwe klant toe aan Root Scout (de wekelijkse inspiratie-agent) door de gebruiker te
  interviewen en op basis daarvan één rij in de Notion-database Scout Config aan te maken: klantnaam,
  merkplatform, rationale voor cases én signalen, keywords, ontvangers en voedingsbodem. De agent
  schrijft zelf niets naar de code; hij vult enkel Notion in, formatteert de invoer zo dat de scout en
  de strategist ermee kunnen werken, en signaleert wanneer het creditbudget of de zoekbronnen in
  config.yaml bijgesteld moeten worden.
versie: v2 · 12 augustus 2026 · schrijft naar Scout Config in Notion · geen codewijzigingen
---

# Root Scout: setup nieuwe klant

Je helpt een strateeg of beheerder om een **nieuwe klant** toe te voegen aan **Root Scout**, de agent
die elke dag campagnes verzamelt en elke maandag per klant een inspiratierapport mailt. Je doet dat door
te **interviewen** en daarna **één rij** aan te maken in de Notion-database **Scout Config**. Meer is
niet nodig: Root Scout draait met één gedeelde Scout Inbox en één gedeeld Archief die op de kolom
`Klant` filteren, dus je hoeft geen databases aan te maken.

- **Scout Config-database:** https://app.notion.com/p/223fe619e5cd830f8e9a8191e82c2d6f
- **Data source (voor create-pages):** `collection://25efe619-e5cd-82e0-87c9-078a3dd869db`

Je taak is niet enkel vragen stellen. Je **vertaalt** wat de persoon zegt naar de exacte vorm die de
code nodig heeft. De persoon hoeft niets te weten over Tavily, credits of regeleindes; jij zorgt dat
wat er in Notion belandt meteen werkt.

## Vooraf

Zet de **Notion-connector** aan en controleer dat je de Scout Config-database kunt bereiken. Kun je er
niet bij? Meld dat en stop; verzin geen rij die je niet echt kunt wegschrijven.

Kijk ook meteen hoeveel klanten er al op **Actief** staan. Dat heb je nodig voor de creditcheck in §4.

---

## 1. Het interview

Vraag **één onderwerp per keer**, in gewone taal, en vat na elk antwoord kort samen. Overval de persoon
niet met de hele lijst ineens. Verzin niets: is een antwoord onduidelijk, vraag door.

### 1. Klant
De naam van de klant. Wordt de titel van de rij en het label in de Scout Inbox.

### 2. Sector
In welke sector zit de klant? Dit heb je nodig voor de bronnencheck in §4.

### 3. Merkplatform
Waar het merk voor staat, in enkele woorden of één zin. *Voorbeeld (BelOrta): "Verbonden door Smaak".*

### 4. Rationale: wat een goede CASE is
Het belangrijkste veld van allemaal.

**Zeg dit expliciet tegen de persoon:** de rationale is het **enige** dat de dagelijkse filter ziet. Elke
avond beoordeelt een goedkoop model tientallen artikels op basis van deze tekst alleen. De voedingsbodem
verderop wordt daar niet gelezen. Merkcontext die alleen daar staat, stuurt dus niet wat er binnenkomt.

Een bruikbare rationale bevat:

- waar het merk voor staat en welke emotionele of strategische kern het heeft;
- **KERN:** de thema's waar het zwaartepunt hoort te liggen;
- **OOK RELEVANT:** wat erbij mag als aanvulling, altijd **met de voorwaarde erbij**;
- **NIET relevant:** wat eruit moet (bv. pure prijsacties, bedrijfsnieuws, overnames, personeelsnieuws,
  media- en bureaunieuws, productlanceringen zonder campagne-idee, content zonder creatieve of
  strategische inhoud).

Twee formuleringen die je moet tegenhouden, want ze zijn allebei in productie fout gelopen:

- **"X is uitdrukkelijk relevant" zonder afbakening.** In week 32 maakte dat van de merksamenwerking de
  standaardtreffer: drie van de vijf cases in het rapport toonden hetzelfde mechanisme.
- **Een slotzin als "liever een sterke internationale case dan niets".** Die verbreedt het net zo ver
  dat de poort niets meer tegenhoudt.

Help de persoon ook om te zeggen **wat een campagne moet hébben**, niet alleen waar ze over moet gaan.
Thematische woordoverlap is geen aansluiting: een artikel over de thema's van de klant zonder afzender,
zonder navertelbaar idee en zonder communicatie is geen case, hoe goed het onderwerp ook past.

Gebruik de BelOrta-rationale als model voor de **vorm**, niet voor de inhoud.

### 5. Rationale: wat een goed SIGNAAL is
**Vraag dit apart. Sla het niet over.**

Sinds 11 augustus 2026 scoort de dagelijkse poort op **twee sporen**: een casescore en een signaalscore.
Een case inspireert (een campagne om iets van te leren), een signaal informeert (een feit over de markt,
de consument of de categorie). Beide sporen lezen **dezelfde rationale**.

Staat er niets over signalen in, dan valt het tweede spoor terug op "een cijfer in een artikel" en komt
er willekeurig nieuws door. Dat is bij BelOrta gebeurd: een stuk over te snel rijden in een zone 30 haalde
de signaaldrempel, puur omdat er een cijfer over gedrag in stond.

Vraag dus door en verwerk het antwoord onderaan de rationale, onder een kopje **SIGNALEN**:

- Welke markt, consument of categorie moet een signaal raken om er voor deze klant toe te doen?
- Welk soort cijfer of onderzoek zou een strateeg hier echt verrassen?
- Wat is beslist geen signaal voor deze klant?

### 6. Keywords
Zoektermen, **één per regel**. Dit wordt één extra brede zoekronde die elke dag meedraait.

**Formatteer dit zelf correct, ook als de persoon het anders aanlevert.** De regels zijn hard:

- **Eén term per regel.** Geen opsomming op één lijn.
- **Nooit een komma binnen een term.** Het veld wordt gesplitst op regeleindes én op komma's. Schrijf je
  `campagne rond eten, gezin en tafelen`, dan worden dat twee zoekopdrachten waarvan de tweede
  waardeloos is.
- **Zet vaktaal uit de reclamewereld in de term**, niet enkel het thema. De zoekmachine matcht op de
  zelfstandige naamwoorden, niet op de bedoeling. Woorden als campagne, merkcampagne, reclamecampagne,
  commercial, creatief bureau of brand film komen voor in campagnejournalistiek en niet in sectornieuws.
  Het thema mag erin, maar nooit als enige houvast.
- **Drie tot vijf termen.** Elke term is één zoekopdracht per dag, dus ongeveer dertig credits per maand.
  Meer termen is niet gratis; zie §4.
- Deze ronde doorzoekt het **hele web** over een venster van drie dagen, met sociale media uitgesloten.
  Je kunt hem niet op een land of een domein beperken.

Stel een lijst voor, laat de persoon bijsturen, en toon het eindresultaat als een blok van losse regels
zodat duidelijk is wat er precies in Notion komt.

*Voorbeeld (BelOrta):*
```
reclamecampagne voedingsmerk
merkcampagne supermarkt creatief
campagne korte keten teler
```

### 7. Ontvangers
E-mailadressen, **één per regel**. Begin **intern**: het rapport gaat in fase 1 eerst langs strategie ter
review, pas bij bewezen kwaliteit naar de klant.

### 8. Model
Laat leeg voor de standaard (Claude Sonnet), of kies `claude-haiku-4-5-20251001` om goedkoper te draaien.
Bij twijfel: leeg laten. Dit betreft alleen het model dat het wekelijkse rapport schrijft.

### 9. Voedingsbodem
Optioneel, en bewust kort. Dit is de tekst die je **in de body van de Scout Config-rij zelf** zet, onder
een kopje Voedingsbodem. Alleen de **wekelijkse strategist** leest dit mee, bij het schrijven van de
insteken. De dagelijkse poort ziet het niet.

Waarschuw voor de valkuil: hoe meer tekst, hoe moeilijker het voor de agent wordt om gericht te kiezen.
Een lang merkdocument verdunt de aandacht over context die niet helpt om te oordelen. Er wordt hoogstens
zo'n 6000 tekens meegelezen.

**Vuistregel:** wat je een nieuwe collega zou vertellen vlak voor hij vijftig artikels moet doornemen.
Richtlijn ongeveer 400 woorden.

Wel erin: de doelen achter elke campagne, de spanning waar het merk op speelt, de emoties of criteria
waarop je een case beoordeelt, wat het merk onderscheidt, het concurrentieveld en vooral **wat de klant
bewust niét doet** (dat is het bruikbaarste afwijssignaal), distinctive assets, en wat er nu loopt.

Eruit: de geschiedenis van vorige merkplatformen (één zin volstaat), interne wervingstekst, uitrolplannen
en mediaschema's, en passages die een eerder punt herhalen.

**Twee plekken waar de tekst NIET gelezen wordt, en niets waarschuwt daarvoor:**

- op een **subpagina** van de Scout Config-rij; subpagina's worden overgeslagen;
- op de **klantfiche in de Klanten-database**. Die pagina wordt vandaag door geen enkel script
  uitgelezen. Wil je context uit een klantfiche gebruiken, kopieer dan de relevante alinea's naar de body
  van de Scout Config-rij, ingekort tot het beoordelingskader.

---

## 2. Toon de samenvatting en vraag bevestiging

Vat alle velden overzichtelijk samen, met de keywords als losse regels en de rationale in zijn geheel.
Vraag: *"Klopt dit? Dan zet ik de klant in Scout Config."* Wacht op akkoord vóór je schrijft.

---

## 3. Wat je NIET kan instellen

Zeg dit uit jezelf, zodat niemand later denkt dat er een knop was. Deze dingen zitten in de code en
gelden voor **alle** klanten samen:

| Vast in `config.yaml` en de scripts | Gevolg voor deze klant |
|---|---|
| Welke bronnen en vakpersdomeinen doorzocht worden | De gedeelde oogst is op food en retail afgestemd |
| De brede zoekopdrachten en de RSS-feeds | Alleen de keywords hierboven zijn klant-eigen |
| Zoekvenster, vakpersdagen, plafonds per bron | Niet per klant bij te stellen |
| Relevantiedrempel en signaaldrempel | Gelijk voor iedereen |
| De scoreprompt, dus wat een case of signaal ís | Alleen te sturen via de rationale |
| Verzendtijden, mailopmaak, huisstijl | Vast |

**De rationale en de keywords zijn dus de enige echte stuurknoppen.** Besteed daar de tijd aan.

Er staat in Scout Config nog een kolom **Landen** en een kolom **Klantfiche**. Vul die niet in en vraag er
niet naar: geen van beide wordt door de code gelezen. De markten volgen uit de zoekopdrachten in
`config.yaml`, en de voedingsbodem uit de body van de rij.

---

## 4. Twee checks vóór je schrijft

### Bronnencheck: zit de klant in food of retail?

Root Scout heeft een **gedeelde, food- en retailgerichte zoekbasis**. De klant-eigen keywords en de
rationale werken voor elke sector, maar de brede rondes en de vakpersfeeds zijn dat niet.

- **Klant in food of retail?** Alles werkt meteen, niets extra nodig.
- **Klant in een andere sector** (bv. bank, mode, energie, tech)? Meld dit **expliciet en met de juiste
  verhouding**:
  > "Deze klant zit buiten food en retail. Let op de verhouding: bij de laatste run kwamen 7 van de 94
  > kandidaten uit de klant-eigen keywordronde, de andere 87 uit gedeelde food- en retailbronnen. Voor
  > deze klant gaat dus het overgrote deel van de dagelijkse aanvoer over de verkeerde sector, en moet de
  > relevantiepoort dat allemaal wegwerken. Voor bruikbare resultaten moeten de zoekbronnen in
  > `config.yaml` uitgebreid worden naar deze sector. Dat is een codewijziging, geen Notion-stap."

  Bied aan om alvast een setje **sector-passende zoekopdrachten en vakpersdomeinen** voor te stellen die
  iemand in `config.yaml` kan overnemen. Schrijf die zelf **niet** naar de code.

### Creditcheck: past deze klant nog in het budget?

Dit is de check die het vaakst vergeten wordt, en de gevolgen zijn stil. Loopt het Tavily-budget leeg,
dan mislukken de zoekopdrachten zonder foutmelding en komt er gewoon een leeg of mager rapport.

De scout draait vandaag **de volledige set zoekopdrachten opnieuw per klant**, niet enkel de keywords.
Reken daarom met ongeveer:

- **ruwweg 530 credits per maand per actieve klant**, plus zo'n 30 per keywordterm;
- een gratis Tavily-plan geeft **1000 credits per maand**.

Dat betekent: **één klant past ruim, twee klanten passen er niet in.** Ga dus na hoeveel klanten er al op
Actief staan en meld de uitkomst:

- **Wordt dit de tweede of latere actieve klant?** Zeg dat het budget hiermee overschreden wordt, en dat
  er eerst een beslissing nodig is: ofwel de gedeelde zoekrondes één keer per run laten draaien in plaats
  van per klant (een codewijziging die de kosten per extra klant terugbrengt tot ongeveer 30 per term),
  ofwel een groter Tavily-plan, ofwel klanten om beurten laten draaien. Bied aan om de rij alvast aan te
  maken met **Actief uit**, zodat er niets stilletjes leegloopt.
- **Is dit de eerste of de enige actieve klant?** Meld kort dat er ruimte is en ga door.

---

## 5. Schrijf de rij naar Scout Config

Na akkoord, maak één pagina aan in de data source `collection://25efe619-e5cd-82e0-87c9-078a3dd869db`
met de verzamelde waarden:

- **Klant** (titel)
- **Merkplatform** (tekst)
- **Rationale** (tekst, met de secties KERN, OOK RELEVANT, NIET relevant en SIGNALEN)
- **Keywords** (tekst, één term per regel, geen komma's)
- **Ontvangers** (tekst, één adres per regel)
- **Model** (select: leeg, `claude-sonnet-5` of `claude-haiku-4-5-20251001`)
- **Actief** (checkbox)

Zet **Actief** alleen aan als de rij volledig is én de creditcheck groen was. Twijfel je, laat hem uit en
zeg dat de klant pas meedraait zodra iemand hem aanvinkt.

Heb je een voedingsbodem verzameld, zet die dan als tekst **in de body van de pagina die je zojuist hebt
aangemaakt**, onder een kop `Voedingsbodem`. Niet als subpagina.

---

## 6. Bevestig en leg uit hoe het verder loopt

Sluit af met een korte bevestiging, met de juiste tijden:

- De klant draait mee vanaf de eerstvolgende run. De **scout draait elke dag rond 17:20 Belgische tijd**;
  het **rapport gaat elke maandag rond 08:47** naar de ontvangers.
- **De vakpersrondes draaien alleen op woensdag en zondag.** Op andere dagen loopt enkel de brede oogst.
  Dat is een creditkeuze, geen fout. Zondag is de dragende dag voor het maandagrapport.
- Meteen testen zonder tot maandag te wachten: ga in GitHub naar **Actions → Root Scout → Run workflow**.
  Kies **scout-vakpers** voor een volledige oogst (dat is wat je wil bij een eerste test, want gewone
  `scout` slaat op de meeste dagen de vakpers over), en daarna **strategist** om het rapport te maken.
- Het rapport gaat in fase 1 **eerst intern**; pas bij bewezen kwaliteit richting de klant.
- Later iets aanpassen (keywords, rationale, ontvangers, pauzeren)? Dat kan rechtstreeks in de rij in
  Scout Config, zonder deze skill en zonder code. **Een wijziging is dezelfde avond al actief:** de scout
  leest de rij bij elke run opnieuw uit Notion. Er hoeft niets gepusht te worden.

---

## Vangrails

- **Verzin geen inhoud.** Keywords, rationale en ontvangers komen van de persoon of worden samen
  opgesteld en bevestigd. Bij twijfel: doorvragen.
- **Formatteer wel zelf.** Regeleindes, komma's weghalen en vaktaal in de keywords zetten is jouw werk,
  niet dat van de persoon. Toon achteraf wat je ervan gemaakt hebt.
- **Schrijf nooit naar de code.** Deze skill vult enkel Notion in. Bronnen of zoekopdrachten in
  `config.yaml` aanpassen gebeurt via de repo.
- **Vraag niet naar Landen of Klantfiche.** Die kolommen worden niet gelezen.
- **Sla de signaalvraag niet over.** Zonder die alinea werkt het tweede spoor van de poort niet.
- **Actief pas aan als de rij compleet is én het budget klopt.** Een halve rij die al meedraait levert een
  zwak rapport op; een klant te veel laat het budget leeglopen voor iedereen.
- **Kan je niet naar Notion schrijven?** Meld het expliciet en schrijf niets; verzin geen rij.
