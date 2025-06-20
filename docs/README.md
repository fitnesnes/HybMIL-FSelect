# HybMIL-FSelect : Classification faiblement supervisée des images WSI

Ce projet propose une méthode de classification automatique des lames histologiques entières (WSI) sous supervision faible. Il repose sur une approche hybride combinant :

- Un encodage visuel avec le modèle pré-entraîné UNI
- Un filtrage stratégique basé sur la norme L2 et le clustering KMeans
- Une classification via le modèle CLAM_MB (Multiple Instance Learning)

## Pipeline proposé

![Pipeline](images/pipeline_hybmil.png)

## Résultats expérimentaux

| Métrique    | Moyenne ± Écart-type |
|-------------|----------------------|
| Accuracy    | 93.3% ± 8.6%         |
| AUC         | 94.8% ± 7.7%         |
| F1-score    | 85.5% ± 19.2%        |

## Exemple de visualisation

![Cartes d'attention](images/attention_maps.png)

## Données utilisées

- **Dataset** : SLN-Breast (TCIA)
- 130 Whole Slide Images (WSI)
- 78 patientes – annotations globales (présence/absence de métastase)

## Auteur

- Nouhayla Skhounate – Master AIDC, FST Béni Mellal
- Encadrée par Pr. Abdelali Elmoufidi

