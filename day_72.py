from replit import db
import os,time,datetime,random


def addThought():
    os.system("clear")
    timestamp = str(datetime.datetime.now())
    content = input(f"Diary entry for {timestamp}\n\n> ")
    key = f"DE{timestamp}"
    db[key] = content

def viewThoughts():
    os.system("clear")
    matches = db.prefix("DE")
    matches = matches[::-1]
    for key in matches:
        print(db[key])
        menu = str(input("Next or exit? > ")).lower()
        if menu != "next":
            break
        os.system("clear")

def createUser():
  os.system("clear")
  print("Create the user.")
  user = input("Username: > ")
  password = input("Password: > ")
  salt = random.randint(1000,9999)
  saltPass = f"{password}{salt}"
  saltPass = hash(saltPass)
  db[user] = {"password": saltPass,"salt": salt}
  print("\nUser created.")

def login(user, password):
    if user in db:
        salt = db[user]["salt"]
        passSalt = f"{password}{salt}"
        passSalt = hash(passSalt)
        if passSalt == db[user]["password"]:
            return True
        else:
            print("Wrong user or password")
            return False
    else:
        print("User don't exist")

while True:
    counter = 0
    for key in db:
        counter += 1
        
    if counter == 0:
        createUser()
    else:
        os.system("clear")
        user = input("Username: > ")
        password = input("Password: > ")
        logResult = login(user,password)
        while logResult:
            os.system("clear")  
            print("Welcome to your diary!")
            menu = int(input("1: ADD\n2: VIEW\n> "))
            if menu == 1:
                addThought()
            elif menu == 2:
                viewThoughts()
            else:
                print("Invalid option")
            time.sleep(1)
