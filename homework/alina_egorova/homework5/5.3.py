# Выполните random.random() 15 раз, сохраняя куда-то каждый результат.
import random

random_list = []

for i in range(15):
    random_num = random.random()
    random_list.append(random_num)

print(max(random_list))  # максимальное из сгенеренных рандомов
print(min(random_list))  # минимальное из сгенеренных рандомов
print(sum(random_list))  # сумма из сгенеренных рандомов
print((sum(random_list)) / len(random_list))  # среднее арифметическое
