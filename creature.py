import builtins
class Creature:

    # Constructor
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    # String override for printing
    def __str__(self):
        return str("Creature: "
                   + "\n\tName: " + self.name
                   + "\n\tHealth: " + str(self.health)
                   + "\n\tWeapon: " + self.weapon
                   + "\n\tArmor: " + self.armor)