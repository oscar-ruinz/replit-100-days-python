import os, time

toDoList = []

def printList():
  print() 
  for item in toDoList:
    print(item)
  print()

while True:
  os.system("clear")
  print("\033[34mToDo List Manager\033[0m")
  menu = input("Do you want to view, add or edit the todo list?:\n\033[32m")
  print("\033[0m")
  if menu == "add":
    item = input("What's next on the ToDo List?: ")
    toDoList.append(item)
  elif menu == "edit":
    item = input("What do you want to remove?: ")
    if item in toDoList:
      toDoList.remove(item)
    else:
      print("That task doesn’t exist")
  elif menu == "view":
    printList()
  else:
    print("Invalid option!")
  time.sleep(2)