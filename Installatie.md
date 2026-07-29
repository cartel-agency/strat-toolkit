# Root Analyst installeren in Claude

Root Analyst is onze research-agent: je geeft hem een briefing en de beslissing die de research moet
opleveren, en hij bouwt een research-summary en een research-dossier volgens onze 4M-methodologie
(Maatschappij, Markt, Mens, Merk). Hij levert het bronmateriaal; jij maakt de strategie.

Je installeert hem één keer. Daarna krijg je updates automatisch.

## Vooraf

Eerst **toegang geven tot de GitHub-repo** (de agent staat in een privé-repo). Je hebt
dus een GitHub-account nodig; geef je gebruikersnaam door.

## Installeren (één keer)

1. Open **Claude**. In Cowork: open eerst het tabblad **Cowork**.
2. Klik in de linkerbalk op **Customize**.
3. Ga naar het tabblad **Plugins**.
4. Onder **Personal plugins**, klik op **+** → **Add marketplace** → **Add from a repository**.
5. Plak deze link en bevestig:

   ```
   tomasmoesen/strat-toolkit
   ```

6. De marketplace "Cartel Strategy" verschijnt. Klik **Install** bij **Root Analyst**.

## Notion koppelen (één keer)

Root Analyst leest onze voorbeeldrapporten uit Notion en schrijft er zijn output naartoe.

1. In Claude: **Customize → Connectors → Notion** → aanzetten en inloggen.
2. Deel de pagina's die hij nodig heeft: de **Research-database**, **Kennisbank**, **Templates** en
   **Methodologie**.

## Gebruiken

Typ `/` of klik **+** in een gesprek en kies **Root Analyst**. Begin met de briefing plus de beslissing
die de research moet opleveren. Hij werkt in drie stappen (eerst de researchvragen bevestigen, dan een
kort vooronderzoek, dan het volledige onderzoek) en stopt telkens even zodat jij kunt bijsturen.

## Updates

Je hoeft niets te doen. Wanneer een verbetering wordt doorgevoerd, krijg je die vanzelf bij een volgende
sessie. Wil je meteen de nieuwste versie: **Customize → Plugins →** bij de Cartel Strategy-marketplace
op het menu klikken → **Update**.
