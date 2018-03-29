import random


class Armor:
    def __init__(self):
        random.seed()
        self.value = random.randint(1, 10)
