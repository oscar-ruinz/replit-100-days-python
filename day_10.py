print("=== BILL CALCULATOR ===")

myBill = float(input("What was the bill?: "))
tipPercentage = int(input("How much tip you will leave? (10%,15%,18% or 20%): "))
numberOfPeople = int(input("How many people?: "))
tip = myBill * (tipPercentage/100)
answer = (myBill + tip) / numberOfPeople
answer = round(answer,2)
print("Total: ", round(myBill + tip))
print("You all owe", answer)