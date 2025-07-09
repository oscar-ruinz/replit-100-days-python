import os
import random
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('day_28/naruto.wav')

def stop():
  pygame.mixer.fadeout(1000)

def play():
  sound.play(loops=-1)

def rollDice(sides):
  return random.randint(1,sides)

def generateStats(sixDice,twelveDice,type):
  multiplier = 10 if type == "health" else 12
  return int(((sixDice * twelveDice) / 2) + multiplier)

user = "yes"
while user == "yes":
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️\n")
  legendNameP1 = input("Name your Legend:\n")
  characterType = input("Character Type (Human, Elf, Wizard, Orc):\n")
  time.sleep(1)
  print()
  print(legendNameP1)
  time.sleep(1)
  legendHealthP1 = generateStats(rollDice(6),rollDice(12),"health")
  print("HEALTH:", legendHealthP1)
  time.sleep(1)
  legendStrengthP1 = generateStats(rollDice(6),rollDice(12),"strength")
  print("STRENGTH:",legendStrengthP1)
  time.sleep(1)
  print("\nWho are they battling?⚔️\n")
  time.sleep(1)
  legendNameP2 = input("Name your Legend:\n")
  characterType = input("Character Type (Human, Elf, Wizard, Orc):\n")
  time.sleep(1)
  print()
  print(legendNameP2)
  time.sleep(1)
  legendHealthP2 = generateStats(rollDice(6),rollDice(12),"health")
  print("HEALTH:", legendHealthP2)
  time.sleep(1)
  legendStrengthP2 = generateStats(rollDice(6),rollDice(12),"strength")
  print("STRENGTH:",legendStrengthP2)
  time.sleep(5)

  os.system("clear")

  roundNumber = 0
  play()

  while True:
    roundNumber += 1
    print("⚔️ BATTLE TIME ⚔️")
    time.sleep(1)
    print("\nThe battle begins!\n") if roundNumber == 1 else print("\nThe battle continues!\n")

    # roll the dices
    diceP1 = rollDice(6)
    diceP2 = rollDice(6)

    damage = abs(legendStrengthP1 - legendStrengthP2) + 1

    if diceP1 > diceP2:
      print(legendNameP1,"wins the first blow")
      print(legendNameP2,"takes a hit, with",damage,"damage\n")
      legendHealthP2 -= damage
    elif diceP2 > diceP1:
      print(legendNameP2,"wins the first blow")
      print(legendNameP1,"takes a hit, with",damage,"damage\n")
      legendHealthP1 -= damage
    else:
      print("Round",roundNumber,"its a draw!!")
      print("Lets play the next round :D\n")
    
    time.sleep(1)
    print(legendNameP1)
    time.sleep(1)
    print("HEALTH:",legendHealthP1,"\n")
    time.sleep(1)
    print(legendNameP2)
    time.sleep(1)
    print("HEALTH:",legendHealthP2,"\n")
    time.sleep(1)

    if legendHealthP1 > 0 and legendHealthP2 > 0:
      print("\nAnd they're both standing for the next round!\n")
      os.system("clear")
    elif legendHealthP1 <= 0:
      print("Oh no",legendNameP1,"has died!")
      print(legendNameP2, "destroyed",legendNameP1,"in",roundNumber,"rounds!")
      break
    else:
      print("Oh no",legendNameP2,"has died!")
      print(legendNameP1, "destroyed",legendNameP2,"in",roundNumber,"rounds!")
      break
    time.sleep(2)
  stop()
  user = input("\nAnother battle?:\n")
