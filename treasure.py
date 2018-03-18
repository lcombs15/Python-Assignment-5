class Treasure:
    def __init__(self, value):
        self.value = value

    # String override for printing
    def __str__(self):
        return str(self.value)