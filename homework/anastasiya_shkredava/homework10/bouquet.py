# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов. Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.
#
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)(методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).


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


class Cornflake(Flower):
    def __init__(self, life_time, freshness, color, stem, cost):
        super().__init__(life_time, freshness, color, stem, cost)


class Bouquet:
    def __init__(self, flower_list):
        self.__flower_list = flower_list
        cost = sum(list(map(lambda flower: flower.cost, self.__flower_list)))
        print(f'The cost of the bouquet {cost}')

    def time_withering(self):
        sum_life_time = [flower.life_time for flower in self.__flower_list]
        return f'Average life time of a bouquet {round(sum(sum_life_time) / len(sum_life_time), 1)}'

    def freshness_sorting(self):
        self.__flower_list.sort(key=lambda flower: flower.freshness, reverse=True)
        return f'Flowers are sorted by freshness:\n{self.__flower_list}'

    def color_sorting(self):
        self.__flower_list.sort(key=lambda flower: flower.color.lower())
        return f'Flowers are sorted by color:\n{self.__flower_list}'

    def stem_sorting(self):
        self.__flower_list.sort(key=lambda flower: flower.stem)
        return f'Flowers are sorted by stem length:\n{self.__flower_list}'

    def cost_sorting(self):
        self.__flower_list.sort(key=lambda flower: flower.cost)
        return f'Flowers are sorted by cost:\n{self.__flower_list}'

    def search_by_color(self):
        user_color = input('Type the color name: ')
        search_result = list(filter(lambda flower: flower.color.lower() == user_color.lower(), self.__flower_list))
        return f'{user_color} flowers in the bouquet:\n{search_result}' if search_result \
            else f'There are no flowers with {user_color} color.'


flower_list1 = [
    Rose(1, True, 'Red', 10, 150),
    Tulip(4, False, 'yellow', 2, 100),
    Cornflake(5, True, 'blue', 11, 250)
]

bouquet = Bouquet(flower_list1)
print(bouquet.time_withering())
print(bouquet.freshness_sorting())
print(bouquet.color_sorting())
print(bouquet.stem_sorting())
print(bouquet.cost_sorting())
print(bouquet.search_by_color())
