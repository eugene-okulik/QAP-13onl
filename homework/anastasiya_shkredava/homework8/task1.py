def operations(func):
    def wrapper(first_number, second_number, operation=None):
        if first_number == second_number:
            operation = '+'
        if first_number > second_number:
            operation = '-'
        if second_number > first_number:
            operation = '/'
        if second_number < 0 or first_number < 0:
            operation = '*'
        return func(first_number, second_number, operation)
    return wrapper


@operations
def calc(first_number, second_number, operation=None):
    if operation == '+':
        return first_number + second_number
    if operation == '-':
        return first_number - second_number
    if operation == '*':
        return first_number * second_number
    if operation == '/':
        return first_number / second_number


num_1 = int(input('Enter the first number:'))
num_2 = int(input('Enter the second number:'))
print(calc(num_1, num_2))
