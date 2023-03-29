# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 1, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(3, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_brie_old(self):
        items = [Item("Aged Brie", 0, 47)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(49, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_brie_new(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 2, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)
        self.assertEquals(2, items[0].sell_in)

    def test_backstage(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 12, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(2, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(3, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(5, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(7, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(11, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(13, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(16, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(19, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(22, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(25, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(28, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)
        
    def test_conjured(self):
        items = [Item("Conjured foo", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(8, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(6, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(2, items[0].quality)
    



        
if __name__ == '__main__':
    unittest.main()
