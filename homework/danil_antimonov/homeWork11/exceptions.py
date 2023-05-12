from datetime import datetime

user_date = input('Enter the date: ')
while True:
    try:
        py_date = datetime.strptime(user_date, '%d-%b-%Y - %H:%M:%S')
        break
    except ValueError:
        user_date = input('Invalid input. Type your date in the next format: 01-Jan-1900 - 23:59:59:\n')
print(f'Your datetime is accepted: {py_date}')
