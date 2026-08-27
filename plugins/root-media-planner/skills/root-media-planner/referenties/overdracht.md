# Overdracht naar Root Presentation

Jij schrijft de inhoud, Root Presentation bouwt het deck. Die grens is bewust: er is een deckmotor en
er hoort er maar een te zijn. Twee kopieen van dezelfde motor lopen na drie maanden uiteen en dan
kloppen de layouts niet meer.

**Wat je oplevert is een pakket van vier stukken.** Daarmee kan Root Presentation, of een collega met
de hand, meteen aan de slag.

---

## Het pakket

| Stuk | Bestand | Wat erin zit |
|---|---|---|
| 1. De verhaallijn | in de chat, als tabel | Per slide: blok, action title, layout, wat erop komt, bron |
| 2. Het slideplan | `slideplan.json` | Dezelfde rij, in de vorm die `bouw-deck.py` leest |
| 3. De grafiekbladen | `grafieken/*.md` en `*.png` | Per grafiek de reeksen, de eenheid en de bronregel |
| 4. Het huiswerk | in de chat | Aannames, gaten, en wat de strateeg nog moet aanleveren |

**Stap 1 leg je altijd eerst voor.** Een regel herschrijven kost niets, een slide herbouwen kost veel.
Dat is dezelfde gate als bij Root Presentation, en je neemt hem hier over zodat de strateeg niet twee
keer moet goedkeuren.

---

## De verhaallijn

Per slide een regel, met deze kolommen:

| # | Blok | Action title | Layout | Wat erop komt | Bron |
|---|---|---|---|---|---|

**Vier regels voor de action titles.** Ze staan uitgebreider in `referenties/schrijfstijl.md` van
Root Presentation; dit is wat er voor een mediadeck het meest toe doet.

1. **De titel is de conclusie, niet het onderwerp.** Niet "Budgetverdeling" maar "Onder 30 procent
   merkinvestering valt de groei stil".
2. **Elk cijfer krijgt hier al zijn bron.** Geen bron betekent: niet op de slide. Dat is een harde
   regel van het huis en ze wordt machinaal gecontroleerd.
3. **Blijf onder het maximum aantal tekens** van de gekozen rol. Die staan per layout in
   `assets/layouts.md` van Root Presentation. Voor de gewone tekstslide is dat 79 tekens voor de
   action title.
4. **Lees op het einde alleen de titelrij.** Klopt het verhaal dan nog, en spreekt geen enkele titel
   de klant tegen.

---

## Welk type deck, en welke blokvolgorde

Root Presentation kent drie types. Een mediadocument valt bijna altijd onder een van deze twee:

| Wat je maakt | Type in Root Presentation | Waarom |
|---|---|---|
| Mediaplan of KPI-raamwerk voor de klant, jaarplan, werksessie | **strategische sessie** | Er wordt samen beslist, dus er zitten beslismomenten en agendaschermen in |
| Onderzoek of resultaten presenteren, bevindingen overdragen | **researchdeck** | Het presenteert wat er gemeten is, met een smalle set layouts |

De **creatieve briefing** is het derde type en die is niet van jou: dat is de strateeg met de SD of
CD. Wel van jou is wat er over media in staat, en dat lever je als blok aan, niet als deck.

Twijfel je tussen strategische sessie en researchdeck, vraag het. Ze verschillen echt: een
researchdeck gebruikt vijf layouts, een strategische sessie twintig.

---

## De blokken per document

De blokvolgorde uit `mediaplan.md` en `kpi-en-meting.md`, vertaald naar een sliderij.

### Mediaplan

| Blok | Slides | Typische layouts |
|---|---|---|
| Titel | 1 | `CartelAgency-Titeldia-4` |
| De beslissing | 1 tot 2 | `CartelAgency-Titel+Tekst-Zwart`, of `Sentence-Black` als het een scherpe zin is |
| Waar we staan | 3 tot 6 | `Titel+Tekst`, `Titel+Bullets+Grafiek` |
| De doelstelling | 1 tot 2 | `Titel+Blokken` |
| Het budget | 2 tot 4 | `Titel+Bullets+Grafiek`, `Titel+Tekst+Titel+Tabel` |
| De verdeling | 3 tot 5 | `Titel+Bullets+Grafiek`, `Titel+Blokken` |
| Bereik, frequentie, fasering | 2 tot 4 | `Titel+Timeline` voor de fasering, tabel voor de rest |
| Meten | 2 tot 3 | `Titel+Tekst+Titel+Tabel` |
| Aannames en gaten | 1 | `Titel+Tekst` |

