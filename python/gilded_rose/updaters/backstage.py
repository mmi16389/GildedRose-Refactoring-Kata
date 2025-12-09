# -*- coding: utf-8 -*-
from gilded_rose import Item

from .base import ItemUpdater, decrease_sell_in, increase_quality

class BackstagePassesUpdater(ItemUpdater):
    """
    Backstage passes :
    - +1 si sell_in > 10
    - +2 si 10 >= sell_in > 5
    - +3 si 5 >= sell_in > 0
    - 0 si sell_in <= 0
    - Qualité max = 50
    """

    def update(self, item: Item) -> None:
        old_sell_in = item.sell_in

        if old_sell_in <= 0:
            # Après le concert : qualité tombe à 0
            item.quality = 0
        else:
            # Avant le concert : augmentation progressive
            increase_quality(item, 1)
            if old_sell_in <= 10:
                increase_quality(item, 1)
            if old_sell_in <= 5:
                increase_quality(item, 1)

        decrease_sell_in(item)

