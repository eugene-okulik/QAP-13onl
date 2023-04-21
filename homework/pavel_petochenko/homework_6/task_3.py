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
#
print('Выбирете операцию: \n'
      '1. Сложение \n'
      '2. Вычитание \n'
      '3. Умножение \n'
      '4. Деление \n'
      )
input_op = input('Введите номер пункта меню ')

input_num1 = input('Введите первое число ')
input_num2 = input('Введите второе число ')


def summ():
    sum1 = int(input_num1) + int(input_num2)
    print(sum1)


def subt():
    sub = int(input_num1) - int(input_num2)
    print(sub)


def multp():
    mult = int(input_num1) * int(input_num2)
    print(mult)


def divis():
    if int(input_num2) == 0:
        print('Делить на ноль нельзя!')
        return
    div = int(input_num1) // int(input_num2)
    div_1 = int(input_num1) % int(input_num2)
    print('Частное ' + str(div) + ' Остаток деления ' + str(div_1))


match input_op:
    case '1':
        summ()
    case '2':
        subt()
    case '3':
        multp()
    case '4':
        divis()
