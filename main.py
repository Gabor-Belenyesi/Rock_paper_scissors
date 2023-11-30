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

#Write your code below this line 👇
import random

while True:
  computer_choose = random.randint(0, 2)
  user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
  
  
  if user_input == "0":
    print(rock)
  
  elif user_input == "1":
    print(paper)
    
  elif user_input == "2":
    print(scissors)
    
  else:
    print("Invalid input") 

  print("Computer chooses:")

  if computer_choose == 0:
    print(rock)
  elif computer_choose == 1:
    print(paper)
  else:
    print(scissors)

  if user_input == "0" and computer_choose == 0:
    print("Tie")
  elif user_input == "0" and computer_choose == 1:
    print("You lose")
  elif user_input == "0" and computer_choose == 2:
    print("You win")
  elif user_input == "1" and computer_choose == 0:
    print("You win")
  elif user_input == "1" and computer_choose == 1:
    print("Tie")
  elif user_input == "1" and computer_choose == 2:
    print("You lose")
  elif user_input == "2" and computer_choose == 0:
    print(("You lose"))
  elif user_input == "2" and computer_choose == 1:
    print("You win ")
  elif user_input == "2" and computer_choose == 2:
    print("Tie")

  user_choose = input("You wanna try again? 'Y' or 'N' ")
  if user_choose.upper() != "Y":
    print("Ok, bye!")
    break