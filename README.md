![Python](https://img.shields.io/badge/python-3.10-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/tkinter-GUI-lightgrey?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-3-003B57?logo=sqlite&logoColor=white)
![Matplotlib](https://img.shields.io/badge/matplotlib-data%20viz-11557c)
![Status](https://img.shields.io/badge/statut-terminé-green)
![Projet](https://img.shields.io/badge/projet-académique-blueviolet)
![YNOV](https://img.shields.io/badge/YNOV-Master-002B5C)

# Application de Bureau Intégrée — Pipeline de Traitement et d'Analyse Automatisée

> Projet final de programmation — Paris Ynov Campus, Master Data Science & Engineering  
> Module : **Python Avancé**

## Sommaire

- [Contexte du projet](#contexte-du-projet)
- [Fonctionnalités de l'application](#fonctionnalités-de-lapplication)
- [Architecture du projet](#architecture-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Gestion des tests unitaires](#gestion-des-tests-unitaires)
- [Livrables attendus](#livrables-attendus)
- [Auteur](#auteur)

---

## Contexte du projet

Ce projet consiste à concevoir une application de bureau Python modulaire et robuste à l'aide de l'interface graphique **Tkinter**. L'objectif principal est de lier deux pipelines de données indépendants et d'en assurer la gestion complète (téléchargement réseau, persistance en base de données, manipulations d'images, analyses statistiques avancées et génération de rapports) tout en sécurisant l'expérience utilisateur grâce à une gestion rigoureuse des exceptions.

---

## Fonctionnalités de l'application

L'application est divisée en deux grandes sections indépendantes, pilotables depuis l'interface graphique :

### Première partie : Base de données & Données JSON
* **Obtention des données Internet** : Téléchargement dynamique de données via l'API REST Countries au format JSON.
* **Stockage SQLite** : Persistance d'un sous-ensemble strict des attributs requis (`nom`, `taille`, `état`, `longueur`).
* **Gestion des conflits** : Prise en charge automatique du cas où la base de données n'est pas vide (alerte utilisateur et ajout sécurisé des données à la suite).
* **Analyses & Graphiques** : Bouton d'agrégation calculant la moyenne de la valeur `longueur` directement par requête SQL, et bouton d'affichage d'un graphique de distribution Matplotlib au sein de l'interface.
* **Menu contextuel** : Menu supérieur permettant d'effacer le contenu de la base et de personnaliser les thèmes d'affichage (Clair / Sombre).

### Deuxième partie : Génération du Rapport Word Automatisé
* **Extraction de contenu** : Téléchargement d'une œuvre textuelle depuis *Project Gutenberg* et isolation automatisée des métadonnées (titre, auteur) et du premier chapitre.
* **Traitement de texte & Statistiques** : Décompte des mots par paragraphe, arrondi statistique à la dizaine la plus proche, tri et distribution de fréquence.
* **Pipeline d'images (Pillow)** : Téléchargement asynchrone d'une illustration, recadrage centré, redimensionnement et incrustation en filigrane d'un logo noir et blanc pivoté.
* **Rapport Word de niveau professionnel (`python-docx`)** : Édition d'une page de garde stylisée (polices modifiées, gras, italique) et d'une page d'analyse intégrant le graphique de distribution Matplotlib, une table de synthèse, et un extrait de l'œuvre.

---

## Architecture du projet

```text
Projet-Python/
│
├── data/                       # Stockage des fichiers de données locaux
│   ├── projet.db               # Base de données SQLite3 locale
│   ├── graphique_paragraphes.png
│   ├── image_livre.png
│   └── rapport_livre.docx
│
├── src/                        # Code source de l'application
│   ├── __init__.py
│   ├── gui.py                  # Interface graphique Tkinter et menus
│   ├── pipeline_part1.py       # Traitement JSON, requêtes SQL et BDD
│   └── pipeline_part2.py       # Traitement Gutenberg, Pillow et rapport Word
│
├── tests/                      # Suite de tests unitaires automatisés
│   ├── __init__.py
│   ├── test_part1.py           # Tests unitaires de la base de données
│   └── test_part2.py           # Tests unitaires de l'analyse textuelle
│
├── main.py                     # Point d'entrée de l'application
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Installation

### Prérequis
- Python 3.10 ou supérieur
- pip

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/L-em-hash/Projet-Python-B3.git
cd Projet-Python

# 2. Installer les dépendances
pip install -r requirements.txt
```

---

## Utilisation

### Lancer l'application desktop

```bash
python src/gui.py 
```

L'application s'ouvre avec deux onglets :
- **Partie 1** : cliquez sur "Télécharger les données" puis "Afficher la moyenne" ou "Afficher le graphique"
- **Partie 2** : cliquez sur "Lancer le pipeline" pour générer le rapport Word automatiquement

Le rapport Word est sauvegardé dans `data/rapport_livre.docx`.

---

## Gestion des tests unitaires

Les tests couvrent les fonctions critiques des deux pipelines.

```bash
# Lancer tous les tests
python -m pytest tests/ -v

# Lancer uniquement les tests partie 1
python -m pytest tests/test_part1.py -v

# Lancer uniquement les tests partie 2
python -m pytest tests/test_part2.py -v
```

### Résultats attendus

```
tests/test_part1.py::TestPartie1::test_insertion_et_aggregation   PASSED
tests/test_part2.py::TestProjetPythonAvance::test_compter_mots_paragraphes  PASSED
tests/test_part2.py::TestProjetPythonAvance::test_extraire_metadonnees      PASSED
tests/test_part2.py::TestProjetPythonAvance::test_extraire_premier_chapitre PASSED
tests/test_part2.py::TestProjetPythonAvance::test_statistiques              PASSED
5 passed
```

---

## Livrables attendus

| Livrable | Statut |
|---|---|
| Application desktop Tkinter (Partie 1) |  |
| Téléchargement et stockage JSON/SQLite |  |
| Agrégation SQL + graphique intégré |  |
| Pipeline Gutenberg + rapport Word (Partie 2) |  |
| Tests unitaires (pytest) |  |
| Gestion des exceptions |  |
| GitHub |  |

---

## Auteur

**LAWSON-LARTEGO Nadou Emmanuella** — Module Python Avancé — 2025/2026