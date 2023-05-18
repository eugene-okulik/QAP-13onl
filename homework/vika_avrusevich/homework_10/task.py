# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов. Создать экземпляры (объекты)
# цветов разных видов. Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).

class Flowers:
    def __init__(self, name, fresh, stem_len, lifetime, price):
        self.name = name
        self.fresh = fresh
        self.stem_len = stem_len
        self.price = price
        self.lifetime = lifetime

    def __repr__(self):
        return (f'{self.name}, Freshness: {self.fresh}, Length of stem: {self.stem_len}, '
                f'Lifetime: {self.lifetime}, Price: {self.price}')

    def get_fresh(self):
        return self.fresh

    def get_stem_len(self):
        return self.stem_len

    def get_lifetime(self):
        return self.lifetime

    def get_price(self):
        return self.price


class Rose(Flowers):
    def __init__(self, color, fresh, stem_len, lifetime, price):
        name = f'Rose: {color}'
        super().__init__(name, fresh, stem_len, lifetime, price)
        self.color = color


class Lilyi(Flowers):
    def __init__(self, color, fresh, stem_len, lifetime, price):
        name = f'Lilyi: {color}'
        super().__init__(name, fresh, stem_len, lifetime, price)
        self.color = color


class Gipsophily(Flowers):
    def __init__(self, color, fresh, stem_len, lifetime, price):
        name = f'Gipsophily: {color}'
        super().__init__(name, fresh, stem_len, lifetime, price)
        self.color = color


class Buqet:
    def __init__(self, flowers):
        self.flowers = flowers

    # сортировка по цветам
    def sort_by_color(self):
        self.flowers.sort(key=lambda flw: flw.color)
        return f'Sorting by color: {[f.color for f in buqet.flowers]}'

    # сортировка по свежести
    def sort_by_fresh(self):
        self.flowers.sort(key=lambda flw: flw.get_fresh())
        return f'Sorting by fresh: {[f.fresh for f in buqet.flowers]}'

    # сортировка по длине стебля
    def sort_by_stem_len(self):
        self.flowers.sort(key=lambda flw: flw.get_stem_len())
        return f'Sorting by length of stem: {[f.stem_len for f in buqet.flowers]}'

    # поиск по продолж. жизни цветов
    def search_by_lifetime(self, lifetime):
        return f'Serching by lifetime: {[flw for flw in self.flowers if flw.get_lifetime() == lifetime].__repr__()}'

    # средняя продолж. жизни цветов
    def get_avg_lifetime(self):
        return f'Average lifetime: {sum([flw.get_lifetime() for flw in self.flowers]) / len(self.flowers)}'

    # общая стоимость
    def get_price(self):
        return f'Total price of bouquet: {sum([flw.get_price() for flw in self.flowers])}'


roses = [Rose('white', 3, 60, 12, 4), Rose('pink', 5, 50, 18, 3)]
lilyis = [Lilyi('white', 5, 20, 15, 8), Lilyi('yellow', 4, 15, 10, 7)]
gipsophilis = [Gipsophily('rainbow', 1, 50, 30, 7), Gipsophily('blue', 9, 25, 35, 5)]

buqet = Buqet(roses + lilyis + gipsophilis)

for flower in buqet.flowers:
    print(f'{flower.name}\n'
          f'Freshness: {flower.fresh}\n'
          f'Length of stem: {flower.stem_len}\n'
          f'Lifetime: {flower.lifetime}\n'
          f'Price: {flower.price}\n')

print(buqet.get_price())
print(buqet.get_avg_lifetime())
print(buqet.sort_by_color())
print(buqet.sort_by_fresh())
print(buqet.sort_by_stem_len())
print(buqet.search_by_lifetime(10))
