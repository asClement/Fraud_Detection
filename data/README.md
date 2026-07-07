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

Si vous travaillez depuis une plateforme de concours, la procédure habituelle est la suivante :

1. Ouvrir la page du concours.
2. Aller dans l'onglet des données.
3. Accepter les éventuelles conditions d'utilisation.
4. Télécharger les fichiers fournis par l'organisation.
5. Placer les CSV à la racine du projet ou dans le répertoire attendu par les notebooks.

## Vérification locale

Avant de lancer l'analyse, vérifier que les fichiers sont bien présents et lisibles par les notebooks :

- `train.csv`
- `test.csv`

Les notebooks de la première phase se trouvent dans `notebooks/1.0-exploration.ipynb` et `notebooks/1.1-modeling.ipynb`. La deuxième phase est prévue sous `notebooks/2.0-exploration.ipynb` et `notebooks/2.1-modeling.ipynb`.