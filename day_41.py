websiteInfo = {"website name": None,"URL": None,"description": None,"rating": None}

print("🌟Website Rating🌟\n")

def printInfo(dict):
  for name, value in dict.items():
    print(f"{name}: {value}.")

for key in websiteInfo:
  value = str(input(f"Input the {key}: "))
  websiteInfo[key] = value
  print()


printInfo(websiteInfo)