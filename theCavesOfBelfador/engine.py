#! /usr/bin/env python
# Python 2.7
# created by Steve Bateman
# Copyright 2016, Creative Commons

import random
import player
import equipped
import inventory
import map


#This is initiated by the __init__.py file
class Start(object):
    startGame = False

    def enter(self):
        CheckHP().enter()
        print "\n"
        print "Welcome to Belfador's Cave."
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        print "I'm sorry to inform you,"
        print "but you have fallen into a cave."
        print "Unfortunately, you can't climb out."
        print "You must press forward to find a way out."
        print "This cave is dangerous."
        print "Be on your guard and use any resources you find."
        print "\n"
        while self.startGame is False:
            print "Are you ready to continue your journey?"
            self.startGame = raw_input("> ")
            if ("yes" in self.startGame or "y" in self.startGame
            or "Y" in self.startGame or "Yes" in self.startGame):
                self.startGame = True
                print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
                print "Good, let's begin."
            else:
                self.startGame = False
                print "\nWe don't have all day."
                print "You may die soon.\n"
        Help().enter()

        #Begins the true user interactions
        #After each command is completed it will come back this this
        # to eliminate nesting commands
        Command().enter()


class Help(object):

    def enter(self):
        CheckHP().enter()
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        print "Below are the commands you must know:\n"
        print "move -------- To move in a specified direction"
        print "look -------- To see what is in your location"
        print "inventory --- To view your inventory"
        print "trade ------- To enter transactions with a Trader"
        print "grab ------ To pick up an item"
        print "drop -------- To drop item from inventory"
        print "equip ------- To equip a weapon"
        print "unequip ----- To disarm your weapon"
        print "\t\t  Only weapons can be equipped"
        print "drink ------- To drink a potion or elixer"
        print "\t\t  Only potions and elixers can be drank"
        print "attack ------ To attack enemy with equipped weapon"
        print "\t\t  If you have no weapons,"
        print "\t\t  you can attack with your fists"
        print "status ------ To view the status of your character"
        print "quit -------- To end game at any time"
        print "help -------- To view this list of commands"
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        CheckHP().enter()


class Look(object):

    #This will establish if the location is a trade location or a previously
    # visited location or new location
    def enter(self):
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        if map.currentLocation.trade is True:
            self.trade()
        elif map.currentLocation.look is True:
            self.lookTrue()
        elif map.currentLocation.look is False:
            self.lookFalse()
        else:
            print "something happened"

    #Performed when location is a trade location
    def trade(self):
        CheckHP().enter()
        print map.currentLocation.locInfo
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        if map.currentLocation.items:
            for x in map.currentLocation.items:
                print "%s is on the ground" % x.name
        else:
            pass
        CheckHP().enter()

    #Performed when player has previously visited
    def lookTrue(self):
        CheckHP().enter()
        if not map.currentLocation.items:
            print "\nThe place is empty"
        else:
            print "\nYou can see:"
            for x in map.currentLocation.items:
                print x.name
        if not map.currentLocation.enemy:
            print "\nThere are no enemies here."
        else:
            print "Don't forget the big fat %s you need to kill." % (
                map.currentLocation.enemy.name)
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        CheckHP().enter()

    #Performed when location hasn't been previously visited
    def lookFalse(self):
        CheckHP().enter()
        print map.currentLocation.locInfo
        if not map.currentLocation.items:
            print "\nYou have scoured the area for anything that might help.."
            print "\n"
            print "\nNothing...you found nothing..."
        else:
            print map.currentLocation.itemInfo
            for x in map.currentLocation.items:
                print x.name
            print "\nYou lucky little bitch."
        if not map.currentLocation.enemy:
            print "\n"
            print "\nHot damn, I almost shit myself"
            print "I thought I saw a rat."
            print "\nLuckily, nothing creepy or angry here."
        else:
            print "\n"
            print map.currentLocation.enemyInfo
            print map.currentLocation.enemy.name
            print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        map.currentLocation.look = True
        CheckHP().enter()


class Inventory(object):

    #Shows what has been picked up as well as the weight and max weight
    def enter(self):
        CheckHP().enter()
        inventory.inventory.calcWeight
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        print "Load = %d / %d\n" % (inventory.inventory.weight,
            inventory.inventory.maxWeight)
        for x in inventory.inventory.inventory:
            print "%s - %d pounds - %d value" % (x.name, x.weight, x.value)
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        CheckHP().enter()


