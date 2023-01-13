import random
print('\nWelcome in Lotto game!')
while True:
    drawn_numbers = []
    for i in range(6):
        while True:
            i = random.randint(1, 49)
            if i not in drawn_numbers:
                drawn_numbers.append(i)
                break

    user_numbers = []
    print('\nGive me six numbers from 1 to 49: ')
    for i in range(6):
        while True:
            number = ''
            while not number.isnumeric():
                number = input(f'{i+1}: ')
                if number.isnumeric():
                    if 0 < int(number) < 50:
                        number = int(number)
                        break
                    else:
                        print('Only numbers from 1 to 49. Try again')
                        number = ''
                        continue
                if not number.isnumeric():
                    print('Only integer numbers!')
                    continue

            if number not in user_numbers:
                user_numbers.append(number)
                break
            else:
                print('Numbers cannot be repeated. Try again')
                continue

    drawn_numbers = set(drawn_numbers)
    user_numbers = set(user_numbers)
    common_numbers = drawn_numbers.intersection(user_numbers)

    print(
        f'\nDrawn numbers are: {drawn_numbers}.\nYou entered: {user_numbers}.')

    if len(common_numbers) > 0:
        print(f'You hit: {common_numbers}')
        if len(common_numbers) == 1:
            print(f'\n{len(common_numbers)} hit. You lost your money.')
        if len(common_numbers) == 2:
            print(f'\n{len(common_numbers)} hits. You lost your money.')
        if len(common_numbers) == 3:
            print(f'\n{len(common_numbers)} hits! You won 24 PLN.')
        if len(common_numbers) == 4:
            print(f'\n{len(common_numbers)} hits! You won 100 PLN.')
        if len(common_numbers) == 5:
            print(f'\n{len(common_numbers)} hits! You won 3500 PLN.')
        if len(common_numbers) == 6:
            print(f'\n{len(common_numbers)} HITS! You won 1 000 000 PLN.')
    else:
        print('You missed and lost your money.')

    play_again = ''
    while play_again not in ['y', 'Y', 'n', 'N']:
        play_again = input('\nDo you want to play again? (Y/N) ')
    if play_again == 'n' or play_again == 'N':
        break

print(f'\n\nMarek Gozdera\nemail: ', end='')
print(f'gozderamarek@gmail.com')
print(f'{169:c} 2023')
print('\nPress enter...', end='')
input()
