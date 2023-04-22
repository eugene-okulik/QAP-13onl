# Реализуйте программу, которая спрашивала у пользователя, какую операцию он хочет произвести над числами,
# а затем запрашивает два числа, передаёт эти числа в функцию и выводит результат
# Не забудьте о проверке деления на 0.

def multiplication(a, b):
    return print(f'Произведение {a} и {b}:', a * b)


def division(a, b):
    if b == 0:
        return print('Деление на 0 запрещено')
    else:
        return print(f'Частное {a} и {b} = ', int(a / b), '\nОстаток: ', a % b)


def addition(a, b):
    return print(f'Сумма {a} и {b} = ', a + b)


def subtraction(a, b):
    return print(f'Разница {a} и {b} = ', a - b)


print('Эта программа может выполнять\n' +
      '1. Умножение\n' +
      '2. Деление\n' +
      '3. Сложение\n' +
      '4. Вычитание')
selected_action = int(input('Введите номер действия которое хотите выполнить:\n'))
a = int(input('Введите первое число:\n'))
b = int(input('Введите второе число:\n'))
if selected_action == 1:
    multiplication(a, b)
elif selected_action == 2:
    division(a, b)
elif selected_action == 3:
    addition(a, b)
elif selected_action == 4:
    subtraction(a, b)
