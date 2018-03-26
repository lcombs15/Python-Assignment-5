import random

# return winner of fight
def fight(a, b):
    return NotImplementedError


class Room:
    def __init__(self, treasure, exits):
        self.treasure = treasure
        self.exits = exits

    def __init__(self, exits):
        self.treasure = random.randint(20,100)
        self.exits = exits

    """
        
        Fight if needed, then:
        
        Print something like this:
        
        while(still_here)
        
            You are in room n. What will you do?
                (1) Fight monster (If one is alive)
                (2) Pick up ...
                (2) Pick up ...
                (3) exit to X
                (4) exit to Z
        
        Carry out actions until user exits, then return new room #
    """
    # TODO, RETURNS ZERO TO END GAME SINCE THIS ISN"T FINISHED
    def prompt(self, player):
        # IE: fight(player, monster)
        return 0
