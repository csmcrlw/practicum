""" Основной модуль, использующий фабричный метод """

from sushi_delivery import OnigiriFactory, MakiSushiFactory, TempuraRollFactory, SpicyTunaRollFactory


def main():
    onigiri_factory = OnigiriFactory()
    onigiri_sushi = onigiri_factory.create_sushi()
    onigiri_sushi.prepare()
    onigiri_sushi.pack()
    onigiri_sushi.deliver()

    maki_factory = MakiSushiFactory()
    maki_sushi = maki_factory.create_sushi()
    maki_sushi.prepare()
    maki_sushi.pack()
    maki_sushi.deliver()

    tempura_factory = TempuraRollFactory()
    tempura_roll = tempura_factory.create_sushi()
    tempura_roll.prepare()
    tempura_roll.pack()
    tempura_roll.deliver()

    spicy_tuna_factory = SpicyTunaRollFactory()
    spicy_tuna_roll = spicy_tuna_factory.create_sushi()
    spicy_tuna_roll.prepare()
    spicy_tuna_roll.pack()
    spicy_tuna_roll.deliver()


if __name__ == "__main__":
    main()
