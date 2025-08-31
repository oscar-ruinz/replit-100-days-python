from replit import db
import os,time,datetime


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

Password = "admin"
loginPass = input("Enter the password > ")
while Password==loginPass:
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
    