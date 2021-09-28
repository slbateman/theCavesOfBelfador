#! /usr/bin/env python
# Python 2.7
# created by Steve Bateman
# Copyright 2016, Creative Commons

import random
import player


# These are all the weapons available in the game


class Weapon(object):

    def enter(self):
        pass


class Dagger(Weapon):
    name = "DAGGER"
    damage = 10
    weight = 1
    value = damage + 5


class Sword(Weapon):
    name = "SWORD"
    damage = 15
    weight = 3
    value = damage + 10


class Axe(Weapon):
    name = "AXE"
    damage = 20
    weight = 6
    value = damage + 15


class Sledge(Weapon):
    name = "SLEDGE"
    damage = 25
    weight = 10
    value = damage + 20


class SwordBroad(Weapon):
    name = "BROADSWORD"
    damage = 30
    weight = 15
    value = damage + 25


class AxeDouble(Weapon):
    name = "DOUBLE SIDED AXE"
    damage = 40
    weight = 21
    value = damage + 30


class SledgeSuper(Weapon):
    name = "SUPER SLEDGE"
    damage = 50
    weight = 28
    value = damage + 35


#This will randomly load weapons to rooms/locations based on player stats
class WeaponChooser(object):
    weaponTypes = [
        Dagger(),
        Sword(),
        Axe(),
        Sledge(),
        SwordBroad(),
        AxeDouble(),
        SledgeSuper()
    ]

    #Called by map.py when a location loads
    def enter(self):
        #Since there are only 7 weapons, if the player's level is greater than
        # 6, this won't work
        if player.user.level > 6:
            x = 6
            weapon = self.weaponTypes[random.randint(0, x)]
        else:
            x = player.user.level
            weapon = self.weaponTypes[random.randint(0, x)]
        return weapon

#weapon = WeaponChooser().enter()