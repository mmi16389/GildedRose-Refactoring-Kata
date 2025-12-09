# -*- coding: utf-8 -*-
from gilded_rose import Item

from .base import ItemUpdater

class SulfurasUpdater(ItemUpdater):
    """
    "Sulfuras, Hand of Ragnaros" :
    - Ne change jamais de sell_in ni de quality
    """

    def update(self, item: Item) -> None:
        # On ne touche à rien
        return
