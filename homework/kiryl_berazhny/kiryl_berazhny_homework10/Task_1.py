# Цветочница

class Flowers:

    def __init__(self, name=None, lifetime=None, freshness=None, stem_len=None, color=None, price=None):

        self.lifetime = lifetime
        self.freshness = freshness
        self.color = color
        self.price = price
        self.stem_len = stem_len
        self.name = name

    def __str__(self):

        return (
            f'Наименование: {self.name}, время увядания: {self.lifetime}, свежесть: {self.freshness}, '
            f'длина стебля: {self.stem_len}, цвет: {self.color}, стоимость: {self.price}.'
        )

    def d_lifetime(self):

        return self.lifetime

    def d_freshness(self):

        return self.freshness

    def d_price(self):

        return self.price

    def d_color(self):

        return self.color

    def d_stem_len(self):

        return self.stem_len

    def d_name(self):

        return self.name


class Roses(Flowers):

    def __init__(self, name, lifetime, freshness, stem_len, color, price):

        super().__init__(name, lifetime, freshness, stem_len, color, price)
        self.freshness = self.freshness_check()

    def freshness_check(self):

        if self.freshness > self.lifetime:
            while self.freshness > self.lifetime:
                self.freshness = int(
                    input(f'Откорректируйте свежесть цветов, максимальный срок жизни {self.name} - {self.lifetime}.\n'
                          f'Введите параметр свежести цветов:')
                )
        return self.freshness


class Lilies(Flowers):

    def __init__(self, name, lifetime, freshness, stem_len, color, price):

        super().__init__(name, lifetime, freshness, stem_len, color, price)
        self.freshness = self.freshness_check()

    def freshness_check(self):

        if self.freshness > self.lifetime:
            while self.freshness > self.lifetime:
                self.freshness = int(
                    input(f'Откорректируйте свежесть цветов, максимальный срок жизни {self.name} - {self.lifetime}.\n'
                          f'Введите параметр свежести цветов:')
                )
        return self.freshness


class Chrysanthemum(Flowers):

    def __init__(self, name, lifetime, freshness, stem_len, color, price):

        super().__init__(name, lifetime, freshness, stem_len, color, price)
        self.freshness = self.freshness_check()

    def freshness_check(self):

        if self.freshness > self.lifetime:
            while self.freshness > self.lifetime:
                self.freshness = int(
                    input(f'Откорректируйте свежесть цветов, максимальный срок жизни {self.name} - {self.lifetime}.\n'
                          f'Введите параметр свежести цветов:')
                )
        return self.freshness


class Bouquet(Flowers):

    def __init__(self, list_bouq: list):

        super().__init__()
        self.list_bouq = list_bouq
        self.total = list(
            map(lambda flower: [flower.d_name(), flower.d_lifetime(), flower.d_freshness(), flower.d_stem_len(),
                                flower.d_color(), flower.d_price()], self.list_bouq)
        )  # создаю массив из списков со значениями объекта

    def total_cost(self):

        total = sum(list(map(lambda flower: flower.d_price(), self.list_bouq)))
        print(f'Общая стоимость букета: {total}')

    def average_lifetime(self):

        total = sum(list(map(lambda flower: flower.d_lifetime(), self.list_bouq))) / len(self.list_bouq)
        print(f'Время увядания букета: {total}')

    def sort_flowers(self):  # сортировка списка по выбранному значению

        print(
            'Виды сортировки:\n1. Наименование.\n2. Время увядания.'
            '\n3. Свежесть.\n4. Длина стебля.\n5. Цвет.\n6. Стоимость'
        )
        choice = int(input('Выберите пункт: ')) - 1  # -1 чтобы выбор совпадал с индексом списка
        while choice not in range(6):
            choice = int(input('Выберите пункт: ')) - 1
        self.total.sort(key=lambda total: total[choice])  # раньше такого не делал, искал в интернете.
        for el in self.total:
            print(
                f'Наименование: {el[0]}, время увядания: {el[1]},'
                f' свежесть: {el[2]}, длина стебля: {el[3]}, цвет: {el[4]}, стоимость: {el[5]}.'
            )

    def search_flowers(self):  # поиск в списке по выбранному значению

        print(
            'Поиск по параметру:\n1. Наименование.\n2. Время увядания.'
            '\n3. Свежесть.\n4. Длина стебля.\n5. Цвет.\n6. Стоимость'
        )
        choice = int(input('Выберите пункт: ')) - 1  # -1 чтобы выбор совпадал с индексом списка
        while choice not in range(0, 6):
            choice = int(input('Выберите пункт: ')) - 1
        if choice == 0 or choice == 4:
            search_name = input('Введите запрос (не менее 3 символов): ')
            while len(search_name) in range(3):
                search_name = input('Введите запрос (не менее 3 символов): ')
        else:
            search_name = input('Введите запрос (число): ')
        print('\nРезультата поиска:')
        for el in self.total:
            if search_name in str(el[choice]).lower():
                print(
                    f'Наименование: {el[0]}, время увядания: {el[1]},'
                    f' свежесть: {el[2]}, длина стебля: {el[3]}, цвет: {el[4]}, стоимость: {el[5]}.'
                )


floribunda = Roses('Floribunda', 14, 10, 100, 'pink', 15)
miniature = Roses('Miniature', 12, 12, 60, 'blue', 14)
pleated = Roses('Pleated', 14, 4, 80, 'white', 15)
asian = Lilies('Asian', 21, 18, 70, 'white', 23)
oriental = Lilies('Oriental', 20, 13, 80, 'yellow', 25)
tubular = Lilies('Tubular', 21, 18, 70, 'pink', 23)
talisman = Chrysanthemum('Talisman', 28, 20, 60, 'red', 14)
avrora = Chrysanthemum('Avrora', 28, 14, 50, 'white', 15)
inga = Chrysanthemum('Inga', 25, 12, 60, 'yellow', 15)
bouq = list()
bouq.append(floribunda)
bouq.append(miniature)
bouq.append(pleated)
bouq.append(asian)
bouq.append(oriental)
bouq.append(tubular)
bouq.append(talisman)
bouq.append(avrora)
bouq.append(inga)
flowers = Bouquet(bouq)
flowers.total_cost()
flowers.average_lifetime()
flowers.sort_flowers()
flowers.search_flowers()
