class Armor:
    def __init__(self, strength):
        self.strength = strength

    # String override for printing
    def __str__(self):
        return str(self.strength)