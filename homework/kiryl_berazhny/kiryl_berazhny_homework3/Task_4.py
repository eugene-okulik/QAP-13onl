# Нахождение гипотенузы и площади прямоугольного треугольника по заданным значениям катетов.
# В условии задания ничего не говорится про тип числа. Примем, что введенные числа могут быть с плавающей точкой

cathetus1 = float(input('Введите длину первого катета треугольника: '))
cathetus2 = float(input('Введите длину второго катета треугольника: '))
hypotenuse = (cathetus1 ** 2 + cathetus2 ** 2) ** 0.5
triangle_area = (cathetus1 * cathetus2) / 2
print('Гипотенуза треугольника равняется: ', hypotenuse)
print('Площадь треугольника равняется: ', triangle_area)
