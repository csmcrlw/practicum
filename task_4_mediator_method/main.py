from buyer import Buyer
from seller import Seller
from purchase_mediator import PurchaseMediator


def main():
    # Создаем посредников
    mediator = PurchaseMediator()
    mediator_without_sellers = PurchaseMediator()

    # Создаем покупателей и продавца, связываем их с посредником
    buyer1 = Buyer("Steve", mediator)
    buyer2 = Buyer("Kanye", mediator)
    buyer3 = Buyer("Bob", mediator_without_sellers)
    seller = Seller("Sneakers Store", mediator)

    mediator.add_buyer(buyer1)
    mediator.add_buyer(buyer2)
    mediator.set_seller(seller)

    mediator_without_sellers.add_buyer(buyer3)

    # Покупатели создают заявки на покупку кроссовок
    buyer1.request_purchase("New Balance 992", 2)
    buyer2.request_purchase("Adidas Yeezy Boost 350 V2", 1)
    buyer3.request_purchase("Nike Air Force", 3)


if __name__ == "__main__":
    main()
