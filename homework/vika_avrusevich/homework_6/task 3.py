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

def calc(sign, first_number, second_number):
    if sign == 1:
        return f'\nСумма чисел: {first_number + second_number}.'
    if sign == 2:
        return f'\nРазность чисел: {first_number - second_number}.'
    if sign == 3:
        return f'\nПроизведение чисел: {first_number * second_number}.'
    if sign == 4:
        if second_number == 0:
            other_number = int(input('\nНа 0, к сожалению, делить нельзя. Введите другое число: '))
            return calc(sign, first_number, other_number)
        else:
            return f'\nЧастное чисел: {first_number // second_number}, ' \
                   f'и остаток от него: {first_number % second_number}.'


print('Выберите операцию:\n'
      '1. Сложение\n'
      '2. Вычитание\n'
      '3. Умножение\n'
      '4. Деление\n')

user_choice = int(input('Введите номер пункта меню -> '))
while user_choice < 1 or user_choice > 4:
    user_choice = int(input('Такой операции нет. Выберите другую операцию -> '))

first_user_number = int(input('Введите первое число -> '))
second_user_number = int(input('Введите второе число-> '))
print(calc(user_choice, first_user_number, second_user_number))
