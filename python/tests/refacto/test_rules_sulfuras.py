# -*- coding: utf-8 -*-
from gilded_rose import Item
from .base_gilded_rose_test import GildedRoseTestCase


class TestSulfuras(GildedRoseTestCase):
    """
    Tests unitaires pour les règles spécifiques à "Sulfuras, Hand of Ragnaros".
    "Sulfuras" est un objet légendaire qui ne change jamais de qualité ou de date de vente.
    """
    def test_sulfuras_never_changes(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 80)

        updated = self.run_update(item)

        self.assertEqual(0, updated.sell_in)
        self.assertEqual(80, updated.quality)
    
    # verifie que Sulfuras ne change jamais meme avec un sell_in non nul
    def test_sulfuras_never_changes_even_with_non_zero_sell_in(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 80)

        updated = self.run_update(item)

        self.assertEqual(5, updated.sell_in)
        self.assertEqual(80, updated.quality)

    # verifie que Sulfuras ne change jamais meme apres plusieurs jours
    def test_sulfuras_never_changes_over_multiple_days(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 80)

        updated = item
        for _ in range(5):
            updated = self.run_update(updated)

        self.assertEqual(0, updated.sell_in)
        self.assertEqual(80, updated.quality)
