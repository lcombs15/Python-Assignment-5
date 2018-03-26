import random
from weapon import Weapon

class Creature:

    # Constructor
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    #Rand gen
    def __init__(self, name):
        self.name = name
        self.health = random.randInt(20, 100)
        self.weapon = Weapon()
        self.armor = random.randInt(1, 10)

    # String override for printing
    def __str__(self):
        return str(type(self).__name__ + ": "
                   + "\n\tName: " + self.name
                   + "\n\tHealth: " + str(self.health)
                   + "\n\tWeapon: " + str(self.weapon)
                   + "\n\tArmor: " + str(self.armor))


class Hero(Creature):
    # Hero Wrapper Class
    def __init__(self, name, health, weapon, armor):
        Creature.__init__(self, name, health, weapon, armor)

    #Random gen
    def __init__(self, name):
        Creature.__init__(self, name)


class Monster(Creature):
    # Monster Wrapper Class
    def __init__(self, name, health, weapon, armor):
        Creature.__init__(self, name, health, weapon, armor)

    #Random gen
    def __init__(self):
        names = ["Nasty, slimy blob", "Mega Bird", "Headless Git Repo", "Segmentation Fault", "Angry Bird", "Off-by-one guy"]
        Creature.__init__(self, names[random.randint(0,len(names)-1)])

""" 
Example Creatures
    print(Creature("Lucas",100,Weapon("Knife",17,4), Armor(9001)))
    print(Hero("Lucas",100,Weapon("Knife",17,4), Armor(9001)))
    print(Monster("Lucas",100,Weapon("Knife",17,4), Armor(9001)))
"""