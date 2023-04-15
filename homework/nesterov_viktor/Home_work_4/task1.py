my_dict = {
    'tuple': (1, 2, 3, 4, 5, 6),
    'list': [1, 2, 3, 4, 5],
    'dict': {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'},
    'set': {1, 2, 3, 4, 5},
    'str': 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'
}

# Для tuple
print(my_dict['tuple'][1:])

# Для list
my_dict['list'].append(6)
del my_dict['list'][1]

# Для dict
var = my_dict['dict'][('i am a tuple',)] = 'tuple value'
my_dict['dict'].popitem()

# Для set
my_dict['set'].add(6)
my_dict['set'].discard(2)

# Для str
print(my_dict['str'][0:8])
print(my_dict['str'][len(my_dict['str'])//2-2:len(my_dict['str'])//2+2])
print(my_dict['str'][::3])

# Вывод словаря
print(my_dict)
    