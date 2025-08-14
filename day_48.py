print("HIGH SCORE TABLE")
f = open("HighScores.txt","a+")
while True:
  initials = str(input("Input your 3 letters initials > ")).upper()
  score = str(input("Input your score (0 - 100000) > "))
  f.write(f"{initials} {score}\n")
  print("\nAdded to high score table.\n")

  menu = input("Add another? y/n?")
  if menu.lower() != "y":
    break
f.close()