print("HOW MANY SECONDS ARE IN A YEAR?")

days = int(input("How many days have the current year?"))
seconds = 60
minutes = 60
hours = 24
totalSeconds = seconds * minutes * hours * days

if days == 366:
  print("Number of seconds in a leap year are", totalSeconds)
else:
  print("Number of seconds in a year are", totalSeconds)