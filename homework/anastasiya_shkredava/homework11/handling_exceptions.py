from datetime import datetime

user_date = input('Enter the date: ')
while True:
    try:
        py_date = datetime.strptime(user_date, '%d-%b-%Y - %H:%M:%S')
        break
    except ValueError:
        user_date = input('Invalid input. Enter the date using the format 23-Jun-2023 - 23:23:23: ')
print(f'Datetime object is created successfully from your date: {py_date}')
