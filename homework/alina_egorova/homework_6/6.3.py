operation = input('''
Выберите операцию:
1. Сложение
2. Вычитание
3. Умножение
4. Деление
Введите номер пункта меню: 
''')
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))


def calculate():
    if operation == '1':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif operation == '2':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif operation == '3':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif operation == '4':
        if number_2 == 0:
            print('Делить на ноль нельзя')
        else:
            print('{} / {} = '.format(number_1, number_2))
            print('Частное:', number_1 // number_2, ';', 'остаток:', number_1 % number_2)
    else:
        print('Такой операции нет')


calculate()
