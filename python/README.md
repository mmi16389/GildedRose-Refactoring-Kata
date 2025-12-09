
# ![Gilded Rose – Refactoring Python](logo.png)

> ### Ce projet est un refactoring complet du célèbre kata **Gilded Rose**.
L’objectif est de restructurer la logique de mise à jour des objets sans modifier l’API publique (`Item`, `GildedRose`), tout en rendant le code plus clair, plus testé, et plus facile à étendre.

Les fonctionnalités couvertes :

- gestion des objets standard,
- gestion des objets spéciaux :
  - **Aged Brie**,
  - **Sulfuras, Hand of Ragnaros**,
  - **Backstage passes to a TAFKAL80ETC concert**,
  - objets **Conjured** (dégradation accélérée),
- conservation stricte du comportement d’origine (tests de non-régression),
- architecture orientée **stratégies** (pattern Strategy) avec une fabrique `get_updater_for`.

---

## Objectifs du refactoring

- Supprimer le gros bloc de conditions dans `update_quality`.
- Introduire une **architecture claire et découplée**, basée sur des stratégies (`ItemUpdater`).
- Faciliter l’ajout de nouveaux types d’objets sans modifier `GildedRose`.
- Sécuriser le comportement via :
  - des tests unitaires,
  - des tests d’approval/golden master.
- Documenter l’architecture dans un fichier dédié : `ARCHITECTURE.md`.

---

## Organisation du repository

```text
GildedRose-Refactoring-Kata/
└── python/                            # Implémentation Python du kata
    ├── gilded_rose.py                 # API publique (Item, GildedRose)
    ├── gilded_rose/
    │   ├── updaters/                  # Stratégies de mise à jour
    │   │   ├── base.py                # Interface commune ItemUpdater
    │   │   ├── standard.py            # Comportement des objets standard
    │   │   ├── aged_brie.py           # Règles spécifiques Aged Brie
    │   │   ├── sulfuras.py            # Règles spécifiques Sulfuras
    │   │   ├── backstage.py           # Règles spécifiques Backstage passes
    │   │   ├── conjured.py            # Règles spécifiques Conjured
    │   │   └── __init__.py            # Fabrique get_updater_for + mapping
    │   │
    │   └── __init__.py                # Package Python
    │
    ├── tests/
    │   ├── test_gilded_rose.py        # Tests de règles métier (comportement par type d’objet)
    │   ├── test_gilded_rose_approvals.py
    │   └── approved_files/            # Fichiers approuvés pour les tests d’approval
    │
    ├── texttest_fixture.py            # Script fourni par le kata (simulation sur plusieurs jours)
    ├── ARCHITECTURE.md                # Documentation détaillée de l’architecture
    └── requirements.txt               # Dépendances Python

```
---
## Comment ça fonctionne

Le cœur du fonctionnement est le suivant :

- La classe **GildedRose** reçoit une liste d’objets `Item`.
- Pour chaque `Item`, elle demande à une fabrique (`get_updater_for`) de lui fournir la bonne stratégie de mise à jour.
- Cette stratégie applique les règles métiers associées au type d’objet (standard, Brie, Sulfuras, etc.).
- Le comportement global reste identique à l’implémentation d’origine, mais il est maintenant structuré par type d’objet.
- Toutes les décisions métier sont encapsulées dans des classes dédiées (`StandardItemUpdater`, `AgedBrieUpdater`, etc.), ce qui permet un code plus lisible et plus facilement extensible.
---

# Pour commencer

## Prérequis

Assurez-vous d'avoir installé :

-   **Python 3.11+** (ou version compatible avec le projet)
-   **pip** pour la gestion des dépendances

----

## Installation

Positionnez-vous dans le dossier `python/` du kata :

``` bash
cd python
```

### 1. Créer un environnement virtuel

``` bash
python -m venv .env
```

#### macOS / Linux

``` bash
source .env/bin/activate
```

#### Windows (PowerShell)

``` powershell
.env\Scripts\Activate.ps1
```

### 2. Installer les dépendances

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Lancer les tests

Tout le refactoring est couvert par des tests automatisés.

### 1. Lancer toute la suite de tests

``` bash
pytest
```

Cela exécute :

-   les tests métier (`tests/test_gilded_rose.py`) -> Legacy
-   les tests d'approval / golden master
    (`tests/test_gilded_rose_approvals.py`)
-   les tests de caractérisation -> Legacy (`tests/refacto/`)
-   les tests unitaires des stratégies -> Refacto (`gilded_rose/updaters/tests/`)

### 2. Lancer uniquement le test d'approval

``` bash
pytest tests/test_gilded_rose_approvals.py
```

En cas de modification du comportement, un fichier `*.received.txt` sera
généré dans `approved_files/`.\
Pour valider ce nouveau comportement, renommez simplement le fichier en
`*.approved.txt`.

------------------------------------------------------------------------

## Script de simulation (TextTest)

Le script `texttest_fixture.py` permet de visualiser l'évolution des
objets sur plusieurs jours.

Par exemple, pour simuler **10 jours** :

``` bash
python texttest_fixture.py 10
```

Les états des objets sont affichés jour par jour dans la console.

------------------------------------------------------------------------

## Documentation

-   **Architecture & choix de conception :** `ARCHITECTURE.md`\
    *(pattern Strategy, fabrique, principes SOLID, tests, pistes
    d'évolution)*

-   **Code principal :** `gilded_rose.py`

-   **Stratégies de mise à jour :** `gilded_rose/updaters/`





# Gilded Rose starting position in Python(Legacy)

For exercise instructions see [top level README](../README.md)

Suggestion: create a python virtual environment for this project. See the [documentation](https://docs.python.org/3/library/venv.html)

## Run the unit tests from the Command-Line

```
python -m unittest
```

## Run the TextTest fixture from the Command-Line

For e.g. 10 days:

```
python texttest_fixture.py 10
```

You should make sure the command shown above works when you execute it in a terminal before trying to use TextTest (see below).


## Run the TextTest approval test that comes with this project

There are instructions in the [TextTest Readme](../texttests/README.md) for setting up TextTest. You will need to specify the Python executable and interpreter in [config.gr](../texttests/config.gr). Uncomment these lines:

    executable:${TEXTTEST_HOME}/python/texttest_fixture.py
    interpreter:python

## Run the ApprovalTests.Python test

This test uses the framework [ApprovalTests.Python](https://github.com/approvals/ApprovalTests.Python). You will need to install  Run it like this:

```
python tests/test_gilded_rose_approvals.py
```

You will need to approve the output file which appears under "approved_files" by renaming it from xxx.received.txt to xxx.approved.txt.
