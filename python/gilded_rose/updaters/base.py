# -*- coding: utf-8 -*-
from gilded_rose import Item
from abc import ABC, abstractmethod

class ItemUpdater(ABC):
    """Interface commune pour toutes les stratégies de mise à jour."""

    @abstractmethod
    def update(self, item: Item) -> Item:
        """Met à jour l'objet selon les règles spécifiques."""
        ...

def decrease_sell_in(item, amount: int = 1) -> None:
    """Diminue le nombre de jours restants avant l'expiration."""
    item.sell_in -= amount

def increase_quality(item, amount: int = 1) -> None:
    """Augmente la qualité de l'objet, sans jamais dépasser 50."""
    item.quality = min(50, item.quality + amount)

def decrease_quality(item, amount: int = 1) -> None:
    """Diminue la qualité de l'objet, sans jamais descendre en dessous de 0."""
    item.quality = max(0, item.quality - amount)

def is_conjured(item) -> bool:
    """Détermine si l'objet est de type 'Conjured', basé sur son nom."""
    return item.name.startswith("Conjured")
