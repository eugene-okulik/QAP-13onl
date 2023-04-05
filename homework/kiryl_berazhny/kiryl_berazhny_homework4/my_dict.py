# работа со словарями, списками, кортежами, множествами и строками
# я может и лишнего расписал, но просто для практики пальцев и привычки писать правильно

my_dict = {
    'tuple': (1, 2, 3, 4, 5), 'list': ['6', [7], 8, 9, [10]], 'dict': {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15},
    'set': {16, 17, 18, 19, '20'},
    'str': 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'
}
print(f'РАБОТА С КОРТЕЖЕМ\nЭлементы кортежа от второго до конца: {my_dict["tuple"][2:]}.\n')
my_dict['list'] += [input('РАБОТА СО СПИСКОМ''\nВведите значение которое хотите добавить в список: ')]
list_index1 = my_dict['list'].pop(1)
print(
    f"Из первоначального списка удалено значение с индексом [1], а именно: {list_index1}.\n"
    f"Добавлено значение в конец списка: {my_dict['list'][-1]}.\n"
    f"Итоговый список выглядит следующим образом: {my_dict['list']}.\n"
)
my_dict['dict']['i am a tuple'] = input('РАБОТА СО СЛОВАРЕМ\nДобавление ключа "i am a tuple". Введите его значение: ')
my_dict['dict'].pop('c')
print(
    f'В словарь dict добавлен ключ "i am a tuple" которому передано значение "{my_dict["dict"]["i am a tuple"]}".\n'
    f'Из словаря удален ключ "c".\n'
    f'Итоговый словарь выглядит следующим образом: {my_dict["dict"]}\n'
)
new_value = input('РАБОТА С МНОЖЕСТВОМ\nВведите значение для добавления в множество: ')
my_dict['set'].add(new_value)
my_dict['set'].remove(18)
print(f'В множество добавлено значение "{new_value}", и удален элемент "18".\nИтоговое множество: {my_dict["set"]}\n')
mid_str = len(my_dict["str"]) // 2
print(
    f'РАБОТА СО СТРОКОЙ\nПервые восемь символов строки: {my_dict["str"][0:8]}\n'
    f'Четыре символа из центра строки: {my_dict["str"][mid_str:mid_str + 4]}\n'
    f'Все символы с индексами кратные трем: {my_dict["str"][::3]}\n'
)
print('ИТОГО')
for key in my_dict:
    print(my_dict[key])
