#Задание 1 - Генераторы


PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''
dict_price = {item.split()[0]: int(item.split()[1][:-1]) for item in PRICE_LIST.split('\n')}
print(dict_price)
