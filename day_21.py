tableNumber = int(input("What multiplication table wanna practice?: "))

points = 0
for i in range(1,11):
  answer = int(input("How much is " + str(tableNumber) + "x" + str(i) + "?"))

  if answer == (i*tableNumber):
    print("Great work!")
    points += 1
  else:
    print("Nope. The answer was",i*tableNumber)

print("------")
print("You scored",points,"out of 10.")