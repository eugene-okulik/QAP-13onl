my_list = [1, 4, 6, 2, 8, 4, 4]


def summ_3(number):
    return number + 3


# summ_4 = lambda x: x + 4

# new_list = list(map(summ_4, my_list))
# print(new_list)

new_list2 = list(map(lambda x: x + 5, my_list))
print(new_list2)

new_list3 = [x + 6 for x in my_list]
print(new_list3)

filtered_list = list(filter(lambda x: x <= 5, my_list))
print(filtered_list)

filtered_list2 = [x for x in my_list if x <= 5]
print(filtered_list2)

for elt in filter(lambda x: x <= 5, my_list):
    print(elt)

my_tuple = tuple(my_list)
filtered_tuple = list(filter(lambda x: x <= 5, my_tuple))
print(filtered_tuple)

my_dict = {'one': 1, 'two': 2, 'three': 3}


def dict_f(tup):
    k, v = tup
    return v < 3


filtered_dict = filter(dict_f, my_dict.items())
filtered_dict2 = filter(lambda tup: tup[1] < 3, my_dict.items())
print(filtered_dict2)
for z in filtered_dict:
    print(z)
