import random

def play_the_game():
    user_input = input("Input `rock` for rock, `paper` for paper, or `scissors` for scissors").lower()
    computer_input = random.choice(['rock', 'paper', 'scissors'])

    if user_input == computer_input:
        return "It's a tie"
    else:
        determine_the_winner(user_input, computer_input)

def determine_the_winner(user_input, computer_input):
    if ((user_input == 'rock') and (computer_input == 'scissors')) or ((user_input == 'paper') and (computer_input == 'rock')) or ((user_input == 'scissors') and (computer_input == 'paper')):
        # user_input wins
        return f'User won by using {user_input} onto computer\'s  {computer_input}.'
    else:
        return f'Computer won by using {computer_input} onto user\'s  {user_input}.'

