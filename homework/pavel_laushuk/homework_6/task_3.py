print('Выберите операцию: '
      '1.Сложение '
      '2.Вычитание '
      '3.Умножение '
      '4.Деление ')
print('Введите номер пункта меню:')
menu = int(input())
print('Введите первое число:')
a = float(input())
print('Введите второе число:')
b = float(input())
if menu < 2:
    print(f'Сумма этих чисел равна:{a + b}')
if menu == 2:
    print(f'Разность этих чисел равна:{a - b}')
if menu == 3:
    print(f'Произведение этих чисел равна:{a * b}')
if menu == 4:
    print(f'Деление этих чисел равна:{a / b}')
    # calc(a, b)
    # print(calc(a + b))
