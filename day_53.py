import os,time
inventory = []

try:
  f = open("items.txt","r")
  items = eval(f.read())
  f.close()
except Exception as err:
  print("The file items.txt doesn't exist.")
  print(f"Error: {err}")

def addItem():
  os.system("clear")
  item = input("Input the item to add: >").capitalize()
  inventory.append(item)
  print(f"{item} has been added to your inventory.")



def removeItem():
  os.system("clear")
  item = input("Input the item to remove: >").capitalize()
  if item in inventory:
    inventory.remove(item)
    print(f"{item} has been removed from your inventory.")
  else:
    print("That item doesn't exist in your inventory")
  
def viewItems():
  os.system("clear")
  print("Inventory\n----------")
  seen = []
  for item in inventory:
    if item not in seen:
        print(f"You have {inventory.count(item)} {item}")
        seen.append(item)

while True:
  os.system("clear")
  print("RPG Inventory")
  menu = input("1: Add 2: Remove 3: View > ")

  if menu == "1":
    addItem()
  elif menu == "2":
    removeItem()
  elif menu == "3":
    viewItems()
  else:
    print("Invalid option")

  
  f = open("items.txt", "w")
  f.write(str(inventory))
  f.close()
  time.sleep(2)