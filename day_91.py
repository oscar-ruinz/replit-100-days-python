import requests, json, time, os
from replit import db


def saveJoke(id,joke):
  db[id] = joke

def printJokes():
  for key in db.keys():
    print(f"{db[key]}\n")
  time.sleep(2)

while True:
  os.system("clear")
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
  callResults = result.json()
  joke = callResults["joke"]
  id = callResults["id"]
  print(f"{joke}\n")
  menu = input("(s)ave joke, (l)oad old jokes, (n)ew joke\n>").lower()

  if menu == "s":
    saveJoke(id,joke)
  elif menu == "l":
    printJokes()