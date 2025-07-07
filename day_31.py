def textToColor(color,word):
  if color=="red":
    print("\033[31m", word,"\033[0m", sep="", end="")
  elif color=="green":
    print("\033[32m", word,"\033[0m",sep="", end="")
  elif color=="brown":
    print("\033[33m", word,"\033[0m", sep="", end="")
  elif color=="blue":
    print("\033[34m", word,"\033[0m", sep="", end="")
  elif color=="yellow":
    print("\033[1;33m", word,"\033[0m", sep="", end="")
  else:
    print("\033[0m", word,"\033[0m", sep="", end="")


print("INTERFACE 1")
print(f"{"":>10}",end="")
textToColor("red","=")
print("=",end="")
textToColor("blue","=")
textToColor("yellow"," Music App ")
textToColor("blue","=")
print("=",end="")
textToColor("red","=")
print("\n")
print("🔥▶️   Radio Gaga")
print(f"{"":>6}",end="")
textToColor("yellow","Queen")
print("\n\n")
print("PREV")
print(f"{"":>6}",end="")
textToColor("green","NEXT\n")
print(f"{"":>12}",end="")
textToColor("red","PAUSE")

print("\n\n\n")
print("INTERFACE 2")
print(f"{"":>15}WELCOME TO")
print(f"{"":>12}",end="")
textToColor("blue","--   ARMBOOK   --")
print("\n")
print(f"{"":>12}",end="")
textToColor("yellow","Definitely not a rip off of")
print()
print(f"{"":>17}",end="")
textToColor("yellow","a certain other social")
print()
print(f"{"":>23}",end="")
textToColor("yellow","networking site.")
print("\n")
print(f"{"":>17}",end="")
textToColor("red","Honest.")
print("\n")
Username = "Username:"
print(f"{Username:>25}")
password = "Password:"
print(f"{password:>25}")







