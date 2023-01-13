import random

print('\nWelcome to BlackJack!')
user_bank = 1000
ai_bank = 1000
game_number = 0

while user_bank > 9 and ai_bank > 9:
    user_bet = '0'
    user_game_point = 0
    user_game_list = [0]
    ai_bet = 0
    ai_game_point = 0
    ai_game_list = []
    ai_core = 0
    game_number += 1
    print(f'\nGame number {game_number}.\nBank accounts:\nUser: [', end='')
    print(f'{user_bank} $', end='')
    print(f']\nA.I.: [', end='')
    print(f'{ai_bank} $', end='')
    print(']\n\n[Q]uit')

    # MAIN GAME
    print('\nCards have values from 2 to 11. The goal is 21 points.')

    user_game_point = random.randint(2, 11)
    user_game_list.append(user_game_point)

    while user_game_point <= 21:
        user_choice = 'default'
        print(
            f'\nYou draw a card with {user_game_list[len(user_game_list)-1] - user_game_list[len(user_game_list)-2]} points so now you have [', end='')
        print(f'{user_game_point}', end='')
        print(f'] points.\n')

        while user_choice not in ['y', 'Y', 'n', 'N', 'q', 'Q']:
            user_choice = input("Do you want to go on? (Y/N): ")
        if user_choice == 'q' or user_choice == 'Q':
            break
        if user_choice == 'y' or user_choice == 'Y':
            user_game_point += random.randint(2, 11)
            user_game_list.append(user_game_point)
            if user_game_point > 21:
                print(
                    f'\nUnfortunately, you failed. Your score is now: {user_game_point}.')
            if user_game_point == 21:
                print('\nBRAVO! You hit 21!')
                break
        if user_choice == 'n' or user_choice == 'N':
            break
    if user_choice == 'q' or user_choice == 'Q':
        break

    while ai_game_point < 12:
        ai_game_point += random.randint(2, 11)
        ai_game_list.append(ai_game_point)
    else:
        ai_core = random.randint(0, 1)
        if ai_core == 1:
            ai_game_point += random.randint(2, 11)
            ai_game_list.append(ai_game_point)

    # BETS
    while not user_bet.isnumeric() or int(user_bet) <= 0 or int(user_bet) > user_bank:
        user_bet = input('\nHow much do you bet? ')

        if not user_bet.isnumeric():
            print(f'Gimme a number from 1 to {user_bank}!')
            continue
        elif int(user_bet) == 0:
            print(
                f'You have to bet something. Gimme a number from 1 to {user_bank}.')
        elif int(user_bet) > user_bank:
            print(
                f"You don't have enough money. Gimme a number from 1 to {user_bank}.")
        if int(user_bet) == user_bank:
            print("WOW! You're playing VA BANQUE! Good luck!")

    user_bank -= int(user_bet)

    ai_bet = random.randint(1, ai_bank)
    if ai_bet == ai_bank:
        print('A.I. plays VA BANQUE!')
    ai_bank -= ai_bet

    print(f"\nStakes are:\nA.I.:\t[", end='')
    print(f'{ai_bet} $', end='')
    print(f']\nYours:\t[', end='')
    print(f'{user_bet} $', end='')
    print(']')

    # RESULTS

    print(f'\nResults:\nA.I. ', end='')
    print(f'{ai_game_list}')
    print(f'User: ', end='')
    print(f'{user_game_list}')
    if ai_game_point == 21:
        print('\nA.I. HIT 21!')
    if user_game_point < 22 and user_game_point > ai_game_point:
        user_bank += ai_bet + int(user_bet)
        print(f'\nCongratulations! You won and got ', end='')
        print(f'{ai_bet} $')
    if user_game_point < 22 and ai_game_point > 21:
        user_bank += ai_bet + int(user_bet)
        print(f'\nCongratulations! You won and got ', end='')
        print(f'{ai_bet} $')
    if ai_game_point < 22 and ai_game_point > user_game_point:
        ai_bank += ai_bet + int(user_bet)
        print(f"\nA.I. wins ", end='')
        print(f"{int(user_bet)} $")
    if user_game_point > 21 and ai_game_point < 22:
        ai_bank += ai_bet + int(user_bet)
        print(f"\nA.I. wins ", end='')
        print(f"{int(user_bet)} $")
    if user_game_point < 22 and user_game_point == ai_game_point:
        ai_bank += ai_bet
        user_bank += int(user_bet)
        print("\nIt's a draw.")
    if user_game_point > 21 and ai_game_point > 21:
        ai_bank += ai_bet
        user_bank += int(user_bet)
        print("\nIt's a draw.")

    if ai_bank < 10:
        print('A.I. has too little money. You won the game!')
        break

    if user_bank < 10:
        print('You have too little money and lost the game.')
        break

    play_again = 'default'
    while play_again not in ['y', 'Y', 'n', 'N']:
        play_again = input('\nDo you want to play again? (Y/N): ')
    if play_again == 'n' or play_again == 'N':
        print(f'\nFinal bank accounts:\nUser: [', end='')
        print(f'{user_bank} $', end='')
        print(f']\nA.I.: [', end='')
        print(f'{ai_bank} $', end='')
        print(']')
        if user_bank > ai_bank:
            print("\nYou're a winner!")
        if ai_bank > user_bank:
            print("\nYou lost.")
        if user_bank == ai_bank:
            print("\nIt's a draw.")
        break

print('\n\nThanks for playing!')
print(f'Marek Gozdera\nemail: ', end='')
print(f'gozderamarek@gmail.com')
print(f'{169:c} 2023')
print('\nPress enter...', end='')
input()
