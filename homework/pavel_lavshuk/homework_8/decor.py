user_num1 = int(input('Введите первое число: '))
user_num2 = int(input('Введите второе число: '))


def decorator(func):
    def wrapper(a, b, operation=None):
        if a == b:
            operation = '+'
        if a > b:
            operation = '-'
        if a or b < 0:
            operation = '*'
        if a < b:
            operation = '/'
        return func(a, b, operation)
    return wrapper


@decorator
def calc(a, b, operation=None):
    if operation == '+':
        return a + b
    if operation == '-':
        return b - a
    if operation == '/':
        return a / b
    if operation == '*':
        return a * b


print(calc(user_num1, user_num2))
