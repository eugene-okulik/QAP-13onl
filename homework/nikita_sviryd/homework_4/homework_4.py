my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [1.1, 2.1, 3.1, 4.1, 5.1],
    'dict': {'a': 1.2, 'b': 2.2, 'c': 3.2, 'd': 4.2, 'e': 5.2},
    'set': {1.3, 2.3, 3.3, 4.3, 5.3},
    'str': 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'
}

print(my_dict['tuple'][1:])

my_dict['list'].append(6.1)
del my_dict['list'][1]

my_dict['dict'][('i am a tuple',)] = '6.2'
del my_dict['dict']['b']

my_dict['set'].add(6.3)
my_dict['set'].discard(1.3)

print(my_dict['str'][:8])
print(my_dict['str'][len(my_dict['str'])//2-2:len(my_dict['str'])//2+2])
print(my_dict['str'][::3])

print(my_dict)
