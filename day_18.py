print("---Guess the random number---")

randomNumber = 12384
attempts = 0

while True:
  attempts += 1
  userNumber = int(input("What is your guess?: "))
  
  if randomNumber == userNumber:
    print("Correct!!")
    break
  elif userNumber > randomNumber:
    print("Too high!")
  elif userNumber < randomNumber:
    print("Too low!")
  else:
    print("Ese no es un número pescabicho")
    exit()
print("It took you",attempts,"guesses to get the number correct.")
print("Click 'run' to try again with a different number.")
