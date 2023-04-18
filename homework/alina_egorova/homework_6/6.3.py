# теперь у меня глобальная проблема не только с циклами, но и с функциями


print('Выберите операцию:')
print(' 1. Сложение\n', '2. Вычитание\n', '3. Умножение\n', '4. Деление')
operation = int(input('Введите номер пункта меню: '))
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if operation == 1:
    print(a+b)
elif operation == 2:
    print(a-b)
elif operation == 3:
    print(a*b)
elif operation == 4:
    if b == 0:
        print('Делить на ноль нельзя')
    else:
        print('Частное:', a / b, ',', 'Остаток:', a % b)
