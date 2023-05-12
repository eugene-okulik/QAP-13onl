def operation_selector(func):
    def wrapper(num_1, num_2):
        if num_1 == num_2:
            operation = '+'
        elif num_1 > num_2:
            operation = '-'
        elif num_2 > num_1:
            operation = '/'
        if num_1 < 0 or num_2 < 0:
            operation = '*'
        return func(num_1, num_2, operation)
    return wrapper


@operation_selector
def calc(one, two, operation):
    if operation == '+':
        return one + two
    elif operation == '-':
        return one - two
    elif operation == '/':
        return one / two
    elif operation == '*':
        return one * two


num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

result = calc(num_1, num_2)
print(f"Результат операции: {result}")
