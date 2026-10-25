# 04 — Guide de production visuelle (GPT / ChatGPT Images)

> Objectif : que les 600 épisodes aient **le même style** et que **chaque personnage reste reconnaissable** d'une image à l'autre.
> Honnêteté : aucun générateur d'images ne garantit une cohérence parfaite à 100 %. Ce protocole la maximise (≈ 85–90 %) et prévoit les retouches.

---

## 1. Spécifications techniques

| Élément | Valeur |
|--------|--------|
| Format de génération | **1024 × 1536** (portrait) — le plus proche du scroll vertical |
| Format final webtoon | **800 px de large**, tranches de **≤ 1280 px** de haut |
| Cases par épisode | 40–60 (≈ 18–30 images à recadrer/combiner) |
| Texte (bulles, SFX, Lawh) | **Jamais généré par l'IA** → ajouté à la main (Canva, Photopea, Clip Studio, Photoshop) |
| Fichiers de référence | `REF_<code>.png` pour chaque personnage (fiche turnaround) |

---

## 2. Préfixe de style (à coller en TÊTE de CHAQUE prompt)

```
Korean webtoon (manhwa) style, high-contrast dramatic digital painting with crisp clean line art and soft cel-shading, cinematic lighting, very deep blacks, warm ochre and terracotta Sahelian palette with indigo shadows and glowing gold-ink accents (#F2C14E), dynamic camera angles, vertical webtoon composition. African and Arab setting, realistic proportions, expressive faces. No text, no letters, no speech bubbles, no watermark, no logo.
```

## 3. Négatifs / interdits (à ajouter en FIN de prompt)

```
Avoid: any text or letters, speech bubbles, chibi/cartoon proportions, photorealistic photography look, western superhero comic style, extra fingers, deformed hands, mismatched eyes, changing the character's hairstyle/scarf/scar/glasses, white-washed or lightened skin tones, generic fantasy elf/medieval European armor.
```

## 4. Palette officielle

| Usage | Couleur | Hex |
|------|---------|-----|
| Noir profond (fonds, ombres) | Nuit | `#0B0B14` |
| Indigo (Gardiens, écharpe, ombres froides) | Indigo | `#2B3A7A` / `#1F2A5C` |
| Or d'encre (pouvoir, glyphes) | Or | `#F2C14E` |
| Ocre / sable (décor) | Ocre | `#C8903E` |
| Terre cuite (banco) | Terre | `#A8532F` |
| Ivoire (Lawh) | Ivoire | `#F4EBD9` |
| Argent-bleu (Nour) | Argent-bleu | `#8FB8DE` |
| Rouge Fièvre (Oum-Humma) | Braise | `#C23B22` |
| Blanc Page (Al-Bayaad) | Blanc | `#FFFFFF` |

**Codes couleur par pouvoir** : Idriss = or · Nour = argent-bleu · Safiya = vert-argent (Nyama) · Yaw = ocre · Trônes = couleur de leur fléau · Al-Bayaad = blanc.

---

## 5. Protocole de cohérence (étape par étape)

### Étape 0 — Créer un projet / GPT personnalisé
Dans ChatGPT : créer un **GPT personnalisé « Sans-Ligne Studio »** (ou un Projet) et y coller les **Instructions** de la section 9. Y téléverser `03_personnages.md` et les images de référence.

### Étape 1 — Générer les **fiches de référence** (une seule fois)
Pour chaque personnage principal, demander une **fiche turnaround** :

```
[STYLE PREFIX]
Character reference sheet (turnaround) on a neutral dark-grey background: full-body FRONT view, SIDE view, BACK view, plus a row of 6 head close-ups with expressions (neutral, smiling, angry, sad, determined, shocked). Consistent proportions and outfit across all views.
[CHARACTER BLOCK from 03_personnages.md, unchanged]
[NEGATIVE]
```

→ Choisir la meilleure image, la renommer `REF_ID_phaseA.png`, etc. **Une fiche par personnage par phase de tenue.**
Pour les Gardiens : même méthode (`REF_AM.png`, …).

