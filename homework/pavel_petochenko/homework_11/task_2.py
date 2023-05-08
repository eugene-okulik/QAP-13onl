# Попросите пользователя ввести дату и попробуйте преобразовать дату в формат питона.
# В случае, если пользователь не угадал с форматом ввода даты, вы получите исключение.
# Обработайте это исключение и подскажите пользователю в каком формате нужно вводить дату

from datetime import datetime

while True:
    input_data = input('Введите дату в формате YYYY-MM-DD: ')
    try:
        convert = datetime.strptime(input_data, '%Y-%m-%d')
        print(convert)
        break
    except ValueError:
        print('Введен неверный формат даты. Попробуйте ещё раз.')
