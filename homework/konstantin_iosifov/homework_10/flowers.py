class Flower:
    def __init__(self, name, price, freshness, long_flower, life_long):
        self.name = name
        self.price = price
        self.freshness = freshness
        self.long_flower = long_flower
        self.life_long = life_long

    def get_freshness(self):
        return self.freshness

    def get_lifespan(self):
        return self.life_long

    def get_stem_length(self):
        return self.long_flower

    def get_price(self):
        return self.price


class Rose(Flower):
    def __init__(self, color, price, freshness, long_flower, life_long):
        name = f"Rose - {color}"
        super().__init__(name, price, freshness, long_flower, life_long)
        self.color = color


class Tulip(Flower):
    def __init__(self, color, price, freshness, long_flower, life_long, kind):
        name = f"Tulip - {color}"
        super().__init__(name, price, freshness, long_flower, life_long)
        self.kind = kind
        self.color = color


class Lily(Flower):
    def __init__(self, color, price, freshness, long_flower, life_long, aroma):
        name = f"Lily - {color}"
        super().__init__(name, price, freshness, long_flower, life_long)
        self.aroma = aroma
        self.color = color


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def get_price(self):
        return sum([f.get_price() for f in self.flowers])

    def get_average_life_long(self):
        return sum([f.get_life_long() for f in self.flowers]) / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda f: f.get_freshness())

    def sort_by_color(self):
        self.flowers.sort(key=lambda f: f.color)

    def sort_by_long_flower(self):
        self.flowers.sort(key=lambda f: f.get_long_flower())

    def sort_by_price(self):
        self.flowers.sort(key=lambda f: f.get_price())

    def search_by_life_long(self, life_long):
        return [f for f in self.flowers if f.get_life_long() == life_long]


rose1 = Rose("red", 10, 80, 30, 5)
rose2 = Rose("pink", 12, 90, 35, 7)
tulip = Tulip("yellow", 8, 70, 25, 1, "Rembrandt")
lily = Lily("white", 7, 75, 22, 2, "Stargazer")

flowers = [rose1, rose2, tulip, lily]
bouquet = Bouquet(flowers)

for flower in bouquet.flowers:
    print(flower.name)
    print("Price -", flower.price)
    print("Freshness -", flower.freshness)
    print("Long_Flower -", flower.long_flower)
    print("Life_Long -", flower.life_long)
    print("\n")

print("Total Price Bouquet =", bouquet.get_price())
