#Задание 3 - Простейший калькулятор


def calc(num1, num2):
    if operation == 1:
        return f'{num1} + {num2} = {num1 + num2}'
    if operation == 2:
        return f'{num1} - {num2} = {num1 - num2}'
    if operation == 3:
        return f'{num1} * {num2} = {num1 * num2}'
    if operation == 4:
        while num2 == 0:
            num2 = float(input('Math ERROR (division by zero is not possible)\n'
                               'Enter the second number again: '))
        return f'Quotient: {num1 // num2}, Remainder: {num1 % num2}'


operations_list = 'List of arithmetic operations:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division'
operation = int(input(f'{operations_list}\nEnter the number of the desired operation: '))
while operation < 1 or operation > 4:
    operation = int(input('Entered number does not correspond to any operation from the list, try again: '))
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
print(calc(num1, num2))
