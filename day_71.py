from replit import db
import random, os, time

def login():
  os.system("clear")
  try:
    user = input("Username: > ")
    password = input("Password: > ")
    salt = db[user]["salt"]
    saltPass = f"{password}{salt}"
    saltPass = hash(saltPass)

    if saltPass == db[user]["password"]:
      print("Login succesful")
    else:
      print("Wrong password.")
  except:
    print("User not found")

def createUser():
  os.system("clear")
  user = input("Username: > ")
  password = input("Password: > ")
  salt = random.randint(1000,9999)
  saltPass = f"{password}{salt}"
  saltPass = hash(saltPass)
  db[user] = {"password": saltPass,"salt": salt}
  print("\nUser created.")

while True:
  os.system("clear")
  print("Login system")

  menu = input("1: Add User\n2: Login\n> ")
  if menu == "1":
    createUser()
  elif menu == "2":
    login()
  else:
    print("Invalid option")
  time.sleep(3)