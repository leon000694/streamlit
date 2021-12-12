print()
"""
這是 110/2/11 的Code練習
Testing template for number_to_name()
"""
import random
# Copy and paste your definiton of number_to_name() here
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    else:
        return "scissors"

# Test calls to number_to_name()
remainder = (3-3) % 5
print("remainder= ", remainder)
print(number_to_name(0))
print(number_to_name(1))
print(number_to_name(2))
print(number_to_name(3))
print(number_to_name(4))

print()