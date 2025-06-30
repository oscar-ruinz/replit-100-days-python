def login():
  while True:
    username = input("What is your username? ")
    password = input("What is your password? ")  

    if username == "oscar" and password == "1234":
      print("Welcome to Replit!!")
      break
    else:
      print("Whoops! I don't recognize that username or password. Try again!")
      continue

print("Replit Login System")
login()