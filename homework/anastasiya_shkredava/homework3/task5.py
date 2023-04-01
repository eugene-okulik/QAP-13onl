# Программа запрашивает у пользователя длину ребра куба.
# И находит объем куба и площадь его боковой поверхности

edge = int(input('Input the cube edge length: '))
volume = edge**3
lateral_square = 4 * edge**2
print('cube volume =', volume,
      '\ncube lateral surface square =', lateral_square)
