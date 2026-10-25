#!/usr/bin/env python3
"""Construit episodes_index.csv à partir des tableaux de livres/*.md et vérifie la numérotation.

Usage : python3 outils/build_index.py
"""
import csv
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
LIVRES = sorted((BASE / "livres").glob("livre_*.md"))

ROW = re.compile(r"^\|\s*(\d{1,3})\s*\|(.+)\|\s*$")
CHAP = re.compile(r"^##\s+Chapitre\s+(\d+)\s+—\s+(.+?)\s+\((\d+)–(\d+)\)")
BOOK = re.compile(r"^#\s+LIVRE\s+(\d+)\s+—\s+(.+?)\s+\(")


def main():
    rows = []
    for path in LIVRES:
        livre = titre_livre = chap = titre_chap = None
        for line in path.read_text(encoding="utf-8").splitlines():
            m = BOOK.match(line)
            if m:
                livre, titre_livre = int(m.group(1)), m.group(2)
                continue
            m = CHAP.match(line)
            if m:
                chap, titre_chap = int(m.group(1)), m.group(2)
                continue
            m = ROW.match(line)
            if m and livre and chap:
                cells = [c.strip() for c in m.group(2).split("|")]
                if len(cells) != 4:
                    sys.exit(f"{path.name}: ligne mal formée pour l'ép. {m.group(1)}: {len(cells)} colonnes")
                titre, resume, persos, typ = cells
                rows.append({
                    "episode": int(m.group(1)),
                    "livre": livre, "titre_livre": titre_livre,
                    "chapitre": chap, "titre_chapitre": titre_chap,
                    "titre": titre, "resume": resume,
                    "persos": persos, "type": typ,
                })
    nums = [r["episode"] for r in rows]
    expected = list(range(1, 601))
    if nums != expected:
        missing = sorted(set(expected) - set(nums))
        extra = sorted({n for n in nums if nums.count(n) > 1})
        sys.exit(f"Numérotation invalide : {len(nums)} épisodes ; manquants={missing[:20]} doublons={extra[:20]}")

    # contrôle de rythme : cliffhanger au 10e épisode de chaque chapitre
    bad = [r["episode"] for r in rows if r["episode"] % 10 == 0 and r["type"] != "CLIFF"]
    out = BASE / "episodes_index.csv"
    with out.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"OK : {len(rows)} épisodes -> {out.name}")
    if bad:
        print("Attention, fin de chapitre sans type CLIFF :", bad)


if __name__ == "__main__":
    main()
