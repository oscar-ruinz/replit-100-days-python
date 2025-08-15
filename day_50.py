import os, time,random

def addIdea():
  os.system("clear")
  f = open("my.ideas","a+")
  idea = input("Input your idea. > ")
  f.write(f"{idea}\n")
  print("Nice! Your idea has been stored.")
  f.close()

def printRandomIdea():
  ideas = []
  os.system("clear")
  if os.path.exists("my.ideas"):
    f = open("my.ideas","r")
    while True:
      idea = f.readline().strip()
      if idea == "":
        break
      else:
        ideas.append(idea)
    print(random.choice(ideas))
    time.sleep(1)
    f.close()
  else:
    print("You have no ideas stored yet!") 

print("Idea storage")

while True:
  os.system("clear")
  menu = input("What do you want to do?\n1 - Add idea.\n2 - Print random idea.\n>")
  if menu == "1":
    addIdea()
  elif menu == "2":
    printRandomIdea()
  else:
    print("Invalid option!")

  exit = input("Again? (y/n) > ")
  if exit.lower() != "y":
    break