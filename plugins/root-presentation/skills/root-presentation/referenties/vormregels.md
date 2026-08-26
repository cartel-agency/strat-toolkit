# Vormregels

> Deze regels zijn niet afgeleid uit een huisstijlgids. Ze zijn opgeschreven uit de sessies waarin
> een strateeg met de hand een Cartel-deck heeft laten bouwen en telkens dezelfde dingen heeft moeten
> corrigeren. Elke regel hier staat er omdat ze één keer fout is gegaan.

## Het bestand

- **Vertrek altijd van een kopie van het sjabloon.** Nooit een leeg bestand, nooit `pptxgenjs`.
  Een deck dat van nul gebouwd is, ziet er niet uit als Cartel en moet alsnog overgetikt worden.
- **Behoud masters, layouts, placeholder-indexen en raster.** Je verplaatst geen placeholders en
  je verandert geen afmetingen, tenzij de strateeg erom vraagt.
- **Extra slides komen uit het sjabloon.** Is er meer nodig dan er in het sjabloon staat, dupliceer
  dan een bestaande layout. Meestal is dat de zwarte titel-plus-tekstslide, want die geeft de
  titelpositie, het kader en de voettekst mee die een blanco slide niet heeft.
- **Geen limiet op het aantal slides.** Zoveel als het verhaal nodig heeft. Liever meer slides met
  minder tekst dan minder slides met meer tekst.
- **Slidenummering per blok.** 1.01, 1.02, 2.01 en zo verder. Zo weet iedereen in welk blok hij zit
  en kan de strateeg gericht feedback geven.

## Kleur

- **Cartel-eigen elementen blijven Cartel.** De zwarte slides, het logo en de voettekst passen we
  niet aan, ook niet als het deck voor een klant is.
- **Klantkleuren vervangen de accentkleuren**, niet de structuur. De strateeg levert de hexwaarden
  aan; verzin ze niet en haal ze niet van een website.
- **Let op de omgekeerde kleurmapping.** Layouts met `Zwart` in de naam staan in `assets/layouts.md`
  met "donkere mapping: ja". Daar is wit de leeskleur. Donkere tekst op zo'n slide is onzichtbaar.
- **Wissel donkere en lichte slides af** zodat er ritme in het deck komt.

## Tekst op de slide

- **Eén inzicht per slide.** Eén zin of één cijfer dat het werk doet, met daaronder de onderbouwing.
- **Cijfers groot.** Het cijfer is het argument, de tekst eromheen is de uitleg.
- **Geen tekst in kadertjes.** Geen tekstvakken met randen of omlijnde blokjes. Hiërarchie maak je
  met grootte, kleur en witruimte, niet met lijnen.
- **Geen gedachtestreepjes.** Geen lang streepje en geen half streepje als zinsonderbreking, nergens
  in het deck en ook niet in de spreeknotities. Gebruik een dubbele punt, een komma, een puntkomma,
  haakjes of een nieuwe zin. Koppeltekens in samenstellingen en streepjes in getallenreeksen mogen wel.
- **Geen tekst in hoofdletters alleen.** Ook niet in labels of koppen.
- **Geen lappen tekst.** Korte oneliners of bullets, met subkoppen om te structureren.
- **Bullets erven van de layout.** Nooit een letterlijk bulletteken in de tekst zetten.

## Beeld

- **Nooit een echte afbeelding invoegen.** Ook geen stockbeeld, geen gegenereerd beeld, geen icoon
  van het web.
- **Wel een placeholder**: een rechthoek op exact dezelfde plek en met exact dezelfde afmeting als
  het beeldvlak in het sjabloon, in dezelfde stijl, met een korte omschrijving erin van wat er moet
  komen. Bijvoorbeeld: "screenshot van het HLN-artikel van 12 maart".
- Staat er in de layout al een beeldvlak met een overlay, neem die overlay dan mee. Een placeholder
  moet er in het deck uitzien alsof het beeld er straks in past, niet alsof er een gat zit.
- **Lever op het einde de lijst van placeholders op**, met per stuk wat erin moet. Dat is het
  huiswerk van de strateeg en hij moet het niet zelf gaan zoeken in het bestand.

## Grafieken

- **Hergebruik bestaande grafieken** uit het sjabloon en vervang de data. Bouw er geen nieuwe als
  er een bruikbare staat.
- Elke grafiek krijgt een bronregel op de slide.
- Een grafiek die uit een aangeleverd document komt, wordt overgenomen zoals hij is, niet
  geherinterpreteerd.

## Spreeknotities

- **Elke slide krijgt notities.** Wat de spreker zegt, en waar het cijfer op de slide vandaan komt.
- Beeldspraak en metaforen die de strateeg mondeling wil gebruiken, horen in de notities en niet
  op de slide.

## De checklist voor je oplevert

| Controle | Hoe |
|---|---|
| Bestand opent en valideert | `validate.py deck.pptx --original sjabloon.pptx` |
| Geen tekstoverloop | alle slides renderen en één voor één bekijken |
| Geen gedachtestreepjes | zoek letterlijk op beide streepjestekens in de uitgepakte XML |
| Geen ALL CAPS | zoek op woorden van drie letters of meer in hoofdletters |
| Geen kaders om tekst | visueel op de renders |
| Elk cijfer heeft een bron | teruggelegd op het brondocument, cijfer per cijfer |
| Placeholders opgelijst | in de oplevering, niet alleen in het bestand |
