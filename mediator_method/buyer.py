""" Создаем покупателя и заявку на покупку """


class Buyer:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def request_purchase(self, product, quantity):
        print(f"{self.name} requests to purchase {quantity} pairs of {product}")
        self.mediator.process_purchase_request(self, product, quantity)

    def receive_confirmation(self, product, quantity):
        print(f"{self.name} receives confirmation of the purchase of {quantity} pairs of {product}")
