#  игра "Угадайка"

import random

number = random.randint(0, 10)
number1 = int(input('Enter an integer from 1 to 10: '))
while number != number1:
    number1 = int(input('Try again. Re-enter an integer from 1 to 10: '))
print('Congratulations! You guessed it!')
