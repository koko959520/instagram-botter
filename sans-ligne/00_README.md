# SANS-LIGNE — Webtoon de 600 épisodes

> *« Personne n'est écrit avant de naître. Mais tout le monde peut écrire. »*

**Pitch** : Idriss Keïta, porteur de rang Sable — le plus faible des Éveillés d'Al-Wagadou — survit seul à un massacre dans un caravansérail hanté et reçoit le **Calame**, la plume du Premier Scribe. Il monte en niveau, inscrit le nom de ses ennemis pour en faire des **Gardiens d'encre**, traverse l'Afrique et le monde arabe contre les **Neuf Trônes**… et découvre que le monde ne se sauve pas seul.

**Format** : 12 Livres × 5 chapitres × 10 épisodes = **600 épisodes** · action-fantasy sombre · inspiration structurelle : *Solo Leveling* (grammaire, pas contenu) · univers : Sahel, Maghreb, Nil, Afrique de l'Est/Ouest/Australe, péninsule arabique.

---

## Contenu du dossier

| Fichier | Contenu |
|---------|---------|
| `01_analyse_solo_leveling.md` | Analyse complète : structure, mécanismes, esthétique, faiblesses, ce qu'on garde / change |
| `02_bible_univers.md` | Monde, système de pouvoir (Calame/Lawh), cosmologie, glossaire, motifs |
| `03_personnages.md` | ~40 personnages, **codes**, ancres visuelles, **blocs de prompt** anglais |
| `04_guide_visuel_GPT.md` | Style, palette, protocole de cohérence, gabarits de prompts, instructions de GPT personnalisé |
| `05_structure_12_livres.md` | Vue d'ensemble, 60 chapitres, fils rouges, ledger des morts, promesses/paiements |
| `livres/livre_01…12_*.md` | **Les 600 épisodes** : titre, résumé, personnages, type, par chapitre |
| `episodes_index.csv` | Les 600 épisodes en tableau (Excel / Notion / Airtable) |
| `episodes/ep001.json` | **Épisode 1 découpé en 42 cases** (pilote de production) |
| `episodes/ep001_storyboard.md` | Storyboard FR de l'épisode 1 |
| `episodes/ep001_prompts.md` | **42 prompts prêts à coller dans ChatGPT** |
| `outils/personnages.json` | Source canon des blocs de prompt |
| `outils/build_prompts.py` | Génère storyboard + prompts depuis un épisode JSON |
| `outils/build_index.py` | Régénère le CSV et vérifie les 600 numéros |

---

## Les 12 Livres

| Livre | Ép. | Titre | Lieu | Trône / menace |
|------|-----|-------|------|----------------|
| 1 | 1–50 | **Le Porteur** | Al-Wagadou | Sphinx, Seigneur du Puits |
| 2 | 51–100 | **Le Sceau de Fer** | Sahel, Taoudenni | Roi du Sel, Caravane d'Or |
| 3 | 101–150 | **Les Remparts de l'Atlas** | Maroc | Hibr, Moustapha |
| 4 | 151–200 | **Le Minaret des Cent Épreuves** | Le Caire | Pharaon sans Visage |
| 5 | 201–250 | **La Nuée** | Afrique de l'Est | Abou-Jarad (Faim) |
| 6 | 251–300 | **Le Serpent de Bida** | Al-Wagadou | Bida, Moustapha |
| 7 | 301–350 | **Mami Wata** | Lagos, Bénin | Oum-Humma (Fièvre) |
| 8 | 351–400 | **L'Or Maudit** | Afrique australe | Dhahab (Or) |
| 9 | 401–450 | **Les Sables de Wabar** | Arabie | Sarab-Roi (Mirage), Veilleurs |
| 10 | 451–500 | **Le Grand Siège** | Monde | Harb (Guerre), Samoum (Simoun) |
| 11 | 501–550 | **La Cité de Cuivre** | Ghayb | Sakt (Silence), Zamma (Soif) |
| 12 | 551–600 | **La Page Blanche** | Bibliothèque des Brouillons | Al-Bayaad |

---

## Comment produire un épisode (workflow)

1. **Une fois** : suivre `04_guide_visuel_GPT.md` §5 → générer les fiches de référence (`REF_*.png`) et l'ancre de style.
2. **Par épisode** : demander à Claude le découpage en cases (même format que `ep001.json`).
3. `python3 outils/build_prompts.py episodes/epNNN.json` → storyboard + prompts.
4. Coller les prompts case par case dans ChatGPT (une conversation par épisode, références téléversées).
5. Assembler + lettrage (bulles, SFX, fenêtres Lawh) à la main dans Canva / Clip Studio / Photoshop.

Recommandation : produire **les épisodes 1–20** (chapitres 1–2) pour valider le style avant d'industrialiser.
