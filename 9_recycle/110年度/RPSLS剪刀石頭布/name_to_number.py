print()
"""
這是 110/2/11 的Code練習 
Testing template for name_to_number()
"""
import random

# Copy and paste your definiton of name_to_number() here
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    else:
        return 4

# Test calls to name_to_number()
print("rock= ",name_to_number("rock"))
print("Spock= ",name_to_number("Spock"))
print("paper= ",name_to_number("paper"))
print("lizard= ",name_to_number("lizard"))
print("scissors= ",name_to_number("scissors"))

print()