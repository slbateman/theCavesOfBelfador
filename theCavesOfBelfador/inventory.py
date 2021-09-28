#! /usr/bin/env python
# Python 2.7
# created by Steve Bateman
# Copyright 2016, Creative Commons

import equipped
import player


#Holds the items the player picks up
class Inventory(object):
    inventory = []
    gold = 0
    weight = 0
    maxWeight = 50 + player.user.level * 5

    #Calculates the weight of the inventory along with the equipped item weight
    #This is called everytime the player attempts to move
    # or when an item is dropped or drank
    def calcWeight(self):
        self.weight = 0
        self.inventory.sort()
        for x in self.inventory:
            self.weight += x.weight
            self.maxWeight = 50 + player.user.level * 5
            x.enter()
        if equipped.equipped:
            self.weight += equipped.equipped.weight
        else:
            pass
        pass

#Allows other .py files to utilize the inventory
inventory = Inventory()
