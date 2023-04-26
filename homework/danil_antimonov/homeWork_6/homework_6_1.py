# При помощи генераторов превратите этот текст в словарь такого вида:
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)


PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

my_list = PRICE_LIST.split('\n')
print(my_list)
price_dict = {item.split()[0]: int(item.split()[1][:-1]) for item in my_list}
print(price_dict)