#Estabilishes interactions with the trader in trade locations
class Trade(object):

    def enter(self):
        CheckHP().enter()
        player.user.enter()
        map.currentLocation.visited = True
        if map.currentLocation.trade is True:
            buySell = raw_input(
                "Do you want to 'BUY' or'SELL' or 'EXIT' the trade?\n> "
                ).upper()
            if buySell == "BUY":
                self.buy()
            elif buySell == "SELL":
                self.sell()
            elif buySell == "EXIT":
                print "The clown says: 'I wish you were sticking around.'"
                print "'We could have some fun.'"
            else:
                print "Not sure what that means..."
                self.enter()
        elif map.currentLocation.trade is False:
            print "There is no Trader here."
            print "How about you look around?..."
        else:
            pass
        CheckHP().enter()

    def buy(self):
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        print "Your gold: %d  -  Clown's gold: %d\n" % (
            player.user.gold, map.currentLocation.gold)
        for x in map.currentLocation.tradeItems:
            print "%s - %d value" % (x.name, x.value)
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        buy = raw_input("Pick an Item to buy\n> ").upper()
        check = False
        for x in map.currentLocation.tradeItems:
            if x.name == buy:
                if ((x.value <= player.user.gold) and
                (x.weight + inventory.inventory.weight <=
                inventory.inventory.maxWeight)):
                    inventory.inventory.inventory.append(x)
                    player.user.gold -= x.value
                    map.currentLocation.gold += x.value
                    map.currentLocation.tradeItems.remove(x)
                    inventory.inventory.calcWeight()
                    print "%r has been bought" % x.name
                    check = True
                    break
                else:
                    print "You don't have enough gold for that item or you overloaded"
            else:
                pass
        if check is False:
            print "The clown isn't carrying that."
        else:
            pass
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        self.enter()

    def sell(self):
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        print "Your gold: %d  -  Clown's gold: %d\n" % (
            player.user.gold, map.currentLocation.gold)
        for x in inventory.inventory.inventory:
            print "%s - %d value" % (x.name, x.value)
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        sell = raw_input("Pick an Item to sell\n> ").upper()
        check = False
        for x in inventory.inventory.inventory:
            if x.name == sell:
                if x.value <= map.currentLocation.gold:
                    inventory.inventory.inventory.remove(x)
                    player.user.gold += x.value
                    map.currentLocation.gold -= x.value
                    map.currentLocation.tradeItems.append(x)
                    print "%r has been sold." % x.name
                    inventory.inventory.calcWeight()
                    check = True
                    break
                else:
                    print "The Clown doen't have enough gold to buy that."
            else:
                pass
        if check is False:
            print "You're not carrying that."
        else:
            pass
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        self.enter()


#Allows player to pickup items or not, based on weight/max weight
class Grab(object):

    def enter(self):
        CheckHP().enter()
        if inventory.inventory.weight < inventory.inventory.maxWeight:
            print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
            get = (raw_input("Which item?\n> ")).upper()
            check = False
            for x in map.currentLocation.items:
                if x.name == get:
                    inventory.inventory.inventory.append(x)
                    map.currentLocation.items.remove(x)
                    inventory.inventory.calcWeight()
                    print "\n%s added to inventory" % x.name
                    check = True
                    break
                else:
                    pass
            if check is False:
                print "That item isn't here"
            print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        else:
            print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
            print "You can't carry any more items."
            print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        CheckHP().enter()


#Allows player to drop unwanted items
class Drop(object):

    def enter(self):
        CheckHP().enter()
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        get = (raw_input("Which item:\n> ")).upper()
        check = False
        for x in inventory.inventory.inventory:
            if x.name == get:
                map.currentLocation.items.append(x)
                inventory.inventory.inventory.remove(x)
                inventory.inventory.calcWeight()
                print "\n%s removed from inventory" % x.name
                check = True
                break
            else:
                pass
        if check is False:
            print "You don't have that item."
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        CheckHP().enter()


