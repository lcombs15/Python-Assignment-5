import random
import creature


# return winner of fight


class Room:
    def __init__(self, exits, room_id):
        random.seed(None)
        self.treasure = random.randint(20, 100)
        self.exits = exits
        self.id = room_id
        self.monster = creature.Monster()
        self.weapons = list()

    #adds amount of gold in room to hero's treasure
    def loot(self, player):
        print("\n Picked up " + str(self.treasure) + " gold.")
        player.treasure += self.treasure
        self.treasure = 0

    #moves to selected room adjacent to current room
    def leave(self):
        retval = int(input("\nLeave to which room? " + str(self.exits) + " "))

        if retval not in self.exits:
            print("Invalid room.")
            return self.leave()

        return retval

    #If retreating from fight, moves back to previous room
    def retreat(self):
        retval = self.id - 1

        return retval

    #hero picks up weapon if available
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

            #if weapon is picked up, removed from room inventory
            self.weapons.remove(self.weapons[i])
            self.weapons.remove(None)

    #prompt when a room is entered
    def prompt(self, player):
        random.seed(None)

        print("\n" + player.name + " has entered room #" + str(self.id))

        # Monster may decide to attack user when they enter the room
        if self.monster is not None:
            if random.randint(0, 100) % 2 is 0:
                print("\n OH NO! The " + str(self.monster.name) + " STRIKES!")
                print("\n Do you fight or retreat!?"
                      "\n (f) Fight"
                      "\n (r) Retreat")
                option = input("\n: ")
                if option is "f":
                    if self.fight(player, self.monster) == self.monster:
                        return -1
                elif option is "r":
                    return self.retreat()
                else:
                    print("\n INVALID INPUT.")
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

    #called when a fight is commenced
    def fight(self, hero, monster):
        # Seed Random
        random.seed(None)

        #allows hero to select from available weapons
        self.weaponSelect(hero)


        while hero.health > 0 and monster.health > 0:
            for i in range(0, hero.weapons[0].swings_per_turn):
                heroHit = random.randint(1, 20)
                if heroHit > monster.armor:
                    monster.health -= random.randint(1, hero.weapons[0].max_damage)

            if monster.health > 0:
                for i in range(0, monster.weapons[0].swings_per_turn):
                    monsterHit = random.randint(1, 20)
                    if monsterHit > hero.armor:
                        hero.health -= random.randint(1, monster.weapons[0].max_damage)

        if hero.health <= 0:
            print("\n" + hero.name + " has been defeated by " + monster.name)

            return monster
        elif monster.health <= 0:
            print("\n" + monster.name + " has been defeated by " + hero.name)

            #monster drops weapon if defeated; added to room inventory
            for weapon in monster.weapons:
                self.weapons.append(weapon)
                print("\n" + monster.name + " dropped " + weapon.name)
            #if monster is defeated, monster removed from room
            self.monster = None
            return hero

    #Select from hero's weapon inventory
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