### Étape 2 — Générer l'**ancre de style**
Une illustration clé (ex. Idriss dans le Faubourg des Sables à l'aube) → `STYLE_ANCHOR.png`. Elle fixe le rendu pour toute la série.

### Étape 3 — Générer un épisode
1. **Une conversation par épisode** (le contexte reste).
2. Téléverser : `STYLE_ANCHOR.png` + les `REF_*.png` des personnages **présents dans l'épisode**.
3. Message d'ouverture :
   > « Ces images sont des références STRICTES. Garde exactement les mêmes visages, coiffures, tenues, couleurs. Je vais te donner des cases une par une. »
4. Envoyer **case par case** avec le gabarit de la section 6.
5. Si un personnage dérive : renvoyer sa fiche + « *Correct the character to exactly match reference image X* ».

### Étape 4 — Contrôle qualité (checklist section 8)

### Étape 5 — Assemblage et lettrage
Découper/réarranger dans Clip Studio / Photoshop / Canva ; ajouter bulles, SFX et fenêtres Lawh ; exporter à 800 px.

---

## 6. Gabarit de prompt d'une case

```
[STYLE PREFIX]
SHOT: <plan : extreme close-up / close-up / medium / full / wide / low-angle / high-angle / over-the-shoulder / bird's-eye>
SCENE: <lieu + heure + météo + ambiance lumineuse>
CHARACTERS: <bloc personnage 1 EXACT>. <bloc personnage 2 EXACT>.
ACTION: <ce qui se passe, posture, expression>
COMPOSITION: <espace vide pour bulles ? silhouette ? split panel ?>
LIGHTING/COLOR: <palette, source de lumière>
[NEGATIVE]
```

### Vocabulaire de plans (pour le storyboard)
| Code | Plan |
|------|------|
| GP | Gros plan visage |
| TGP | Très gros plan (yeux, main) |
| PM | Plan moyen |
| PA | Plan américain |
| PE | Plan d'ensemble / large |
| CP | Contre-plongée (puissance) |
| PL | Plongée (vulnérabilité) |
| OTS | Par-dessus l'épaule |
| SPL | Pleine page / splash |
| SIL | Silhouette |
| VID | Case vide / silence |

---

## 7. Prompts spéciaux

### 7.1 Fenêtre du Lawh (à générer SANS texte, puis écrire le texte à la main)
```
[STYLE PREFIX]
A floating translucent parchment tablet (sand-ivory #F4EBD9) with a border of ornate golden Arabic-style calligraphic arabesques and thin gold Tifinagh dots, glowing softly, hovering in a dark room, blank interior surface left EMPTY for text overlay, subtle gold dust particles.
```

### 7.2 Gardien en action
```
[STYLE PREFIX]
[GARDIEN BLOCK exact]. Dramatic low-angle shot, body made of indigo-black smoke, golden calligraphic glyphs flowing along the silhouette, glowing gold eyes, ink droplets floating in the air, background dark.
```

### 7.3 Splash pleine page (moment iconique)
```
[STYLE PREFIX]
Epic full-page splash, extreme perspective, <scene>, hero in the center lit from below by gold ink light, a massive crowd of ink-smoke guardians behind him, debris and sand floating, dramatic scale contrast.
```

### 7.4 Silhouette
```
[STYLE PREFIX]
Pure black silhouette of <character>, only the golden eyes and golden glyph lines glowing, against a huge pale moon or desert sky.
```

### 7.5 Case vide (silence)
```
[STYLE PREFIX] Nearly empty dark panel with a single small detail: <detail>. Lots of negative space.
```

---

## 8. Checklist de contrôle qualité (avant d'accepter une image)

- [ ] Idriss : **cicatrice sourcil gauche**, **écharpe indigo**, **cauri** ? (+ glyphe main droite après ép. 9)
- [ ] Nour : **lunettes rondes**, tresses à perles ?
- [ ] Safiya : **fibule argent**, **tatouage menton** ?
- [ ] Yaw : **bouclier Gye Nyame** ?
- [ ] Peaux **non éclaircies** ; traits africains/arabes respectés.
- [ ] Mains : 5 doigts, correctes ?
- [ ] Aucun texte généré.
- [ ] Palette dans les codes ?
- [ ] Cohérence de tenue avec la phase (voir fiche) ?
- [ ] Gardiens : fumée **indigo + glyphes or + yeux or** ?

---

## 9. Instructions à coller dans le GPT personnalisé « Sans-Ligne Studio »

```
Tu es l'illustrateur-assistant du webtoon "SANS-LIGNE" (600 épisodes).
RÔLE : générer des images de cases pour un webtoon vertical, avec une cohérence visuelle stricte.
RÈGLES :
1. Toujours commencer chaque prompt d'image par le PRÉFIXE DE STYLE officiel (fichier 04).
2. Utiliser les BLOCS DE PROMPT des personnages (fichier 03) sans les reformuler.
3. Les images de référence téléversées priment : mêmes visages, coiffures, tenues, couleurs.
4. Ne jamais générer de texte, bulle, SFX ni logo dans l'image.
5. Respecter la palette (ocre, terre cuite, indigo, noir, or d'encre).
6. Peaux africaines et arabes naturelles, jamais éclaircies. Représentations respectueuses des cultures.
7. Gardiens : fumée indigo-noire, glyphes calligraphiques or, yeux or.
8. Idriss : cicatrice en croissant sourcil gauche, écharpe indigo, cauri, glyphe or main droite (après l'épisode 9).
9. Si une demande contredit la bible, signale-le avant de générer.
10. Format : 1024x1536 portrait par défaut. Case par case.
FORMAT DE RÉPONSE : 1 image par case, puis 1 ligne "OK / à corriger : …".
```

---

## 10. Automatisation incluse dans ce dossier

| Outil | Rôle |
|-------|------|
| `outils/personnages.json` | **Source canon** des blocs de prompt (personnages, tenues par phase, plans, préfixe de style, négatifs) |
| `episodes/epNNN.json` | Un épisode = liste de cases (plan, décor, personnages, action, lumière, texte, SFX) |
| `outils/build_prompts.py` | Transforme un épisode en **storyboard FR** + **un prompt complet par case** à copier-coller |
| `outils/build_index.py` | Recalcule `episodes_index.csv` (600 lignes) et vérifie la numérotation |

Commande type : `python3 outils/build_prompts.py episodes/ep001.json` (ou `--from 1 --to 10` pour un lot).
Si un personnage dérive visuellement, on corrige **une seule fois** dans `personnages.json` et on régénère.

---

## 11. Estimation de production (indicative)

| Étape | Par épisode |
|------|-------------|
| Script détaillé (cases + dialogues) | Claude (moi) — 1 épisode ≈ 1 message |
| Images à générer | 18–30 |
| Retouches / lettrage | 1–2 h manuelles |
| Cadence conseillée | **2 épisodes / semaine** → 300 semaines (≈ 5,8 ans) ; ou lots de 10 épisodes par chapitre |

> Astuce : produire d'abord les **Chapitres 1 et 2 (ép. 1–20)** pour valider le style, puis industrialiser.
