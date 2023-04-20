PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_dict = {}

for item in PRICE_LIST.split('\n'):
    if item.strip():
        key, value = item.split()
        price_dict[key] = int(value[:-1])

print(price_dict)

# Не догоняю как это записать генератором О_о

