import functions as fun

websiteInfo = {"website name": None,"URL": None,"description": None,"rating": None}
list = [1,2,3,4,5]

print("Change color")
fun.textToColor("red","Hello world!")

print()
print("Roll a dice:")
print(fun.rollDice(6))

print()
print("pretty list")
fun.prettyPrint(list)

print()
print("Dictionary")
fun.printDict(websiteInfo)