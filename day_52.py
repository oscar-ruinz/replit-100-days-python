import os, time

debugMode = False
pizza = []
pizzaList = []

try:
  f = open("pizza.txt","r")
  pizzaList = eval(f.read())
  f.close()
except Exception as err:
  print("Error to open the file")
  if debugMode:
    print(err)

def addPizza():
  os.system("clear")
  name = str(input("Name > "))
  toppings = str(input("Toppings >"))
  try:
    qty = int(input("Quantity > "))
  except Exception as err:
    qty = int(input("You must input a numerical character, try again. >"))
    if debugMode:
      print(err)
  size = str(input("Size (s/m/l) > ")).lower()
  if size == "s":
    total = qty * 9.99
  elif size == "m":
    total = qty * 12.99
  else:
    total = qty * 14.99
  total = round(total,2)
  pizza = [name,toppings,size,qty,total]
  pizzaList.append(pizza)
  f = open("pizza.txt", "w") 
  f.write(str(pizzaList)) 
  f.close()

def printPizzas():
  os.system("clear")
  if pizzaList == []:
    print("No pizzas registered!")
  else:
    print(f"{'Name':^20}|{'Topping':^20}|{'Size':^10}|{'Quantity':^10}|{'Total':^10}")
    for row in pizzaList:
      print(f"{row[0]:^20}|{row[1]:^20}|{row[2]:^10}|{row[3]:^10}|{row[4]:^10}")

  
while True:
  os.system("clear")
  print("Pepe's Pizzerias\n")
  menu = str(input("1: Add Pizza\n2: View Pizzas\n>"))

  if menu == "1":
    addPizza()
  elif menu == "2":
    printPizzas()
  else:
    print("Invalid option")
  time.sleep(2)