# Даны два действительных числа.
# Найти среднее арифметическое и среднее геометрическое этих чисел.

import math


a = 78
b = 12
arithmetic_mean = (a + b) / 2
geometric_mean = math.sqrt(a * b)
print('(a+b)/2 =', arithmetic_mean, '\nsqrt(a*b) =', round(geometric_mean, 4))
