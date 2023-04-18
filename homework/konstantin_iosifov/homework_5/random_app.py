import random

super_random_list = []

for sr in range(15):
    random_result = round(random.random(), 3)
    super_random_list.append(random_result)

max_random = max(super_random_list)
min_random = min(super_random_list)
sum_random = sum(super_random_list)
avg_random = sum_random / len(super_random_list)

print(super_random_list)
print(max_random)
print(min_random)
print(round(sum_random, 3))
print(round(avg_random, 3))
