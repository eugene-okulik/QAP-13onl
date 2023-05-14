from dataclasses import dataclass


@dataclass
class Flower:
    life_time: int
    freshness: bool
    color: str
    stem: int
    cost: int


class Rose(Flower):
    def __init__(self, life_time, freshness, color, stem, cost):
        super().__init__(life_time, freshness, color, stem, cost)


class Tulip(Flower):
    def __init__(self, life_time, freshness, color, stem, cost):
        super().__init__(life_time, freshness, color, stem, cost)


class Chamomile(Flower):
    def __init__(self, life_time, freshness, color, stem, cost):
        super().__init__(life_time, freshness, color, stem, cost)


class Iris(Flower):
    def __init__(self, life_time, freshness, color, stem, cost):
        super().__init__(life_time, freshness, color, stem, cost)


class Bouquet:
    def __init__(self, flower_list):
        self.__flower_list = flower_list
        cost = sum(list(map(lambda flower: flower.cost, self.__flower_list)))
        print(f'Стоимость букета: {cost}')

    def time_withering(self):
        sum_life_time = [flower.life_time for flower in self.__flower_list]
        return f'Среднее время жизни: {round(sum(sum_life_time) / len(sum_life_time), 1)}'

    def freshness_sorting(self):
        self.__flower_list.sort(key=lambda flower: flower.freshness, reverse=True)
        return f'Цветы сортированы по свежести:\n{self.__flower_list}'

    def color_sorting(self):
        self.__flower_list.sort(key=lambda flower: flower.color.lower())
        return f'Цветы сортированы по цвету:\n{self.__flower_list}'

    def stem_sorting(self):
        self.__flower_list.sort(key=lambda flower: flower.stem)
        return f'Цветы сортированы по длине стебля:\n{self.__flower_list}'

    def cost_sorting(self):
        self.__flower_list.sort(key=lambda flower: flower.cost)
        return f'Цветы сортированы по цене:\n{self.__flower_list}'

    def search_by_color(self):
        user_color = input('Введите цвет на русском языке: ')
        search_result = list(filter(lambda flower: flower.color.lower() == user_color.lower(), self.__flower_list))
        return f'{user_color} цветов в букете:\n{search_result}' if search_result \
            else f'Нет таких цветов с таких цветом: {user_color} .'


flower_list1 = [
    Rose(1, True, 'Красный', 5, 110),
    Tulip(4, False, 'Желтый', 4, 100),
    Chamomile(5, True, 'Белый', 11, 120),
    Iris(7, True, 'Синий', 3, 500)
]

bouquet = Bouquet(flower_list1)
print(bouquet.time_withering())
print(bouquet.freshness_sorting())
print(bouquet.color_sorting())
print(bouquet.stem_sorting())
print(bouquet.cost_sorting())
print(bouquet.search_by_color())
