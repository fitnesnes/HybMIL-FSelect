# HybMIL-FSelect

**HybMIL-FSelect** est une pipeline modulaire et faiblement supervisée, conçue pour la classification binaire des lames histologiques numériques (*Whole Slide Images*, WSI). Elle combine un encodeur visuel pré-entraîné (**UNI**), une phase de sélection de caractéristiques (norme L2 + clustering KMeans) et un classificateur attentionnel basé sur le **Multiple Instance Learning** (MIL) via le modèle **CLAM_MB**.

---

## 🧠 Présentation

Les WSIs sont des images médicales de très haute résolution, souvent annotées uniquement au niveau global, ce qui limite l’application des techniques supervisées classiques. **HybMIL-FSelect** propose une approche hybride légère et interprétable :

- 📌 Découpage des WSIs en tuiles (patches)
- 🧠 Encodage des patches par le modèle **UNI**
- 📉 Sélection des vecteurs informatifs (filtrage L2 + KMeans)
- 🎯 Classification par attention avec **CLAM_MB**

<p align="center">
  <img src="images/pipeline_hybmil.png" alt="Pipeline HybMIL-FSelect" width="700">
</p>

---

## 🔧 Installation

```bash
git clone https://github.com/utilisateur/HybMIL-FSelect.git
cd HybMIL-FSelect
pip install -r requirements.txt
