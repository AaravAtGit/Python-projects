rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
choices = [rock, paper , scissors]


a = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

b = random.randint(0,2)

print(choices[a])

print(f"the computer Choosed{choices[b]}")



if a == 0 and b == 0:
  print("IT'S A TIE LOL")
elif(a == 0 and b ==1): 
  print("YOU LOST LOL")
elif a == 0 and b == 2:
  print("YOU WON GG!")
elif a == 1 and b ==0:
  print("YOU WON GG!")
elif a == 1 and b == 1: 
  print("IT'S A TIE LOL")
elif a == 1 and b == 2:
  print("You lost Lmao")
elif a == 2 and b == 0:
  print("You lost lol")
elif a == 2 and b == 1:
  print("YOU WIN EZ GG!")
elif a == 2 and b ==2:
  print("Its a tie LOL")
else:
  print("WRONG INPUT RETRY")
