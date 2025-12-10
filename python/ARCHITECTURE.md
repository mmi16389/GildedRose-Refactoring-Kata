# Architecture Technique – Gilded Rose Refactoring Kata (Python)
> “J’ai commencé par écrire des tests de caractérisation pour sécuriser le code legacy.
Ensuite, j’ai isolé la logique métier dans une hiérarchie de stratégies, ce qui applique naturellement SRP, OCP, LSP et DIP.
GildedRose ne connaît plus les règles, il délègue via une factory (get_updater_for).
Cela permet d’ajouter un nouveau type d’item sans toucher au code existant.
Je pourrais aller plus loin avec une registry dynamique ou un système de plugins si le domaine évolue.”


Ce document détaille les choix d’architecture réalisés lors du refactoring,  
les principes SOLID appliqués, les patterns utilisés, ainsi que les limites  
et arbitrages conscients (dont les raisons pour lesquelles une architecture  
DDD ou hexagonale complète n’a pas été retenue).

---

# 1. Objectifs du refactoring

- Clarifier et isoler les règles métier du kata Gilded Rose.  
- Faciliter l’ajout de nouveaux comportements (ex : Conjured).  
- Respecter strictement les contraintes du kata,  
  notamment : **ne jamais modifier la classe `Item`**.  
- Remplacer les chaînes de `if/else` du code legacy par un design extensible.  
- Appliquer une démarche de Software Craftsmanship (tests -> refacto -> patterns).

---

# 2. Sécurisation du legacy (tests de caractérisation)

Avant tout refactoring, une suite de tests :

- exhaustive,
- structurée par type d’item,
- indépendante des implémentations futures,

a été écrite.

Elle constitue la "filet de sécurité" garantissant la préservation stricte  
du comportement existant (Golden Master + tests unitaires).

---

# 3. Design retenu : Pattern Strategy + découplage modulaire

## Pourquoi Strategy ?

Chaque type d’item est une **variation de règles métier** appliquées au même concept :  
-> *mettre à jour un item en fonction de son type et de sa date de péremption.*

Au lieu d’entasser des conditions :

```python
if name == ...:
elif name == ...:
...
```

Chaque type d’item possède une stratégie dédiée :

```python   
class AgedBrieUpdater(ItemUpdater):
    ...         
class SulfurasUpdater(ItemUpdater):
    ...
class BackstagePassUpdater(ItemUpdater):
    ...
```

Toutes implémentent un contrat unique de la classe mère abstraite `ItemUpdater` :

```python   
    @abstractmethod
    def update(self, item: Item) -> Item:
        """Met à jour l'objet selon les règles spécifiques."""
        ...
```

La façade GildedRose ne connaît pas les détails métier :
elle délègue au bon updater via `get_updater_for`.

# 4. Respect des principes SOLID

## SRP — Single Responsibility

Chaque updater porte une seule règle métier.
GildedRose n’orchestration que la sélection de stratégie.

## OCP — Open/Closed

Ajouter un type d’item ≠ modifier du code existant.
On ajoute une classe + un binding dans la registry.

## LSP — Liskov Substitution

Tous les updaters sont interchangeables via ItemUpdater.

## ISP — Interface Segregation

Interface minimaliste : une seule méthode obligatoire.

## DIP — Dependency Inversion

GildedRose dépend d’une abstraction (ItemUpdater),
jamais de classes concrètes.

# 5. Structure du code retenue
```text
gilded_rose/      -> package principal
    core.py         -> GildedRose + factory get_updater_for
    updaters/
        base.py         -> contrat + helpers métier
        standard.py
        aged_brie.py
        sulfuras.py
        backstage.py
        conjured.py
        __init__.py     -> registry + sélection dynamique
README_legacy.md -> description de l’implémentation legacy initiale
README.md         -> documentation générale du projet
ARCHITECTURE.md  -> documentation détaillée de l’architecture
gilded_rose.py    -> façade API demandée par le kata
tests/            -> tests unitaires par type d’item
    test_gilded_rose.py
    test_gilded_rose_approvals.py
    refacto/        -> tests de caractérisation du legacy
        test_legacy_items.py
        test_legacy_behavior.py
        approved_files/
            ...
```
Cette structure est :

- lisible,

- modulaire,

- proche d’un découpage “domaine / policies”.

# 6. Limitations et arbitrages architecturaux

Une architecture plus avancée (DDD complet, Hexagonal Architecture)
a été envisagée, mais écartée pour plusieurs raisons limitantes et contextuelles.

## 6.1. Contrainte bloquante : impossibilité de modifier Item

Un modèle hexagonal ou DDD complet nécessite généralement :

- une entité de domaine propre,

- séparée d’un DTO ou adaptateur,

- contrôlée par un service applicatif.

Le kata interdit de modifier Item :

`Vous ne devez en aucun cas modifier la classe Item…`

Cela empêche toute forme propre de mapping ou de séparation Domaine / Infrastructure.

## 6.2. Périmètre trop réduit pour justifier une architecture hexagonale

Une architecture full hexagonale suppose :

- plusieurs interfaces d’entrée,

- une infrastructure variée,

- des ports/adapters multipliés,

- un domaine stable et évolutif.

Le kata, par design, se limite à une opération unique :
mettre à jour la qualité des items.

Une architecture trop complexe serait :

- disproportionnée (overkill),

- moins lisible,

- plus coûteuse cognitivement,

- peu pédagogique dans ce contexte.

# 7. Choix assumé & Design évolutif

Même sans aller vers un DDD strict, ce refactoring :

- isole clairement les règles métier,

- structure le code selon une logique “domaine light”,

- rend l’ajout de nouvelles variances trivial,

- laisse la façade compatible avec l’exigence du kata,

- prépare l’évolutivité si un jour l’inventaire devait être géré dans :

    - un service Django,

    - un batch de fond,

    - un microservice,

    - ou une API REST.

On obtient donc un équilibre :

- suffisamment simple pour le kata,

- suffisamment robuste pour passer à l’échelle.

# 8. Conclusion

Cette architecture représente un choix raisonné, ni minimaliste ni sur-ingénierie.
Elle maximise :

- la lisibilité,

- l’évolutivité,

- et la conformité aux contraintes du kata,

- tout en appliquant des concepts avancés (SOLID, Strategy, separation of concerns)
de manière pertinente et pragmatique.