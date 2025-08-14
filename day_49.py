print("🌟Current Leader🌟")
print("Analyzing high scores.....")
highScore = 0
name = None
f = open("high.score","r")
while True:
  score = f.readline().strip()
  if score == "":
    break
  else:
    currentScore = score.split()
    if int(currentScore[1]) > int(highScore):
      highScore = currentScore[1]
      name = currentScore[0]
f.close()

print(f"Current leader is {name} {highScore}")