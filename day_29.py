def textToColor(color,word):
  if color=="red":
    print("\033[31m", word, sep="", end="")
  elif color=="green":
    print("\033[32m", word, sep="", end="")
  elif color=="brown":
    print("\033[33m", word, sep="", end="")
  elif color=="blue":
    print("\033[34m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")


print("Super Subroutine")
print("With my ", end="")
textToColor("red", "new program")
textToColor("reset", " I can just call red('and') ")
textToColor("red", "it will print in red ")
textToColor("blue", "or even blue")

