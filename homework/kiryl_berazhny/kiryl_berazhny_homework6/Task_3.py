# Задание 3 - Простейший калькулятор

def calc(a, b, c):
    if c == 1:
        return print(a + b)
    elif c == 2:
        return print(a - b)
    elif c == 3:
        return print(a * b)
    elif c == 4:
        if b == 0:
            b = float(input('Деление на 0 невозможно, введите число неравное 0: '))
            calc(num1, b, operation)
        else:
            return print(f'Частное: {int(a // b)}\nОстаток: {a % b}')


print('Выберите операцию:\n'
      '1. Сложение\n'
      '2. Вычитание\n'
      '3. Умножение\n'
      '4. Деление\n')
operation = int(input('Введите номер пункта меню: '))
num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
calc(num1, num2, operation)
