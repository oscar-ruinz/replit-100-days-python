sentence = input("What sentence do you want rainbow-ising?\n\033[0;32m")
print("\033[0m", end='')
for letter in sentence:
  if letter.lower() == "y":
    print('\033[1;33m', end='') #yellow
  elif letter.lower() == "g":
    print('\033[0;32m', end='') #green
  elif letter.lower() == "b": 
    print('\033[0;34m', end='') #blue
  elif letter.lower() == "r":
    print('\033[0;31m', end='') #red
  elif letter.lower() == "p":
    print('\033[0;35m', end='') #purple
  elif letter.lower() == " ":
    print('\033[0m', end='') #back to default
  print(letter, end="")
  