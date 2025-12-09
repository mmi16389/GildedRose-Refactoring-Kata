# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTestCase(unittest.TestCase):
    """
    Class de base pour les tests unitaires de GildedRose.
    Fournit des utilitaires communs pour les tests.
    """

    def run_update(self, item, days: int = 1):
        """Applique update_quality plusieurs fois pour un seul item."""
        items = [item] # Liste contenant un seul item
        app = GildedRose(items)
        for _ in range(days):
            app.update_quality()
        return items[0]