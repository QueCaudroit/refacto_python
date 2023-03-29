# -*- coding: utf-8 -*-
MAX_QUALITY = 50
MIN_QUALITY = 0

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality_old(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1

    def update_quality(self):
        for item in self.items:
            item.update()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        if name == "Sulfuras, Hand of Ragnaros":
            self.update_quality = update_sulfuras 
        elif name == "Aged Brie":
            self.update_quality = update_brie 
        elif name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_quality = update_backstage
        elif "Conjured" in name:
            self.update_quality = update_conjured
        else:
            self.update_quality = update_default


    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update(self):
        if self.name != "Sulfuras, Hand of Ragnaros":
            self.sell_in -= 1
        self.quality = self.update_quality(self.sell_in, self.quality)

def update_sulfuras(sell_in, quality):
    return 80

def update_backstage(sell_in, quality):
    if sell_in == 10:
        return min(quality + 2, MAX_QUALITY)
    elif sell_in == 5:
        return min(quality + 3, MAX_QUALITY)
    elif sell_in <= 0:
        return MIN_QUALITY
    else:
        return quality

def update_brie(sell_in, quality):
    if sell_in > 0:
        return min(quality + 1, MAX_QUALITY)
    else:
        return min(quality + 2, MAX_QUALITY)

def update_default(sell_in, quality):
    if sell_in < 0:
        return max(quality - 2, MIN_QUALITY)
    else:
        return max(quality - 1, MIN_QUALITY)

def update_conjured(sell_in, quality):
    if sell_in < 0:
        return max(quality - 4, MIN_QUALITY)
    else:
        return max(quality - 2, MIN_QUALITY)