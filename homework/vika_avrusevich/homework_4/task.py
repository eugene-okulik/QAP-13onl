# 1. Для того, что хранится под ключом ‘tuple’: выведите на экран все элементы начиная со второго и до конца
# 2. Для того, что хранится под ключом ‘list’: добавьте в конец списка еще один элемент
#                                              удалите второй элемент списка
# 3. Для того, что хранится под ключом ‘dict’: добавьте элемент с ключом ('i am a tuple',) и любым значением
#                                              удалите какой-нибудь элемент
# 4. Для того, что хранится под ключом ‘set’: добавьте новый элемент в множество и удалите элемент из множества
# 5. Для того, что хранится под ключом ‘str’: Выведите на экран из строки следующие срезы:
#                                             первые восемь символов
#                                             четыре символа из центра строки
#                                             символы с индексами кратными трем
# 6. В конце выведите на экран весь словарь

my_dict = {
    'tuple': (1, 3, 6, 7, 'text', False, 12.3, [4, 5]),
    'list': [1, 3, 6, 7, 'text', False, 12.3, [4, 5]],
    'dict': {'name': 'Ivan', 'age': [4, 5], 'name1': 'Peter', (1, 2): 42, 'height': 180},
    'set': {'asjhdf', 'zsdsdf', 1, 3, 6, 7, 'text', False, 12.3, (1, 2)},
    'str': 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'
}

# print(type(my_dict['list']))
# 1
print(f"\n1 task(tuple):\n{my_dict['tuple'][1:]}\n")
# 2
my_dict['list'].append('new_element')
del_el2 = my_dict['list'].pop(1)
print(f"2 task(list):\ndeleted element = {del_el2}\n{my_dict['list']}\n")
# 3
my_dict['dict']['i am a tuple'] = 'Good Luck!'
del_el3 = my_dict['dict'].pop('name')
print(f"3 task(dict):\ndeleted element = {del_el3}\n{my_dict['dict']}\n")
# 4
my_dict['set'].add('new_element')
del_el4 = my_dict['set'].pop()
print(f"4 task(set):\ndeleted element = {del_el4}\n{my_dict['set']}\n")
# 5
first_8 = my_dict['str'][:8]
centr_4 = my_dict['str'][(len(my_dict['str']) // 2) - 2:(len(my_dict['str']) // 2) + 2]
krat_3 = my_dict['str'][::3]
print(f'5 task(str):\n- {first_8}\n- {centr_4}\n- {krat_3}\n')
# 6
print(f"Final dict:\n"
      f"{my_dict['tuple']}\n"
      f"{my_dict['list']}\n"
      f"{my_dict['dict']}\n"
      f"{my_dict['set']}\n"
      f"{my_dict['str']}")
