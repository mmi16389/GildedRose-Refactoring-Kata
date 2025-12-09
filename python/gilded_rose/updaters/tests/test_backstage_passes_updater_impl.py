# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item
from gilded_rose.updaters.backstage import BackstagePassesUpdater


class TestBackstagePassesUpdaterImpl(unittest.TestCase):

    def setUp(self):
        self.updater = BackstagePassesUpdater()

    def test_increases_by_one_when_more_than_ten_days_left(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)

        self.updater.update(item)

        self.assertEqual(14, item.sell_in)
        self.assertEqual(21, item.quality)

    def test_increases_by_two_when_ten_days_or_less(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 25)

        self.updater.update(item)

        self.assertEqual(9, item.sell_in)
        self.assertEqual(27, item.quality)

    def test_increases_by_three_when_five_days_or_less(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 30)

        self.updater.update(item)

        self.assertEqual(4, item.sell_in)
        self.assertEqual(33, item.quality)

    def test_quality_drops_to_zero_after_concert(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 40)

        self.updater.update(item)

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_quality_never_exceeds_fifty(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)

        self.updater.update(item)

        self.assertEqual(4, item.sell_in)
        self.assertEqual(50, item.quality)
