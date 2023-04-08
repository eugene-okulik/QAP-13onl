my_dict = {
    'tuple': (2, 4, 6, 8, 10),
    'list': [1, 2, False, 'cat', 6.01],
    'dict': {'roses': 'red', 'violets': 'blue', 'a': 'b', 'name': 'Pasha', 'city': 'Minsk'},
    'set': {3, 9, True, 56.88, 'text'},
    'str': 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'
}

# Для ‘tuple’: выведите на экран все элементы начиная со второго и до конца
print(my_dict['tuple'][1:])

# Для ‘list’:
# добавьте в конец списка еще один элемент
my_dict['list'].append(12)
print(my_dict['list'])
# удалите второй элемент списка
my_dict['list'].pop(1)
print(my_dict['list'])

# Для ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением,
my_dict['dict']['i am a tuple,'] = 'and this is my destiny'
print(my_dict['dict'])
# удалите какой-нибудь элемент
my_dict['dict'].pop('a')
print(my_dict['dict'])

# Для ‘set’:
# добавьте новый элемент в множество
my_dict['set'].add('John Cena')
print(my_dict['set'])
# удалите элемент из множества
my_dict['set'].remove(56.88)
print(my_dict['set'])

# Для ‘str’: выведите на экран из строки следующие срезы:
# первые восемь символов
print(my_dict['str'][:8])
# четыре символа из центра строки
str_len = (len(my_dict['str']))
print(str_len)
print(my_dict['str'][43:47])
# символы с индексами кратными трем
print(my_dict['str'][::3])
