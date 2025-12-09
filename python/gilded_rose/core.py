# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import List

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class GildedRose:
    def __init__(self, items: List[Item]):
        self.items = items

    def update_quality(self) -> None:
        # Importation locale pour éviter les dépendances circulaires
        from gilded_rose.updaters import get_updater_for

        for item in self.items:
            updater = get_updater_for(item)
            updater.update(item)