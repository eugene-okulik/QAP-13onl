# Даны катеты прямоугольного треугольника.
# Найти его гипотенузу и площадь.

import math


leg1 = 4
leg2 = 6
hypotenuse = math.sqrt(leg1**2 + leg2**2)
square = (leg1 * leg2 / 2)
print('hypotenuse =', round(hypotenuse, 4), '\nsquare =', square)
