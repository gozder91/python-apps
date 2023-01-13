import random

def randomint_easy():
    rand_int = random.randint(1, 10)
    trials = 0
    while True:
        guess_int = input('Guess the number: ')
        trials += 1
        if not guess_int.isnumeric() or int(guess_int) not in range(1, 11):
            print('Wrong number. On easy level the range is 1-10. Try again.\n')
            continue
        if int(guess_int) == rand_int:
            if trials == '1':
                print(f'Super, you needed only 1 try!\n')
            else:
                print(f'Good, you needed: {trials} tries.\n')
            break
        if int(guess_int) > rand_int:
            print('The random is lower.\n')
        if int(guess_int) < rand_int:
            print('The random is higher.\n')


def randomint_normal():
    rand_int = random.randint(1, 100)
    trials = 0
    guesses = []
    while True:
        guess_int = input('Guess the number: ')
        trials += 1
        if not guess_int.isnumeric() or int(guess_int) not in range(1, 101):
            print('Wrong number. On easy level the range is 1-100. Try again.\n')
            continue
        guesses.append(int(guess_int))
        if int(guess_int) == rand_int:
            if trials == '1':
                print(f'Super, you needed only 1 try!\n')
            else:
                print(f'Good, you needed: {trials} tries.\n')
            break
        if len(guesses) == 1:
            print('Keep looking!\n')
            continue
        if abs(rand_int - guesses[len(guesses)-2]) > abs(rand_int - guesses[len(guesses)-1]):
            print("You're getting closer.\n")
        if abs(rand_int - guesses[len(guesses)-2]) < abs(rand_int - guesses[len(guesses)-1]):
            print("You're getting farther.\n")
        if abs(rand_int - guesses[len(guesses)-2]) == abs(rand_int - guesses[len(guesses)-1]):
            print("You're standing still.")


def randomint_hard():
    rand_int = random.randint(1, 1000)
    trials = 0
    print(f'Randint {rand_int}')
    while True:
        guess_int = input('Guess the number: ')
        trials += 1
        if not guess_int.isnumeric() or int(guess_int) not in range(1, 1001):
            print('Wrong number. On easy level the range is 1-1000. Try again.\n')
            continue
        if int(guess_int) == rand_int:
            if trials == '1':
                print(f'Super, you needed only 1 try!\n')
            else:
                print(f'Good, you needed: {trials} tries.\n')
            break
        if abs(rand_int - int(guess_int)) > 50:
            print('Cold.')
        if abs(rand_int - int(guess_int)) <= 50:
            print('Warm.')


print('\nWelcome to the random integer game.')

while True:
    print(
        'Select game level:\n\n[E]easy\t\t(1-10)\n[N]ormal\t(1-100)\n[H]ard\t\t(1-1000)\n\n[Q]uit')
    while True:
        game_lvl = input('\nYour choice is: ')
        if game_lvl == 'e' or game_lvl == 'E' or game_lvl == 'n' or game_lvl == 'N' or game_lvl == 'h' or game_lvl == 'H' or game_lvl == 'q' or game_lvl == 'Q':
            break

    if game_lvl == 'e' or game_lvl == 'E':
        randomint_easy()
    if game_lvl == 'n' or game_lvl == 'N':
        randomint_normal()
    if game_lvl == 'h' or game_lvl == 'H':
        randomint_hard()
    if game_lvl == 'q' or game_lvl == 'Q':
        break

    play_again = 'default'
    while play_again not in ['Y', 'y', 'N', 'n']:
        play_again = input('Do you want to play again (Y/N)? ')
    if play_again == 'n' or play_again == 'N':
        break
    else:
        continue
print(
    f'\n\nThanks for playing!\nMarek Gozdera\ngozderamarek@gmail.com\n{169:c} 2023\n\nPress enter...', end='')
input()
