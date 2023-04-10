# Выполните random.random() 15 раз, сохраняя куда-то каждый результат.
# После этого выведите на экран максимальное из сгенеренных рандомов, минимальное,
# сумму всех рандомов и их среднее арифметическое.
import random

i = 0
my_list = []
while i < 15:
    my_list.append(round(random.random() * 10))
    i += 1
print(my_list)
print(max(my_list))
print(min(my_list))
print(sum(my_list))
print(sum(my_list) / i)
