
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
    │   └── refacto/                      # Tests de caractérisation du legacy
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
ou 

``` bash
python -m pytest
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
- **`README_legacy.md`** : Description de l’implémentation legacy initiale.
-   **Code principal :** `gilded_rose/core.py`

-   **Stratégies de mise à jour :** `gilded_rose/updaters/`

---

## Workflow Git & Branching Strategy

> Tout le refactoring a été réalisé sur une seule branche de travail : ***feature/refactor-gilded-rose***


---

### Pourquoi pas plusieurs branches ?

Le contexte du kata :

- un code de petite taille,
- un objectif de démonstration **Craftsmanship**,
- un pipeline de test très rapide,
- une limitation de temps.

rend l’approche **multi-branches** trop lourde et peu pertinente.

**Une seule branche** a donc été privilégiée, avec une structure de commits **très granulaire** pour exprimer une démarche progressive, claire et linéaire.

---

### Chaque étape correspond à un commit identifié
L’ensemble du refactoring a été structuré autour d’une démarche Craftsmanship guidée par les tests.
Chaque étape est isolée dans un commit identifiable, permettant de rejouer et comprendre la transformation progressive du legacy.
Ci-dessous, la table complète des commits, classés par étape du workflow.

### Table of Commit References

> A -> **caractérisation de tests et préparation**, B -> **Structuration, mise en place de la factory,** C -> **Implémentation des stratégies,** D -> **Migration finale et nettoyage,** E -> **Documentation.**

| Étape | Description                                                      | Commit SHA |
|-------|------------------------------------------------------------------|------------|
| A0    | Initialisation de la branche + baseline tests                    | 94bda51    |
| A1    | Ajout utilitaires communs pour les tests                         | 606da61    |
| A2    | Tests de caractérisation – normal items (1)                      | 299427e    |
| A3    | Tests de caractérisation – Aged Brie                             | e5d2bdb    |
| A4    | Tests de caractérisation – Backstage passes + tests supplémentaires | 5606949 |
| A5    | Tests de caractérisation – Sulfuras                              | 51ae823    |
| A6    | Tests de caractérisation – Normal items (2, scénarios supplémentaires) | f447a86 |
| A7    | Tests de caractérisation – Conjured items                        | a0d12c6    |
| B1    | Création du package gilded_rose/                                  | 5154bab    |
| C1    | Introduction de l’abstraction ItemUpdater                        | 8921fe6    |
| C2    | Implémentation DefaultUpdater                                     | b205121    |
| C3    | Ajout test StandardItemUpdater                                     | 86c477e    |
| C4    | Implémentation AgedBrieUpdater                                     | e534e85    |
| C5    | Implémentation BackstagePassUpdater                                 | 7245372    |
| C6    | Implémentation SulfurasUpdater                                      | c410125    |
| C7    | Implémentation ConjuredUpdater                                      | 1b9fd64    |
| C8    | Wiring de la factory dans updaters                                   | e217596    |
| C9    | Tests de la factory                                                  | a1b29b1    |
| D1    | Migration de Item & GildedRose vers core.py + suppression du legacy | 55ad4e2 |
| D2    | Transformation du fichier gilded_rose.py en simple façade           | cb10b4d    |
| E1    | Documentation – Ajout d’une spec d'installation                     | 69f424f    |
| E2    | Documentation – Mise à jour README finale                            | 1bb68d8    |

## Application du workflow
```bash
git checkout <SHA>
pytest
```
Exemple:
Tester l’état après l’implémentation de `AgedBrieUpdater` étape C4 (commit e534e85) :

```bash
git checkout e534e85
pytest

```

## Pistes d’amélioration

Quelques évolutions possibles à partir de ce refactoring :

- Ajouter de nouveaux types d’objets via de nouvelles stratégies, sans toucher à GildedRose.

- Remplacer le mapping statique de SPECIAL_UPDATERS par un registry dynamique (auto-enregistrement des stratégies). Ou encore utiliser un decorateur pour marquer les classes de stratégie.
> Decorateur
```python
UPDATERS = {}

def register(name):
    def decorator(cls):
        UPDATERS[name] = cls()
        return cls
    return decorator

## Pour chaque stratégie :
@register("Aged Brie")
class AgedBrieUpdater(ItemUpdater):
    ...

## Pour la factory :
return UPDATERS.get(item.name, AgedBrieUpdater())
```

- Introduire une couche métier plus riche (par exemple des classes de domaine pour les types d’objets plutôt que de se baser sur le name brut).

---
