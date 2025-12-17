import random

#printing welcoming
print("Welcome to the Paper Scissors Rock game!")
rock  = r'''    
    _______
---' ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = r''' 
    _______
---' ____)____
           ______)
          _______)
         _______)
---.__________)'''

scissors = r'''
    _______
---' ____)____
          ______)
       __________)
      (____)
---.__(___)'''

# List that stores all possible game choices
list_of_choices = [rock, paper, scissors]

# Ask the player to choose an option:
# 0 for Rock, 1 for Paper, 2 for Scissors
player_choice = int(input("Please choose paper, rock or scissors. Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# Display the player's choice
print(f"You chose: {list_of_choices[player_choice]}")

# Generate a random choice for the computer
# randint includes both start and end values
random_choice = random.randint(0, len(list_of_choices) - 1)

# Display the computer's choice
print(f"Computer chose: {list_of_choices[random_choice]}")

# Check if both choices are the same
if player_choice == random_choice:
    print("It's a draw.")

# Winning conditions for the player:
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock
elif (player_choice == 0 and random_choice == 2) or (player_choice == 2 and random_choice == 1) or (player_choice == 1 and random_choice == 0):
    print("You WIN!")

# If none of the above conditions are met, the player lose
else:
    print("You loose!")
