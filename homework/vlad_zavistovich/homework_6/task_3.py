print('Добро пожаловать в калькулятор. Выберите оперецию:')
print(' 1. Сложение\n', '2. Вычитание\n', '3. Умножение\n', '4. Деление')
user_choice = int(input('Выберите операцию:'))
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        print('Ошибка: Деление на ноль! Делить на ноль нельзя!')
        return None
    else:
        div_number = x // y
        mod_number = x % y
        return div_number, mod_number


if user_choice == 1:
    print('Операция сложения:', number_1, "+", number_2, "=", addition(number_1, number_2))
elif user_choice == 2:
    print('Операция вычитания:', number_1, "-", number_2, "=", subtraction(number_1, number_2))
elif user_choice == 3:
    print('Операция умножения:', number_1, "*", number_2, "=", multiplication(number_1, number_2))
elif user_choice == 4:
    result = divide(number_1, number_2)
    if result is not None:
        div, mod = result
        print('Операция деления. Частное:', div, ',Остаток:', mod)
else:
    print('Ошибка! Неверено выбран пункт меню.')
