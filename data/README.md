# Données de la compétition

Ce dossier ne contient pas les fichiers CSV de la compétition dans le dépôt Git. Les données doivent être téléchargées localement depuis la page officielle du concours, puis déposées dans l'arborescence du projet pour les notebooks d'exploration et de modélisation.

## Pourquoi les données ne sont pas versionnées

Les fichiers de compétition sont volontairement exclus du dépôt pour plusieurs raisons :

- ils sont volumineux,
- ils peuvent être soumis à des règles de distribution spécifiques,
- ils n'ont pas vocation à être dupliqués dans l'historique Git,
- le dépôt doit rester léger et centré sur le code et la documentation.

Le fichier `.gitignore` du projet est configuré pour exclure les CSV, ainsi que les artefacts de l'environnement d'entraînement local.

## Fichiers attendus

À la racine du projet, les fichiers utilisés pour la compétition sont les suivants :

- `train.csv`
- `test.csv`

## Où récupérer les données ?

Téléchargez les fichiers depuis la page officielle de la compétition, dans la section dédiée aux données.

Les données proviennent de la compétition officielle **DATATOUR 2026** organisée par **Data Afrique Hub**. 

Pour y accéder :
1. Connectez-vous à votre espace participant sur la plateforme officielle de **Data Afrique Hub** (Créez-en un si vous n'en disposez pas). Lien de connection : [competition.dataafriquehub.org/login](https://competition.dataafriquehub.org/login)
2. Accédez à la section dédiée aux compétitions et sélectionnez le projet **DATATOUR 2026**.
3. Téléchargez les fichiers de transactions mis à disposition pour le volet **Données**.

## Vérification locale

Avant de lancer l'analyse, vérifier que les fichiers sont bien présents et lisibles par les notebooks :

- `train.csv`
- `test.csv`

Les notebooks de la première phase se trouvent dans `notebooks/1.0-exploration.ipynb` et `notebooks/1.1-modeling.ipynb`. La deuxième phase est prévue sous `notebooks/2.0-exploration.ipynb` et `notebooks/2.1-modeling.ipynb`.