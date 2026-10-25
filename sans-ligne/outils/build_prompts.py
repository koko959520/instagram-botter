#!/usr/bin/env python3
"""Génère, à partir d'un épisode JSON, le storyboard (FR) et les prompts d'images (EN)
prêts à coller dans ChatGPT, en réutilisant les blocs canon de personnages.

Usage :
    python3 outils/build_prompts.py episodes/ep001.json
    python3 outils/build_prompts.py episodes/ep001.json --from 1 --to 10
Sorties (dans le dossier de l'épisode) :
    ep001_storyboard.md   storyboard lisible (français)
    ep001_prompts.md      un prompt complet par case (anglais)
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def character_block(chars, code, outfit_key, opts, without=()):
    """Bloc canon d'un personnage. `without` retire des accessoires (ex. écharpe accrochée au mur)."""
    c = chars[code]
    if "core" in c:
        parts = [c["core"]] + [v for k, v in c.get("acc", {}).items() if k not in without]
    else:
        parts = [c["base"]]
    outfit = c.get("outfits", {}).get(outfit_key, "")
    if outfit:
        parts.append(outfit)
    for o in opts:
        extra = c.get("optional", {}).get(o)
        if extra:
            parts.append(extra)
    return ", ".join(parts) + "."


def build_prompt(panel, chars):
    prefix = chars["_style_prefix"]
    negative = chars["_negative"]
    shot = chars["_shots"].get(panel["shot"], panel["shot"])
    lines = [prefix, f"SHOT: {shot}", f"SCENE: {panel['scene']}"]
    blocks = []
    for code in panel.get("chars", []):
        outfit_key = panel.get("outfit", {}).get(code, "A")
        opts = panel.get("opt", {}).get(code, [])
        without = panel.get("without", {}).get(code, [])
        blocks.append(character_block(chars, code, outfit_key, opts, without))
    if blocks:
        lines.append("CHARACTERS: " + " ".join(blocks))
    lines.append(f"ACTION: {panel['action']}")
    lines.append(f"LIGHTING/COLOR: {panel['light']}")
    lines.append(negative)
    return "\n".join(lines)


def refs_needed(ep, chars):
    codes = []
    for p in ep["panels"]:
        for c in p.get("chars", []):
            if c not in codes:
                codes.append(c)
    return [(c, chars[c]["name"]) for c in codes]


def write_storyboard(ep, chars, out, panels):
    t = [f"# Épisode {ep['episode']:03d} — {ep['titre']}", "",
         f"**Livre {ep['livre']} · Chapitre {ep['chapitre']}** · {len(ep['panels'])} cases", "",
         f"**Résumé** : {ep['resume']}", "",
         f"**Intention** : {ep['intention']}", ""]
    t.append("| N° | Plan | Description | Texte / dialogue | SFX |")
    t.append("|---|------|-------------|------------------|-----|")
    for p in panels:
        texte = p.get("texte", "").replace("|", "/")
        t.append(f"| {p['n']} | {p['shot']} | {p['fr']} | {texte} | {p.get('sfx', '')} |")
    out.write_text("\n".join(t) + "\n", encoding="utf-8")


def write_prompts(ep, chars, out, panels):
    t = [f"# Prompts — Épisode {ep['episode']:03d} : {ep['titre']}", "",
         "## Avant de commencer — images de référence à téléverser dans la conversation", ""]
    for code, name in refs_needed(ep, chars):
        t.append(f"- `REF_{code}.png` — {name}")
    t += ["- `STYLE_ANCHOR.png` — ancre de style", "",
          "> Message d'ouverture à coller : *« Ces images sont des références STRICTES. "
          "Garde exactement les mêmes visages, coiffures, tenues et couleurs. "
          "Je vais te donner les cases une par une. »*", ""]
    for p in panels:
        t.append(f"## Case {p['n']:02d} — {p['shot']}")
        if p.get("texte"):
            t.append(f"*Texte à ajouter après coup (jamais dans l'image)* : {p['texte']}")
        t.append("")
        t.append("```")
        t.append(build_prompt(p, chars))
        t.append("```")
        t.append("")
    out.write_text("\n".join(t) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode", help="chemin du JSON d'épisode")
    ap.add_argument("--from", dest="start", type=int, default=1)
    ap.add_argument("--to", dest="end", type=int, default=10 ** 6)
    args = ap.parse_args()

    ep_path = Path(args.episode)
    ep = load(ep_path)
    chars = load(ROOT / "personnages.json")

    unknown = {c for p in ep["panels"] for c in p.get("chars", []) if c not in chars}
    if unknown:
        sys.exit(f"Personnages inconnus : {sorted(unknown)}")

    panels = [p for p in ep["panels"] if args.start <= p["n"] <= args.end]
    stem = ep_path.with_suffix("")
    write_storyboard(ep, chars, Path(f"{stem}_storyboard.md"), panels)
    write_prompts(ep, chars, Path(f"{stem}_prompts.md"), panels)
    print(f"{len(panels)} cases -> {stem}_storyboard.md, {stem}_prompts.md")


if __name__ == "__main__":
    main()
