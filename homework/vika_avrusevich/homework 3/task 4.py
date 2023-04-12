# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь
from math import sqrt

a = 6
b = 4

hypot = sqrt(a ** 2 + b ** 2)
sqr = a * b

print(f'\nГипотенуза = {hypot}\nПлощадь = {sqr}')
