print('Выберите операцию:')
print('  1. Сложение')
print('  2. Вычитание')
print('  3. Умножение')
print('  4. Деление')
operation = int(input('Введите номер пункта меню: '))


def calculate(num_1, num_2, operation_code):
    if operation == 1:
        return num1 + num2
    elif operation == 2:
        return num1 - num2
    elif operation == 3:
        return num1 * num2
    elif operation == 4 and num2 != 0:
        return f'Частное: {num1 // num2}, Остаток: {num1 % num2}'
    else:
        return 'Такой операции не существует или вы выбрали деление на ноль'


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

result = calculate(num1, num2, operation)

print('Результат: ', result)
