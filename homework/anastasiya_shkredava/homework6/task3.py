# Задание 3 - Простейший калькулятор


def calc(first_num, second_num, user_operation):
    if user_operation == 1:
        return f'{first_num} + {second_num} = {first_num + second_num}'
    if user_operation == 2:
        return f'{first_num} - {second_num} = {first_num - second_num}'
    if user_operation == 3:
        return f'{first_num} * {second_num} = {first_num * second_num}'
    if user_operation == 4:
        while second_num == 0:
            second_num = float(input('Math ERROR (division by zero is not possible)\n'
                               'Enter the second number again: '))
        return f'Quotient: {first_num // second_num}, Remainder: {first_num % second_num}'


operations_list = 'List of arithmetic operations:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division'
operation = int(input(f'{operations_list}\nEnter the number of the desired operation: '))
while operation < 1 or operation > 4:
    operation = int(input('Entered number does not correspond to any operation from the list, try again: '))
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
print(calc(num1, num2, operation))
