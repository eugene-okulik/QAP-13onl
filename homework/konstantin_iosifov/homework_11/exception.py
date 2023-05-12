from datetime import datetime

while True:
    user_input = input("Enter date in dd/mm/yyyy format \n")

    try:
        date = datetime.strptime(user_input, "%d/%m/%Y")
        print("Date is Python format:", date)
        break

    except ValueError:
        print("You entered wrong date format. Right format is: dd/mm/yyyy.")
        continue
