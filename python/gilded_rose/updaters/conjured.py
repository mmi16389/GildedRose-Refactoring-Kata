# -*- coding: utf-8 -*-
from gilded_rose import Item

from .base import ItemUpdater, decrease_quality, decrease_sell_in

class ConjuredItemUpdater(ItemUpdater):
    """
    Conjured :
    - Se dégrade 2x plus vite qu'un item standard :
      * -2 avant sell_in <= 0
      * -4 à partir de sell_in <= 0
    - Qualité jamais négative
    """

    def update(self, item: Item) -> None:
        old_sell_in = item.sell_in

        degrade = 2
        if old_sell_in <= 0:
            degrade = 4

        decrease_quality(item, degrade)
        decrease_sell_in(item)
