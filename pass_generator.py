import random
ints = range(33, 127)
print('\nWelcome to passgen.')
while True:
    chars = 0
    password = ''
    while chars not in ['8', '9', '10', '11', '12', '13', '14', '15', '16']:
        chars = input(
            'How many characters do you want your password to have? (8-16) ')

    for i in range(int(chars)):
        password += chr(random.choice(ints))

    print('\nGenerated password: ', end='')
    print(password)

    play_again = ''
    while play_again not in ['y', 'Y', 'n', 'N']:
        play_again = input(
            '\nDo you want to generate another password? (Y/N): ')
    if play_again == 'n' or play_again == 'N':
        break

print(f'\n\nMarek Gozdera\nemail: ', end='')
print(f'gozderamarek@gmail.com')
print(f'{169:c} 2023')
print('\nPress enter...', end='')
input()
