from getpass import getpass as input

player1 = input("Player 1, enter your movement (R,S,P): ")
print()
player2 = input("Player 2, enter your movement (R,S,P): ")
print()


if player1 == player2:
  print("Its a draw!!")
  if player1 == "R":
    print("You both picked Rock, draw!")
  elif player1 == "P":
    print("You both picked Paper, draw!")
  elif player1 == "S":
    print("You both picked Scissors, draw!")
  else:
    print("Both made an invalid move.")
elif player1 == "P":
  if player2 == "R":
    print("Player 1 🧻 has wrapped Player 2 🪨.")
  elif player2 == "S":
    print("Player 2's ✂️ have torn Player 1's 🧻.")
  else:
    print("Player 2 invalid movement ❌")
elif player1 == "S":
  if player2 == "P":
    print("Player 1's ✂️ have torn Player 2's 🧻.")
  elif player2 == "R":
    print("Player 2's 🪨 has broken Player 1's ✂️.")
  else:
    print("Player 2 invalid movement ❌")
elif player1 == "R":
  if player2 == "P":
    print("Player 2 🧻 has wrapped Player 1 🪨.")
  elif player2 == "S":
    print("Player 1's 🪨 has broken Player 2's ✂️.")
  else:
    print("Player 2 invalid movement ❌")
else:
  print("Player 1 invalid movement ❌")