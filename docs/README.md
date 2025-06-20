# HybMIL-FSelect – Classification Faiblement Supervisée des Lames WSI

Ce dépôt contient les scripts, modules et figures associés à l’approche **HybMIL-FSelect**, développée dans le cadre d’un mémoire de Master à la FST Béni Mellal. L’objectif est de classifier automatiquement des images histopathologiques (*Whole Slide Images* – WSI) en contexte de supervision faible.

---

## 1. Vue d'ensemble

**HybMIL-FSelect** repose sur une pipeline en quatre phases :

1. 📌 Découpage des WSIs en tuiles informatives (`create_patches_fp.py`)
2. 🧠 Encodage visuel avec le modèle pré-entraîné **UNI** (`extract_features_fp.py`)
3. 🧮 Filtrage des vecteurs par norme L2 et clustering KMeans (`filter_features_l2_kmeans.py`)
4. 🎯 Classification finale par **Multiple Instance Learning**, via **CLAM_MB** (`main.py`)

<p align="center">
  <img src="docs/pipeline HybMIL‑FSelec.drawio.png" alt="Pipeline HybMIL-FSelect" width="700">
</p>

---

## 2. Structure du projet

├── dataset_csv/ # Fichiers CSV d’annotations

├── dataset_modules/ # Prétraitement et loaders

├── heatmaps/ # Cartes d’attention générées

├── models/ # Implémentation de CLAM_MB

├── presets/ # Fichiers de configuration

├── topk/ # Extraction des tuiles top-attention

├── utils/, vis_utils/ # Fonctions utilitaires

├── wsi_core/ # Fonctions WSI & tiling

├── main.py # Script d’entraînement et test

├── create_patches_fp.py # Découpage en tuiles

├── extract_features_fp.py # Encodage UNI

├── filter_features_l2_kmeans.py

├── create_heatmaps.py # Visualisation attention

├── create_splits_seq.py # K-fold splits

└── tumor_vs_normal_dummy_clean.csv


---

## 3. Données utilisées

- 📌 **Dataset** : [SLN-Breast – TCIA](https://wiki.cancerimagingarchive.net/display/Public/TCGA-BRCA)
- 130 lames `.svs` scannées à 20x
- Annotations binaires globales (présence / absence de métastases)
- Données organisées sous forme : `images/ + CSV (slide_id, label)`

---

## 4. Instructions de lancement

### Étape 1 : Découpage des lames

```bash
python create_patches_fp.py --source ./images --save_dir ./patches
```
## Étape 2 : Encodage visuel

```bash
python extract_features_fp.py --model UNI --input ./patches --output ./features
```
## Étape 3 : Filtrage des vecteurs

```bash
python filter_features_l2_kmeans.py --input ./features --k 5
```
## Étape 4 : Entraînement CLAM_MB

```bash
python main.py --task train --config configs/hybmil.yaml
```
## Étape 5 : Génération de cartes d’attention

```bash
python create_heatmaps.py --model_path ./checkpoints/fold_1.pth
```

## 5. Résultats obtenus

| Métrique   | Moyenne ± Écart-type (10-fold CV) |
|------------|------------------------------------|
| Accuracy   | 93.3% ± 8.6%                       |
| F1-score   | 85.5% ± 19.2%                      |
| AUC        | 94.8% ± 7.7%                       |

<p align="center">
  <img src="docs/2beccbfc-c380-4ccc-b9eb-0383a72abd44.png" alt="Cartes d’attention WSI" width="650">
</p>

---

## 6. Configuration requise

- Python ≥ 3.8  
- PyTorch ≥ 1.10  
- OpenSlide  
- h5py  
- scikit-learn  
- pandas  

ℹ️ Voir `env.yml` ou `requirements.txt`.

---

## 7. Références principales

- Lu et al., *CLAM: Clustering-constrained Attention MIL* (2021)  
- Chen et al., *UNI: A Universal Image Encoder for Histopathology* (2024)  
- [TCIA – SLN-Breast Dataset](https://wiki.cancerimagingarchive.net/display/Public/TCGA-BRCA)

---

## 8. Auteure

**Nouhayla Skhounate**  
Master Intelligence Artificielle et Informatique Digitale  
Université Sultan Moulay Slimane – FST Béni Mellal  
Encadrée par **Pr. Abdelali Elmoufidi**

---

## 9. Citation

```bibtex
@mastersthesis{skhounate2025hybmil,
  title = {HybMIL-FSelect: Développement d'une approche hybride pour la classification faiblement supervisée de lames WSI},
  author = {Nouhayla Skhounate},
  school = {Université Sultan Moulay Slimane – FST Béni Mellal},
  year = {2025}
}
```


