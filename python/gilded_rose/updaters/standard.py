# -*- coding: utf-8 -*-
from gilded_rose import Item

from .base import ItemUpdater, decrease_quality, decrease_sell_in

class StandardItemUpdater(ItemUpdater):
    """
    Règles des objets standards :
    - Perdent 1 point de qualité par jour avant la date de vente.
    - Perdent 2 points de qualité par jour une fois la date dépassée.
    - La qualité ne devient jamais négative.
    """

    def update(self, item: Item) -> None:
        # On utilise la valeur actuelle de sell_in pour déterminer la dégradation
        old_sell_in = item.sell_in

        # Dégradation normale : -1
        degrade = 1
        # Dégradation accélérée après expiration : -2
        if old_sell_in <= 0:
            degrade = 2

        # Mise à jour de la qualité et de la date de vente
        decrease_quality(item, degrade)
        decrease_sell_in(item)
