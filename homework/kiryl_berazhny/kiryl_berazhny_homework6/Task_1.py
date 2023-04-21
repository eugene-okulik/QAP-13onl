# Задание 1 - Генераторы

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''
PRICE_LIST = PRICE_LIST.split('\n')
for index in range(len(PRICE_LIST)):
    PRICE_LIST[index] = PRICE_LIST[index].split()
price_dict = {name: int(price[:-1]) for name, price in PRICE_LIST}
print(price_dict)
