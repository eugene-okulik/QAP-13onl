#  random.random() 15 раз

import random

my_list = list()
for i in range(15):
    my_list.append(random.random())
print(max(my_list))
print(min(my_list))
print(sum(my_list))
print(sum(my_list)/15)
