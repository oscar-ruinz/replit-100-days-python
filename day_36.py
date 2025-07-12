peopleNames = []

def printList():
  print()
  for i in peopleNames:
    print(i)
  print()

while True:
  firstName = input("First Name: ").strip().capitalize()
  lastName = input("Last Name: ").strip().capitalize()
  fullName = f"{firstName} {lastName}"
  if fullName not in peopleNames:
    peopleNames.append(fullName)
  else:
    print("\nERROR: Duplicate name")
  printList()
  