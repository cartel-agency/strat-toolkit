#!/usr/bin/env python3
"""Meet hoeveel tekst er in een placeholder past.

Tekstoverloop is de stille fout in een gegenereerd deck: het ziet er goed uit tot
slide 23. Instructies helpen daar niet tegen, meten wel. Deze module leidt uit de
layout af welke lettergrootte een placeholder krijgt en hoeveel tekens er dan in
zijn kader passen.

De schatting is bewust conservatief. Ze is bedoeld als grens waar de agent onder
blijft, niet als exacte voorspelling van de renderer.
"""

from pptx.util import Emu
from pptx.oxml.ns import qn

# Gemiddelde breedte van een teken als fractie van de lettergrootte, voor Arial.
TEKENBREEDTE = 0.50
# Regelhoogte als fractie van de lettergrootte.
REGELHOOGTE = 1.22
# Veiligheidsmarge: liever te weinig beloven dan een slide die overloopt.
MARGE = 0.88
# De schatting is bewust streng. Pas boven deze factor spreken we van een fout,
# daaronder van een aandachtspunt. Gemeten aan echte slides die net wél passen.
TOLERANTIE = 1.25

STANDAARD = {"TITLE": 40.0, "CENTER_TITLE": 40.0, "SUBTITLE": 20.0, "BODY": 14.0}


def _sz_uit(element):
    """Zoek de eerste expliciete lettergrootte onder een element, in punten."""
    if element is None:
        return None
    for pad in ("a:lvl1pPr/a:defRPr", "a:defRPr", "a:rPr"):
        gevonden = element.find(qn_pad(pad))
        if gevonden is not None and gevonden.get("sz"):
            return int(gevonden.get("sz")) / 100.0
    for kind in element.iter():
        if kind.get("sz"):
            try:
                return int(kind.get("sz")) / 100.0
            except (TypeError, ValueError):
                continue
    return None


def qn_pad(pad):
    return "/".join(qn(deel) for deel in pad.split("/"))


def lettergrootte(ph, master=None):
    """Effectieve lettergrootte van een placeholder, in punten."""
    soort = str(ph.placeholder_format.type or "BODY").split(" ")[0]

    # 1. expliciet op de placeholder zelf
    lst = ph._element.find(qn("p:txBody") + "/" + qn("a:lstStyle"))
    maat = _sz_uit(lst)
    if maat:
        return maat

    # 2. een run die al in de placeholder staat
    try:
        for para in ph.text_frame.paragraphs:
            if para.font.size is not None:
                return para.font.size.pt
            for run in para.runs:
                if run.font.size is not None:
                    return run.font.size.pt
    except Exception:
        pass

    # 3. de tekststijlen van de master
    if master is not None:
        stijlen = master._element.find(qn("p:txStyles"))
        if stijlen is not None:
            sleutel = "p:titleStyle" if "TITLE" in soort else "p:bodyStyle"
            maat = _sz_uit(stijlen.find(qn(sleutel)))
            if maat:
                return maat

    return STANDAARD.get(soort, 14.0)


def krimpt_mee(ph):
    """True als PowerPoint de tekst in dit vak automatisch verkleint."""
    try:
        body = ph._element.find(qn("p:txBody"))
        if body is None:
            return False
        return body.find(qn("a:bodyPr") + "/" + qn("a:normAutofit")) is not None
    except Exception:
        return False


def max_tekens(ph, master=None):
    """Schat het maximale aantal tekens dat in deze placeholder past."""
    if ph.width is None or ph.height is None:
        return None
    grootte = lettergrootte(ph, master)
    breedte_pt = Emu(ph.width).inches * 72.0
    hoogte_pt = Emu(ph.height).inches * 72.0
    per_regel = max(1, int(breedte_pt / (grootte * TEKENBREEDTE)))
    regels = max(1, int(hoogte_pt / (grootte * REGELHOOGTE)))
    ruimte = per_regel * regels * MARGE
    # Krimpt de tekst automatisch mee, dan mag er meer in. Niet onbeperkt: onder de
    # helft van de ontworpen lettergrootte gaat de slide er hoe dan ook slecht uit.
    if krimpt_mee(ph):
        ruimte *= 1.8
    return int(ruimte), int(grootte), regels


def meet_layout(layout, master=None):
    """Geef per placeholder de gemeten capaciteit."""
    uit = []
    for ph in layout.placeholders:
        meting = max_tekens(ph, master)
        fmt = ph.placeholder_format
        uit.append(
            {
                "idx": fmt.idx,
                "type": str(fmt.type).split(" ")[0] if fmt.type is not None else "",
                "naam": ph.name,
                "pt": meting[1] if meting else None,
                "regels": meting[2] if meting else None,
                "max_tekens": meting[0] if meting else None,
            }
        )
    return uit


BEELDSOORTEN = {"PICTURE", "CHART", "TABLE", "DATE", "SLIDE_NUMBER", "FOOTER"}


def rollen(layout, master=None):
    """Leid per placeholder af welke rol hij op de slide speelt.

    Nodig omdat de Cartel-layouts de zichtbare titel niet in de TITLE-placeholder
    zetten. Die staat op 9pt en draagt het navigatielijntje. De echte action title
    zit meestal in een BODY-placeholder van 35pt of meer. Een agent die dat niet
    weet, vult de verkeerde vakjes.
    """
    metingen = meet_layout(layout, master)
    uit = {}
    tekst_ph = []
    for m in metingen:
        if m["type"] in BEELDSOORTEN:
            uit[m["idx"]] = {"rol": m["type"].lower(), **m}
            continue
        if m["max_tekens"] is None:
            uit[m["idx"]] = {"rol": "onbekend", **m}
            continue
        # 9pt-elementen met een vaste plek zijn sjabloonwerk, geen inhoud
        if (m["pt"] or 0) <= 10:
            uit[m["idx"]] = {"rol": "sjabloonelement", **m}
            continue
        tekst_ph.append(m)

    if tekst_ph:
        # heel groot maar met plaats voor een handvol tekens: een cijfer of label
        labels = [m for m in tekst_ph if m["max_tekens"] < 8]
        rest = [m for m in tekst_ph if m["max_tekens"] >= 8]
        for m in labels:
            uit[m["idx"]] = {"rol": "kort label", **m}
        if rest:
            titel = max(rest, key=lambda m: m["pt"] or 0)
            uit[titel["idx"]] = {"rol": "action title", **titel}
            rest = [m for m in rest if m["idx"] != titel["idx"]]
        if rest:
            tekst = max(rest, key=lambda m: m["max_tekens"])
            uit[tekst["idx"]] = {"rol": "tekst", **tekst}
            rest = [m for m in rest if m["idx"] != tekst["idx"]]
        for m in rest:
            uit[m["idx"]] = {"rol": "bron" if (m["pt"] or 0) <= 14 else "extra", **m}
    return uit


def past(tekst, ph, master=None):
    """True als deze tekst binnen de placeholder past."""
    meting = max_tekens(ph, master)
    if meting is None:
        return True
    return len(tekst) <= meting[0]
