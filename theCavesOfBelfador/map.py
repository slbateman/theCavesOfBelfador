#! /usr/bin/env python
# Python 2.7
# created by Steve Bateman
# Copyright 2016, Creative Commons

import random
import enemies
import health
import weapons
import player


# A list of descriptions of areas
locInfo_list = [
"""It's a bit strange here. It's very damp. Not sure
if something is living in here. You should look around
a bit...
""",
"""You've entered into a small dark tunnel. You have to crawl
through. You can't see a thing... Maybe you might get lucky
and bump into something...
""",
"""Wow, what a grand opening you have found. It's lit quite
well for being underground. There are boxes everywhere, some
broken, some intact. Hope luck is with you on this one
""",
"""You have entered what appears to be a old jail cell. There
are bones scattered about. There is a large rat in the corner
chewing on a rotted piece of flesh...I wonder where he got it...
""",
"""It's pitch black. You can't see anything. You feel around
the walls to find your way. A brief glimmer catches your eye.
""",
"""You're in a large room, but there is no floor. The walls go
down as far as your eye can see. There is light coming from above.
Enough so you can see there is no chance of climbing up the walls,
and the rickety bridge at your feet to cross the cavern.
""",
"""As you crawl under the small opening under a large log that
has blocked your path, you look up to see the shimmer of spikes
covering the ceiling of the cave. Stay low and stay slow. You
never know what nasty things can be on the tips of those spikes.
""",
"""You slide your body through a tall but tight pathway. On the
other end you find yourself in a small cramped room.
""",
"""Your enter a room with a breeze. A strong and musky breeze.
With a smell of...a smell of... hmm... kinda like the underside
of a sweaty, nonbathing creature...I suggest you find a way out.
""",
"""Figures, a room with no floor. Just a small ledge along the
sides. Perfect for falling to your death. Be careful and keep
your hands out and along the slimy wall. I'm sure that will help.
""",
]

# A list of descriptions for item locations
itemInfo_list = [
"""You find a wooden box. It looks like it's been down here a while.
Inside you find:
""",
"""While looking around you see a odd shelf in the rock wall.
Something is reflecting light, what little there is. You climb
up to the shelf to find:
""",
"""There is a pile of bodies in a corner. Normally, I wouldn't
suggest looting corpses, but times aren't that great for you
right now.
Under a particularly smelly corpse you find:
""",
"""Wow, right there in open. What shall you find, but:
""",
"""There is a crack in the wall. As you nearly rip your hand
off, you find:
""",
"""You find a large chest. After pulling out rotted clothes
and blankets, you find:
""",
"""Chances are you're screwed. There's no way anything good is here,
except for maybe:
""",
]

# A list of descriptions for enemies
enemyInfo_list = [
"""You hear a strange growling noise. You can feel hot breathe
coming your way. You squint hard to can barely make out its shape.
Good luck, now you have to kill a:
""",
"""In front of you, you can see a creature huddled over a corpse.
Maybe you can run away. But you know you have to go beyond the
creature to escape the cave. As you move closer you can see it
clearly. Just in time for it to see you as well.
Good luck, now you have to kill a:
""",
"""Up ahead, you can see a creature clinging to the wall. As if
it's been waiting for you this whole time.
Good luck, now you have to kill a:
""",
"""Just as you pass the jagged rock at then end of the room, you
see it. Its teeth, its claws, and those evil eyes.
Good luck, now you have to kill a:
""",
"""Well, now you've done it. He's angry, and he's angry at you.
Good luck, now you have to kill a:
""",
]


# Area types (Start, Trade, Weak Enemy, Strong Enemy,
# Boss, Random Event, Aid, and Finish )


#This is the location type for the starting room/location
class Start(object):
    locInfo = """This place is dark and cold.
It's difficult to see anything.
\nIn the corner you see a slight glimmer...
"""
    itemInfo = """The glimmer is a bottle. Under a
pallet of wood. Two bottles!!
How did you get this lucky to find:"""
    enemyInfo = None
    #I want to ensure the player has some potions/elixirs before they progress
    items = [
            (health.HealthChooser().enter()),
            (health.HealthChooser().enter()),
    ]
    tradeItems = None
    enemy = None
    visited = False
    look = False
    trade = False

    #Since this is the starting room/location,
    #we don't need to refresh stats of potions/enemies
    def enter(self):
        pass


