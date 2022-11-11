# Plan
import random
print("Welcome to the password generator")

# 1. Create an alphabet
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789¬£$%^&*()_+=-[]{}#;:./,|@~!"
password = ""

# 2. Take input from user_input how long he wants the password to be
print("Please input how long would you like your password to be.")
user_input = int(input())

# 3. Generate a random password on the given alphabet with the length provided
for index in range(user_input):
    password += random.choice(alphabet)
# 4. Log the password to the console with a message
print("This is your automatically generated, secure password: ", password)