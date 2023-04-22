PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''
x = PRICE_LIST.split()

dict1 = {x[i]: x[i + 1][0:-1] for i in range(0, len(x), 2)}

my_dict2 = {k:  int(v) for k, v in dict1.items()}
print(my_dict2)
