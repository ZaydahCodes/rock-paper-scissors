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

# #Write your code below this line 👇
import random

player = int(input ("what do youchoose: Type O for rock, 1 for paper or 2 for Scissors:\n"))

if player < 0 or player >= 3:
  print("please enter a valid number")
else:
  computer = random.randint(0,2)
  choice = [rock, paper, scissors]
  print(choice[player])
  print("computer chose:")
  print(choice[computer])
  
  
  
  if player == 0:
    if computer == 2:
      print("You win")
    elif computer == 0:
      print("it's a tie, play again")
    else:
      print("You lose")
  
  if player == 1:
    if computer == 0:
      print("You win")
    elif computer == 1:
      print("it's a tie, play again")
    else:
      print("You lose")

if player == 2:
  if computer == 1:
    print("You win")
  elif computer == 2:
    print("it's a tie, play again")
  else:
    print("You lose")
