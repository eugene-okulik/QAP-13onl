# Задание на "Декораторы"
# По условию вопросы - например если оба числа отрицательные и они равны или одно больше другого,
# то какое должно быть действие? Или тут два действия должны произойти?
# В условии написано, "... и управляет тем какая ОПЕРАЦИЯ будет произведена". В моем понимании будет одна операция.

def decorator(func):

    def wrapper(first_num, second_num):

        if first_num == second_num and first_num > 0:
            func(first_num, second_num, '+')
        elif first_num > second_num > 0:
            func(first_num, second_num, '-')
        elif 0 < first_num < second_num:
            func(first_num, second_num, '/')
        elif first_num < 0 or second_num < 0:
            func(first_num, second_num, '*')

    return wrapper


@decorator
def calc(first_num, second_num, operation):

    if operation == '+':
        return print('The numbers are equal, the addition operation:', first_num + second_num)
    if operation == '-':
        return print('The first number is greater, the operation of subtraction:', first_num - second_num)
    if operation == '/':
        return print('The second number is greater, dividing the first number by the second:', first_num / second_num)
    if operation == '*':
        return print('One of the numbers is negative, multiplication operation:', first_num * second_num)


num1, num2 = [int(i) for i in input('Enter two numbers separated by a space: ').split()]
calc(num1, num2)
