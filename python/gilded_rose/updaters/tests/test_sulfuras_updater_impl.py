# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item
from gilded_rose.updaters.sulfuras import SulfurasUpdater


class TestSulfurasUpdaterImpl(unittest.TestCase):

    def setUp(self):
        self.updater = SulfurasUpdater()

    def test_sulfuras_never_changes_before_sell_date(self):
        item = Item("Sulfuras, Hand of Ragnaros", 10, 80)

        self.updater.update(item)

        self.assertEqual(10, item.sell_in)
        self.assertEqual(80, item.quality)

    def test_sulfuras_never_changes_after_sell_date(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 80)

        self.updater.update(item)

        self.assertEqual(0, item.sell_in)
        self.assertEqual(80, item.quality)

    def test_sulfuras_quality_stays_constant_even_if_not_80(self):
        # Test de robustesse si jamais l'item est mal initialisé
        item = Item("Sulfuras, Hand of Ragnaros", -5, 50)

        self.updater.update(item)

        self.assertEqual(-5, item.sell_in)
        self.assertEqual(50, item.quality)
