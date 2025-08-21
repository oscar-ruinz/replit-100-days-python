import csv # Imports the csv library

with open("Day54Totals.csv") as file: 
  reader = csv.DictReader(file) 

  total = 0
  for row in reader: 
    total += float(row["Cost"]) * float(row["Quantity"])

print("Shop $$ Tracker")
print(f"Your shop took {round(total,2)} dollars today.")

