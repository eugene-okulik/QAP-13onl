# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов.
# Собрать букет (букет - еще один класс) с определением его стоимости. В букете цветы пусть хранятся в списке.
# Это будет список объектов.
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)
# (это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни)(и это тоже метод).


class Flower:
    def __init__(self, price, freshness, stem_length, life_span):
        self.price = price
        self.freshness = freshness
        self.stem_length = stem_length
        self.life_span = life_span

    def __repr__(self):
        return f'{self.price} руб., {self.freshness}, {self.stem_length} см., {self.life_span} дней'


class Rose(Flower):
    def __init__(self, color, price, freshness, stem_length, life_span):
        super().__init__(price, freshness, stem_length, life_span)
        self.color = color

    def __repr__(self):
        return f'Роза ({self.color}): ' + super().__repr__()


class Sunflower(Flower):
    def __init__(self, color, price, freshness, stem_length, life_span):
        super().__init__(price, freshness, stem_length, life_span)
        self.color = color

    def __repr__(self):
        return f'Подсолнух ({self.color}): ' + super().__repr__()


class Lily(Flower):
    def __init__(self, color, price, freshness, stem_length, life_span):
        super().__init__(price, freshness, stem_length, life_span)
        self.color = color

    def __repr__(self):
        return f'Лилия ({self.color}): ' + super().__repr__()


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def get_cost(self):
        return sum([f.price for f in self.flowers])

    def get_life_span(self):
        return sum([f.life_span for f in self.flowers]) / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers = sorted(self.flowers, key=lambda f: f.freshness, reverse=True)

    def sort_by_color(self):
        self.flowers = sorted(self.flowers, key=lambda f: f.color.lower())

    def sort_by_stem_length(self):
        self.flowers = sorted(self.flowers, key=lambda f: f.stem_length, reverse=True)

    def sort_by_price(self):
        self.flowers = sorted(self.flowers, key=lambda f: f.price)

    def search_by_life_span(self):
        life_span = input("Введите среднее время жизни цветов: ")
        matching_flowers = [f for f in self.flowers if f.life_span == int(life_span)]
        if matching_flowers:
            print("Цветы с средним временем жизни {} дней:".format(life_span))
            for flower in matching_flowers:
                print(flower.__repr__())
        else:
            print("Цветы с таким средним временем жизни не найдены.")


rose1 = Rose('красная', 10, False, 35, 7)
sunflower1 = Sunflower('желтый', 13, True, 50, 8)
lily1 = Lily('белая', 8, True, 25, 5)

bouquet = Bouquet([rose1, lily1, sunflower1])

# определение стоимости букета
print(f'Цена букета: {bouquet.get_cost()} руб.')

# средняя продолжительность жизни цетов в букете:
print('Средняя продолжительность жизни цветов:', bouquet.get_life_span(), 'дней.')

# отсортировать цветы в букете по свежести:
bouquet.sort_by_freshness()
print('Сортировка по свежести:', bouquet.flowers)

# отсортировать цветы в букете по цвету:
bouquet.sort_by_color()
print('Сортировка по цвету:', bouquet.flowers)

# отсортировать цветы в букете по длине стебля:
bouquet.sort_by_stem_length()
print('Сортировка по длине стебля:', bouquet.flowers)

# остсортировать цветы в букете по стоимости:
bouquet.sort_by_price()
print('Сортировка по цене:', bouquet.flowers)

# поиск по продолжительности жизни цветов:
bouquet.search_by_life_span()
