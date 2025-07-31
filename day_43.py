import random

bingocard = []

def createBingoCard():
  for x in range(0,3):
    row = []
    for y in range(0,3):
      row.append(random.randint(0,90))
    row.sort()
    bingocard.append(row)
  bingocard[1][1] = "BINGO"
  
def printCard():
  print("\033[1;33m")
  counter = 0
  for row in bingocard:
    print(f"{row[0]:^10}|{row[1]:^10}|{row[2]:^10}")
    if counter < 2:
      print("-------------------------------")
    counter += 1

print("David's Nan's Bingo Card Generator")
createBingoCard()
printCard()