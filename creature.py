class Creature:

    # Constructor
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

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


class Monster(Creature):
    # Monster Wrapper Class
    def __init__(self, name, health, weapon, armor):
        Creature.__init__(self, name, health, weapon, armor)