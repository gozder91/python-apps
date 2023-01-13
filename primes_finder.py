print('\nPrimes App')

while True:
    print('This app finds prime numbers in the given range.')
    given_number_1 = ''
    given_number_2 = ''
    primes = []

    while not given_number_1.isnumeric():
        given_number_1 = input('\nStart from: ')

    given_number_1 = int(given_number_1)

    while not given_number_2.isnumeric():
        given_number_2 = input('Finish at: ')
        if not given_number_2.isnumeric():
            continue

        elif int(given_number_2) < given_number_1:
            print("I can't finish before start. Try again.")
            given_number_2 = ''
            continue

    given_number_2 = int(given_number_2)

    for value in range(given_number_1, given_number_2+1):
        isPrime = True
        for div in range(2, value):
            if value % div == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(value)

    if 1 in primes:
        primes.remove(1)

    if len(primes) == 0:
        print(
            f'\nThere are no primes from {given_number_1} to {given_number_2}.')

    if len(primes) == 1:
        print(
            f'\nThere is only one prime from {given_number_1} to {given_number_2} and it is: [{primes[0]}].')
    if len(primes) > 1:
        print(
            f'\nThere are [{len(primes)}] primes from {given_number_1} to {given_number_2}.\nHere they are: {primes}')

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
