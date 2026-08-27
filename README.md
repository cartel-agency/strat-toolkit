# Cartel Strategy: marketplace

De interne Claude-marketplace van het Cartel-strategieteam. Een verzamelplek voor de AI-agents die het
team gebruikt.

- **Root Analyst** is de research-agent: van een briefing naar een research-summary en een
  research-dossier volgens de 4M-methodologie (Maatschappij, Markt, Mens, Merk). Levert materiaal en
  stopt bewust vóór het inzicht.
- **Root Strategist** is de sparringpartner: hij pikt op waar Root Analyst stopt en spart met de
  strateeg tot de creatieve briefing staat. Werkt met de vier blokken, dwingt de flow Problem →
  Insight → Communication af en toetst de shift in wat de doelgroep gaat denken, doen en voelen. Daagt
  uit, schrijft niet in jouw plaats, en levert nooit de boodschap of het concept.
- **Root Media Planner** is de mediastrateeg: van briefing naar mediavoorstel, KPI-raamwerk en de
  duiding van aangeleverd onderzoek. Onderbouwt budget, kanaalrollen, bereik en aandacht op zes
  mediapapers, en labelt elk cijfer op herkomst. Levert wel af, in tegenstelling tot de strategist,
  maar bouwt het deck niet zelf.
- **Root Presentation** bouwt het deck: van briefing, research of strategie naar een afgewerkt deck in
  het Cartel-sjabloon. Vult het sjabloon in en ontwerpt nooit een slide van nul.
- **Scout Setup** voegt een klant toe aan Root Scout, de learninglaag.

## Hoe zit dit in elkaar?

Vier lagen, van groot naar klein:

- **Deze repository** (`strat-toolkit`) is de opslagplek op GitHub.
- **De marketplace** (`.claude-plugin/marketplace.json`) is de catalogus erin. Eén catalogus, meerdere
  plugins.
- **Een plugin** is één bundel die je in Claude installeert. Root Analyst is er nu één van; later komen
  hier bijvoorbeeld Root Scout of een Junior Strateeg bij.
- **Een skill** is één vaardigheid binnen een plugin.

Het voordeel boven een los `.skill`-bestand: **wanneer een wijziging gepusht wordt, krijgt iedereen die
de marketplace heeft toegevoegd de nieuwe versie automatisch** bij de volgende refresh. En elke nieuwe
agent die hier bijkomt, verschijnt vanzelf in de catalogus van je collega's, zonder dat zij opnieuw iets
moeten toevoegen.

---

## Installeren (één keer)

1. Open **Claude** → in de linkerbalk **Customize** (in Cowork: eerst het tabblad **Cowork**, dan **Customize**).
2. Ga naar het tabblad **Plugins**.
3. Onder **Personal plugins**, klik op **+** → **Add marketplace** → **Add from a repository**.
4. Plak deze repo:

   ```
   tomasmoesen/strat-toolkit
   ```

5. Zodra de marketplace is toegevoegd, klik **Install** bij de plugin **Root Analyst**.
6. Zet daarna eenmalig de **Notion-connector** aan (Customize → Connectors → Notion) en deel de
   Research-database, Kennisbank, Templates en Methodologie. Root Analyst leest daaruit de
   voorbeeldrapporten en schrijft er zijn output naartoe.

Klaar. Typ `/` of klik **+** in een gesprek om Root Analyst te gebruiken. Toekomstige agents uit deze
marketplace kun je op dezelfde plek installeren zodra ze verschijnen.

### Al een los `.skill`-bestand geïnstalleerd?

Verwijder dat eerst (Customize → Skills → de losse Root Analyst verwijderen). Een handmatig
geïnstalleerd bestand krijgt geen automatische updates; de marketplace-versie wél. Anders heb je de
skill dubbel.

---

## Een wijziging uitrollen

1. Pas de bestanden in `plugins/root-analyst/skills/root-analyst/` aan (SKILL.md, referenties, assets).
2. Verhoog het versienummer in **twee** bestanden (bv. van `2.0.0` naar `2.1.0`):
   - `plugins/root-analyst/.claude-plugin/plugin.json`
   - `.claude-plugin/marketplace.json` (het `version`-veld bij die plugin)
3. Commit en push naar GitHub:

   ```bash
   git add -A
   git commit -m "Root Analyst: <korte omschrijving van de wijziging>"
   git push
   ```

4. Collega's krijgen de update bij hun volgende **plugin-refresh** (Customize → Plugins → marketplace →
   menu → *Update*), of automatisch bij een nieuwe sessie. Zij hoeven niets opnieuw te installeren.

### Een nieuwe agent toevoegen (later)

1. Maak naast `plugins/root-analyst/` een nieuwe map `plugins/<naam>/` met dezelfde structuur
   (`.claude-plugin/plugin.json` + `skills/<naam>/SKILL.md`).
2. Voeg een extra entry toe in de `plugins`-lijst van `.claude-plugin/marketplace.json`.
3. Push. De nieuwe agent verschijnt vanzelf in de catalogus van iedereen die de marketplace heeft.

> **Belangrijk:** deze marketplace is **niet openbaar** in Claude. Alleen wie de repo-link
> `tomasmoesen/strat-toolkit` toevoegt, ziet de plugins. Zet de GitHub-repo op **privé** als je hem
> enkel binnen het team wil houden. Collega's hebben dan wel een GitHub-account met leesrechten op de
> repo nodig. Let op: de voorbeeldrapporten en de skill kunnen klantgevoelige data bevatten.

---

## Structuur van deze repo

```
.
├── .claude-plugin/
│   └── marketplace.json         # de marketplace-definitie (lijst met plugins)
├── plugins/
│   ├── root-analyst/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json       # de plugin-definitie
│   │   └── skills/
│   │       └── root-analyst/     # de eigenlijke skill (SKILL.md, referenties, assets)
│   ├── root-strategist/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   └── skills/
│   │       └── root-strategist/  # SKILL.md + referenties (vier blokken, toetsstenen,
│   │                             # creatieve briefing, notion)
│   └── scout-setup/
└── README.md
```

## Eerste keer naar GitHub pushen

Maak de repo `strat-toolkit` eerst aan op github.com (zonder README, zodat de push niet botst).
Daarna, vanuit de map van deze repo:

```bash
git init
git add -A
git commit -m "Cartel Strategy marketplace: Root Analyst v2"
git branch -M main
git remote add origin https://github.com/tomasmoesen/strat-toolkit.git
git push -u origin main
```
