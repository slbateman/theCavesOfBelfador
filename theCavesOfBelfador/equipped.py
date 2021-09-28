#! /usr/bin/env python
# Python 2.7
# created by Steve Bateman
# Copyright 2016, Creative Commons


class Equipped(object):
    equiptItem = None

    def enter(self):
        self.equipped = Equipped().equiptItem

#This allows the other .py files to equip and unequip the item
equipped = Equipped().equiptItem