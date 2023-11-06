class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name, self.price

    def __add__(self, other):
        return Food(other.name, other.price)


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def __str__(self):
        return self.name


restaurant1 = Restaurant("xy")

food1 = Food("1",100)
food2 = Food("2",200)
food3 = Food("3",300)


print(restaurant1)

