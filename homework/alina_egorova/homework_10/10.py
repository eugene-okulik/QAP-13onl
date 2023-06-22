# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов. Создать экземпляры (объекты) цветов
# разных видов. Собрать букет (букет - еще один класс) с определением его стоимости. В букете цветы пусть хранятся в
# списке. Это будет список объектов.
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)
# (это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).
class Flower:
    def __init__(self, name, freshness, color, stem_length, price, life):
        self.name = name
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.life = life

    def get_name(self):
        return self.name

    def get_freshness(self):
        return self.freshness

    def get_color(self):
        return self.color

    def get_length(self):
        return self.stem_length

    def get_price(self):
        return self.price

    def get_life(self):
        return self.life


class Rose1(Flower):
    def __init__(self, name, freshness, color, stem_length, price, life):
        super().__init__(name, freshness, color, stem_length, price, life)


class Rose2(Flower):
    def __init__(self, name, freshness, color, stem_length, price, life):
        super().__init__(name, freshness, color, stem_length, price, life)


class Rose3(Flower):
    def __init__(self, name, freshness, color, stem_length, price, life):
        super().__init__(name, freshness, color, stem_length, price, life)


class Chrysanthemums(Flower):
    def __init__(self, name, freshness, color, stem_length, price, life):
        super().__init__(name, freshness, color, stem_length, price, life)


class Peony(Flower):
    def __init__(self, name, freshness, color, stem_length, price, life):
        super().__init__(name, freshness, color, stem_length, price, life)


class Buket:
    def __init__(self, flowers_in_bouquet):
        self.flowers_in_bouquet = flowers_in_bouquet

    def get_price(self):
        return sum([x.get_price() for x in self.flowers_in_bouquet])

    def sorted_by_freshness(self):
        self.flowers_in_bouquet.sort(key=lambda x: x.get_freshness())

    def sorted_by_life(self):
        return [x for x in self.flowers_in_bouquet if x.get_life()]

    def sorted_by_length(self):
        self.flowers_in_bouquet.sort(key=lambda x: x.get_stem_length())

    def sort_by_color(self):
        self.flowers_in_bouquet = sorted(self.flowers_in_bouquet, key=lambda f: f.color.lower())

    def search_by_param(self, param_name, param_value):
        return [x for x in self.flowers_in_bouquet if getattr(x, param_name) == param_value]


rose = Rose1('Rose Freedom', 90, 'red', 80, 170, 10)
rose2 = Rose2('Rose Nicole', 95, 'yellow', 120, 200, 12)
rose3 = Rose3('Rose Lens', 80, 'red', 60, 160, 7)
chrysanthemums = Chrysanthemums('Chrysanthemum', 80, 'white', 110, 150, 15)
peony = Peony('Peony', 75, 'dark-pink', 80, 250, 5)

flowers = [rose, rose2, rose3, chrysanthemums, peony]
bouquet = Buket(flowers)


for flower in bouquet.flowers_in_bouquet:
    print('Name -', flower.name)
    print('Color -', flower.color)
    print('Price -', flower.price, 'rubles')
    print('Freshness -', flower.freshness, '%')
    print('Flower stem length -', flower.stem_length, 'cm')
    print('Average life time -', flower.life, 'days')

found_flowers = bouquet.search_by_param('color', 'red')
for flower in found_flowers:
    print(flower.name, flower.color)

print('Bouquet price =', bouquet.get_price(), 'rubles')
