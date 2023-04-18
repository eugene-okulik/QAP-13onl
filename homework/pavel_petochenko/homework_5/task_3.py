# Выполните random.random() 15 раз, сохраняя куда-то каждый результат.
# После этого выведите на экран максимальное из сгенеренных рандомов:
# минимальное, сумму всех рандомов и их среднее арифметическое.

import random

list_1 = []
num = [random.random()]
for number in range(15):
    list_1.append(random.random())
print(list_1)
print(max(list_1))
print(min(list_1))
print(sum(list_1))
print(sum(list_1) / len(list_1))
