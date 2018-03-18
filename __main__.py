from creature import Creature, Hero, Monster
from armor import Armor
from room import Room
from treasure import Treasure
from weapon import Weapon

print("Welcome to Dungeons & Snakes!")
print("NKU\t - \tCSC407")
print("Coded by: "
      "Lucas Combs, "
      "Graeham Heil, & "
      "Chris Mckenney\n")

print(Creature("Lucas",100,Weapon("Knife",17,4), Armor(9001)))
print(Hero("Lucas",100,Weapon("Knife",17,4), Armor(9001)))
print(Monster("Lucas",100,Weapon("Knife",17,4), Armor(9001)))