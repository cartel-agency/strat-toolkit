#!/usr/bin/env python3
"""
grafiek.py: zet een cijfer uit kerncijfers.json (of eigen data) om naar
een grafiekblad en een png in de Cartel-kleuren.

Waarom twee uitvoerbestanden en niet alleen een png. De vormregels van Root
Presentation zeggen: hergebruik een bestaande grafiek uit het sjabloon en
vervang de data, bouw er geen nieuwe. Het grafiekblad (.md) is dus de
hoofduitvoer: het bevat de reeksen, de labels en de bronregel, klaar om in
een sjabloongrafiek geplakt te worden. De png is een controlebeeld en een
terugvaloptie voor het geval er geen bruikbare sjabloongrafiek bestaat. In dat
geval hoort ze in het deck als plaatshouder benoemd te worden, niet stil
ingevoegd.

Gebruik:
    python3 grafiek.py --lijst
    python3 grafiek.py --id attention-volume -o uitvoer/
    python3 grafiek.py --eigen mijn-data.json -o uitvoer/
    python3 grafiek.py --alles -o uitvoer/

Vorm van een eigen databestand (dezelfde vorm als het veld "grafiek" in
kerncijfers.json, met bron en basis erbij):

    {
      "id": "belorta-penetratie",
      "bron": "VLAM huishoudpanel via de klant",
      "jaar": 2026,
      "basis": "Belgische huishoudens, kwartaalmeting",
      "grafiek": {
        "type": "lijn",
        "titel": "Penetratie per kwartaal",
        "eenheid": "% van de huishoudens",
        "reeksen": [
          {"naam": "Categorie", "labels": ["Q1", "Q2"], "waarden": [61.2, 63.4]}
        ]
      }
    }
"""

import argparse
import json
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
STANDAARD_DATA = os.path.join(HIER, "..", "data", "kerncijfers.json")

# Kleuren uit documentatie/stand-van-zaken/huisstijl.md, uitgelezen uit het
# Cartel-sjabloon. Volgorde is de volgorde waarin reeksen ingekleurd worden.
KLEUREN = ["#082676", "#085CF0", "#8FA9C6", "#B0E8FD", "#040B35"]
TEKSTKLEUR = "#141414"
RASTERKLEUR = "#D5DBE6"
LETTERTYPES = ["Favorit", "Montserrat", "Arial", "DejaVu Sans"]

TYPES = {"staaf", "staaf-horizontaal", "lijn", "lijn-dubbel", "gestapeld"}


def laad_kerncijfers(pad):
    with open(pad, encoding="utf-8") as f:
        ruw = json.load(f)
    items = []
    for sleutel, waarde in ruw.items():
        if sleutel == "over_dit_bestand" or not isinstance(waarde, list):
            continue
        for item in waarde:
            item["_thema"] = sleutel
            items.append(item)
    return ruw, items


def bronregel(item):
    stukken = [item.get("bron", "bron onbekend")]
    if item.get("jaar"):
        stukken.append(str(item["jaar"]))
    regel = "Bron: " + ", ".join(stukken)
    if item.get("basis"):
        regel += ". Basis: " + item["basis"]
    return regel


def schrijf_grafiekblad(item, pad):
    g = item["grafiek"]
    regels = []
    regels.append("# " + g.get("titel", item.get("onderwerp", item["id"])))
    regels.append("")
    regels.append("> Grafiekblad voor Root Presentation. Vervang hiermee de data van een")
    regels.append("> bestaande sjabloongrafiek. Bouw geen nieuwe grafiek als er een bruikbare staat.")
    regels.append("")
    regels.append("**Type:** " + g["type"] + "  ")
    regels.append("**Eenheid:** " + g.get("eenheid", "niet opgegeven") + "  ")
    regels.append("**Bronregel op de slide:** " + bronregel(item))
    regels.append("")
    if item.get("waarde"):
        regels.append("**Het cijfer in een zin:** " + item["waarde"])
        regels.append("")
    if item.get("uitleg"):
        regels.append(item["uitleg"])
        regels.append("")

    labels = g["reeksen"][0]["labels"]
    kop = "| Categorie | " + " | ".join(r["naam"] for r in g["reeksen"]) + " |"
    lijn = "|---|" + "---|" * len(g["reeksen"])
    regels.append(kop)
    regels.append(lijn)
    for i, label in enumerate(labels):
        cellen = []
        for r in g["reeksen"]:
            waarden = r["waarden"]
            cellen.append(str(waarden[i]) if i < len(waarden) else "")
        regels.append("| " + label + " | " + " | ".join(cellen) + " |")
    regels.append("")

    with open(pad, "w", encoding="utf-8") as f:
        f.write("\n".join(regels) + "\n")


