print('\nCaesar cipher')

while True:
    user_choice = ''
    while user_choice not in ['e', 'E', 'd', 'D']:
        user_choice = input('\nWould you like to [e]ncrypt or [d]ecrypt? ')

    if user_choice == 'e' or user_choice == 'E':

        text = input('\nEnter your text here: ')
        text_list = []
        for i in range(len(text)):
            if ord(text[i]) < 124:
                if ord(text[i]) == 32:
                    text_list.append(ord(text[i]))
                else:
                    text_list.append(ord(text[i]) + 3)
            else:
                text_list.append(ord(text[i]) - 91)

        enc_text = ''
        enc_text_list = []
        for i in range(len(text_list)):
            enc_text_list.append(chr(text_list[i]))

        enc_text = enc_text.join(enc_text_list)
        print(f'Encrypted: [ {enc_text} ]')

    if user_choice == 'd' or user_choice == 'D':

        text = input('\nEnter your text here: ')
        text_list = []
        for i in range(len(text)):
            if ord(text[i]) < 36:
                if ord(text[i]) == 32:
                    text_list.append(ord(text[i]))
                else:
                    text_list.append(ord(text[i]) + 91)
            else:
                text_list.append(ord(text[i])-3)

        enc_text = ''
        enc_text_list = []
        for i in range(len(text_list)):
            enc_text_list.append(chr(text_list[i]))

        enc_text = enc_text.join(enc_text_list)
        print(f'Decrypted: [ {enc_text} ]')

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