class Trade(object):
    locInfo = """There is a creepy clown in front of you.
He's got a big-ass backpack. He might have something
to TRADE with you. Although, he seems to want to play...
\nI suggest you don't play.\n"""
    itemInfo = None
    enemyInfo = None
    items = []
    tradeItems = None
    enemy = None
    visited = False
    look = False
    trade = True
    gold = player.user.maxHp * 3

    # Loads random Items for trade and the gold the trader has
    def enter(self):
        self.gold = player.user.maxHp * 3
        self.tradeItems = [
            (health.HealthChooser().enter()),
            (health.HealthChooser().enter()),
            (health.HealthChooser().enter()),
            (health.HealthChooser().enter()),
            (health.HealthChooser().enter()),
            (health.HealthChooser().enter()),
            (health.HealthChooser().enter()),
            (weapons.WeaponChooser().enter()),
            (weapons.WeaponChooser().enter()),
            (weapons.WeaponChooser().enter()),
        ]


#Some rooms/locations are required to have and enemy.
#This will load one of the two weak enemies.
class EnemyWeak(object):
    locInfo = """You've entered a large room. There are
bones on the floor. Corpses hanging from the ceiling.
There are spikes pointing up from the floor all around
you. The smell is wretched.
"""
    itemInfo = """In the center of room, as if on display,
you find a lonely bottle of:
"""
    enemyInfo = """The creature has been waiting for you.
It's been listing this whole time, hearing your whines, your
little weak battles. It can't wait to rip you limb from limb.
Good luck, now you have to kill a:
"""
    items = None
    tradeItems = None
    enemy = None
    visited = False
    look = False
    trade = False

    # Loads random Items and Enemy to area
    def enter(self):
        self.items = [(health.HealthChooser().enter())]
        self.enemy = enemies.EnemyChooser().enter(2, 3)


#This room/location will only have potions/elixirs with no enemies
class Aid(object):
    locInfo = """You've entered a small room through a
very small door. I can't imagine anything but rats getting
in. I think you're in luck. There are shelves everywhere.
"""
    itemInfo = """Unfortunately, most of the shelves are empty,
except for the one. The one displaying two lovely bottles of:
"""
    enemyInfo = None
    items = None
    tradeItems = None
    enemy = None
    visited = False
    look = False
    trade = False

    # Loads random potions/elixirs to area
    def enter(self):
        self.items = [
            (health.HealthChooser().enter()),
            (health.HealthChooser().enter()),
            (health.HealthChooser().enter()),
        ]


#Some rooms/locations are required to have and enemy.
#This will load one of the two strong enemies.
class EnemyStrong(object):
    locInfo = """What have you gotten yourself into?
There's no way you're getting out of this alive.
There is a small path leading to the center of the
room. The path is surrounded by lava on both sides.
"""
    itemInfo = """In the center you see two bottles.
You're going to need them to fight what's at the other
end of the path. Hurry and pick up the:
"""
    enemyInfo = """This guy isn't like those past creatures.
He stands 10 feet tall and is covered in blood. He's ready
to eat you whole. It looks like he'll do it with ease.
Good luck, now you have to kill a:
"""
    items = None
    tradeItems = None
    enemy = None
    visited = False
    look = False
    trade = False

    # Loads random Items and Enemy to area
    def enter(self):
        self.items = [
            (health.HealthChooser().enter()),
            (health.HealthChooser().enter()),
        ]
        self.enemy = enemies.EnemyChooser().enter(0, 1)


