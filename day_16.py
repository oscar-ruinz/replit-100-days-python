print("Fill in the blanc lyrics")
print("(Type in the blank lyrics and see if you are as cool as me.)")
print()

attempts = 0

while True:
  print("Never gonna ____ you up, never gonna let you down")
  guess = input(" > ")
  attempts += 1
  if guess == "give":
    break
  else:
    print("Nop, try again!")


print("Well done! It only took you",attempts,"attempts.")