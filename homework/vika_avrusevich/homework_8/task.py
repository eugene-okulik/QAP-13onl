# Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции). Функция выглядит примерно так:
#
# def calc(first, second, operation):
#     if opertaion == '+':
#     .....
#
# Программа спрашивает у пользователя 2 числа (вне функции)
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
#
#     если числа равны, то функция calc вызывается с операцией сложения этих чисел
#     если первое больше второго, то происходит вычитание второго из певрого
#     если второе больше первого - деление первого на второе
#     если одно из чисел отрицательное - умножение


def oper(func):
    def wrapper(first, second, operation=None):
        if first == second:
            operation = '+'
        if first > second:
            operation = '-'
        if first < second:
            operation = '/'
        if first < 0 or second < 0:
            operation = '*'
        return func(first, second, operation)
    return wrapper


@oper
def calc(first, second, operation):
    if operation == '+':
        return f'\nРезультат: {first} + {second} = {first + second}'
    if operation == '-':
        return f'\nРезультат: {first} - {second} = {first - second}'
    if operation == '/':
        if second == 0:
            return f'\nРезультат: {first} / {second} = Деление на 0 невозможно!'
        else:
            return f'\nРезультат: {first} / {second} = {first / second}'
    if operation == '*':
        return f'\nРезультат: {first} * {second} = {first * second}'


f_numb = float(input('Введите первое число: '))
s_numb = float(input('Введите второе число: '))
print(calc(f_numb, s_numb))
