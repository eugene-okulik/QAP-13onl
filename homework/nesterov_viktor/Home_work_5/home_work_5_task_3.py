import random

random_nums = []
for i in range(15):
    rand_num = random.random()
    random_nums.append(rand_num)
    print(rand_num)

max_num = max(random_nums)
min_num = min(random_nums)
avg_num = sum(random_nums) / len(random_nums)

print(f"Максимальное значение: {max_num}")
print(f"Минимальное значение: {min_num}")
print(f"Среднее арифметическое: {avg_num}")
