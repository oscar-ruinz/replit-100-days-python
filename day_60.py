import datetime

today = datetime.date.today() 

print("Event Countdown Timer")

eventName = input("Input the event > ")
eventYear = int(input("Input the year > "))
eventMonth = int(input("Input the month > "))
eventDay = int(input("Input the day > "))



event = datetime.date(eventYear,eventMonth,eventDay) 
differenceDays = abs(today - event).days

if event > today:
  print(f"{eventName} is in {differenceDays} days!!")
elif event < today:
  print(f"🥲🤧{eventName} was {differenceDays} ago!!🥲🤧")
else:
  print(f"🥳🥳{eventName} is today!🥳🥳")