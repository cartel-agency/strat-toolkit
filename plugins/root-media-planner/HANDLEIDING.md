# Root Media Planner: handleiding

## Waarvoor dient dit

Er ligt een briefing of een creatieve briefing, en er moet een mediavoorstel komen. Of er ligt een
doelstelling en er moeten KPI's bij. Of er ligt een stapel cijfers uit een brand tracker en iemand
moet er iets zinnigs over zeggen in een vergadering.

Dat is werk dat vandaag bij de strateeg terechtkomt naast zijn eigen werk, omdat het mediaprofiel in
het team niet bestaat. Deze agent doet het voorbereidende deel: hij maakt het voorstel, onderbouwt
het met zes internationale mediapapers, en levert het materiaal voor de presentatie aan.

Het verschil met Claude gewoon om een mediaplan vragen: die geeft je een net plan met verzonnen
percentages. Deze agent zegt bij elk cijfer waar het vandaan komt, en zegt het ook wanneer hij het
niet weet.

## Vier dingen die hij kan

| Je vraagt | Je krijgt |
|---|---|
| Hoeveel investeren we, waaraan, welke kanalen | Een mediavoorstel in zeven blokken, met drie manieren om het budget te onderbouwen |
| Waarop sturen we, wat meten we | Een KPI-raamwerk in drie lagen, met wat je bewust **niet** meet |
| Hier zijn de cijfers, wat zeggen ze | Een duiding van een tracker, omnibus, panelrapport of postbuy |
| Er moet een presentatie van komen | Een verhaallijn, een slideplan en grafiekbladen voor Root Presentation |

## Zo gebruik je hem

1. Start een gesprek in Cowork met je materiaal erbij, of in een gewone Claude-chat.
2. Zeg wat je wil: "maak een mediavoorstel voor het jaarplan van X, budget staat nog niet vast."
3. Hij stelt eerst **vragen in een keer** en legt terug wat hij begrepen heeft, met de gaten erbij.
   Dit is jouw moment om bij te sturen.
4. Dan komt het **voorstel in tekst**, nog zonder slides. Elk cijfer draagt een label: uit de
   klantdata, uit de vakliteratuur, of aanname.
5. Na je akkoord levert hij de **verhaallijn, het slideplan en de grafieken** aan voor Root
   Presentation.

## Wat je mag verwachten

- Een budgetonderbouwing via drie methodes naast elkaar, niet via een percentage uit de lucht.
- Kanalen op **rol** in plaats van op de indeling merkkanaal tegenover performancekanaal, want die
  indeling houdt in de data geen stand.
- Een aandachtslaag bovenop de gewone bereikcijfers: wat wordt geleverd tegenover wat wordt gezien.
- Bij elk cijfer de bron, het jaar en de meetbasis.
- Twee lijsten onderaan die er altijd staan: de aannames, en wat we niet weten.

## Wat hij niet doet

Media inkopen, tarieven noemen, de strategie schrijven, het concept bedenken of het deck bouwen. En
hij verzint geen Belgische benchmark: alle bronnen meten in de VS, het VK of internationaal, en dat
zegt hij erbij.

## De grens met de andere agents

| Wie | Wat |
|---|---|
| **Root Analyst** | Doet de research die hieraan voorafgaat |
| **Root Strategist** | Spart over het inzicht en de strategie, en schrijft niets |
| **Root Media Planner** | Vertaalt de strategie naar investering, kanalen en KPI's, en levert wel af |
| **Root Presentation** | Bouwt het deck uit het slideplan dat hij aanlevert |

Ze blijven bewust apart. Een agent met een taak levert werk dat je kan nakijken; een agent met vier
taken levert werk waarvan je niet meer weet welk deel je moet wantrouwen.

## Wat je zelf nog moet doen

De aannames nakijken en de gaten vullen. Het budget en de tarieven komen van jou of van het
mediabureau. En jij tekent af, niet de agent.

## Voor wie eraan sleutelt

De cijfers staan allemaal in `skills/root-media-planner/data/kerncijfers.json`, elk met bron, jaar en
meetbasis. Dat is bewust de enige plek waar een cijfer ontstaat: komt er een nieuw rapport bij, dan
voeg je het daar toe en niet in de tekst.

```bash
cd skills/root-media-planner
python3 scripts/grafiek.py --lijst                       # wat er te tekenen valt
python3 scripts/grafiek.py --id cpm-val -o grafieken/    # een grafiek
python3 scripts/grafiek.py --eigen klantdata.json -o grafieken/
```

De brondocumenten zelf staan in `Root Media Planner/Input/` in de projectmap. Let op: de
WARC-rapporten daar dragen een licentie die verspreiden en archiveren verbiedt.
