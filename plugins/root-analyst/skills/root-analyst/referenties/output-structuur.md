# Output-structuur: research-summary & research-dossier

Lees dit in **gate 3**, vlak voordat je de documenten opmaakt.

**Kijk eerst naar de echte voorbeelden.** In Notion staat
[📚 Voorbeeldrapporten research: huisstijl](https://app.notion.com/p/3a597e952547813eb39bca266bb4e960):
zes rapporten die door strategen van Cartel geschreven zijn. Die tonen hoe het er hier uitziet.
Onderstaande sjablonen zijn de codificatie daarvan; bij twijfel wint het voorbeeld.

Dit bestand gaat over de **inhoud en opbouw**. Voor de **opmaak** van het Word-document (Aptos,
Word-stijlen, geen inhoudstafel, geen horizontale lijnen) volg je **`rapport-opmaak.md`** en gebruik je
het bouwscript `assets/bouw-rapport.js`. Het format is vast; alleen de inhoud wisselt per case.

---

## Algemene regels voor beide documenten

- Lever **altijd twee afzonderlijke `.docx`-bestanden**. Nooit enkel platte tekst in de chat, nooit
  rechtstreeks naar Notion zonder dat de strateeg de Word-versies zag.
- Bestandsnamen: `[Klant]_Research-Summary.docx` en `[Klant]_Research-Dossier.docx`.
- **Geen insights, human truths of strategische aanbevelingen.** Zie de harde grens in §1 van SKILL.md.
- **Geen gedachtestreepjes.** Nooit `—` of `–` als zinsonderbreking. Gebruik een dubbele punt, een
  komma, een puntkomma, haakjes of een nieuwe zin. Koppeltekens in samenstellingen (`4M-onderzoek`) en
  in getallenreeksen (`10-30 pagina's`) mogen wel. Ook in koppen en tabellen: schrijf
  `Document 2: Research-dossier`, niet `Document 2 — Research-dossier`. **Zoek na het schrijven
  letterlijk op `—` en `–`** en vervang wat je vindt, in beide documenten.

---

## Klikbare bronnen: verplicht

Elke bron is een **werkende hyperlink**, in beide documenten, overal waar hij voorkomt.

**Regels**

- Toon de **brontitel als linktekst**, niet de kale URL. Dus *Statbel, Eenpersoonshuishoudens (2023)*,
  niet `https://statbel.fgov.be/...`. In de voorbeeldrapporten staat de link vaak als losse regel
  meteen onder de kop, dat mag ook, zolang hij klikbaar is.
- Neem de **volledige, directe URL** naar de specifieke pagina of het rapport. Geen homepages,
  geen zoekresultaat-URL's, geen verkorte links.
- Kon je geen stabiele URL vinden? Vermeld de bron mét de nota *(geen directe link beschikbaar)*.
  Verzin nooit een URL: een dode of gefantaseerde link is erger dan geen link.

**Technisch (docx-js)**

```js
new Paragraph({
  children: [
    new ExternalHyperlink({
      children: [ new TextRun({ text: "Statbel, Eenpersoonshuishoudens (2023)",
                                style: "Hyperlink" }) ],
      link: "https://statbel.fgov.be/nl/themas/bevolking/...",
    }),
  ],
})
```

Werk je in Markdown en converteer je met pandoc, dan volstaat `[Brontitel](https://…)`.
Beide wegen zijn goed; kale tekst zonder link is dat niet. **Controleer na het schrijven** dat de
links effectief klikbaar zijn.

---

## Document 1: Research-summary

De compacte, gecureerde synthese. Richtwaarde 4-8 pagina's.

**0. De beslissing**
De beslissing uit gate 1, in één of twee zinnen, plus de researchvragen die eruit volgden.

**1. Herkaderd probleem**
Wat de data zegt over het probleem achter de vraag (1-3 zinnen), **beschrijvend**. Je stelt vast wat de
bronnen tonen; je concludeert geen strategische richting.

**2. Objectives & KPI's** *(indicatief, te valideren met de klant)*
Business-objectives, gedrags-KPI's en eventuele kennis-KPI's, voor zover de briefing en de bronnen ze
ondersteunen. Ontbreken ze in de briefing? Zeg dat, in plaats van ze te verzinnen.

**3. Kernbevindingen per 4M**
Per pijler (Maatschappij → Markt → Mens → Merk), in die volgorde. Per bevinding: wat de data toont ·
de onderbouwing (cijfer, citaat, vaststelling) · de klikbare bron met datum · confidence (hoog/midden/laag).

**4. Eerste spanningen**
2 à 4 feitelijke tegenstellingen uit de data. Dit is de enige plek waar je data tegen elkaar mag
leggen. Twee sterke soorten: bronnen die elkaar tegenspreken, en vooral de **say/do-gap** waar
gedragsdata botst met wat mensen zeggen (mensen zeggen X, maar hun gedrag toont Y). Per spanning: beide
kanten met hun bron, en de spanning **open gelaten**, zonder verklaring. Geen toelichting over waarom
deze rubriek er staat; de kop volstaat.

**5. Gaps / waar verder graven**
Wat ontbreekt, wat onzeker is, welke bronnen je niet kon bereiken, welk eigen onderzoek nodig is.
Concreet en eerlijk; dit is een van de nuttigste rubrieken voor de strateeg.

**6. Bronnenlijst**
Gegroepeerd per kwaliteit: **primair / gezaghebbend · secundair · zwak of illustratief**.
Elke regel klikbaar, met datum en type.

Geen afsluitende beschouwing, geen bronmethode-vermelding, geen zin over "vertrekpunt / SD tekent af".
Het laatste in het document is de bronnenlijst.

> **Let op:** de oude rubriek *"Kandidaat-insight(s)"* uit v1 is geschrapt. Voeg die niet opnieuw toe,
> ook niet onder een andere naam.

---

## Document 2: Research-dossier

Hier volg je de **huisstijl uit de voorbeeldrapporten**, niet een AI-fiche-format. Richtwaarde
10-30 pagina's, maar **lengte is nooit het doel**.

### De opbouw

```
Briefing / recap            → context, doelstellingen, budget, doelgroep (kort, uit de briefing)
Research plan               → de researchvragen per M uit gate 1
Vragen aan de klant         → welke interne data je nodig hebt en niet zelf kon vinden
Maatschappij                → H1 per pijler, narratieve volgorde
Markt
Mens
Merk
[Media]                     → alleen als mediagedrag een aparte pijler verdient
Openstaande vragen en to do's
```

Het dossier **opent altijd** met Briefing/recap, Research plan en Vragen aan de klant, daarna komt het
4M-hart, en het **sluit af** met Openstaande vragen en to do's. Media is optioneel (tussen haakjes).
Dit staat ook al voorgestructureerd in `assets/Rapport-sjabloon.docx`.

Begin onder een pijlerkop **meteen met de eerste bevinding**. Geen inleidende of samenvattende zin
onder de pijler; de koppen dragen het verhaal.

### Hoe een bevinding eruitziet

Dit is het belangrijkste stijlkenmerk van Cartel-rapporten:

> **De kop is de bevinding, niet een label.**
> Niet *"Bron 4: Statistiek Vlaanderen"*, maar *"Ouderen zijn veel dynamischer dan vroeger"* of
> *"40% van de Vlamingen biedt informele zorg, meestal aan een ouder"*.
> De inhoudstafel leest daardoor als een reeks vaststellingen.

Onder die kop, en niets meer dan dit:

1. De **klikbare bron** (titel of losse linkregel), met datum waar relevant.
2. **Bullets met de concrete inhoud:** cijfers, percentages, letterlijke passages. Neem de inhoud
   echt over; een parafrase van één zin is te weinig.
3. **Tabellen** voor vergelijkende data (marktaandelen, bekendheidscijfers, operationele vergelijking).
4. Waar je een screenshot of grafiek niet kunt overnemen: beschrijf wat erop staat, of zet de cijfers
   in een tabel.

**Geen duiding onder de bron.** Zet onder een bron, tabel of case geen regel als "wat dit raakt",
"relevantie" of "wat dit betekent". De bevinding staat al in de kop en de cijfers spreken voor zich.
De strateeg legt de verbanden; jij levert het materiaal.

### Terugkerende bouwstenen

Deze komen in bijna elk Cartel-rapport terug. Neem op wat relevant is; verzin niets wat je niet vond.

| Pijler | Bouwsteen |
|---|---|
| **Merk** | SWOT · positionering en slagzin · beeldtaal en tone of voice · sonic branding · past campaigns · website- en UX-observaties |
| **Markt** | Concurrentieanalyse (direct én indirect) · marktomvang en groei · share of search · prijs- en assortimentsobservatie bij concurrenten · Meta Ad Library · recente campagnes van concurrenten · jaarrekeningen · internationale precedenten ("andere landen") · *SEMrush-analyse en WARC-cases enkel als de strateeg ze aanlevert* |
| **Mens** | Doelgroepdefinitie · jobs-to-be-done · drempels en drivers · academisch onderzoek · reviews (Trustpilot, Google) · social listening met letterlijke quotes · AnswerThePublic en Google Trends |
| **Maatschappij** | Macrotrends · demografie en statistiek · wetgeving en beleid · cultural moments · trendrapporten · nieuwsanalyse en achtergrondstukken uit de pers |

### Social listening

Zo doe je het (zie het Lapperre-voorbeeld):

- **Letterlijke quotes**, gegroepeerd per thema, met **link, datum en korte context** (wie, waar).
- Onder elke groep quotes: de feitelijke vaststelling die eruit volgt, in bullets.
- Kon je geen betrouwbare, gedateerde quotes ophalen? Zeg dat in de gaps, in plaats van vage
  samenvattingen op te nemen.

### Openstaande vragen en to do's

Die blijven gewoon in het document staan. In de voorbeeldrapporten staan doorgestreepte to do's,
vragen voor diepte-interviews en expliciet benoemde hypotheses die nog getoetst moeten worden. Dat is
een kwaliteit, geen slordigheid: het toont de strateeg waar het werk nog ligt.

**Hypotheses mag je formuleren**, mits je ze zo benoemt en er de bronnen bij zet die ze ondersteunen
of tegenspreken. Een hypothese is een toetsbare stelling over de feiten, geen insight en geen
strategische richting.

> **Let op:** de oude regel *"Wat betekent dit voor de beslissing"* per bron uit v1 is volledig
> geschrapt. Voeg per bron géén duidingsregel meer toe, ook niet als "relevantie" of "wat dit raakt".

**Doel van het dossier:** de strateeg kan zelf verder graven zonder alles opnieuw op te zoeken, en
gebruikt het als inspiratiebron bij het bouwen van zijn eigen verhaal.
