# Выполните random.random() 15 раз, сохраняя куда-то каждый результат.
# После этого выведите на экран максимальное из сгенеренных рандомов:
# минимальное, сумму всех рандомов и их среднее арифметическое.

import random

list = []
num = [random.random()]
for number in range(15):
    list.append(random.random())
print(list)
print(max(list))
print(min(list))
print(sum(list))
print(sum(list) / len(list))