#! /usr/bin/env python
# Python 2.7
# created by Steve Bateman
# Copyright 2016, Creative Commons

import player
import random


#This is the final monster in the game
class Boss(object):
    name = "BELFADOR"
    level = None
    maxHp = None
    hp = maxHp
    damage = None

    #This refreshes the monster's stats according to the player's stats
    # Called by map.py when loading final location
    def enter(self):
        self.level = player.user.level + 5
        self.maxHp = 100 + self.level * 30
        self.hp = self.maxHp
        self.damage = self.level * 5 + 50


class Gargoyle(object):
    name = "GARGOYLE"
    level = None
    maxHp = None
    hp = maxHp
    damage = None

    #This refreshes the monster's stats according to the player's stats
    # Called by map.py when loading new area
    def enter(self):
        self.level = player.user.level + 2
        self.maxHp = 50 + self.level * 20
        self.hp = self.maxHp
        self.damage = self.level * 3 + 15


class Griffen(object):
    name = "GRIFFEN"
    level = None
    maxHp = None
    hp = maxHp
    damage = None

    #This refreshes the monster's stats according to the player's stats
    # Called by map.py when loading new area
    def enter(self):
        self.level = player.user.level + 2
        self.maxHp = 40 + self.level * 15
        self.hp = self.maxHp
        self.damage = self.level * 3 + 10


class Goblin(object):
    name = "GOBLIN"
    level = None
    maxHp = None
    hp = maxHp
    damage = None

    #This refreshes the monster's stats according to the player's stats
    # Called by map.py when loading new area
    def enter(self):
        self.level = player.user.level
        self.maxHp = 30 + self.level * 15
        self.hp = self.maxHp
        self.damage = self.level * 2 + 8


class Gremlin(object):
    name = "GREMLIN"
    level = None
    maxHp = None
    hp = maxHp
    damage = None

    #This refreshes the monster's stats according to the player's stats
    # Called by map.py when loading new area
    def enter(self):
        self.level = player.user.level
        self.maxHp = 20 + self.level * 15
        self.hp = self.maxHp
        self.damage = self.level * 2 + 6


class EnemyChooser(object):
    enemyTypes = [
        Gargoyle(),
        Griffen(),
        Goblin(),
        Gremlin()
    ]

    #Called by map.py when loading a location to load random enemy based on
    # parameters give by the location type
    def enter(self, x, y):
        enemy = self.enemyTypes[(random.randint(x, y))]
        return enemy

#enemy = EnemyChooser().enter(2,3)