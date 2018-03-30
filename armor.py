import random


# Simple armor class to associate name with armor value
class Armor:
    def __init__(self):
        random.seed()
        self.value = random.randint(1, 10)
        names = ["Leather Vest", "T-Shirt", "Chain Mail",
                 "Banana Suit", "Ugly Sweater", "Fedora & a tie",
                 "Super-fresh suite", "Worthless 2018 UK NCAA Champs Gear"]
        # Assign random name from list
        self.name = self.names[random.randint(0, len(self.names) - 1)]

    def __str__(self):
        return self.name + " (a=" + str(self.value) + ")"
