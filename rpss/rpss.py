import random


while True:
    user_action = input('Enter a choice (rock, paper, scissors, shotgun):')
    possible_actions = ['rock', 'paper', 'scissors', 'shotgun']
    computer_action = random.choice(possible_actions)
    print(f'\nYou chose {user_action} and the computer chose {computer_action}. \n')

    if user_action == computer_action:
        print(f'Both players selected {user_action}. Its a tie')
    elif user_action == 'rock':
        if computer_action == 'paper':
            print('computer chose paper, computer wins')
        elif computer_action == 'scissors':
            print('computer chose scissors, user wins')
        elif computer_action == 'shotgun':
            print('computer chose shotgun, user dies RIP')
    elif user_action == 'paper':
        if computer_action == 'scissors':
            print('computer chose scissors, computer wins')
        elif computer_action == 'rock':
            print('computer chose rock, user wins')
        elif computer_action == 'shotgun':
            print('computer chose shotgun, user dies RIP')
    elif user_action == 'scissors':
        if computer_action == 'rock':
            print('computer chose rock, computer wins')
        elif computer_action == 'paper':
            print('computer chose paper, user wins')
        elif computer_action == 'shotgun':
            print('computer chose shotgun, user dies RIP')
    elif user_action == 'shotgun':
        if computer_action == 'paper':
            print('computer chose paper, computer got shot')
        elif computer_action == 'scissors':
            print('computer chose scissors, computer got shot')
        elif computer_action == 'rock':
            print('computer chose rock, computer got shot')        
    play_again = input('Play again (y/n):')
    if play_again.lower() != 'y':
        break