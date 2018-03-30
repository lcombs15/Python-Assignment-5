import random


class Armor:
    def __init__(self):
        random.seed()
        self.value = random.randint(1, 10)
        self.names = ["Leather Vest", "T-Shirt", "Chain Mail", "Banana Suit"]
        self.name = self.names[random.randint(0, len(self.names) - 1)]

    def __str__(self):
        return self.name + " (a=" + str(self.value) + ")"
