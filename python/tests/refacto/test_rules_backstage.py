# -*- coding: utf-8 -*-
from gilded_rose import Item, GildedRose
from .base_gilded_rose_test import GildedRoseTestCase


class TestBackstagePasses(GildedRoseTestCase):
    """
    Tests unitaires pour les règles spécifiques aux "Backstage passes"."
    La qualité des "Backstage passes" augmente à mesure que la date de vente approche :
    - Augmente de 1 lorsque plus de 10 jours restent.
    - Augmente de 2 lorsque 10 jours ou moins restent.
    - Augmente de 3 lorsque 5 jours ou moins restent.
    - La qualité tombe à 0 après la date de vente.
    """
    # verifie que la qualité et le sell_in sont mis à jour correctement
    # et que la qualité augmente de 1 lorsque plus de 10 jours restent
    def test_backstage_increases_by_one_when_more_than_10_days(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)

        updated = self.run_update(item)

        self.assertEqual(14, updated.sell_in)
        self.assertEqual(21, updated.quality)

    # verifie que la qualité et le sell_in sont mis à jour correctement
    # et que la qualité augmente de 2 lorsque 10 jours ou moins restent
    def test_backstage_increases_by_two_when_10_days_or_less(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)

        updated = self.run_update(item)

        self.assertEqual(9, updated.sell_in)
        self.assertEqual(22, updated.quality)

    # verifie que la qualité et le sell_in sont mis à jour correctement
    # et que la qualité augmente de 3 lorsque 5 jours ou moins restent
    def test_backstage_increases_by_three_when_5_days_or_less(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)

        updated = self.run_update(item)

        self.assertEqual(4, updated.sell_in)
        self.assertEqual(23, updated.quality)

    # verifie que la qualité des "Backstage passes" tombe à 0 après la date de vente
    def test_backstage_quality_drops_to_zero_after_concert(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)

        updated = self.run_update(item)

        self.assertEqual(-1, updated.sell_in)
        self.assertEqual(0, updated.quality)

    # verifie que la qualité des "Backstage passes" ne dépasse jamais 50(zone à +2 qualité)
    def test_backstage_quality_never_exceeds_50_in_10_day_window(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 49)

        updated = self.run_update(item)

        self.assertEqual(9, updated.sell_in)
        self.assertEqual(50, updated.quality)

    # verifie que la qualité des "Backstage passes" ne dépasse jamais 50(zone à +3 qualité)
    def test_backstage_quality_never_exceeds_50_in_5_day_window(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)

        updated = self.run_update(item)

        self.assertEqual(4, updated.sell_in)
        self.assertEqual(50, updated.quality)

    # verifie que la qualité des "Backstage passes" augmente de 1 lorsque 11 jours restent(frontière 11)
    def test_backstage_increases_by_one_when_11_days_left(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)

        updated = self.run_update(item)

        self.assertEqual(10, updated.sell_in)
        self.assertEqual(21, updated.quality)

    # verifie que la qualité des "Backstage passes" augmente de 2 lorsque 6 jours restent(frontière 6)
    def test_backstage_increases_by_two_when_6_days_left(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 20)

        updated = self.run_update(item)

        self.assertEqual(5, updated.sell_in)
        self.assertEqual(22, updated.quality)

    # verifie que la qualité des "Backstage passes" retombe à 0 après la date de vente même si elle est au maximum
    def test_backstage_at_max_quality_drops_to_zero_after_concert(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 50)

        updated = self.run_update(item)

        self.assertEqual(-1, updated.sell_in)
        self.assertEqual(0, updated.quality)
