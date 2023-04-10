my_dict = {
    'tuple': (4, 5, 9, 14, 53),
    'list': [6, 7, 11, 22, 78],
    'dict': {
        'name': 'Vasya',
        'age': 30,
        'job': 'Itishnik',
        'company': 'Very good',
        'single': True
    },
    'set': {90, 1, 22, 43, 7},
    'str': 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'}

tuple_action = my_dict['tuple'][1:]

my_dict['list'].append(99)
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = 'i am a terminator'
my_dict['dict'].pop('company')

my_dict['set'].add(13)
my_dict['set'].remove(1)

str_action_1 = my_dict['str'][:8]
# str_action_2 = len(my_dict['str'])
str_action_2 = my_dict['str'][43:47]
str_action_3 = my_dict['str'][::3]

print(tuple_action)
print(my_dict['list'])
print(my_dict['dict'])
print(my_dict['set'])
print(str_action_1)
print(str_action_2)
print(str_action_3)
print(my_dict)
