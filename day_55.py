import os, time, random

toDoList = []
files = os.listdir()
if "todo.list" in files:
  f = open("todo.list","r")
  toDoList = eval(f.read())
  f.close()
else:
  f = open("todo.list","a")
  f.close()

def pprintList(priority):
  os.system("clear")
  if priority == "high" or priority == "medium" or priority == "low":
    print(f"VIEW {priority.upper()} PRIORITY\n")
    for row in toDoList:
      if row[2].lower() == priority.lower(): 
        print(f"{row[0]:^10}|{row[1]:^10}|{row[2]:^10}")
  else:
    print("VIEW ALL\n")
    for row in toDoList:
      print(f"{row[0]:^10}|{row[1]:^10}|{row[2]:^10}")

def addTask():
  os.system("clear")
  print("ADD\n")
  task = input("What is it? ").strip()
  date = input("When is it due? ").strip()
  priority = input("How Important? ").strip().capitalize()
  row = [task,date,priority]
  toDoList.append(row)
  print("\nAdded to list")

def viewTask():
  os.system("clear")
  print("","1: View All","2: View Priority",sep="\n")
  option = input("> ")
  if option == "1":
    pprintList("")
  elif option == "2":
    priority = input("\nWhich Priority? ").strip().lower()
    pprintList(priority)
  else:
    print("Invalid option")

def removeTask():
  os.system("clear")
  print("REMOVE\n")
  rmTask = input("What would you like to remove?\n> ")
  for row in toDoList:
    if row[0] == rmTask:
      toDoList.remove(row)
  os.system("clear")
  print("REMOVE\n")
  for row in toDoList:
    print(f"{row[0]:^10}|{row[1]:^10}|{row[2]:^10}")

def editTask():
  os.system("clear")
  print("EDIT\n")
  rmTask = input("What would you like to edit?\n> ")
  os.system("clear")
  print("EDIT\n")
  for row in toDoList:
    if row[0] == rmTask:
      row[0] = input("New title: ")
      row[1] = input("New Due date: ")
      row[2] = input("New Priority: ")
      print("\nUpdated\n")

fileExist = False
while True:
  os.system("clear")
  print("\033[34mToDo List Management System\033[0m")
  print("","1: Add","2: View","3: Remove","4: Edit", "5: Exit",sep="\n")
  menu = input(">")
  if menu == "1":
    addTask()
  elif menu == "2":
    viewTask()
  elif menu == "3":
    removeTask()
  elif menu == "4":
    editTask()
  elif menu == "5":
    break
  else:
    print("Invalid option")

  folders = os.listdir()
  if "Backups" not in folders:
    os.mkdir("Backups")

  if not fileExist:
    randomName = "backup" + str(random.randint(0,10000000)) + ".txt"
    Filename = os.path.join("Backups/",randomName)
    f = open(Filename, "a+")
    f.write(str(toDoList))
    f.close()
    fileExist = True
  
  f = open("todo.list", "w") 
  f.write(str(toDoList)) 
  f.close()
  time.sleep(2)
