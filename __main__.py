from creature import Hero
from room import Room
import random

#simple greeting output at beginning of game
def greeting():
    print("Welcome to Dungeons & Snakes!")
    print("NKU\t - \tCSC407")
    print("Coded by: "
          "Lucas Combs, "
          "Graeham Heil, & "
          "Chris Mckenney\n")


# Setup random rooms
def gen_rooms():
    global rooms
    rooms = list()
    for x in range(8):
        rooms.append(Room(list(), x))
        if x in (0, 8):
            # No monsters in the start/end rooms
            rooms[x].monster = None
        if x is 0:
            rooms[x].exits.append(1)
        elif x is 8:
            rooms[x].exits.append(7)
        else:
            rooms[x].exits.append(x - 1)
            rooms[x].exits.append(x + 1)


# Prompt user for name, generate random armor, weapon, & health
def gen_hero():
    global player
    player = Hero(input("Enter hero name: "))


greeting()
gen_rooms()
gen_hero()
current_room = 0
while current_room >= 0:
    current_room = rooms[current_room].prompt(player)
    if current_room is 8:
        print("You survived the dungeon with " + str(player.treasure) + "gold!")
        print()
        exit()

print("\nGAME OVER!!!")
