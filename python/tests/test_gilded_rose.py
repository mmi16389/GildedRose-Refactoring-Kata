# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # Remplacer  "fixme" par "foo" pour sécuriser le métier
        self.assertEqual("foo", items[0].name) 

        
if __name__ == '__main__':
    unittest.main()
