# -*- coding: utf-8 -*-
from gilded_rose import Item

from .base import ItemUpdater, decrease_quality, decrease_sell_in, increase_quality

class AgedBrieUpdater(ItemUpdater):
    """
    "Aged Brie" :
    - +1 de qualité par jour avant la date de vente
    - +2 à partir de sell_in <= 0
    - Qualité max = 50
    """

    def update(self, item: Item) -> None:
        old_sell_in = item.sell_in

        increase = 1
        if old_sell_in <= 0:
            increase = 2

        increase_quality(item, increase)
        decrease_sell_in(item)

 