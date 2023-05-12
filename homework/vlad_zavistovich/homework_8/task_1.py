num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите первое число: '))


def decorator(func):
    def wrapper(first, second):

        if first == second and first > 0:
            func(first, second, '+')
        elif first > second > 0:
            func(second, first, '-')
        elif 0 < first < second:
            func(first, second, '/')
        elif first < 0 or second < 0:
            func(first, second, '*')

    return wrapper


@decorator
def calc(first, second, operation):
    if operation == '+':
        return print('Сумма двух чисел равна: ', first + second)
    if operation == '-':
        return print('Разность двух чисел равна:', first - second)
    if operation == '/':
        return print('Деление первого числа на второе равно: ', first / second)
    if operation == '*':
        return print('Произведение двух чисел равно: ', first * second)


calc(num_1, num_2)
