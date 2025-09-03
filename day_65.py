class character:
  name = None
  health = None
  magicPoints = None
  
  def __init__(self,name, health,magicPoints):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints

  def print(self):
    print(f"Name: {self.name}")
    print(f"Health: {self.health}")
    print(f"Magic Points: {self.magicPoints}\n")
      
  def setStats(self,health,mp):
    self.health = health
    self.magicPoints = mp


class player(character):
  
  def __init__(self,name, health,magicPoints,lives):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.lives = lives

  def print(self):
    print(f"Name: {self.name}")
    print(f"Health: {self.health}")
    print(f"Magic Points: {self.magicPoints}")
    print(f"Lives: {self.lives}")
    print(f"Alive?: {self.isAlive()}\n")
    

  def isAlive(self):
    if int(self.lives) > 0:
      return "Yes"
    else:
      return "No"


class enemy(character):

  def __init__(self,name, health,magicPoints,type,strength):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.type = type
    self.strength = strength

  def print(self):
    print(f"Name: {self.name}")
    print(f"Health: {self.health}")
    print(f"Magic Points: {self.magicPoints}")
    print(f"Type: {self.type}")
    print(f"Strength: {self.strength}\n")



class orc(enemy):

  def __init__(self,name, health,magicPoints,type,strength,speed):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.type = type
    self.strength = strength
    self.speed = speed
  
  def print(self):
    print(f"Name: {self.name}")
    print(f"Health: {self.health}")
    print(f"Magic Points: {self.magicPoints}")
    print(f"Type: {self.type}")
    print(f"Strength: {self.strength}")
    print(f"Speed: {self.speed}\n")


class vampire(enemy):

  def __init__(self,name, health,magicPoints,type,strength,day):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.type = type
    self.strength = strength
    self.day = day
  
  def print(self):
    print(f"Name: {self.name}")
    print(f"Health: {self.health}")
    print(f"Magic Points: {self.magicPoints}")
    print(f"Type: {self.type}")
    print(f"Strength: {self.strength}")
    print(f"Day: {self.day}\n")

print("🌟Generic RPG🌟\n")
David = player("David",100,50,3)
David.print()

Boris = vampire("Boris",45,70,"Vampire",3,"Day")
Boris.print()

Rishi = vampire("Rishi",70,10,"Vampire",75,"Day")
Rishi.print()

Bill = orc("Bill",60,5,"Orc",75,90)
Bill.print()

Ted = orc("Ted",75,40,"Orc",80,45)
Ted.print()

Station = orc("Station",35,40,"Orc",49,50)
Station.print()
