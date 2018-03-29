import random
import creature


# return winner of fight
# A is challenger

class Room:
    def __init__(self, exits, room_id):
        random.seed(None)
        self.treasure = random.randint(20, 100)
        self.exits = exits
        self.id = room_id
        self.monster = creature.Monster()
        self.weapons = list()


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
        if len(self.weapons) == 0:
            print("\nThere are no weapons to pick up")
        else :

            print("\nWhat would you like to pick up?")

            for i in range(0, len(self.weapons)):
                print("\n\t(" + str(i) + ")" + str(self.weapons[i]))
            i = int(input("\n: "))
            if i not in range(0, len(self.weapons)):
                print("\nInvalid selection.")
                return self.pickup(player)

            # If a player drops a weapon it lands in the room
            self.weapons.append(player.pickup(self.weapons[i]))
            print("\n" + player.name + " picked up " + self.weapons[i].name)

            self.weapons.remove(self.weapons[i])
            self.weapons.remove(None)


    def prompt(self, player):
        random.seed(None)

        print("\n" + player.name + " has entered room #" + str(self.id))

        # Monster may decide to attack user when they enter the room
        if self.monster is not None:
            if random.randint(0, 100) % 2 is 0:
                print("\n OH NO! The " + str(self.monster.name) + " STRIKES!")
                if self.fight(self.monster, player) == self.monster:
                    return -1
            else:
                print("\n" + player.name + " spots " + str(self.monster) + " in the corner.....")

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
                    if self.fight(player, self.monster) == self.monster:
                        return -1
                else:
                    print("\nNo monster here to fight....")
            elif option is "e":
                return self.leave()
            elif option is "p":
                self.pickup(player)
            else:
                print("\nINVALID INPUT.")

    def fight(self, a, b):
        # Seed Random
        random.seed(None)

        self.weaponSelect(b)

        while a.health > 0 and b.health > 0:
            for i in range(0, a.weapons[0].swings_per_turn):
                aHit = random.randint(1, 20)
                if aHit > b.armor:
                    b.health -= random.randint(1, a.weapons[0].max_damage)

            if b.health > 0:
                for i in range(0, b.weapons[0].swings_per_turn):
                    bHit = random.randint(1, 20)
                    if bHit > a.armor:
                        a.health -= random.randint(1, b.weapons[0].max_damage)

        if a.health <= 0:
            print("\n" + a.name + " has been defeated by " + b.name)

            for weapon in a.weapons:
                self.weapons.append(weapon)
                print("\n" + a.name + " dropped " + weapon.name)

            return b
        elif b.health <= 0:
            print("\n" + b.name + " has been defeated by " + a.name)

            for weapon in b.weapons:
                self.weapons.append(weapon)
                print("\n" + b.name + " dropped " + weapon.name)

            return a

    def weaponSelect(self, hero):
        print("Please select which weapon you want to use:")
        i = 0
        for weapon in hero.weapons:
            print("\n(" + str(i) + ") " + weapon.name + ": Max damage: " + str(weapon.max_damage))
            i += 1
        option = int(input("\n: "))
        #add error handling incase user types a char instead of an int

        if option in range(0, len(hero.weapons)):
            print("current weapon is now " + hero.weapons[option].name)
            hero.currentWeapon = hero.weapons[option]

        else:
            print("invalid input")
            self.weaponSelect(hero)


