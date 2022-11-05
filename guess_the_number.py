# Plan
import random
# 1. Create a random number that will need to be guessed in a specific range
number_to_be_guessed = random.randint(1, 100)
print("number to be guessed: ", number_to_be_guessed)
# 2. Ask user for an input,
print("Please guess a number")
user_input = 0

# Making sure the number input is bigger than 0
while True:
    try:
        user_input = int(input("Enter the number you want to guess "))
    except ValueError:
        print("Please enter a number > 0")
        continue
    if user_input > 0:
        print(f'You entered: {user_input}')
        break
    else:
        print("Number you are guessing is definitely bigger than 0!")

while user_input != number_to_be_guessed:
    # 3. If input < random_number tell user
    if user_input < number_to_be_guessed:
        print("Guess is low.")
        user_input = int(input("Enter the number you want to guess "))
        continue
    # 4. Elif input > random_number tell user
    elif user_input > number_to_be_guessed:
        print("Guess is high.")
        user_input = int(input("Enter the number you want to guess "))
        continue
    # 5. If he gets it right, the game is won
    else:
        break
print("You have won!")


