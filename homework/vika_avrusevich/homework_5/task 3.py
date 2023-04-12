# Выполните random.random() 15 раз, сохраняя куда-то каждый результат.
# После этого выведите на экран максимальное из сгенеренных рандомов, минимальное,
# сумму всех рандомов и их среднее арифметическое.

import random

final_list = []
for i in range(1, 16):
    final_list.append(round(random.random() * 15))

print(final_list)
print(f'Максимальный рандом = {max(final_list)}')
print(f'Минимальный рандом = {min(final_list)}')
print(f'Сумма рандомов = {sum(final_list)}')
print(f'Cреднее арифметическое рандомов = {sum(final_list) / len(final_list)}')

