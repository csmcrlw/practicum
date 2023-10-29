""" Создаем посредника, через которого происходит связь между покупателем и продавцом """


class PurchaseMediator:
    def __init__(self):
        self.buyers = []
        self.seller = None

    def add_buyer(self, buyer):
        self.buyers.append(buyer)

    def set_seller(self, seller):
        self.seller = seller

    def process_purchase_request(self, buyer, product, quantity):
        if self.seller:
            self.seller.sell_product(product, quantity)
            buyer.receive_confirmation(product, quantity)
            self.buyers.remove(buyer)  # Убираем пользователя после завершения сделки
            print()
        else:
            print("Error: No seller available!")
