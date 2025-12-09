# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item
from gilded_rose.updaters.standard import StandardItemUpdater


class TestStandardItemUpdaterImpl(unittest.TestCase):
    def setUp(self):
        self.updater = StandardItemUpdater()

    def test_degrades_by_one_before_sell_date(self):
        item = Item("+5 Dexterity Vest", 10, 20)

        self.updater.update(item)

        self.assertEqual(9, item.sell_in)
        self.assertEqual(19, item.quality)

    def test_degrades_twice_as_fast_after_sell_date(self):
        item = Item("Elixir of the Mongoose", 0, 10)

        self.updater.update(item)

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(8, item.quality)

    def test_quality_never_negative(self):
        item = Item("Normal Item", 5, 0)

        self.updater.update(item)

        self.assertEqual(4, item.sell_in)
        self.assertEqual(0, item.quality)
