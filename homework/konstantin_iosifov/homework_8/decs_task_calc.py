a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


def calc_decorator(func):
    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        elif first < 0 or second < 0:
            operation = '*'
        else:
            operation = None
        inner_result = func(first, second, operation)
        return inner_result
    return wrapper


@calc_decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return second - first
    elif operation == '/':
        return first / second
    # всё считает правильно...но с умножением какая-то дичь...ввожу, например, -2 и 7, результат = -0.2857142857142857
    # работает условие деления, если второе больше первого, если первое больше второго (7 и -2), то условие вычитания
    # как отрицательное число чекать?
    # что-то нет идей как порешать это
    elif operation == '*':
        if first < 0 or second < 0:
            return first * second
    else:
        return None


result = calc(a, b)
print("Result is: ", result)


