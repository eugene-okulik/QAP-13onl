# Попросите пользователя ввести дату и попробуйте преобразовать дату в формат питона. В случае,
# если пользователь не угадал с форматом ввода даты, вы получите исключение.
# Обработайте это исключение и подскажите пользователю в каком формате нужно вводить дату

from datetime import datetime

user_date = input('Enter date like ddmmyyyy - HHMMSS: ')
while True:
    try:
        py_user_date = datetime.strptime(user_date, '%d%m%Y - %H%M%S')
        break
    except ValueError:
        user_date = input('Incorrect format of date. Enter date like 01012000 - 232323: ')

print(py_user_date)
