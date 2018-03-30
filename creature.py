import random
from weapon import Weapon
from armor import *


class Creature:
    treasure = 0

    # Rand gen
    def __init__(self, name):
        self.name = name
        self.health = random.randint(20, 100)
        self.weapons = list()
        self.weapons.append(Weapon())
        self.currentWeapon = self.weapons[0]
        self.armor = Armor()

    # pickup selected weapon
    def pickup(self, weapon):
        if len(self.weapons) is 8:
            print("\nSelect a weapon to drop:")

            for i in range(0, len(self.weapons) - 1):
                print("\n\t(" + str(i) + ")" + str(self.weapons[i]))
            temp = int(input("\n: "))
            i = temp
            if i not in range(0, len(self.weapons) - 1):
                print("\nInvalid selection.")
                return self.pickup(weapon)

            retval = self.weapons[i]
            self.weapons[i] = weapon
            # Tell the room which weapon the player dropped
            return retval
        else:
            self.weapons.append(weapon)

    # String override for printing
    def __str__(self):
        return self.name + " (H=" + str(self.health) + ", A=" + str(self.armor) + ")" + "\n\t....wielding a " + str(
            self.weapons[0])


class Hero(Creature):
    # Hero Wrapper Class
    # Random gen
    def __init__(self, name):
        Creature.__init__(self, name)


class Monster(Creature):
    # Monster Wrapper Class

    # Random gen
    def __init__(self):
        names = ["Nasty, slimy blob", "Mega Bird", "Headless Git Repo",
                 "Segmentation Fault", "Angry Bird",
                 "Off-by-one guy"]
        # Random name from list
        Creature.__init__(self, names[random.randint(0, len(names) - 1)])
