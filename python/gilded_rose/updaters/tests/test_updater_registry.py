# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item
from gilded_rose.updaters import (
    get_updater_for,
    StandardItemUpdater,
    AgedBrieUpdater,
    SulfurasUpdater,
    BackstagePassesUpdater,
    ConjuredItemUpdater,
)


class TestGetUpdaterFor(unittest.TestCase):

    def test_returns_aged_brie_updater_for_aged_brie(self):
        item = Item("Aged Brie", 10, 20)

        updater = get_updater_for(item)

        self.assertIsInstance(updater, AgedBrieUpdater)

    def test_returns_sulfuras_updater_for_sulfuras(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 80)

        updater = get_updater_for(item)

        self.assertIsInstance(updater, SulfurasUpdater)

    def test_returns_backstage_updater_for_backstage_passes(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 30)

        updater = get_updater_for(item)

        self.assertIsInstance(updater, BackstagePassesUpdater)

    def test_returns_conjured_updater_for_conjured_item(self):
        # suppose que is_conjured() détecte "Conjured" dans le nom
        item = Item("Conjured Mana Cake", 3, 6)

        updater = get_updater_for(item)

        self.assertIsInstance(updater, ConjuredItemUpdater)

    def test_returns_standard_updater_for_normal_item(self):
        item = Item("+5 Dexterity Vest", 10, 20)

        updater = get_updater_for(item)

        self.assertIsInstance(updater, StandardItemUpdater)

    def test_special_updaters_are_singletons_from_registry(self):
        """On vérifie que les items 'spéciaux' réutilisent la même instance (dict SPECIAL_UPDATERS)."""
        item1 = Item("Aged Brie", 10, 20)
        item2 = Item("Aged Brie", 5, 10)

        updater1 = get_updater_for(item1)
        updater2 = get_updater_for(item2)

        # même objet, pas seulement même type
        self.assertIs(updater1, updater2)
