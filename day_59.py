def palindromize(word):
  if len(word) == 1:
    return word
  return word[len(word)-1] + palindromize(word[0:len(word)-1])

print("Palindrome Checker")
while True:
  word = input("Input a word > ").lower()
  if word == palindromize(word):
    print(f"{word.capitalize()} is a palindrome. Yay!")
  else:
    print(f"{word.capitalize()} is not a palindrome!")
