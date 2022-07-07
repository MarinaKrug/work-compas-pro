# 9.1. Ресторан: создайте класс с именем Restaurant. Метод __init__() класса Restaurant
# должен содержать два атрибута: restaurant_name и cuisine_type. Создайте метод describe_
# restaurant(), который выводит два атрибута, и метод open_restaurant(), который выводит
# сообщение о том, что ресторан открыт.
# Создайте на основе своего класса экземпляр с именем restaurant. Выведите два атрибута
# по отдельности, затем вызовите оба метода.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type, sep=':')

    def open_restaurant(self):
        print('Ресторан открыт')


restaurant = Restaurant('Якитория', 'японская')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

