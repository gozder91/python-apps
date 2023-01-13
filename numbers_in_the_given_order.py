print('\nThis app receives the numbers from the user and then prints them numbered in the order given by the user along with information when they are increasing and decreasing with the streak. Additionally the program can sort numbers in ascending or descending order.')


def is_float(x) -> bool:
    try:
        float(x)
        return True
    except ValueError:
        return False


def entering_numbers():
    number = 'default'

    while not numbers_list or number != 'q' or number != 'Q':
        number = input("\nEnter a number or [q]uit: ")
        if number.isnumeric():
            numbers_list.append(int(number))
            print(numbers_list)
        elif is_float(number):
            numbers_list.append(float(number))
            print(numbers_list)
        else:
            if number == 'q' or number == 'Q':
                break
            else:
                print('This is not a number. Try again or [q]uit.')

    if len(numbers_list) == 1:
        print(
            f"You've entered only one number. Here it is: {numbers_list[0]}.")
    return numbers_list


def menu():
    while True:
        menu_choice = input(
            "\nSelect from the menu:\n[0] Go back to entering numbers.\n[1] Print my list with the streak.\n[2] Sort ascending.\n[3] Sort descending.\n[q] Quit\nYour choice is: ")
        if menu_choice == '0':
            entering_numbers()
            continue
        if menu_choice == '1':
            streak_list = []
            actual_streak = 0
            print(f'\nYour numbers are: {numbers_list}.')
            for counter in range(0, len(numbers_list)):
                if counter == 0:
                    trend = '='
                elif numbers_list[counter] > numbers_list[counter-1]:
                    trend = 'Asc.'
                elif numbers_list[counter] < numbers_list[counter-1]:
                    trend = 'Desc.'
                streak_list.append(trend)

                if len(streak_list) == 1:
                    actual_streak = 1
                elif streak_list[counter-1] == streak_list[counter]:
                    actual_streak += 1
                else:
                    actual_streak = 1

                if counter == 0:
                    print(
                        f'No. {counter+1:<6}Number: {numbers_list[counter]}\tTrend: {trend}')
                else:
                    print(
                        f'No. {counter+1:<6}Number: {numbers_list[counter]}\tTrend: {trend}\tStreak: {actual_streak}.')
        if menu_choice == '2':
            print(
                f'\nYour numbers sorted ascending are: {sorted(numbers_list)}')
        if menu_choice == '3':
            print(
                f'\nYour numbers sorted descending are: {sorted(numbers_list, reverse=True)}')
        if menu_choice == 'q' or menu_choice == 'Q':
            break
        else:
            print('There is no such option. Try again or [q]uit.')


numbers_list = []
entering_numbers()
menu()

print(f'\n\nMarek Gozdera\nemail: ', end='')
print(f'gozderamarek@gmail.com')
print(f'{169:c} 2023')
print('\nPress enter...', end='')

input()
