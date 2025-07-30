print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")

def colorChange(type):
  if type.lower() == 'grass':
    print("\033[32m", end="")
  elif type.lower() == 'fire':
    print("\033[31m", end="")
  elif type.lower() == 'earth':
    print("\033[33m", end="")
  elif type.lower() == 'water':
    print("\033[34m", end="")
  elif type.lower() == 'poison':
    print("\033[35m", end="")
  elif type.lower() == 'electric':
    print("\033[1;33m", end="")

MokeDex = {"name": None, "type": None, "special move": None, "staring HP": None, "staring MP": None}


for key in MokeDex:
  MokeDex[key] = input(f"Input your beast's {key} > ")
  print()

colorChange(MokeDex["type"])
print(f"Your beast is called {MokeDex['name']}. It is an {MokeDex['type']} beast with special move {MokeDex['special move']}. HP: {MokeDex['staring HP']} -- MP:{MokeDex['staring MP']} ")
