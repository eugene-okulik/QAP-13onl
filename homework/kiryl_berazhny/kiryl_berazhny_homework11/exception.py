# Обработка исключений

import datetime


my_date = input('Введите дату своего рождения: ')


def date_birth(date):

    try:
        out = (datetime.datetime.strptime(date, '%d.%m.%Y'))
        print(out)
    except ValueError:
        out = input('Введите дату своего рождения в формате "день.месяц.год": ')
        date_birth(out)


date_birth(my_date)
