print('\nFibonacci sequence')

print('This app calculates the values for the Fibonacci sequence in the given range.')
while True:
    given_number_1 = ''
    given_number_2 = ''
    fibo = [1, 1]

    while not given_number_1.isnumeric():
        given_number_1 = input('\nStart from: ')
        if not given_number_1.isnumeric():
            print('Wrong number.')

    given_number_1 = int(given_number_1)

    while not given_number_2.isnumeric():
        given_number_2 = input('Finish at: ')
        if not given_number_2.isnumeric():
            print('Wrong number.')
            continue

        elif int(given_number_2) < given_number_1:
            print("I can't finish before start. Try again.")
            given_number_2 = ''
            continue

    given_number_2 = int(given_number_2)

    for i in range(given_number_2):
        iter_fibo = fibo[i] + fibo[i+1]
        if iter_fibo > given_number_2:
            break
        fibo.append(iter_fibo)

    counter = 0
    while fibo[counter] < given_number_1:
        fibo.remove(fibo[counter])

    print(fibo)

    play_again = ''
    while play_again not in ['y', 'Y', 'n', 'N']:
        play_again = input('\nDo you want to try again? (Y/N) ')
    if play_again == 'n' or play_again == 'N':
        break

print(f'\n\nMarek Gozdera\nemail: ', end='')
print(f'gozderamarek@gmail.com')
print(f'{169:c} 2023')
print('\nPress enter...', end='')
input()
