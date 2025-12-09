# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item
from gilded_rose.updaters.conjured import ConjuredItemUpdater


class TestConjuredItemUpdaterImpl(unittest.TestCase):

    def setUp(self):
        self.updater = ConjuredItemUpdater()

    def test_conjured_degrades_twice_as_fast_before_sell_date(self):
        item = Item("Conjured Mana Cake", 10, 20)

        self.updater.update(item)

        self.assertEqual(9, item.sell_in)
        self.assertEqual(18, item.quality)  # -2

    def test_conjured_degrades_four_times_as_fast_after_sell_date(self):
        item = Item("Conjured Mana Cake", 0, 10)

        self.updater.update(item)

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(6, item.quality)  # -4

    def test_quality_never_negative(self):
        item = Item("Conjured Mana Cake", 5, 1)

        self.updater.update(item)

        self.assertEqual(4, item.sell_in)
        self.assertEqual(0, item.quality)  # cannot go below 0

    def test_quality_never_negative_even_after_sell_date(self):
        item = Item("Conjured Mana Cake", 0, 3)

        self.updater.update(item)

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)  # would be -4 but capped to 0
