import random, time, os

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downtown","jotas","python","apple"]

wordChosen = random.choice(listOfWords)
wordLetters = set(wordChosen)
tries = 0
listOfUsedLetters = []

print("🌟Hangman🌟")

while True:
  userLetter = input("Choose a letter: ").lower()
  while len(userLetter) > 1:
    userLetter = input("Choose only one letter: ").lower()
    
  if userLetter in listOfUsedLetters:
    print("You already pick this one")
  elif userLetter in wordLetters:
    print("Correct!")
    for letter in wordChosen:
      if letter.lower() == userLetter or letter in listOfUsedLetters:
        print(letter,end="")
      else:
        print("_",end="")
    wordLetters.remove(userLetter)
    if not wordLetters:
      print(f"You won with {7 - tries} lives left.")
      break
    print()
  else:
    tries += 1
    if tries <= 6:
      print("Nope, not in there.")
      print(f"{7 - tries} left.")
      print(HANGMANPICS[tries-1])
    else:
      print("You Lost!")
      print(HANGMANPICS[tries-1])
      break
  time.sleep(2)
  os.system("clear")
    
  listOfUsedLetters.append(userLetter)
  