PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


my_list = PRICE_LIST.split('\n')
for i in range(len(my_list)):
    my_list[i] = my_list[i].split()
new_dict_price = {k: int(v[:-1]) for k, v in my_list}
print(new_dict_price)
