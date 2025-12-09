# -*- coding: utf-8 -*-
from gilded_rose import Item
from .base_gilded_rose_test import GildedRoseTestCase


class TestConjuredItems(GildedRoseTestCase):
    """
    Tests unitaires pour les objets "Conjured".
    Un objet conjured se dégrade deux fois plus vite qu'un objet standard :
    - 2 points par jour avant la date de vente
    - 4 points par jour après la date de vente
    """
    # verifie que la qualité et le sell_in sont mis à jour correctement
    # et dimuent de 2 avant la date de vente
    def test_conjured_degrades_by_two_before_sell_date(self):
        item = Item("Conjured Mana Cake", 5, 10)

        updated = self.run_update(item)

        self.assertEqual(4, updated.sell_in)
        self.assertEqual(8, updated.quality)

    # verifie que la qualité et le sell_in sont mis à jour correctement
    # et dimuent de 4 après la date de vente
    def test_conjured_degrades_by_four_after_sell_date(self):
        item = Item("Conjured Mana Cake", 0, 10)

        updated = self.run_update(item)

        self.assertEqual(-1, updated.sell_in)
        self.assertEqual(6, updated.quality)
    
    # verifie que la qualité d'un objet conjured ne devient jamais négative
    def test_conjured_quality_never_negative(self):
        item = Item("Conjured Mana Cake", 0, 1)

        updated = self.run_update(item)

        self.assertEqual(-1, updated.sell_in)
        self.assertEqual(0, updated.quality)
