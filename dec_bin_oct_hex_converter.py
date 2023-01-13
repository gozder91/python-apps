print('\nWelcome to DEC-BIN-HEX converter.')
while True:
    print('What kind of number would you like to convert?')
    conv_system = ''
    conv_number = ''
    while conv_system not in ['d', 'D', 'b', 'B', 'h', 'H']:
        conv_system = input(
            '[D]ec, [B]in, [H]ex: ')

    if conv_system == 'd' or conv_system == 'D':
        while not conv_number.isnumeric():
            conv_number = input('\nEnter the number: ')
            if not conv_number.isnumeric():
                print("It's not a decimal number.")

        # splitting bin
        bin_list_rev = []
        bin_list = []
        bin_before = str(bin(int(conv_number))[2:])
        bin_after = ''

        for i in range(0, len(bin_before)):
            bin_list_rev.append(bin_before[i])

        bin_list_rev.reverse()

        for i in range(0, len(bin_list_rev)):
            bin_list.append(bin_list_rev[i])
            if i != 0 and (i+1) % 4 == 0:
                bin_list.append(' ')

        bin_list.reverse()
        bin_after = bin_after.join(bin_list).lstrip()

        print(f'Dec: {conv_number}')
        print(f'Bin: {bin_after}')
        print(f'Hex: {int(conv_number):x}')

    if conv_system == 'b' or conv_system == 'B':
        flag = False
        while not flag:
            bin_list = []
            conv_number = input('\nEnter the number: ')
            for i in range(len(conv_number)):
                bin_list.append(conv_number[i])
            for i in range(len(bin_list)):
                if bin_list[i] not in ['0', '1']:
                    flag = False
                    break
                else:
                    flag = True
            if flag == False:
                print("It's not a binary number!")
                conv_number = ''
                continue

        print(f'Dec: {int(str(conv_number), 2)}')
        print(f'Bin: {(conv_number)}')
        print(f'Hex: {int(str(conv_number), 2):x}')

    if conv_system == 'h' or conv_system == 'H':
        flag = False
        while not flag:
            hex_list = []
            conv_number = input('\nEnter the number: ')
            for i in range(len(conv_number)):
                hex_list.append(conv_number[i])
            for i in range(len(hex_list)):
                if hex_list[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                    flag = False
                    break
                else:
                    flag = True
            if flag == False:
                print("It's not a hexadecimal number!")
                conv_number = ''
                continue

        dec = int(str(conv_number), 16)
        # splitting bin
        bin_list_rev = []
        bin_list = []
        bin_before = str(bin(dec)[2:])
        bin_after = ''

        for i in range(0, len(bin_before)):
            bin_list_rev.append(bin_before[i])

        bin_list_rev.reverse()

        for i in range(0, len(bin_list_rev)):
            bin_list.append(bin_list_rev[i])
            if i != 0 and (i+1) % 4 == 0:
                bin_list.append(' ')

        bin_list.reverse()
        bin_after = bin_after.join(bin_list).lstrip()

        print(f'Dec: {dec}')
        print(f'Bin: {bin_after}')
        print(f'Hex: {conv_number}')

    play_again = ''
    while play_again not in ['y', 'Y', 'n', 'N']:
        play_again = input('\nDo you want to convert another value? (Y/N) ')
    if play_again == 'n' or play_again == 'n':
        break

print(f'\n\nMarek Gozdera\nemail: ', end='')
print(f'gozderamarek@gmail.com')
print(f'{169:c} 2023')
print('\nPress enter...', end='')
input()