Zet een `Tussentitel` tussen de blokken, en wissel donkere en lichte slides af.

### KPI-presentatie

| Blok | Slides |
|---|---|
| Waar we op sturen | 1 |
| De drie lagen | 1, als tabel of blokken |
| KPI's per doel | 2 tot 4 |
| Hoe we meten | 1 tot 2 |
| Wat we bewust niet meten | 1 |

**De verleiding bij een KPI-deck is een dashboardslide met dertig tegels.** Doe dat niet. De
kernmaten op de slide, de rest in de bijlage.

---

## Het slideplan

De vorm die `bouw-deck.py` van Root Presentation leest. Per slide een layout en de tekst per **rol**,
nooit per placeholdertype.

```json
{
  "sjabloon": "assets/cartel-basis.pptx",
  "titel": "Mediaplan 2027",
  "slides": [
    {
      "layout": "CartelAgency-Titel+Bullets+Grafiek",
      "action title": "Goedkopere CPM, snellere daling van de opbrengst",
      "tekst": "Naarmate formats minder aandacht vasthouden, zakt de CPM met 41 procent en de opbrengst per euro met 77 procent.",
      "bron": "Bron: Nelson-Field, The Eye-Watering Cost of Dull Media, Amplified, 2025",
      "notities": "Grafiekblad: grafieken/cpm-val.md. Data vervangen in de sjabloongrafiek, niet de png invoegen."
    }
  ]
}
```

De beschikbare rollen zijn `action title`, `tekst`, `kort label`, `bron`, `extra`, `beeld`, `chart`,
`table` en `notities`. Welke rol een layout heeft en hoeveel tekens erin passen, staat in
`assets/layouts.md` van Root Presentation. **Lees dat bestand voor je een layout kiest.**

---

## De grafieken

```bash
python3 scripts/grafiek.py --lijst
python3 scripts/grafiek.py --id cpm-val -o grafieken/
python3 scripts/grafiek.py --eigen klantdata.json -o grafieken/
```

Per grafiek komen er twee bestanden uit.

**Het grafiekblad (`.md`) is de hoofduitvoer.** Het bevat de reeksen, de labels, de eenheid en de
bronregel. Daarmee vervang je de data van een bestaande sjabloongrafiek. Dat is wat de vormregels van
het huis voorschrijven: hergebruik een bestaande grafiek en bouw er geen nieuwe.

**De png is een controlebeeld.** Gebruik hem om te kijken of het verhaal klopt, en als terugvaloptie
wanneer er geen bruikbare sjabloongrafiek bestaat. In dat geval hoort hij in het deck als
plaatshouder benoemd te worden, met in de opleveringslijst wat erin moet komen. **Voeg hem nooit
stilzwijgend in als afbeelding.** Wie een pnggrafiek in een Cartel-deck plakt zonder het te zeggen,
levert een slide die er bijna goed uitziet en die niemand meer kan bijwerken.

**Voor eigen data van de klant** maak je een json in dezelfde vorm, met `bron`, `jaar` en `basis`
ingevuld. De bronregel op de slide wordt daaruit opgebouwd, dus een leeg bronveld levert een slide op
die de controle van Root Presentation niet haalt.

---

## Wat je meelevert als huiswerk

Drie lijsten, kort, in de chat en niet in het deck:

1. **Aannames.** Elk cijfer dat je zelf hebt ingevuld, met waarop je het baseerde.
2. **Gaten.** Wat er ontbreekt, en wat elk gat zou veranderen aan de aanbeveling.
3. **Plaatshouders.** Elk beeld en elke grafiek waar nog iets in moet, met wat erin hoort.

Dat is het huiswerk van de strateeg. Hij moet het niet zelf gaan zoeken in het bestand.

---

## Als Root Presentation niet geinstalleerd is

Dan lever je stuk 1, 3 en 4 en zeg je erbij dat het slideplan pas gebouwd kan worden zodra de plugin
erbij staat. **Bouw het deck niet zelf.** Een deck dat van nul gebouwd is, ziet er niet uit als Cartel
en moet alsnog overgetikt worden in het sjabloon; dan heeft de strateeg dubbel werk in plaats van
minder werk. Dat is precies de reden dat Root Presentation bestaat.