#Allows player to equip weapons from inventory list
class Equip(object):

    def enter(self):
        CheckHP().enter()
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        get = (raw_input("Which item:\n> ")).upper()
        if equipped.equipped:
            inventory.inventory.inventory.append(equipped.equipped)
            equipped.equipped = None
        else:
            equipped.equipped = None
        check = False
        for x in inventory.inventory.inventory:
            if x.name == get:
                #If item doesn't have damage attribute, it's not a weapon
                try:
                    x.damage
                    equipped.equipped = x
                    inventory.inventory.inventory.remove(x)
                    print "%s has been equipped." % equipped.equipped.name
                except AttributeError:
                    print "You can't equip that."
                check = True
                break
            else:
                pass
        if check is False:
            print "You don't have that item."
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        CheckHP().enter()


#Allows player to Unequip weapon and place it in inventory
class Unequip(object):

    def enter(self):
        CheckHP().enter()
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        if not equipped.equipped:
            print "There is no weapon to 'unequip'...."
            print "...dumbass..."
        else:
            print "%s has been unequipped." % equipped.equipped.name
            inventory.inventory.inventory.append(equipped.equipped)
            equipped.equipped = None
            equipped.Equipped().enter()
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        CheckHP().enter()


#Allows player to increase health
class Drink(object):

    def enter(self):
        CheckHP().enter()
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        get = (raw_input("Which item:\n> ")).upper()
        check = False
        for x in inventory.inventory.inventory:
            if x.name == get:
                try:
                    x.effect
                    player.user.hp += x.effect
                    inventory.inventory.inventory.remove(x)
                    if player.user.hp > player.user.maxHp:
                        player.user.hp = player.user.maxHp
                    print "You've been healed %d points" % x.effect
                    check = True
                    break
                except AttributeError:
                    print "You can't drink that."
            else:
                pass
        if check is False:
            print "You don't have that item."
        inventory.inventory.calcWeight()
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        CheckHP().enter()


#Displays stats of player
class Status(object):

    def enter(self):
        CheckHP().enter()
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        print "LEVEL = %d" % player.user.level
        print "XP = %d / %d" % (player.user.xp, ((
            (10 * ((player.user.level + 1)**2) + (100 * (player.user.level+1))))
            ))
        print "HEALTH = %d / %d" % (player.user.hp, player.user.maxHp)
        print "Load = %d / %d" % (inventory.inventory.weight,
            inventory.inventory.maxWeight)
        print "Gold = %d" % player.user.gold
        if not equipped.equipped:
            print "WEAPON = FISTS"
            print "DAMAGE = %d" % (player.user.damage)
        else:
            print "WEAPON = %s" % equipped.equipped.name
            print "DAMAGE = %d" % (player.user.damage +
                equipped.equipped.damage)
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        CheckHP().enter()


#Allows user to quit game
class Quit(object):

    def enter(self):
        print "Ha, you wuss. I knew you'd give up."
        print "Although, I did expect it to be sooner."
        exit()


