# Даны действительные числа x и y.Получить x − y / 1 + xy
#
# Я решила, что нет смысла y / 1, поэтому добавлю скобочки
# и решу выражение (x-y)/(1+xy)


x = 13
y = 6
action1 = x - y
action2 = 1 + x*y
result = action1 / action2
print('(x-y)/(1+xy) =', round(result, 4))
