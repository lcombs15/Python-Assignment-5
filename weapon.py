class Weapon:
    def __init__(self, name, max_damage, swings_per_turn):
        self.name = name
        self.max_damage = max_damage
        self.swings_per_turn = swings_per_turn

    # String override for printing
    def __str__(self):
        return self.name + " (d=" + str(self.max_damage) + ",spt=" + str(self.swings_per_turn) + ")"