#Runs through options available when attacking an enemy
class Attack(object):

    def enter(self):
        CheckHP().enter()
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        if not map.currentLocation.enemy:
            print "You can't 'attack' what isn't there..."
        elif map.currentLocation.enemy.hp <= 0:
            CheckHP().enter()
            print "Good Job! The %s is dead." % map.currentLocation.enemy.name
            map.currentLocation.enemy = None
        else:
            if not equipped.equipped:
                map.currentLocation.enemy.hp -= (player.user.damage)
                player.user.hp -= map.currentLocation.enemy.damage
                player.user.xp += (player.user.damage)
                print "You have damaged him."
                print "He as also attacked you."
                print "His life is at %d of %d." % (
                    map.currentLocation.enemy.hp,
                    map.currentLocation.enemy.maxHp)
                print "Your life is at %d of %d." % (
                    player.user.hp, player.user.maxHp)
            else:
                #Creates random damage from weapons, critals-hits or glances
                x = random.randint(1, 3)
                if x == 1:
                    print "You just glanced him."
                    map.currentLocation.enemy.hp -= ((player.user.damage +
                        equipped.equipped.damage) / 2)
                    print "And he hit you good."
                    print "Your not going to win fighting like that."
                    player.user.hp -= (map.currentLocation.enemy.damage)
                    print "His life is at %d of %d." % (
                        map.currentLocation.enemy.hp,
                        map.currentLocation.enemy.maxHp)
                    print "Your life is at %d of %d." % (
                        player.user.hp, player.user.maxHp)
                elif x == 2:
                    map.currentLocation.enemy.hp -= (
                        player.user.damage + equipped.equipped.damage)
                    print "You hit him."
                    player.user.xp += (
                        player.user.damage + equipped.equipped.damage)
                    player.user.hp -= map.currentLocation.enemy.damage
                    print "But he landed a hit too."
                    print "His life is at %d of %d." % (
                        map.currentLocation.enemy.hp,
                        map.currentLocation.enemy.maxHp)
                    print "Your life is at %d of %d." % (
                        player.user.hp, player.user.maxHp)
                elif x == 3:
                    map.currentLocation.enemy.hp -= (
                        player.user.damage + equipped.equipped.damage * 2)
                    print "Wow, a magnificent hit. CRITICAL DAMAGE."
                    player.user.xp += (
                        player.user.damage + equipped.equipped.damage)
                    print "He landed a decent hit as well."
                    player.user.hp -= map.currentLocation.enemy.damage
                    print "His life is at %d of %d." % (
                        map.currentLocation.enemy.hp,
                        map.currentLocation.enemy.maxHp)
                    print "Your life is at %d of %d." % (
                        player.user.hp, player.user.maxHp)
                else:
                    print "An error occured. Please attack again"
            if map.currentLocation.enemy.hp <= 0:
                CheckHP().enter()
                print "\nGood Job! The %s is dead." % (
                    map.currentLocation.enemy.name)
                map.currentLocation.enemy.hp = map.currentLocation.enemy.maxHp
                map.currentLocation.enemy = None
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        CheckHP().enter()


#Displays options for player when attempting to move from location
class Move(object):

    def enter(self):
        CheckHP().enter()
        player.user.enter()
        self.checkEnemy()
        Look().enter()

    #You can't move if there is a enemy present
    def checkEnemy(self):
        if (not map.currentLocation.enemy or
            map.currentLocation.enemy.hp <= 0):
            self.move()
        else:
            print "Seriously, that %s won't let you just walk away." % (
                map.currentLocation.enemy.name)
            print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        CheckHP().enter()

    #If no enemy is present, gives direction options
    def move(self):
        map.currentLocation.visited = True
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        print "\nFrom here you can 'move' %s" % (
            map.currentLocation.availDir.keys())
        print "Which direction?"
        direction = raw_input("> ").upper()
        if direction in map.currentLocation.availDir:
            map.currentLocation = map.currentLocation.availDir.get(direction)
            if map.currentLocation.visited is False:
                self.load()
            else:
                pass
        else:
            print "That's not an option"
            self.move()

    #Loads new location after direction is established
    def load(self):
        map.currentLocation.enter()
        if not map.currentLocation.enemy:
            pass
        else:
            map.currentLocation.enemy.enter()
        if not map.currentLocation.items:
            pass
        else:
            for x in map.currentLocation.items:
                x.enter()


#This is called on at nearly every command to ensure the player is not dead
class CheckHP(object):

    def enter(self):
        if player.user.hp <= 0 and not map.currentLocation.enemy:
            print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
            print "You have died."
            print "Goodbye....."
            print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
            end = raw_input("Press enter to exit\n>")
            end = end
            exit()
        elif player.user.hp <= 0:
            print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
            print "Both your arms have been ripped off and"
            print "the %s has eaten your face." % (
                map.currentLocation.enemy.name)
            print "You gave it a good effort, but you are now dead."
            print "Goodbye...."
            print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
            end = raw_input("Press enter to exit\n>")
            end = end
            exit()
        else:
            pass


#List of available commands
class Command(object):
    commands = {
        'look': Look(),
        'inventory': Inventory(),
        'trade': Trade(),
        'move': Move(),
        'grab': Grab(),
        'drop': Drop(),
        'equip': Equip(),
        'unequip': Unequip(),
        'attack': Attack(),
        'drink': Drink(),
        'status': Status(),
        'help': Help(),
        'quit': Quit()
    }

    #After is command has run its scprit, with reloads this function
    #Not sure why...but it works for reducing nested commands
    def enter(self):
        while 1 == 1:
            val = raw_input("> ").lower()
            if val in self.commands.keys():
                command = self.commands.get(val)
                command.enter()
            else:
                print "Not a valid input"
                print "Type HELP for command options"