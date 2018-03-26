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
# TODO - THIS JUST MAKES GARBAGE FOR NOW
def gen_rooms():
    global rooms
    rooms = list()
    for x in range(12):
        rooms.append(Room(1))


# Prompt user for name, generate random armor, weapon, & health
def gen_hero():
    global player
    player = Hero(input("Enter hero name:"))


# Instantiate any variables needed
def init():
    # Define globals
    global rooms, current_room, player

    # Call other init methods
    gen_rooms()
    gen_hero()
    random.seed(None)

    # Setup defaults for simple vars
    current_room = 1 # Player starts out in room 1


greeting()
init()
while current_room > 0:
    current_room = rooms(current_room).prompt()
print("\nGAME OVER")
