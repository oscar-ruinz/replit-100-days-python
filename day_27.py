import random, time, os

def rollDice(sides):
  return random.randint(1,sides)

def generateStats(sixDice,twelveDice,type):
  multiplier = 10 if type == "health" else 12
  return int(((sixDice * twelveDice) / 2) + multiplier)
  
exit = "yes"
while exit == "yes":
  print("Character Builder")
  print()
  name = input("Name your Legend:\n ")
  characterType = input("Character Type (Human, Elf, Wizard, Orc):\n ")
  print()
  time.sleep(1)
  print(name)
  time.sleep(1)
  print("HEALTH:",generateStats(rollDice(6),rollDice(12),"health"))
  time.sleep(1)
  print("STRENGTH:",generateStats(rollDice(6),rollDice(12),"strength"))
  time.sleep(1)
  print("May your name go down in Legend")
  print()
  time.sleep(1)
  
  exit = input("Again?: ")
  if exit.lower() != "yes":
    break
  time.sleep(1)
  os.system("clear")