#! /usr/bin/env python
# Python 2.7
# created by Steve Bateman
# Copyright 2016, Creative Commons


import math


#Player stats
class Player(object):
    name = ""
    xp = 0
    level = int((-100 + math.sqrt(40 * xp + 10000)) / 20)
    maxHp = 35 + level * 15
    hp = maxHp
    damage = 6 + level * 2
    gold = 0

    #At each new location this will refresh stats based on Player XP and Level
    def enter(self):
        self.level = int((-100 + math.sqrt(40 * self.xp + 10000)) / 20)
        self.maxHp = 35 + self.level * 15
        self.damage = 6 + self.level * 2

#Allows other .py files to use
user = Player()
