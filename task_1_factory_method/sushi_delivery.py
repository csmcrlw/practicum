""" Модуль, содержащий реализацию конкретных позиций меню """

from base import Sushi, SushiFactory


class Onigiri(Sushi):
    def prepare(self):
        print("Preparing Onigiri")

    def pack(self):
        print("Packing Onigiri")

    def deliver(self):
        print("Delivering Onigiri")


class MakiSushi(Sushi):
    def prepare(self):
        print("Preparing Maki Sushi")

    def pack(self):
        print("Packing Maki Sushi")

    def deliver(self):
        print("Delivering Maki Sushi")


class TempuraRoll(Sushi):
    def prepare(self):
        print("Preparing Tempura Roll")

    def pack(self):
        print("Packing Tempura Roll")

    def deliver(self):
        print("Delivering Tempura Roll")


class SpicyTunaRoll(Sushi):
    def prepare(self):
        print("Preparing Spicy Tuna Roll")

    def pack(self):
        print("Packing Spicy Tuna Roll")

    def deliver(self):
        print("Delivering Spicy Tuna Roll")


class OnigiriFactory(SushiFactory):
    def create_sushi(self):
        return Onigiri()


class MakiSushiFactory(SushiFactory):
    def create_sushi(self):
        return MakiSushi()


class TempuraRollFactory(SushiFactory):
    def create_sushi(self):
        return TempuraRoll()


class SpicyTunaRollFactory(SushiFactory):
    def create_sushi(self):
        return SpicyTunaRoll()
