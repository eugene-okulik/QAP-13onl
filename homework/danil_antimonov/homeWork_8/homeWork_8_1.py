# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

a = int(input('Введите первое число:\n'))
b = int(input('Введите второе число:\n'))


def selector_operation(function_to_decorate):
    def wrapper(arg1, arg2):
        if arg1 == arg2:
            arg3 = '+'
        elif arg1 > arg2:
            arg3 = '-'
        elif arg1 < arg2:
            arg3 = '/'
        elif arg1 < 0 or arg2 < 0:
            arg3 = '*'
        return function_to_decorate(arg1, arg2, arg3)

    return wrapper


@selector_operation
def calc(first: int, second: int, operation):
    if operation == '+':
        return print(first + second)
    elif operation == '-':
        return print(first - second)
    elif operation == '/':
        return print(first / second)
    elif operation == '*':
        return print(first * second)


calc(a, b)
