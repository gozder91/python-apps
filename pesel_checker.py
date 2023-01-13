import calendar
import datetime
print('\nWelcome to PESEL-check')

while True:
    while True:

        user_pesel_list = []
        user_pesel = input('\nEnter your PESEL: ')

        if not user_pesel.isnumeric():
            print('This PESEL is invalid.')
            break

        if len(user_pesel) < 11:
            print('This PESEL is invalid.')
            break

        for i in range(len(user_pesel)):
            user_pesel_list.append(int(user_pesel[i]))

        pesel_val = user_pesel_list[0] + user_pesel_list[1] * 3 + user_pesel_list[2] * 7 + user_pesel_list[3] * 9 + user_pesel_list[4] + user_pesel_list[5] * \
            3 + user_pesel_list[6] * 7 + user_pesel_list[7] * 9 + \
            user_pesel_list[8] + user_pesel_list[9] * 3 + user_pesel_list[10]

        if str(pesel_val).endswith('0'):
            print('\nPESEL is OK!')
        else:
            print('This PESEL is invalid')
            break
        if user_pesel_list[9] % 2 == 0:
            print("You're a woman!")
        else:
            print("You're a man!")

        now_year = datetime.date.today().year
        now_month = datetime.date.today().month
        now_day = datetime.date.today().day

        if str(user_pesel_list[2]) == '2':
            year = '20'+str(user_pesel_list[0]) + str(user_pesel[1])
        elif str(user_pesel_list[2]) == '8':
            year = '18'+str(user_pesel_list[0]) + str(user_pesel[1])
        else:
            year = '19'+str(user_pesel_list[0]) + str(user_pesel[1])

        year = int(year)

        month = str(user_pesel_list[2]) + str(user_pesel_list[3])
        if str(user_pesel_list[2]) == '0':
            month = str(user_pesel_list[3])

        month = int(month)

        day = str(user_pesel_list[4]) + str(user_pesel_list[5])
        if str(user_pesel_list[4]) == '0':
            day = str(user_pesel_list[5])

        day = int(day)

        today = datetime.date.today()
        birthday = datetime.date(year, month, day)

        if now_month < month:
            years = now_year - year - 1
            months = 12 + now_month - month
        if now_month > month:
            years = now_year - year
            months = now_month - month
        if now_month == month:
            if now_day < day:
                years = now_year - year - 1
                months = 12
            if now_day > day:
                years = now_year - year
                months = 0
            if now_day == day:
                years = now_year - year
                months = 0
                days = 0
                print('Today is your birthday! Congratulations!')

        if year % 4 == 0 or year % 400 == 0:
            leap_year = True
        else:
            leap_year = False

        if now_day > day:
            days = now_day - day
        if now_month in [2, 4, 6, 9, 11] and now_day < day:
            days = 31 - day + now_day
        if now_month in [1, 5, 7, 8, 10, 12] and now_day < day:
            days = 30 - day + now_day
        if now_month == 3 and now_day < day:
            if leap_year:
                days = 29 - day + now_day
            else:
                days = 28 - day + now_day

        diff = today - birthday

        next_birthsday = today - datetime.date(now_year, month, day)
        if next_birthsday.days < 0:
            next_birthsday = abs(next_birthsday.days)
        else:
            if leap_year:
                next_birthsday = 366 - next_birthsday.days
            else:
                next_birthsday = 365 - next_birthsday.days

        if now_day != day and next_birthsday > 1:
            print(
                f"Your birthday: {birthday.strftime('%A')}, {day} {birthday.strftime('%B')} {year} (next in {next_birthsday} days).")
        if now_day != day and next_birthsday == 1:
            print(
                f"Your birthday: {birthday.strftime('%A')}, {day} {birthday.strftime('%B')} {year} (next in {next_birthsday} day - tommorow!).")
        if leap_year:
            print("It was a leap year!")

        print(
            f"You have {years} years, ", end='')
        if months > 1:
            print(f"{months} months ", end='')
        else:
            print(f"{months} month ", end='')

        if days > 1:
            print(
                f"and {days} days.\nIt's your {diff.days} day of life.\n\nIt was that month: \n")
        else:
            print(
                f"and {days} day.\nIt's your {diff.days} day of life.\n\nIt was that month: \n")
        print(calendar.month(year, month))
        break

    play_again = ''
    while play_again not in ['y', 'Y', 'n', 'N']:
        play_again = input('\nDo you want to check another PESEL? (Y/N) ')
    if play_again == 'n' or play_again == 'N':
        break

print(f'\n\nMarek Gozdera\nemail: ', end='')
print(f'gozderamarek@gmail.com')
print(f'{169:c} 2023')
print('\nPress enter...', end='')
input()
