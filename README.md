# Fraud Detection in Financial Transactions

Projet personnel de data science réalisé dans le cadre d'une compétition de détection de fraude sur des transactions financières.

## Contexte

L'objectif du projet est de construire un pipeline de bout en bout pour détecter des transactions frauduleuses à partir de variables temporelles, monétaires et comportementales. Les données d'entraînement et de test provenaient directement de la plateforme officielle de la compétition. Le fichier d'entraînement (`train.csv`) servait à l'apprentissage des modèles, tandis que le fichier de test (`test.csv`) était utilisé pour la génération des soumissions, ensuite évaluées sur la plateforme.

Pour récupérer les données de la compétition, veuillez consulter [data/README.md](data/README.md).

Sur cette première version, le feature engineering s'est principalement appuyé sur :

- l'analyse des périodes,
- l'analyse des montants,
- la détection d'incohérences de soldes.

Cette approche a permis d'obtenir une base de travail propre, mais elle ne couvrait pas encore l'ensemble des dimensions disponibles, notamment l'analyse plus complète des comptes et des interactions de transactions.

## Résultat de référence

Meilleure soumission obtenue dans la compétition : **PRAUC = 0.338204**.

Contexte d'entraînement et de prédiction :

- `train.csv` : 1 290 081 lignes
- `test.csv` : 430 100 lignes

Le score se situe en dessous des meilleures équipes du concours, dont les performances moyennes observées avoisinaient **0.355**. Ce résultat constitue donc une baseline sérieuse, mais encore perfectible.

## Approche retenue

Le projet est structuré en deux phases.

### Phase 1

Première exploration du problème avec les notebooks suivants :

- `notebooks/1.0-exploration.ipynb`
- `notebooks/1.1-modeling.ipynb`

Cette phase a servi à :

- comprendre la structure des données,
- construire les premières variables explicatives,
- entraîner des modèles de référence,
- mesurer les limites de l'approche initiale.

Cette phase est à l'origine du résultat de référence.

### Phase 2

Une deuxième phase est prévue pour reprendre le projet en imitant au plus près la démarche du concours. L'idée est de reconstruire une évaluation interne réaliste à partir d'un split temporel (périodes de transaction) sur la donnée d'entraînement :

- 75 premières périodes pour l'entraînement, soit 1 019 826 lignes ;
- 31 dernières périodes pour le test, soit 270 255 lignes.

Cette organisation permet de recréer une logique proche de celle de la compétition, avec un apprentissage sur les périodes historiques puis une validation sur les périodes plus récentes. L'objectif est ensuite d'enrichir le feature engineering, en particulier sur les comptes, les relations entre transactions et les signaux comportementaux absents de la première version.

Les notebooks attendus pour cette suite sont :

- `notebooks/2.0-exploration.ipynb`
- `notebooks/2.1-modeling.ipynb`

L'objectif de cette itération est d'intégrer les aspects manquants lors de la première phase, en particulier l'analyse des comptes et des relations entre transactions, afin d'évaluer plus proprement le gain réel apporté par ces nouvelles variables.

## Organisation finale du dépôt

```text
├── README.md                      # Présentation du projet, du contexte concours et de la méthodologie
├── data/                    
│   └── README.md                  # Instructions pour récupérer les fichiers de la compétition 
├── notebooks/               
│   ├── 1.0-exploration.ipynb      # Première phase d'analyse exploratoire
│   ├── 1.1-modeling.ipynb         # Première phase de modélisation
│   ├── 2.0-exploration.ipynb      # Deuxième phase d'analyse exploratoire
│   └── 2.1-modeling.ipynb         # Deuxième phase de modélisation                    
└── requirements.txt               # Dépendances Python du projet
```

## Reproductibilité

1. Créer et activer l'environnement Python.
2. Installer les dépendances listées dans `requirements.txt`.
3. Télécharger les données depuis la page officielle de la compétition.
4. Placer les fichiers dans l'arborescence locale décrite dans [data/README.md](data/README.md).
5. Exécuter les notebooks d'exploration puis de modélisation dans l'ordre.
