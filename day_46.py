import os

def prettyPrint():
    os.system("clear")
    for key, value in MokeDex.items():
       for subkey,subvalue in value.items():
          print(f"{subkey}: {subvalue}",end=" | ")
       print()

MokeDex = {}
MokeBeast = {"name": None, "type": None, "special move": None, "starting HP": None, "starting MP": None}

while True:
   os.system("clear")
   print("👾 MokéBeast Generator 👾")
   name = input("Input the beast name > ")
   element = input("Input the beast element > ")
   specialMove = input("Input the beast special move > ")
   startingHP = input("Input the beast starting HP > ")
   startingMP = input("Input the beast starting MP > ")
   MokeBeast = {"name": name, "element": element, "special move": specialMove, "starting HP": startingHP, "starting MP": startingMP}
   MokeDex[name] = MokeBeast

   response = input("Again? y/n > ")
   if response == "y":
      continue
   else:
      break



prettyPrint()
