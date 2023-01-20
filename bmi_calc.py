print('\nWelcome to the BMI calculator')

while True:
    user_weight = ''
    user_height = ''

    while not user_weight.isnumeric():
        user_weight = input('\nEnter your weight in kilograms: ')
        if not user_weight.isnumeric():
            print('Only integer numbers. Try again')
        else:
            user_weight = int(user_weight)
            break

    while not user_height.isnumeric():
        user_height = input('Enter your height in centimeters: ')
        if not user_height.isnumeric():
            print('Only integer numbers. Try again')
        else:
            user_height = int(user_height)
            break

    bmi = user_weight / ((user_height/100)**2)
    print(f'\nYour BMI is: {bmi:.2f}.')
    if bmi < 18.5:
        print("You're underweight!")
    if 18.5 <= bmi < 24.9:
        print("Your BMI is OK!")
    if bmi >= 24.9:
        print("You're overweight!")

    play_again = ''
    while play_again not in ['y', 'Y', 'n', 'N']:
    # while play_again not in 'yYnN':
        play_again = input('\nDo you want to try again? (Y/N) ')
    if play_again == 'n' or play_again == 'N':
        break

print(f'\n\nMarek Gozdera\nemail: ', end='')
print(f'gozderamarek@gmail.com')
print(f'{169:c} 2023')
print('\nPress enter...', end='')
input()
