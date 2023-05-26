# Обработка исключений
# Попросите пользователя ввести дату и попробуйте преобразовать дату в формат питона. В случае, если пользователь не
# угадал с форматом ввода даты, вы получите исключение. Обработайте это исключение и подскажите пользователю в каком
# формате нужно вводить дату

from datetime import datetime

date = input('Введите дату: ')
while True:
    try:
        date2 = datetime.strptime(date, '%d.%m.%Y - %H:%M:%S')
        break
    except ValueError:
        print('Неверный формат даты. Введите в формате 29.02.2020 - 16:30:25')
    date = (input('Введите дату: '))
print(f'Формат даты успешно создан: {date2}')
