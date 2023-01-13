import random

print('\nWelcome in Roshambo (rock-paper-scissors) game!')
opts = ['rock', 'paper', 'scissors']
ai_points = 0
user_points = 0
while True:
    random.shuffle(opts)
    ai_choice = opts[0]
    user_choice = ''
    print('\n[R]ock\t[P]aper\t[S]cissors\t[Q]uit')
    while user_choice not in ['r', 'R', 'p', 'P', 's', 'S', 'q', 'Q']:
        user_choice = input(
            '\nPlease select: ')
        if user_choice == 'q' or user_choice == 'Q':
            break
        elif user_choice == 'r' or user_choice == 'R':
            if ai_choice == 'rock':
                print(f'A.I. also selected {ai_choice}. Draw')
            if ai_choice == 'scissors':
                print(f'A.I. selected {ai_choice}. You win!')
                user_points += 1
            if ai_choice == 'paper':
                print(f'A.I. selected {ai_choice}. You lost.')
                ai_points += 1
        elif user_choice == 'p' or user_choice == 'P':
            if ai_choice == 'paper':
                print(f'A.I. also selected {ai_choice}. Draw')
            if ai_choice == 'rock':
                print(f'A.I. selected {ai_choice}. You win!')
                user_points += 1
            if ai_choice == 'scissors':
                print(f'A.I. selected {ai_choice}. You lost.')
                ai_points += 1
        elif user_choice == 's' or user_choice == 'S':
            if ai_choice == 'scissors':
                print(f'A.I. also selected {ai_choice}. Draw')
            if ai_choice == 'paper':
                print(f'A.I. selected {ai_choice}. You win!')
                user_points += 1
            if ai_choice == 'rock':
                print(f'A.I. selected {ai_choice}. You lost.')
                ai_points += 1
        else:
            print('Wrong option.')

    print(f'\nResults:\nA.I. [{ai_points}] : [{user_points}] Human')

    play_again = 'default'
    while play_again not in ['y', 'Y', 'n', 'N']:
        play_again = input('\nDo you want to play again? [Y/N]: ')
    if play_again == 'n' or play_again == 'N':
        break
print(
    f'\n\nThanks for playing!\nMarek Gozdera\ngozderamarek@gmail.com\n{169:c} 2023\n\nPress enter...', end='')
input()
