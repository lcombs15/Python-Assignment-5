from creature import Creature, Hero, Monster
from armor import Armor
from room import Room
from treasure import Treasure
from weapon import Weapon
import menu

current_room = -1
rooms = None
player = None

def greeting():
    print("Welcome to Dungeons & Snakes!")
    print("NKU\t - \tCSC407")
    print("Coded by: "
          "Lucas Combs, "
          "Graeham Heil, & "
          "Chris Mckenney\n")

# Return array of random rooms
def gen_rooms():
    # retVal = []
    return NotImplementedError;

# Prompt user for name, generate random armor, weapon, & health
def gen_hero():
    return NotImplementedError
    # This is actually really close. It's just missing the random nature...
    # return Hero(input("Enter name: "), 100, Weapon("Knife",17,4), Armor(9001))

# Instantiate any variables needed
def init():
    global rooms, current_room, player
    rooms = gen_rooms()
    current_room = 1
    player = gen_hero()


greeting()
init()
while(current_room > 0):
    current_room = rooms[current_room].prompt()

print("\nGAME OVER\n")