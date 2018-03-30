from creature import Hero
from room import Room
import random


# Welcome to the game!
def greeting():
    print("Welcome to Dungeons & Snakes!")
    print("NKU\t - \tCSC407")
    print("Coded by: "
          "Lucas Combs, "
          "Graeham Heil, & "
          "Chris Mckenney\n")


# Setup random rooms & respective exits
def gen_rooms():
    global rooms
    rooms = list()
    for x in range(7):
        rooms.append(Room(list(), x))
        if x in (0, 7):
            # No monsters in the start/end rooms
            rooms[x].monster = None
        if x is 0:
            rooms[x].exits.append(1)
        elif x is 7:
            rooms[x].exits.append(6)
        else:
            rooms[x].exits.append(x - 1)
            rooms[x].exits.append(x + 1)


# Create Hero object for player
def gen_hero():
    global player
    player = Hero(input("Enter hero name: "))


greeting()
gen_rooms()
gen_hero()
current_room = 0

# Keep going until GAME-OVER
# When a player dies, a room returns -1
while current_room >= 0:
    current_room = rooms[current_room].prompt(player)
    if current_room is 8:
        print("You win!")
        exit()

print("\nGAME OVER!!!")
