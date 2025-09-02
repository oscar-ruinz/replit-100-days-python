import random

def rollDice(sides):
  return random.randint(1,sides)

def textToColor(color,word):
  if color=="red":
    print("\033[31m", word,"\033[0m", sep="")
  elif color=="green":
    print("\033[32m", word,"\033[0m", sep="")
  elif color=="brown":
    print("\033[33m", word,"\033[0m", sep="")
  elif color=="blue":
    print("\033[34m", word,"\033[0m", sep="")
  else:
    print(word)

def prettyPrint(list): 
  for index in range(len(list)): 
    print(f"{index + 1}: {list[index]}")

def printDict(dict):
  for name, value in dict.items():
    print(f"{name}: {value}.")