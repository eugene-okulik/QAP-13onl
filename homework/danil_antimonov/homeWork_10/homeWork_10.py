# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов. Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам
# (например, по среднему времени жизни) (и это тоже метод).

class Flowers:
    def __init__(self, colour, long, freshness, price, lifetime):
        self.colour = colour
        self.long = long
        self.freshness = freshness
        self.price = price
        self.lifetime = lifetime


class Roses(Flowers):
    def __init__(self, colour, long, freshness, price, lifetime, spike: bool):
        self.spike = spike
        super().__init__(colour, long, freshness, price, lifetime)

    def __repr__(self):
        return repr((self.colour, self.long, self.freshness, self.price, self.lifetime, self.spike))


class Tulips(Flowers):
    def __init__(self, colour, long, freshness, price, lifetime, leaves: int):
        self.leaves = leaves
        super().__init__(colour, long, freshness, price, lifetime)

    def __repr__(self):
        return repr((self.colour, self.long, self.freshness, self.price, self.lifetime, self.leaves))


class Bouquet:
    def __init__(self, list_of_flowers: list):
        self.list_of_flowers = list_of_flowers
        calculatedprice = sum(list(map(lambda flower: flower.price, self.list_of_flowers)))
        print(f'Bouquet price {calculatedprice}')
        print(len(self.list_of_flowers))

    def lifetime(self):
        lifetime_bouquet = sum(list(map(lambda flower: flower.lifetime, self.list_of_flowers))) / len(
            self.list_of_flowers)
        return f'Bouquet lifetime is {round(lifetime_bouquet)} hours'

    def pricesort(self):
        sorted_by_price_flowers = sorted(self.list_of_flowers, key=lambda flower: flower.price)
        return print(f'Sorted prices for each flower in Bouquet, from lowest to highest:\n{sorted_by_price_flowers}')

    def coloursort(self):
        sorted_by_colour_flowers = sorted(self.list_of_flowers, key=lambda flower: flower.colour)
        return f'Sorted list of colours for each flower in Bouquet:\n{sorted_by_colour_flowers}'

    def sortbylength(self):
        sorted_by_length_flowers = sorted(self.list_of_flowers, key=lambda flower: flower.long)
        return f'Sorted length for each flower in Bouquet, from lowest to highest:\n{sorted_by_length_flowers}'

    def sortbyfreshness(self):
        sorted_by_freshness_flowers = sorted(self.list_of_flowers, key=lambda flower: flower.freshness)
        return f'Sorted freshness for each flower in Bouquet, from freshest:\n{sorted_by_freshness_flowers}'

    def search_by_price(self):
        flower_price = int(input('Type the price value: '))
        search_result = list(filter(lambda flower: flower.price == flower_price, self.list_of_flowers))
        return f'Flowers with price {flower_price} in the bouquet:\n{search_result}' if search_result \
            else f'There are no flowers with price {flower_price}.'


Rose = Roses('Red', 10, 'Fresh', 300, 24, True)
Tulip = Tulips('Yellow', 8, 'Not Fresh', 150, 48, 3)
Tulip1 = Tulips('White', 12, 'Medium Fresh', 180, 48, 1)
flowers_list = [Rose, Tulip, Tulip1]
bouqet1 = Bouquet(flowers_list)
print(bouqet1.lifetime())
bouqet1.pricesort()
print(bouqet1.coloursort())
print(bouqet1.sortbylength())
print(bouqet1.sortbyfreshness())
print(bouqet1.search_by_price())
