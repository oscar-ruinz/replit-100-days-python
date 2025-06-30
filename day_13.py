print("Exam Grade Calculator")

nameExam = input("Enter the exam name: ")
maxScore = int(input("Max. Possible Score: "))
userScore = int(input("Your score: "))

score = round(userScore / maxScore * 100,2)
print()
print()
print("Score in your",nameExam,"Exam :D")
if score >= 90:
  print("You got ",score,"% which is a A+", sep="")
elif score >= 80:
  print("You got ",score,"% which is a A", sep="")
elif score >= 70:
  print("You got ",score,"% which is a B", sep="")
elif score >= 60:
  print("You got ",score,"% which is a C", sep="")
elif score >= 50:
  print("You got ",score,"% which is a D", sep="")
elif score < 50:
  print("You got ",score,"% which is a F", sep="")
else:
  print("Try again!")