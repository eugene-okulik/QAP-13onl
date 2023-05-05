user_num = input('Введите длинну стороны куба ')
user_num = float(user_num)
b = 6 * user_num ** 2
s = 4 * user_num ** 2
phrase11 = 'Вы ввели число '
phrase12 = phrase11 + str(user_num)
print(phrase12, 'площадь куба равна', b, 'а площадь его боковой поверхности равна ', s)
