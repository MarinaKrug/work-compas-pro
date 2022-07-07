
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type, sep=':')

    def open_restaurant(self):
        print('Ресторан открыт')

# 9.2. Три ресторана: начните с класса из упражнения 9.1. Создайте три разных экземпляра,
# вызовите для каждого экземпляра метод describe_restaurant().
restaurant1 = Restaurant('Pizza', 'italic')
restaurant2 = Restaurant('France', 'француская')
restaurant3 = Restaurant('Причал', 'русская')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()