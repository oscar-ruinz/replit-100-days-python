import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()

def pause():
  pygame.mixer.pause()

pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    # Start taking user input and doing something with it
    os.system("clear")
    print("It's playing a drama music audio!!")
    time.sleep(1)
    print("You like it ?")
    time.sleep(2)
    action = input("You wanna keep listening the music? ")
    if action == "yes":
      continue
    else:
      pause()
      break

while True:
  # clear the screen
  os.system("clear")

  # Show the menu
  print("🎵 PeraPOD Music Player 🎵")
  time.sleep(1)
  print("Press 1 to Play")
  print("Press 2 to Exit")
  print()
  print("Press anything else to see the menu again")

  # take user's input
  response = input("Enter your choice > ")
  # check whether you should call the play() subroutine depending on user's input
  if response == "1":
    play()
  elif response == "2":
    os.system("clear")
    exit()
  else:
    continue