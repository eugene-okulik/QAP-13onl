# "Угадайка"


number = 124
user_number = int(input('Enter an integer number: '))
while number:
    if user_number > number:
        print('Your number is greater than the hidden one. Try to enter a smaller number.')
        user_number = int(input('Enter an integer number again: '))
    elif user_number < number:
        print('Your number is smaller than the hidden one. Try to enter a greater number.')
        user_number = int(input('Enter an integer number again: '))
    else:
        print('Congratulations! You guessed the number.')
        break
