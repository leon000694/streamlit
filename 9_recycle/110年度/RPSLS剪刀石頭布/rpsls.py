print()
"""
**使用方法: random_if/elif/else_def/return_
Project solution for Python Programming Essentials
Rock-paper-scissors-lizard-Spock
"""
import random

# To equate the strings "RPSLS" to numbes as follow:
def name_to_number(name): 
    # Given string name, return integer 0, 1, 2, 3, or 4 
    # corresponding to numbering in video
    # convert name to number using if/elif/else
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return 5
    
def number_to_name(number):
    if number == 0:
        return "rock"
    if number == 1:
        return "Spock"
    if number == 2:
        return "paper"
    if number == 3:
        return "lizard"
    else:
        return "scissors"

def rpsls(player_choice):
    # Given string, play a game of RPSLS
    print("Player choose:", player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(5) # ====================> 對方出拳由亂數取值
    comp_choice = number_to_name(comp_number)
    print("You-co choose:", comp_choice)

    # compte difference of player_number and comp_number modelo five
    difference = (comp_number - player_number) % 5 # ================> 主要算法
    if difference == 0: # ===========================================> 主要判斷
        print("You two tie!")
        print()
    elif (difference == 1) or (difference == 2):
        print("You-co wins!")
        print()
    else:
        print("Player wins!")
        print()

# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

print()