#These rooms/location will randomly generate weapons, potions and enemies
class RandomEvent(object):
    locInfo = None
    itemInfo = None
    enemyInfo = None
    items = None
    tradeItems = None
    enemy = None
    visited = False
    look = False
    trade = False

    # Loads Location Description, Item Description and Enemy Description
    # Randomly chooses to load random Items and Enemy to area
    def enter(self):
        self.locInfo = locInfo_list[random.randint(0, 9)]
        self.itemInfo = itemInfo_list[random.randint(0, 6)]
        self.enemyInfo = enemyInfo_list[random.randint(0, 4)]
        self.items = []
        for x in range(2):
            val = random.randint(1, 6)
            if val == 1:
                pass
            elif val == 2:
                y = health.HealthChooser().enter()
                self.items.append(y)
            elif val == 3:
                y = health.HealthChooser().enter()
                self.items.append(y)
            elif val == 4:
                y = weapons.WeaponChooser().enter()
                self.items.append(y)
            elif val == 5:
                pass
            elif val == 6:
                pass
            else:
                pass
        self.enemy = None
        val = random.randint(1, 3)
        if val == 1:
            pass
        elif val == 2:
            pass
        elif val == 3:
            self.enemy = enemies.EnemyChooser().enter(2, 3)
        else:
            pass


#The final location contains the Boss Monster "Belfador"
class Boss(object):
    locInfo = """You've entered a room like no other.
To the left you see a stack of bodies 15 feet high burning
from what appears to be a flamable slime. To the right you
can see flames shooting from the floor billowing smoke and
creating a thick haze in the top of the room.
"""
    itemInfo = """At your feet to see two bottles, as if
mocking you. I'm sure they where place there simply to give
you hope. You probably taste better that way. Well, might
as well use them. Grab:
"""
    enemyInfo = """At the opposite side of the room you can barely
make out the monstrous silhouette. He's got six massive
arms, horns that appear to scrape the ceiling and large
spines thorning off its back.
I would say good luck, but I'm not sure it will do much good.
To get out of this adventure you're going to have to kill:
"""
    items = None
    tradeItems = None
    enemy = None
    visited = False
    look = False
    trade = False

    # Loads random Items and loads boss to area
    def enter(self):
        self.itemInfo = itemInfo_list[random.randint(0, 6)]
        self.items = [
            (health.HealthChooser().enter()),
            (health.HealthChooser().enter()),
        ]
        self.enemy = enemies.Boss()


# Final area after boss fight to end game
class Finish(object):
    locInfo = None
    itemInfo = None
    enemyInfo = None
    items = None
    tradeItems = None
    enemy = None
    visited = False
    look = False
    trade = False

    # Ends game
    def enter(self):
        self.items = []
        self.enemy = None
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        print """I think I see a way out...

In the distance you seen sunlight shinning
though a small opening. You crawl you're way
out and take you first breathe of fresh air in
what seams like days.

 """
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        print """I can't believe you made it. CONGRATULATIONS!!!
Thanks for playing. Tell your friends."""
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        end = raw_input("Press enter to exit game\n>")
        end = end
        exit()

# Assigns each area an area type
a1 = Start()
b1 = RandomEvent()
c1 = RandomEvent()
d1 = RandomEvent()
e1 = RandomEvent()
f1 = RandomEvent()
g1 = RandomEvent()
h1 = RandomEvent()
i1 = Trade()
j1 = EnemyWeak()
l1 = RandomEvent()
m1 = RandomEvent()
n1 = RandomEvent()
j2 = RandomEvent()
l2 = RandomEvent()
n2 = RandomEvent()
b3 = RandomEvent()
c3 = RandomEvent()
d3 = Trade()
e3 = RandomEvent()
f3 = RandomEvent()
g3 = RandomEvent()
h3 = RandomEvent()
i3 = RandomEvent()
j3 = RandomEvent()
l3 = Aid()
n3 = RandomEvent()
b4 = RandomEvent()
l4 = RandomEvent()
n4 = RandomEvent()
b5 = RandomEvent()
c5 = Trade()
d5 = EnemyWeak()
f5 = EnemyWeak()
g5 = RandomEvent()
h5 = RandomEvent()
i5 = RandomEvent()
j5 = RandomEvent()
k5 = RandomEvent()
l5 = Trade()
n5 = EnemyWeak()
d6 = RandomEvent()
f6 = RandomEvent()
n6 = RandomEvent()
a7 = RandomEvent()
b7 = RandomEvent()
c7 = RandomEvent()
d7 = RandomEvent()
f7 = Trade()
h7 = RandomEvent()
i7 = RandomEvent()
j7 = EnemyStrong()
k7 = RandomEvent()
l7 = RandomEvent()
n7 = Trade()
a8 = EnemyStrong()
f8 = RandomEvent()
h8 = RandomEvent()
l8 = RandomEvent()
n8 = RandomEvent()
a9 = Trade()
b9 = Aid()
c9 = RandomEvent()
d9 = RandomEvent()
e9 = RandomEvent()
f9 = RandomEvent()
h9 = Aid()
i9 = RandomEvent()
j9 = RandomEvent()
l9 = RandomEvent()
n9 = RandomEvent()
j10 = RandomEvent()
l10 = RandomEvent()
n10 = RandomEvent()
b11 = Aid()
c11 = Trade()
d11 = RandomEvent()
e11 = RandomEvent()
f11 = RandomEvent()
g11 = RandomEvent()
h11 = RandomEvent()
j11 = RandomEvent()
l11 = RandomEvent()
m11 = Trade()
n11 = Aid()
b12 = RandomEvent()
h12 = RandomEvent()
j12 = RandomEvent()
b13 = RandomEvent()
c13 = RandomEvent()
d13 = RandomEvent()
e13 = RandomEvent()
f13 = Trade()
h13 = RandomEvent()
i13 = RandomEvent()
j13 = EnemyWeak()
k13 = RandomEvent()
l13 = Aid()
m13 = Trade()
n13 = Boss()
f14 = EnemyStrong()
n14 = Finish()

