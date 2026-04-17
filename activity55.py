import random 
while True:
    user_action = input('enter a choice(roch,paper,scissors):')
    possible_actions = ['rock','paper','scissor']
    computer_action = random.choice(possible_actions)
    print('\nyou chose(user_action),computer chose(computer_action).\n')
    if user_action == computer_action:
        print('both players selcted (user_action).its a tie')
    elif user_action == 'rock':
        if computer_action == 'scissors':
            print('you win')
        else:
            print('you lose')
    elif user_action == 'paper':
        if computer_action == 'rock':
            print('you win')
        else:
            print('you lose')
    elif user_action == 'scissors':
        if computer_action == 'paper':
            print('you win')
        else:
            print('you lose')
    play_again = input('play again?(y/n):')
    if play_again != 'y':
        break