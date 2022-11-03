from product import Product


class Drink(Product):
    QUANTITY = 10

    def __init__(self, name: str):
        super(Drink, self).__init__(name, quantity=Drink.QUANTITY)