# Assigns each area possible direction a player can move
a1.availDir = {'EAST': b1}
b1.availDir = {'EAST': c1, 'WEST': a1}
c1.availDir = {'EAST': d1, 'WEST': b1}
d1.availDir = {'EAST': e1, 'WEST': c1}
e1.availDir = {'EAST': f1, 'WEST': d1}
f1.availDir = {'EAST': g1, 'WEST': e1}
g1.availDir = {'EAST': h1, 'WEST': f1}
h1.availDir = {'EAST': i1, 'WEST': g1}
i1.availDir = {'EAST': j1, 'WEST': h1}
j1.availDir = {'SOUTH': j2, 'WEST': i1}
l1.availDir = {'EAST': m1, 'SOUTH': l2}
m1.availDir = {'EAST': n1, 'WEST': l1}
n1.availDir = {'SOUTH': n2, 'WEST': m1}
j2.availDir = {'NORTH': j1, 'SOUTH': j3}
l2.availDir = {'NORTH': l1, 'SOUTH': l3}
n2.availDir = {'NORTH': n1, 'SOUTH': n3}
b3.availDir = {'EAST': c3, 'SOUTH': b4}
c3.availDir = {'EAST': d3, 'WEST': b3}
d3.availDir = {'EAST': e3, 'WEST': c3}
e3.availDir = {'EAST': f3, 'WEST': d3}
f3.availDir = {'EAST': g3, 'WEST': e3}
g3.availDir = {'EAST': h3, 'WEST': f3}
h3.availDir = {'EAST': i3, 'WEST': g3}
i3.availDir = {'EAST': j3, 'WEST': h3}
j3.availDir = {'NORTH': j2, 'WEST': i3}
l3.availDir = {'NORTH': l2, 'SOUTH': l4}
n3.availDir = {'NORTH': n2, 'SOUTH': n4}
b4.availDir = {'NORTH': b3, 'SOUTH': b5}
l4.availDir = {'NORTH': l3, 'SOUTH': l5}
n4.availDir = {'NORTH': n3, 'SOUTH': n5}
b5.availDir = {'NORTH': b4, 'EAST': c5}
c5.availDir = {'EAST': d5, 'WEST': b5}
d5.availDir = {'SOUTH': d6, 'WEST': c5}
f5.availDir = {'EAST': g5, 'SOUTH': f6}
g5.availDir = {'EAST': h5, 'WEST': f5}
h5.availDir = {'EAST': i5, 'WEST': g5}
i5.availDir = {'EAST': j5, 'WEST': h5}
j5.availDir = {'EAST': k5, 'WEST': i5}
k5.availDir = {'EAST': l5, 'WEST': j5}
l5.availDir = {'NORTH': l4, 'WEST': k5}
n5.availDir = {'NORTH': n4, 'SOUTH': n6}
d6.availDir = {'NORTH': d5, 'SOUTH': d7}
f6.availDir = {'NORTH': f5, 'SOUTH': f7}
n6.availDir = {'NORTH': n5, 'SOUTH': n7}
a7.availDir = {'EAST': b7, 'SOUTH': a8}
b7.availDir = {'EAST': c7, 'WEST': a7}
c7.availDir = {'EAST': d7, 'WEST': b7}
d7.availDir = {'NORTH': d6, 'WEST': c7}
f7.availDir = {'NORTH': f6, 'SOUTH': f8}
h7.availDir = {'EAST': i7, 'SOUTH': h8}
i7.availDir = {'EAST': j7, 'WEST': h7}
j7.availDir = {'EAST': k7, 'WEST': i7}
k7.availDir = {'EAST': l7, 'WEST': j7}
l7.availDir = {'SOUTH': l8, 'WEST': k7}
n7.availDir = {'NORTH': n6, 'SOUTH': n8}
a8.availDir = {'NORTH': a7, 'SOUTH': a9}
f8.availDir = {'NORTH': f7, 'SOUTH': f9}
h8.availDir = {'NORTH': h7, 'SOUTH': h9}
l8.availDir = {'NORTH': l7, 'SOUTH': l9}
n8.availDir = {'NORTH': n7, 'SOUTH': n9}
a9.availDir = {'NORTH': a8, 'EAST': b9}
b9.availDir = {'EAST': c9, 'WEST': a9}
c9.availDir = {'EAST': d9, 'WEST': b9}
d9.availDir = {'EAST': e9, 'WEST': c9}
e9.availDir = {'EAST': f9, 'WEST': d9}
f9.availDir = {'NORTH': f8, 'WEST': e9}
h9.availDir = {'NORTH': h8, 'EAST': i9}
i9.availDir = {'EAST': j9, 'WEST': h9}
j9.availDir = {'SOUTH': j10, 'WEST': i9}
l9.availDir = {'NORTH': l8, 'SOUTH': l10}
n9.availDir = {'NORTH': n8, 'SOUTH': n10}
j10.availDir = {'NORTH': j9, 'SOUTH': j11}
l10.availDir = {'NORTH': l9, 'SOUTH': l11}
n10.availDir = {'NORTH': n9, 'SOUTH': n11}
b11.availDir = {'EAST': c11, 'SOUTH': b12}
c11.availDir = {'EAST': d11, 'WEST': b11}
d11.availDir = {'EAST': e11, 'WEST': c11}
e11.availDir = {'EAST': f11, 'WEST': d11}
f11.availDir = {'EAST': g11, 'WEST': e11}
g11.availDir = {'EAST': h11, 'WEST': f11}
h11.availDir = {'SOUTH': h12, 'WEST': g11}
j11.availDir = {'NORTH': j10, 'SOUTH': j12}
l11.availDir = {'NORTH': l10, 'EAST': m11}
m11.availDir = {'EAST': n11, 'WEST': l11}
n11.availDir = {'NORTH': n10, 'WEST': m11}
b12.availDir = {'NORTH': b11, 'SOUTH': b13}
h12.availDir = {'NORTH': h11, 'SOUTH': h13}
j12.availDir = {'NORTH': j11, 'SOUTH': j13}
b13.availDir = {'NORTH': b12, 'EAST': c13}
c13.availDir = {'EAST': d13, 'WEST': b13}
d13.availDir = {'EAST': e13, 'WEST': c13}
e13.availDir = {'EAST': f13, 'WEST': d13}
f13.availDir = {'SOUTH': f14, 'WEST': e13}
h13.availDir = {'NORTH': h12, 'EAST': i13}
i13.availDir = {'EAST': j13, 'WEST': h13}
j13.availDir = {'NORTH': j12, 'EAST': k13, 'WEST': i13}
k13.availDir = {'EAST': l13, 'WEST': j13}
l13.availDir = {'EAST': m13, 'WEST': k13}
m13.availDir = {'EAST': n13, 'WEST': l13}
n13.availDir = {'SOUTH': n14, 'WEST': m13}
f14.availDir = {'NORTH': f13}
n14.availDir = {'NORTH': n13}

# Sets starting location
currentLocation = a1