loan = 1000
apr = 5
years = 10

print("Loan Calculator")
print("$" + str(loan) +" over "+ str(years) + " years at " + str(apr)+ "% APR")
print()

total = loan

for year in range(years):
  interest = total * (apr/100)
  total += interest
  print("Year",year+1,"is",round(total,2))

print()
print("You paid $"+ str(round(total - loan,2)) + " in interest!")