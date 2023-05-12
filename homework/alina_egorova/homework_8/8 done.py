# Программа спрашивает у пользователя 2 числа (вне функции)
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))


def decor(funk):
    def wrapper(first, second):
        result = None
        if first < 0 or second < 0:
            result = funk(first, second, '3')
        elif first == second:
            result = funk(first, second, '1')
        elif first > second:
            result = funk(first, second, '2')
        elif first < second:
            result = funk(first, second, '4')
        return result

    return wrapper


@decor
def calculate(number_1, number_2, operation):
    if operation == '1':
        print(f'{number_1} + {number_2} = ')
        print(number_1 + number_2)
    elif operation == '2':
        print(f'{number_1} - {number_2} = ')
        print(number_1 - number_2)
    elif operation == '3':
        print(f'{number_1} * {number_2} = ')
        print(number_1 * number_2)
    elif operation == '4':
        if number_2 == 0:
            print('Делить на ноль нельзя')
        else:
            print(f'{number_1} / {number_2} = ')
            print('Частное:', number_1 // number_2, ';', 'остаток:', number_1 % number_2)
    else:
        print('Такой операции нет')


calculate(first, second)
