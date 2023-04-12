my_list = [1, 3, 6, 3, 8, 9]

new_list = []
for x in my_list:
    new_list.append(x * 2)

print(new_list)

new_list2 = [num * 2 for num in my_list]
print(new_list2)
new_list3 = [num * 2 for num in my_list if num % 2 == 0 or num == 3]
print(new_list3)
my_dict = {'name': 'Ivan', 'age': 38, 'height': 180, 'children': ['Peter', 'Masha']}
my_dict2 = {k: v for k, v in my_dict.items() if isinstance(v, int)}
my_dict3 = {v: k for k, v in my_dict.items() if isinstance(v, str) or isinstance(v, int) or isinstance(v, tuple)}
print(my_dict2)
print(my_dict3)
