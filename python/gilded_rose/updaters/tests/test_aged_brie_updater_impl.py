# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item
from gilded_rose.updaters.aged_brie import AgedBrieUpdater  # ton fichier


class TestAgedBrieUpdaterImpl(unittest.TestCase):

    def setUp(self):
        self.updater = AgedBrieUpdater()

    def test_increases_quality_before_sell_date(self):
        item = Item("Aged Brie", 10, 25)

        self.updater.update(item)

        self.assertEqual(9, item.sell_in)
        self.assertEqual(26, item.quality)

    def test_increases_quality_twice_as_fast_after_sell_date(self):
        item = Item("Aged Brie", 0, 25)

        self.updater.update(item)

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(27, item.quality)

    def test_quality_never_exceeds_fifty(self):
        item = Item("Aged Brie", 5, 50)

        self.updater.update(item)

        self.assertEqual(4, item.sell_in)
        self.assertEqual(50, item.quality)
