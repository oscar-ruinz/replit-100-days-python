import os, random, time

TopTrump = {}
TopTrump["Barcelona"] = {"Goals per season": 85, "Titles": 97, "Squad value": 880, "Historic wins": 2100}
TopTrump["Real Madrid"] = {"Goals per season": 90, "Titles": 101, "Squad value": 980, "Historic wins": 2250}
TopTrump["Bayern"] = {"Goals per season": 88, "Titles": 83, "Squad value": 920, "Historic wins": 2150}
TopTrump["Milan"] = {"Goals per season": 75, "Titles": 49, "Squad value": 560, "Historic wins": 1900}
teams = ["Barcelona","Real Madrid", "Bayern","Milan"]
while True:
   os.system("clear")
   print("🌟Top Trumps🌟")
   print("Welcome to the Top Trumps 'The best soccer team in the world' Simulator")
   userCardPick = int(input("Chose your card:\n1 - Barcelona\n2 - Real Madrid\n3 - Bayern\n4 - Milan\n>"))
   if userCardPick == 1:
      userCard = "Barcelona"
   elif userCardPick == 2:
      userCard = "Real Madrid"
   elif userCardPick == 3:
      userCard = "Bayern"
   elif userCardPick == 4:
      userCard = "Milan"
   else:
      print("Invalid option - Restarting game")
      time.sleep(1)
      continue
   cpuCard = random.choice(teams)
   stat = int(input("Choose your stat:\n1 - Goals per season\n2 - Titles\n3 - Squad value (M$)\n4 - Historic wins\n>"))
   if stat == 1:
      statname = "Goals per season"
   elif stat == 2:
      statname = "Titles"
   elif stat == 3:
      statname = "Squad value"
   elif stat == 4:
      statname = "Historic Wins"
   else:
      print("Invalid option - Restarting game")
      time.sleep(1)
      continue

   print(f"{userCard} have a {statname} of {TopTrump[userCard][statname]}")
   print(f"{cpuCard} have a {statname} of {TopTrump[cpuCard][statname]}")

   if TopTrump[userCard][statname] > TopTrump[cpuCard][statname]:
      print(f"***** {userCard} wins! *****")
   elif TopTrump[userCard][statname] < TopTrump[cpuCard][statname]:
      print(f"***** {cpuCard} wins! *****")
   else:
      print(f"***** Its a draw! *****")
      
   
   response = input("Again? y/n > ")
   if response == "y":
      continue
   else:
      break

