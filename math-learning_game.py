import random
import datetime

def generate_add():
    expect_result = 1000
    while expect_result > 100:
        number_1 = random.randint(0, 100)
        number_2 = random.randint(0, 100)
        expect_result = number_1 + number_2
    return number_1, number_2, expect_result


def generate_sub():
    expect_result = 0
    while expect_result <= 0:
        number_1 = random.randint(0, 100)
        number_2 = random.randint(0, 100)
        expect_result = number_1 - number_2
    return number_1, number_2, expect_result


def generate_mul():
    expect_result = 1000
    while expect_result > 100:
        number_1 = random.randint(2, 100)
        number_2 = random.randint(0, 100)
        expect_result = number_1 * number_2
    return number_1, number_2, expect_result


def generate_div():
    number_1 = 100
    number_2 = 3
    while number_1 % number_2 != 0:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        expect_result = number_1 // number_2
    return number_1, number_2, expect_result


print('\nWelcome to the math-learning game.\nSolve math operations from range 0 to 100 (integers only).\nYour goal is to get 5 points.')
while True:
    points = 0
    user_choice = 'default'
    print(
        '\nWhat would you like to practice?\n[A]dd\n[S]ubstract\n[M]ultiply\n[D]ivide\n[R]andomly\n\n[Q]uit')
    while user_choice not in ['a', 'A', 's', 'S', 'm', 'M', 'd', 'D', 'r', 'R', 'q', 'Q']:
        user_choice = input('Your choice is: ')
        if user_choice == 'q' or user_choice == 'Q':
            break

        if user_choice == 'a' or user_choice == 'A':
            start = datetime.datetime.now()
            while points < 5:
                number_1, number_2, expect_result = generate_add()
                while True:
                    user_result = input(f'\n{number_1} + {number_2} = ')
                    if user_result.isnumeric():
                        break
                    else:
                        print('Only integers!')
                if int(user_result) == expect_result:
                    points += 1
                    print(f'Nice, you have {points} p.')
                if int(user_result) != expect_result:
                    print(f'Wrong answer. Result is: {expect_result}')
            stop = datetime.datetime.now()
            delta = stop - start
            if delta.seconds >= 60:
                print('\nIt took you over a minute. You should pracice more.')
            else:
                print(f'\nYour time is: {delta.seconds} sec.')

        if user_choice == 's' or user_choice == 'S':
            start = datetime.datetime.now()
            while points < 5:
                number_1, number_2, expect_result = generate_sub()
                while True:
                    user_result = input(f'\n{number_1} - {number_2} = ')
                    if user_result.isnumeric():
                        break
                    else:
                        print('Only integers!')
                if int(user_result) == expect_result:
                    points += 1
                    print(f'Nice, you have {points} p.')
                if int(user_result) != expect_result:
                    print(f'Wrong answer. Result is: {expect_result}')
            stop = datetime.datetime.now()
            delta = stop - start
            if delta.seconds >= 60:
                print('\nIt took you over a minute. You should pracice more.')
            else:
                print(f'\nYour time is: {delta.seconds} sec.')

        if user_choice == 'm' or user_choice == 'M':
            start = datetime.datetime.now()
            while points < 5:
                number_1, number_2, expect_result = generate_mul()
                while True:
                    user_result = input(f'\n{number_1} * {number_2} = ')
                    if user_result.isnumeric():
                        break
                    else:
                        print('Only integers!')
                if int(user_result) == expect_result:
                    points += 1
                    print(f'Nice, you have {points} p.')
                if int(user_result) != expect_result:
                    print(f'Wrong answer. Result is: {expect_result}')
            stop = datetime.datetime.now()
            delta = stop - start
            if delta.seconds >= 60:
                print('\nIt took you over a minute. You should pracice more.')
            else:
                print(f'\nYour time is: {delta.seconds} sec.')

        if user_choice == 'd' or user_choice == 'D':
            start = datetime.datetime.now()
            while points < 5:
                number_1, number_2, expect_result = generate_div()
                while True:
                    user_result = input(f'\n{number_1} / {number_2} = ')
                    if user_result.isnumeric():
                        break
                    else:
                        print('Only integers!')
                if int(user_result) == expect_result:
                    points += 1
                    print(f'Nice, you have {points} p.')
                if int(user_result) != expect_result:
                    print(f'Wrong answer. Result is: {expect_result}')
            stop = datetime.datetime.now()
            delta = stop - start
            if delta.seconds >= 60:
                print('\nIt took you over a minute. You should pracice more.')
            else:
                print(f'\nYour time is: {delta.seconds} sec.')

        if user_choice == 'r' or user_choice == 'R':
            operations = ['+', '-', '*', '/']
            start = datetime.datetime.now()
            while points < 5:
                random.shuffle(operations)
                if operations[0] == '+':
                    number_1, number_2, expect_result = generate_add()
                if operations[0] == '-':
                    number_1, number_2, expect_result = generate_sub()
                if operations[0] == '*':
                    number_1, number_2, expect_result = generate_mul()
                if operations[0] == '/':
                    number_1, number_2, expect_result = generate_div()

                while True:
                    if operations[0] == '+':
                        user_result = input(f'\n{number_1} + {number_2} = ')
                    if operations[0] == '-':
                        user_result = input(f'\n{number_1} - {number_2} = ')
                    if operations[0] == '*':
                        user_result = input(f'\n{number_1} * {number_2} = ')
                    if operations[0] == '/':
                        user_result = input(f'\n{number_1} / {number_2} = ')
                    if user_result.isnumeric():
                        break
                    else:
                        print('Only integers!')
                if int(user_result) == expect_result:
                    points += 1
                    print(f'Nice, you have {points} p.')
                if int(user_result) != expect_result:
                    print(f'Wrong answer. Result is: {expect_result}')
            stop = datetime.datetime.now()
            delta = stop - start
            if delta.seconds >= 60:
                print('\nIt took you over a minute. You should pracice more.')
            else:
                print(f'\nYour time is: {delta.seconds} sec.')
    if user_choice == 'q' or user_choice == 'Q':
        break
    play_again = 'default'
    while play_again not in ['y', 'Y', 'n', 'N']:
        play_again = input('\nDo you want to try again? (Y/N): ')
    if play_again == 'n' or play_again == 'N':
        break

print('\n\nThanks for playing!')
print(f'Marek Gozdera\nemail: ', end='')
print(f'gozderamarek@gmail.com')
print(f'{169:c} 2023')
print('\nPress enter...', end='')
input()
