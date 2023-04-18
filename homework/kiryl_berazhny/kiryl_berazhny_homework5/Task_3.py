#  random.random() выполняется заданное количество раз.

import random

num = int(input('Enter number: '))
my_list = list()
for i in range(num):
    my_list.append(random.random())
print(max(my_list))
print(min(my_list))
print(sum(my_list))
print(sum(my_list) / num)
