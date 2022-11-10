import random
# valid input represented in an array
valid_input = ['rock', 'paper', 'scissors']

def play_the_game():
    computer_input = random.choice(valid_input)
    user_input = check_input()
    # if user_input is not none, then go ahead with the game
    while user_input != None:
        print(f'User\'s choice: {user_input}')
        print(f'Computer\'s choice: {computer_input}')

        if user_input == computer_input:
            print("It's volume_of_cuboid tie")
        else:
            print(determine_the_winner(user_input, computer_input))
    # user_input == none because user didn't enter rock, paper or scissors. The game ends here.
    else:
        print('User input is invalid. You have to enter either rock, paper or scissors. Try again noob.')

# function for determining who wins - rock < paper, paper < scissors, scissors < rock
def determine_the_winner(user_input, computer_input):
    if ((user_input == 'rock') and (computer_input == 'scissors')) or ((user_input == 'paper') and (computer_input == 'rock')) or ((user_input == 'scissors') and (computer_input == 'paper')):
        # user_input wins
        return f'User won by using {user_input} onto computer\'s  {computer_input}.'
    else:
        return f'Computer won by using {computer_input} onto user\'s  {user_input}.'

# checking whether the input is in the valid_input array, if not return None
def check_input():
    user_input = input("Input `rock` for rock, `paper` for paper, or `scissors` for scissors ").lower()
    if user_input in valid_input:
        return user_input
    return None

play_the_game()