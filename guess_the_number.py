# Plan
import random
# 1. Create a random number that will need to be guessed in a specific range
number_to_be_guessed = random.randint(1, 100)
print("number to be guessed: ", number_to_be_guessed)
# 2. Ask user for an input,
print("Please guess a number")

# function to check whether the input > 0, if not it doesn't let it through
def checking_input():
    while True:
        try:
            user_input = int(input("Enter the number you want to guess "))
        except ValueError:
            print("Please enter a number > 0")
            continue
        if user_input > 0:
            print(f'You entered: {user_input}')
            return user_input
            break
        else:
            print("Number you are guessing is definitely bigger than 0!")

# initial guess
user_input = checking_input()

while user_input != number_to_be_guessed:
    # if user_input < random_number tell user it's low,
    # checking_input() to ensure input > 0
    if checking_input() < number_to_be_guessed:
        print("Guess is low.")
        user_input = int(input("Enter the number you want to guess "))
        continue
    # if user_input > random_number tell user it's high,
    # checking_input() to ensure input > 0
    elif checking_input() > number_to_be_guessed:
        print("Guess is high.")
        user_input = int(input("Enter the number you want to guess "))
        continue
    # 5. If he gets it right, the game is won
    else:
        break
print("You have won!")

