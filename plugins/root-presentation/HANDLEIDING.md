# Root Presentation: handleiding

## Waarvoor dient dit

Je hebt een briefing, een researchdossier of een strategie liggen, en er moet een presentatie van
komen. Deze agent maakt daar een deck van in het Cartel-sjabloon.

Het verschil met Claude gewoon om slides vragen: die bouwt een deck van nul en dan moet jij alles
overtikken in het sjabloon. Deze agent vult het sjabloon in. Hij mag niet ontwerpen, alleen kiezen
en invullen.

## Drie types

Zeg er altijd bij welk type je wil, want ze zien er echt anders uit.

| Type | Waarvoor | Omvang |
|---|---|---|
| Researchdeck | Onderzoek overdragen aan een strateeg of intern team | 50 tot 55 slides |
| Creatieve briefing | Creatie briefen, intern of bij de klant | 57 tot 85 slides |
| Strategische sessie | Werksessie met de klant, jaarplan | 107 tot 129 slides |

Die cijfers zijn geen limiet maar de gemeten norm uit zes afgewerkte Cartel-decks.

## Zo gebruik je hem

1. Start een gesprek in Cowork met je materiaal erbij.
2. Zeg wat je wil en welk type: "maak hier een researchdeck van voor een strateeg die er niets van weet."
3. Hij stelt eerst een **verhaallijn** voor: een lijst met per slide de titel en de layout. Nog geen
   bestand. Dit is jouw moment: schrappen, herschikken, titels aanscherpen.
4. Na je akkoord bouwt hij het deck en draait hij de controle.
5. Hij levert op met een lijst van wat je nog moet aanleveren.

## Wat je mag verwachten

- Een deck op de echte Cartel-layouts, in de huisstijl.
- Action titles: de titel is de conclusie, niet het onderwerp.
- Spreeknotities op elke slide, elk cijfer met zijn bron.
- Beeld als plaatshouder met een omschrijving, nooit een verzonnen afbeelding.
- Een machinale controle op tekstoverloop, gedachtestreepjes en hoofdletters voor hij oplevert.

## Wat hij niet doet

Beeld zoeken of maken, research of strategie bedenken die niet in jouw materiaal staat, of een
nieuwe huisstijl ontwerpen.

## Wat je zelf nog moet doen

Beeld aanleveren voor de plaatshouders, en de titels lezen als één rij. Klopt dat verhaal, dan klopt
het deck. Jij tekent af, niet de agent.

## Voor wie eraan sleutelt

Het sjabloon zit in `skills/root-presentation/assets/cartel-basis.pptx`, 27 layouts. Verandert het:

```bash
python3 scripts/bouw-sjabloon.py breed-deck.pptx -o assets/cartel-basis.pptx
python3 scripts/lees-sjabloon.py assets/cartel-basis.pptx > assets/layouts.md
```

De kortlijst van layouts staat bovenaan `scripts/bouw-sjabloon.py`.
