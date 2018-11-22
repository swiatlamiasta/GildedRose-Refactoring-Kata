# -*- coding: utf-8 -*-
import re


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        ''' 
        CC before and after:
        GildedRose.update_quality - C (19)
        GildedRose.update_quality - D (21)

        Halstead before and after:
        difficulty: 10.8
        effort: 4205.47

        difficulty: 11.6
        effort: 4851.58
        '''

        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name.startswith("Conjured"):
                        item.quality = item.quality - 1
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
                            if item.name.startswith("Conjured"):
                                item.quality = item.quality - 1
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1

    def update_quality_new(self):
        '''First naive non OOP attempt
        '''

        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                item.quality = item.quality
                item.sell_in = item.sell_in
            elif item.name == "Aged Brie":
                if item.quality < 50:
                    item.quality += 1
                item.sell_in -= 1
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.quality < 50:
                    if item.sell_in < 1:
                        item.quality = 0
                    elif item.sell_in < 6:
                        item.quality += 3
                    elif item.sell_in < 11:
                        item.quality += 2
                    else:
                        item.quality += 1
                item.sell_in -= 1
            elif item.name.startswith("Conjured"):
                if item.sell_in > 0:
                    item.quality -= 2
                else:
                    item.quality -= 4
                item.sell_in -= 1
            else:
                if 0 < item.quality < 50:
                    if item.sell_in < 1:
                        item.quality -= 2
                    else:
                        item.quality -= 1
                item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
