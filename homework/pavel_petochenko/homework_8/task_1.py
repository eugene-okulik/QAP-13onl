# Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции). Функция выглядит примерно так:
#
# def calc(first, second, operation):
#     if opertaion == '+':
#     .....
# Программа спрашивает у пользователя 2 числа (вне функции)
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '/':
        return num1 / num2
    elif operator == '*':
        return num1 * num2


def operation_decorator(func):
    def wrapper(num1, num2):
        if num1 == num2:
            return func(num1, num2, '+')
        elif num1 > num2:
            return func(num1, num2, '-')
        elif num2 > num1:
            return func(num1, num2, '/')
        elif num1 < 0 or num2 < 0:
            return func(num1, num2, '*')
    return wrapper


@operation_decorator
def calculate_decorated(num1, num2, operator):
    return calculate(num1, num2, operator)


first_num = float(input("Введите первое число: "))
second_num = float(input("Введите второе число: "))
result = calculate_decorated(first_num, second_num)
print(f"Результат операции: {result}")
