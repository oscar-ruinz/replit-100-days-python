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
  menu = input("Do you want to view, add, edit, remove or clear the todo list?:\n\033[32m")
  print("\033[0m")
  if menu == "add":
    item = input("What's next on the ToDo List?:\n")
    if item in toDoList:
      print("That item its already in the list!")
    else:
      toDoList.append(item)
  elif menu == "edit":
    item = input("What do you edit to remove\n")
    if item in toDoList:
      index = toDoList.index(item)
      change = input("What do you want to change it to?\n")
      toDoList[index] = change
    else:
      print("That thask doesn't exist")
  elif menu == "remove":
    item = input("What do you want to remove?:\n")
    if item in toDoList:
      message = f"Are you sure you want to remove'{item}'?\n"
      confirmation = input(message)
      if confirmation == "yes":
        toDoList.remove(item)
    else:
      print("That task doesn’t exist")
  elif menu == "view":
    printList()
  elif menu == "clear":
    toDoList.clear()
    print("The Todo's list its clear")
  else:
    print("Invalid option!")
  time.sleep(2)