def teken(item, pad):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib import font_manager

    beschikbaar = {f.name for f in font_manager.fontManager.ttflist}
    keuze = next((n for n in LETTERTYPES if n in beschikbaar), None)
    if keuze:
        plt.rcParams["font.family"] = keuze

    g = item["grafiek"]
    soort = g["type"]
    reeksen = g["reeksen"]
    labels = reeksen[0]["labels"]
    n = len(reeksen)

    fig, ax = plt.subplots(figsize=(9, 5), dpi=200)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")

    if soort in ("staaf", "gestapeld"):
        posities = range(len(labels))
        if soort == "gestapeld":
            bodem = [0.0] * len(labels)
            for i, r in enumerate(reeksen):
                ax.bar(posities, r["waarden"], bottom=bodem, width=0.55,
                       label=r["naam"], color=KLEUREN[i % len(KLEUREN)])
                bodem = [b + w for b, w in zip(bodem, r["waarden"])]
        else:
            breedte = 0.72 / n
            for i, r in enumerate(reeksen):
                verschoven = [p + (i - (n - 1) / 2) * breedte for p in posities]
                ax.bar(verschoven, r["waarden"], width=breedte,
                       label=r["naam"], color=KLEUREN[i % len(KLEUREN)])
        ax.set_xticks(list(posities))
        ax.set_xticklabels(labels)
        ax.yaxis.grid(True, color=RASTERKLEUR, linewidth=0.8)
        ax.set_axisbelow(True)

    elif soort == "staaf-horizontaal":
        posities = list(range(len(labels)))[::-1]
        breedte = 0.72 / n
        for i, r in enumerate(reeksen):
            verschoven = [p + (i - (n - 1) / 2) * breedte for p in posities]
            ax.barh(verschoven, r["waarden"], height=breedte,
                    label=r["naam"], color=KLEUREN[i % len(KLEUREN)])
        ax.set_yticks(posities)
        ax.set_yticklabels(labels)
        ax.xaxis.grid(True, color=RASTERKLEUR, linewidth=0.8)
        ax.set_axisbelow(True)

    elif soort in ("lijn", "lijn-dubbel"):
        for i, r in enumerate(reeksen):
            ax.plot(labels, r["waarden"], marker="o", linewidth=2.4,
                    markersize=6, label=r["naam"],
                    color=KLEUREN[i % len(KLEUREN)])
        ax.yaxis.grid(True, color=RASTERKLEUR, linewidth=0.8)
        ax.set_axisbelow(True)

    else:
        raise SystemExit("Onbekend grafiektype: " + soort)

    ax.set_title(g.get("titel", ""), color=TEKSTKLEUR, fontsize=13,
                 pad=16, loc="left")
    if g.get("eenheid"):
        if soort == "staaf-horizontaal":
            ax.set_xlabel(g["eenheid"], color=TEKSTKLEUR, fontsize=9)
        else:
            ax.set_ylabel(g["eenheid"], color=TEKSTKLEUR, fontsize=9)
    for kant in ("top", "right"):
        ax.spines[kant].set_visible(False)
    for kant in ("left", "bottom"):
        ax.spines[kant].set_color(RASTERKLEUR)
    ax.tick_params(colors=TEKSTKLEUR, labelsize=9, length=0)
    if n > 1:
        ax.legend(frameon=False, fontsize=9, loc="best")

    fig.text(0.01, 0.01, bronregel(item), fontsize=6.5, color="#6B7280")
    fig.tight_layout(rect=(0, 0.035, 1, 1))
    fig.savefig(pad, facecolor=fig.get_facecolor())
    plt.close(fig)


def verwerk(item, uitvoermap, zonder_png=False):
    os.makedirs(uitvoermap, exist_ok=True)
    basis = os.path.join(uitvoermap, item["id"])
    schrijf_grafiekblad(item, basis + ".md")
    gemaakt = [basis + ".md"]
    if not zonder_png:
        try:
            teken(item, basis + ".png")
            gemaakt.append(basis + ".png")
        except ImportError:
            print("  let op: matplotlib ontbreekt, alleen het grafiekblad is gemaakt.",
                  file=sys.stderr)
    return gemaakt


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--data", default=STANDAARD_DATA, help="pad naar kerncijfers.json")
    p.add_argument("--lijst", action="store_true", help="toon alle beschikbare grafieken")
    p.add_argument("--id", help="maak deze ene grafiek")
    p.add_argument("--alles", action="store_true", help="maak alle grafieken")
    p.add_argument("--eigen", help="pad naar een eigen databestand")
    p.add_argument("-o", "--uit", default="grafieken", help="uitvoermap")
    p.add_argument("--zonder-png", action="store_true", help="alleen het grafiekblad")
    a = p.parse_args()

    if a.eigen:
        with open(a.eigen, encoding="utf-8") as f:
            item = json.load(f)
        if "grafiek" not in item:
            raise SystemExit("Het eigen databestand heeft geen veld 'grafiek'.")
        item.setdefault("id", "eigen-grafiek")
        for pad in verwerk(item, a.uit, a.zonder_png):
            print(pad)
        return

    ruw, items = laad_kerncijfers(a.data)
    met_grafiek = [i for i in items if i.get("grafiek")]

    if a.lijst or not (a.id or a.alles):
        print("Grafieken in kerncijfers.json (%d van %d cijfers):\n" %
              (len(met_grafiek), len(items)))
        thema = None
        for i in met_grafiek:
            if i["_thema"] != thema:
                thema = i["_thema"]
                print("  " + thema.replace("_", " ").upper())
            print("    %-26s %s" % (i["id"], i["grafiek"]["titel"]))
        print("\nLeesregel: " + ruw["over_dit_bestand"]["leesregel"])
        return

    doel = met_grafiek if a.alles else [i for i in met_grafiek if i["id"] == a.id]
    if not doel:
        raise SystemExit("Geen grafiek met id: " + str(a.id))
    for item in doel:
        for pad in verwerk(item, a.uit, a.zonder_png):
            print(pad)


if __name__ == "__main__":
    main()
