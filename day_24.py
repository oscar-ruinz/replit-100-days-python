import random

def rollDice (sides):
  if sides > 0:
    rollNumber = random.randint(1,sides)
    print("You rolled",rollNumber)
  else:
    print("There is no dice with less than one side.")

userSides = int(input("How many sides?: "))

while True:
  rollDice(userSides)
  exit = input("Roll again? ")
  if exit != "yes":
    break