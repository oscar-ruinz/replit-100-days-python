#from getpass import getpass as input

p1Score = 0
p2Score = 0
while True:
  player1 = input("Player 1, enter your movement (R,S,P): ")
  print()
  player2 = input("Player 2, enter your movement (R,S,P): ")
  print()
  
  
  if player1 == player2:
    if player1 == "R":
      print("You both picked Rock, draw!")
    elif player1 == "P":
      print("You both picked Paper, draw!")
    elif player1 == "S":
      print("You both picked Scissors, draw!")
    else:
      print("Both made an invalid move.")
      exit()
  elif player1 == "P":
    if player2 == "R":
      print("Player 1 🧻 has wrapped Player 2 🪨.")
      p1Score += 1
    elif player2 == "S":
      print("Player 2's ✂️ have torn Player 1's 🧻.")
      p2Score += 1
    else:
      print("Player 2 invalid movement ❌")
      exit()
  elif player1 == "S":
    if player2 == "P":
      print("Player 1's ✂️ have torn Player 2's 🧻.")
      p1Score += 1
    elif player2 == "R":
      print("Player 2's 🪨 has broken Player 1's ✂️.")
      p2Score += 1
    else:
      print("Player 2 invalid movement ❌")
  elif player1 == "R":
    if player2 == "P":
      print("Player 2 🧻 has wrapped Player 1 🪨.")
      p2Score += 1
    elif player2 == "S":
      print("Player 1's 🪨 has broken Player 2's ✂️.")
      p1Score += 1
    else:
      print("Player 2 invalid movement ❌")
      exit()
  else:
    print("Player 1 invalid movement ❌")
    exit()

  if p1Score == 3:
    print("Player 1's won.")
    break
  elif p2Score == 3:
    print("Player 2's won.")
    break