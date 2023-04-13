# Задание 3 - Простейший калькулятор
#
# Реализуйте программу, которая спрашивала у пользователя, какую операцию он хочет произвести над числами,
# а затем запрашивает два числа, передаёт эти числа в функцию и выводит результат
# Не забудьте о проверке деления на 0.
# Пример
#
# Выберите операцию:
#     1. Сложение
#     2. Вычитание
#     3. Умножение
#     4. Деление
# Введите номер пункта меню:
# 4
# Введите первое число:
# 10
# Введите второе число:
# 3
# Частное: 3, Остаток: 3
# Можете сделать все в одной функции, можете разделить на разные.

def calc(user_choice, first_number, second_number):
    if user_choice == 1:
        return f'\nСумма чисел: {first_number + second_number}.'
    if user_choice == 2:
        return f'\nРазность чисел: {first_number - second_number}.'
    if user_choice == 3:
        return f'\nПроизведение чисел: {first_number * second_number}.'
    if user_choice == 4:
        if second_number == 0:
            other_number = int(input('\nНа 0, к сожалению, делить нельзя. Введите другое число: '))
            calc(other_number, user_choice, first_number)
        else:
            return f'\nЧастное чисел: {first_number // second_number}, ' \
                   f'и остаток от него: {first_number % second_number}.'


print('Выберите операцию:\n'
      '1. Сложение\n'
      '2. Вычитание\n'
      '3. Умножение\n'
      '4. Деление\n')

sign = int(input('Введите номер пункта меню -> '))
while sign < 1 or sign > 4:
    sign = int(input('Такой операции нет. Выберите другую операцию -> '))

first_user_number = int(input('Введите первое число -> '))
second_user_number = int(input('Введите второе число-> '))
print(calc(sign, first_user_number, second_user_number))
