import random
print('\nWelcome to the Race to 20 game!')

while True:
    race_point = 0
    select_player = 'default'
    start_choice = 'user'
    user_move = 0
    play_again = 'default'
    print(
        '\nDo you want to play with A.I. or with the second player?\n[1] A.I.\n[2] Second player.\n\n[Q]uit\n')
    while select_player not in ['1', '2', 'q', 'Q']:
        select_player = input(
            'Select: ')
        if select_player not in ['1', '2', 'q', 'Q']:
            print('Wrong option. Try again.\n')

        if select_player == 'q' or select_player == 'Q':
            break

        if select_player == '1':
            user_name = input(
                'Ok, before we start, tell me what is your name? ')
            if user_name[-1] == 'a':
                print(f'\nWelcome Ms. {user_name} in the game!')
            else:
                print(f'\nWelcome Mr. {user_name} in the game!')
            while start_choice not in ['y', 'Y', 'n', 'N']:
                start_choice = input('Do you want to start (Y/N): ')
                if start_choice not in ['Y', 'y', 'N', 'n']:
                    print('Wrong option. Try again.')
            if start_choice == 'y' or start_choice == 'Y':
                print(
                    f'\nOk, so you can start the race to 20!\nYou can move 1 or 2 forward.\nWe start from 0.')
                while race_point <= 20:
                    while True:
                        user_move = input(f'\n{user_name} move is: ')
                        if user_move.isnumeric() and abs(int(user_move) - race_point) <= 2 and int(user_move) > race_point:
                            break
                        else:
                            print(
                                'Wrong move. You can move only 1 or 2 forward. Try again.')

                    race_point += (int(user_move) - race_point)
                    if race_point >= 20:
                        print(f'{user_name} wins!')
                        break
                    ai_move = random.randint(1, 2)
                    race_point += ai_move
                    if race_point >= 20:
                        print('A.I. wins.')
                        break

                    print(
                        f'\n{user_name} move is:\t[ {race_point - ai_move} ].\nA.I. moves:\t[ {race_point} ].')

            if start_choice == 'n' or start_choice == 'N':
                print(
                    '\nOk, so A.I. starts the race to 20!\nRemember that you can move only 1 or 2 forward.\nWe start from 0.')
                while race_point <= 20:
                    ai_move = random.randint(1, 2)
                    race_point += ai_move
                    if race_point >= 20:
                        print('A.I. wins.')
                        break

                    while True:
                        user_move = input(
                            f'A.I. moves:\t[ {race_point} ].\n{user_name} move is:\t  ')
                        if user_move.isnumeric() and abs(int(user_move) - race_point) <= 2 and int(user_move) > race_point:
                            break
                        else:
                            print(
                                'Wrong move. You can move only 1 or 2 forward. Try again.')

                    race_point += (int(user_move) - race_point)
                    if race_point >= 20:
                        print(f'{user_name} wins!')
                        break

        if select_player == '2':
            first_player_name = input(
                'What is the name of the first player (the one, who starts the game)? ')
            second_player_name = input(
                'What is the name of the second player? ')

            while race_point <= 20:
                while True:
                    first_player_move = input(
                        f'\n{first_player_name} move is: ')
                    if first_player_move.isnumeric() and abs(int(first_player_move) - race_point) <= 2 and int(first_player_move) > race_point:
                        break
                    else:
                        print(
                            'Wrong move. You can move only 1 or 2 forward. Try again.')

                race_point += (int(first_player_move) - race_point)
                if race_point >= 20:
                    print(f'{first_player_name} wins!')
                    break

                while True:
                    second_player_move = input(
                        f'\n{second_player_name} move is: ')
                    if second_player_move.isnumeric() and abs(int(second_player_move) - race_point) <= 2 and int(second_player_move) > race_point:
                        break
                    else:
                        print(
                            'Wrong move. You can move only 1 or 2 forward. Try again.')

                race_point += (int(second_player_move) - race_point)
                if race_point >= 20:
                    print(f'{second_player_name} wins!')
                    break

    if select_player == 'q' or select_player == 'Q':
        break
    else:
        while play_again not in ['y', 'Y', 'n', 'N']:
            play_again = input('\nDo you want to play again? [Y/N]: ')

        if play_again == 'n' or play_again == 'N':
            break
print(
    f'\nThanks for playing!\nMarek Gozdera\ngozderamarek@gmail.com\n{169:c} 2023\n\nPress enter...', end='')
input()
