import random


class Weapon:
    def __init__(self):
        types = ["Knife", "Sword", "Bow & Arrow",
                 "Spiked Baseball Bat", "Sock o' butter",
                 "Large pipe", "Prison Shank"]
        self.name = types[random.randint(0, types.__len__()) - 1]
        self.max_damage = random.randint(1, 10)
        self.swings_per_turn = random.randint(1, 5)

    # String override for printing
    def __str__(self):
        return self.name + " (d=" + str(self.max_damage) + ",spt=" + str(self.swings_per_turn) + ")"
