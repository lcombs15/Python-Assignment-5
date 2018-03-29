import random
import creature


# return winner of fight
# A is challenger
def fight(a, b):
    # Seed Random
    random.seed(None)

    # Loop until someone (or both) dies
    while a.health > 0 and b.health > 0:
        if a.weapon.max_damage > b.armor:
            b.health -= a.weapon.swings_per_turn * random.randint(0, a.weapon.max_damage - b.armor)

        if b.weapon.max_damage > a.armor:
            a.health -= b.weapon.swings_per_turn * random.randint(0, b.weapon.max_damage - a.armor)

    # If no one dies, the player wins
    if a.health > 0 and b.health > 0:
        print("\nThe fight was a draw!")
        return a
    # If the player died, the Monster wins
    elif a.health <= 0:
        print("\n" + a.name + " has been defeated by " + b.name)
        return b
    # If the player didn't die, it must have been the Monster
    else:
        print("\n" + b.name + " has been defeated by " + a.name)
        return a


class Room:
    def __init__(self, exits, room_id):
        random.seed(None)
        self.treasure = random.randint(20, 100)
        self.exits = exits
        self.id = room_id
        self.monster = creature.Monster()

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

    def loot(self, player):
        print("\n Picked up " + str(self.treasure) + " gold.")
        player.treasure += self.treasure
        self.treasure = 0

    def leave(self):
        retval = int(input("\nLeave to which room? " + str(self.exits) + " "))

        if retval not in self.exits:
            print("Invalid room.")
            return self.leave()
        
        return retval

    def pickup(self, player):
        print("\nWhat would you like to pick up?")

        for i in range(0, len(self.weapons) - 1):
            print("\n\t(" + str(i) + ")" + str(self.weapons[i]))
        if i not in range(0, len(self.weapons) - 1):
            print("\nInvalid selection.")
            return self.pickup()

        # If a player drops a weapon it lands in the room
        self.weapons.append(player.pickup(self.weapons[i]))

    def prompt(self, player):
        random.seed(None)

        # Monster may decide to attack user when they enter the room
        if self.monster is not None:
            if random.randint(0, 100) % 2 is 0:
                print("\n OH NO! The " + str(self.monster.name) + " STRIKES!")
                if fight(self.monster, player) == self.monster:
                    return -1
            else:
                print("In the corner you spot: " + str(self.monster) + " in the corner.....")

        while True:
            print("\nWhat would you like to do?"
                  "\n (t) Pick up treasure"
                  "\n (f) Fight Monster"
                  "\n (p) Pick up weapons"
                  "\n (e) Exit to another room")

            option = input("\n: ")

            if option is "t":
                self.loot(player)
            elif option is "f":
                if self.monster is not None and self.monster.health > 0:
                    if fight(player, self.monster) == self.monster:
                        return -1
                else:
                    print("\nNo monster here to fight....")
            elif option is "e":
                return self.leave()
            elif option is "p":
                self.pickup()
            else:
                print("\nINVALID INPUT.")
