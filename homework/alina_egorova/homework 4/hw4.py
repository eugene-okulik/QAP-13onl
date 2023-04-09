my_dict = {'tuple': (1, 3, 6, 7, 'text', False, 12.3),
           'list': [1, 5, 7, 13, 'Hi', False, 13.3],
           'dict': {'name': 'Tyrion', 'second_name': 'Lannister', 'age': [39],
                    'name2': 'Emilia', 'second_name2': 'Clarke', 'age2': [36]
                    },
           'set': {1, 5, 3, 2, 8, 9},
           'str': 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'
           }
#Для того, что хранится под ключом ‘tuple’: выведите на экран все элементы начиная со второго и до конца

tuple_in_my_dict = my_dict['tuple']
print(tuple_in_my_dict[1:])

#Для того, что хранится под ключом ‘list’: добавьте в конец списка еще один элемент удалите второй элемент списка

list_in_my_dict = my_dict['list']
list_in_my_dict1 = list_in_my_dict.append('Ivan')
print(list_in_my_dict)
list_in_my_dict2 = list_in_my_dict.pop(1)
print(list_in_my_dict)

#Для того, что хранится под ключом ‘dict’: добавьте элемент с ключом ('i am a tuple',) и любым значением
#удалите какой-нибудь элемент

dict_in_my_dict = my_dict['dict']
dict_in_my_dict1 = dict_in_my_dict['i am a tuple'] = '15'
print(dict_in_my_dict)
dict_in_my_dict2 = dict_in_my_dict.pop('name')
print(dict_in_my_dict)

#Для того, что хранится под ключом ‘set’: добавьте новый элемент в множество удалите элемент из множества

set_in_my_dict = my_dict['set']
set_in_my_dict1 = set_in_my_dict.add(25)
print(set_in_my_dict)
set_in_my_dict2 = set_in_my_dict.pop()
print(set_in_my_dict)
set_in_my_dict3 = set_in_my_dict.remove(25)
print(set_in_my_dict)

#Для того, что хранится под ключом ‘str’: Выведите на экран из строки следующие срезы:
#первые восемь символов
#четыре символа из центра строки
#символы с индексами кратными трем

str_in_my_dict = my_dict['str']
str_in_my_dict1 = str_in_my_dict[:8]
print(str_in_my_dict1)
str_in_my_dict2 = str_in_my_dict[41:45]
print(str_in_my_dict2)
str_in_my_dict3 = str_in_my_dict[::3]
print(str_in_my_dict3)

#В конце выведите на экран весь словарь
print(my_dict.items())
