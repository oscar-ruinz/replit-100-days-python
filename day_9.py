print("Generation Generator")
print()
year = int(input("type the year were your born > "))

if year >= 1925 and year < 1947:
  print("You are a Traditionalist!!")
elif year >= 1947 and year < 1965:
  print("You are a Baby boomer!!")
elif year >= 1965 and year < 1982:
  print("You are a Generation X")
elif year >= 1982 and year < 1996:
  print("You are a Millenial!!")
elif year >= 1996 and year < 2015:
  print("You are a Generation Z")
else:
  print("You are probably dead!!")