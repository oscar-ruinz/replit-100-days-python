from replit import db
import os,time,datetime

def addTweet():
    timestamp = str(datetime.datetime.now())
    content = input("What you gonna tweet? > ")
    db[timestamp] = content
def viewTweet():
    counter = 0
    for key in db:
        print(f"{key}: {db.get(key)}")
        counter += 1
        if (counter%10) == 0:
            option = input("Another 10? (y/n)").lower()
            if option == "y":
                os.system("clear")
            else:
                break
while True:
    os.system("clear")
    print("Fake Twitter\n")
    menu = input("Select an option:\n1.- Add\n2.- View\n> ")

    if menu == "1":
        addTweet()
    elif menu == "2":
        viewTweet()
    else:
        print("Invalid option")
    time.sleep(1)