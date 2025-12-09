# -*- coding: utf-8 -*-
from gilded_rose import Item
from .base_gilded_rose_test import GildedRoseTestCase


class TestStandardItems(GildedRoseTestCase):
    """
    Tests unitaires pour les règles des objets standards.
    Un objet standard perd 1 point de qualité par jour avant la date de vente,
    Le sell_in diminue de 1 chaque jour.
    et 2 points par jour après la date de vente.
    La qualité d'un objet standard ne peut jamais être négative.
    
    """
    # verifie que la qualité et le sell_in sont mis à jour correctement
    # et dimuent de 1 avant la date de vente
    def test_standard_item_degrades_by_one_before_sell_date(self):
        item = Item("+5 Dexterity Vest", 10, 20)

        updated = self.run_update(item)

        self.assertEqual(9, updated.sell_in)
        self.assertEqual(19, updated.quality)

    # verifie que la qualité et le sell_in sont mis à jour correctement
    # et dimuent de 2 après la date de vente
    def test_standard_item_degrades_twice_as_fast_after_sell_date(self):
        item = Item("Elixir of the Mongoose", 0, 10)

        updated = self.run_update(item)

        self.assertEqual(-1, updated.sell_in)
        self.assertEqual(8, updated.quality)

    # verifie que la qualité d'un objet standard ne devient jamais négative
    def test_standard_item_quality_never_negative(self):
        item = Item("Normal Item", 5, 0)

        updated = self.run_update(item)

        self.assertEqual(0, updated.quality)