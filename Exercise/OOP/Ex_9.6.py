# 9.6. Киоск с мороженым: киоск с мороженым — особая разновидность ресторана. Напишите класс IceCreamStand,
# наследующий от класса Restaurant из упражнения 9.1 (с. 175) или упражнения 9.4 (с. 180).
# Подойдет любая версия класса; просто выберите ту, которая вам больше нравится.
# Добавьте атрибут с именем flavors для хранения списка сортов мороженого. Напишите метод, который выводит
# этот список. Создайте экземпляр IceCreamStand
# и вызовите этот метод.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type, sep=':')

    def open_restaurant(self):
        print('Ресторан открыт')

class  IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print(*self.flavors)

IceCr = IceCreamStand("Мороженое", "Russia")
# IceCr.flavors.append('Ванильное')
IceCr.show_flavors()