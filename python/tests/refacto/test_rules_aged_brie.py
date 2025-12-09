from gilded_rose import Item
from .base_gilded_rose_test import GildedRoseTestCase


class TestAgedBrie(GildedRoseTestCase):
    """
    Tests unitaires pour les règles spécifiques à "Aged Brie".
    "Aged Brie" augmente en qualité avec le temps.
    La qualité d'"Aged Brie" ne peut jamais dépasser 50.
    """

    # verifie que la qualité et le sell_in sont mis à jour correctement
    def test_aged_brie_increases_in_quality(self):
        item = Item("Aged Brie", 2, 0)

        updated = self.run_update(item)

        self.assertEqual(1, updated.sell_in)
        self.assertEqual(1, updated.quality)

    # verifie que la qualité d'"Aged Brie" ne dépasse jamais 50
    def test_aged_brie_quality_never_exceeds_50(self):
        item = Item("Aged Brie", 5, 50)

        updated = self.run_update(item)

        self.assertEqual(4, updated.sell_in)
        self.assertEqual(50, updated.quality)