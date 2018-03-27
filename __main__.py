from creature import Hero
from room import Room
import random


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
        if x is 0:
            rooms[x].exits.append(1)
        elif x is 8:
            rooms[x].exits.append(7)
        else:
            rooms[x].exits.append(x-1)
            rooms[x].exits.append(x+1)


# Prompt user for name, generate random armor, weapon, & health
def gen_hero():
    global player
    player = Hero(input("Enter hero name: "))


# Instantiate any variables needed
def init():
    # Define globals
    global rooms, current_room, player

    # Call other init methods
    gen_rooms()
    gen_hero()
    random.seed(None)

    # Setup defaults for simple vars
    current_room = 0 # Player starts out in room 0


greeting()
init()
while current_room >= 0:
    current_room = rooms[current_room].prompt(player)
    if current_room is 8:
        print("You win!")
        exit()

print("\nGAME OVER!!!")
