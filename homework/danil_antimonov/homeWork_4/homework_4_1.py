# Создайте словарь (и сохраните его в переменную my_dict) с такими ключами: ‘tuple’, ‘list’, ‘dict’, ‘set’, ‘str’.
# Для каждого элемента задайте значение соответствующее названию ключа.

my_dict = {'tuple': (1, 3, 6, 7, 'text', False, 12.3), 'list': [1, 2, 3, 4, 5],
           'dict': {'list': [213, 4345, 45645], 'name': 'George'},
           'set': {'text1', 'text2', 1, 3, 6, 7, 'text', False, 12.3}, 'str': 'string'}

# Для того, что хранится под ключом ‘tuple’:
# выведите на экран все элементы начиная со второго и до конца

print(my_dict.values())
tuple_in_my_dict = my_dict['tuple']
print('Содержимое вложенного Tuple начиная со 2 элемента:\n', tuple_in_my_dict[1:])

# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
# удалите второй элемент списка

list_in_my_dict = my_dict['list']
print('Вложенный список из словаря до изменений:\n', list_in_my_dict)
list_in_my_dict.append('shuffle')
list_in_my_dict.pop(1)
print('Второй элемент вложенного списка удалён, в конец вложенного списка добавлен новый элемент:\n', list_in_my_dict)

# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
# удалите какой-нибудь элемент

dict_in_my_dict = my_dict['dict']
print('Вложенный словарь до изменений:\n', dict_in_my_dict)
dict_in_my_dict['another tuple'] = 67485, 345435, 345435
dict_in_my_dict.pop('list')
print('Вложенный словарь после изменений:\n', dict_in_my_dict)

# Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество
# удалите элемент из множества


# Для того, что хранится под ключом ‘str’:
# Выведите на экран из строки следующие срезы:
#
# первые восемь символов
# четыре символа из центра строки
# символы с индексами кратными трем
# В конце выведите на экран весь словарь
