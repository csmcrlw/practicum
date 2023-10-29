""" Создаем продавца """


class Seller:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def sell_product(self, product, quantity):
        print(f"{self.name} sells {quantity} pairs of {product}")
