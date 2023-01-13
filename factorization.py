def prime_factorization(number):
    facts = []
    while number != 1:
        i = 2
        while i <= number:
            if number % i == 0:
                facts.append(i)
                print(f'{number} | {i}')
                number = number // i
                i = 2
                continue
            i += 1
        print(1)
    return facts


while True:
    print('\nThis app can find greatest common divisor, least common multiple, deliver prime factorization for the numbers given by the user and marks them as primes if so\nGive me two numbers.')
    gcd = 0
    lcm = 0
    while True:
        number_1 = input('Number 1 is: ')
        if number_1.isnumeric():
            break
        else:
            print('Wrong number.')
    number_1 = int(number_1)

    while True:
        number_2 = input('Number 2 is: ')
        if number_2.isnumeric():
            break
        else:
            print('Wrong number.')
    number_2 = int(number_2)

    n1_divisors = set()
    n2_divisors = set()

    for i in range(2, number_1 + 1):
        if number_1 % i == 0:
            n1_divisors.add(i)
            list(n1_divisors).sort()
    print(f'\nPrime factors for {number_1}: ', sorted(list(n1_divisors)))
    if len(n1_divisors) == 1:
        print("IT'S A PRIME!\n")

    for i in range(2, number_2 + 1):
        if number_2 % i == 0:
            n2_divisors.add(i)
    print(f'Prime factors for {number_2}: ', sorted(list(n2_divisors)))
    if len(n2_divisors) == 1:
        print("IT'S A PRIME!")

    common_divisors = n1_divisors.intersection(n2_divisors)

    try:
        gcd = max(list(common_divisors))
        print(
            f'\nGreatest common divisor for {number_1} and {number_2} is: {gcd}')
    except:
        print('Given numbers do not have common divisors.')

    if len(n1_divisors) != 1:
        print(f'\nPrime factorization for {number_1} is:')
        facts_number_1 = prime_factorization(number_1)

    if len(n2_divisors) != 1:
        print(f'\nPrime factorization for {number_2} is:')
        facts_number_2 = prime_factorization(number_2)

    if gcd != 0:
        lcm = (number_1 * number_2 // gcd)
    else:
        lcm = number_1 * number_2
    print(f'\nLeast common multiple of {number_1} and {number_2} is: {lcm}')

    play_again = 'default'
    while play_again not in ['y', 'Y', 'n', 'N']:
        play_again = input('\nDo you want to try again? (Y/N): ')
    if play_again == 'n' or play_again == 'N':
        break
print(
    f'\n\nMarek Gozdera\ngozderamarek@gmail.com\n{169:c} 2023\n\nPress enter...', end='')
input()
