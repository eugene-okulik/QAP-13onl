my_dict = {'name': 'Ivan', 'age': [4, 5], 'name1': 'Ivan', (1, 2): 42}
my_dict1 = {}
my_dict2 = dict()
print(len(my_dict))
print(my_dict['name1'])
print(42 in my_dict)
my_dict['last_name'] = 'Sidorov'
print(my_dict)
x = my_dict.pop((1, 2))
print(my_dict)
print('Sidorov' in my_dict.values())
print(my_dict.values())
print(my_dict.keys())
print(my_dict.items())
