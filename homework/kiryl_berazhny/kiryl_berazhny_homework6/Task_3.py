# Задание 3 - Простейший калькулятор

def calc(first_num, second_num, oper):
    if oper == 1:
        return print(first_num + second_num)
    elif oper == 2:
        return print(first_num - second_num)
    elif oper == 3:
        return print(first_num * second_num)
    elif oper == 4:
        if second_num == 0:
            rep_num2 = float(input('Деление на 0 невозможно, введите число неравное 0: '))
            calc(num1, rep_num2, operation)
        else:
            return print(f'Частное: {int(first_num // second_num)}\nОстаток: {first_num % second_num}')


print('Выберите операцию:\n'
      '1. Сложение\n'
      '2. Вычитание\n'
      '3. Умножение\n'
      '4. Деление\n')
operation = int(input('Введите номер пункта меню: '))
num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
calc(num1, num2, operation)
