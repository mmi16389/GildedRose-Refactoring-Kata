# -*- coding: utf-8 -*-
# Réexporte les classes legacy pour compatibilité
from .gilded_rose_legacy import Item, GildedRose  # importe depuis gilded_rose.py à la racine

__all__ = ["Item", "GildedRose"]
# Maintenant, les utilisateurs peuvent importer Item et GildedRose directement depuis gilded_rose.updaters