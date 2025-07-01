import random

def rollDice(sides):
  return random.randint(1,sides)

def healthStats():
  sixSideDice = rollDice(6)
  eigthSideDice = rollDice(8)
  return sixSideDice * eigthSideDice


print("⚔️ Character Stats Generator ⚔️")
while True:
  warriorName = input("Name your warrior: ")

  warriorHealth = healthStats()

  if warriorHealth > 40:
    print("Their health is:\033[34m " + str(warriorHealth) + "hp\033[0m")
  elif warriorHealth > 25:
    print("Their health is:\033[32m " + str(warriorHealth) + "hp\033[0m")
  elif warriorHealth > 10:
    print("Their health is:\033[22m " + str(warriorHealth) + "hp\033[0m")
  else:
    print("Their health is:\033[31m " + str(warriorHealth) + "hp\033[0m")

  exit = input("You wanna add another character?: ")
  if exit != "yes":
    break
