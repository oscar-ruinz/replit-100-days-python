exit = "yes"

while exit == "yes":
  animal = input("Enter a animal name: ")

  if animal == "dog":
    print("The dog barks (guau guau) !!")
  elif animal == "cat":
    print("The cat meows (miau)")
  elif animal == "cow":
    print("The cow mooooos")
  else:
    print("I dont know how that animal sound")

  exit = input("You wanna pick another animal? ")
