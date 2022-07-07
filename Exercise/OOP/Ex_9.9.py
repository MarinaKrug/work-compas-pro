# 9.9. Обновление аккумулятора: используйте окончательную версию программы electric_
# car.py из этого раздела. Добавьте в класс Battery метод с именем upgrade_battery(). Этот
# метод должен проверять размер аккумулятора и устанавливать мощность равной 100, если
# она имеет другое значение. Создайте экземпляр электромобиля с аккумулятором по умолчанию, вызовите get_range(), а затем вызовите get_range() во второй раз после вызова
# upgrade_battery(). Убедитесь в том, что запас хода увеличился
class Car():
     """Простая модель автомобиля."""
     def __init__(self, make, model, year):
         self.make = make
         self.model = model
         self.year = year
         self.odometer_reading = 0
     def get_descriptive_name(self):
         long_name = f"{self.year} {self.manufacturer} {self.model}"
         return long_name.title()
     def read_odometer(self):
         print(f"This car has {self.odometer_reading} miles on it.")
     def update_odometer(self, mileage):
         if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
         else:
            print("You can't roll back an odometer!")
     def increment_odometer(self, miles):
         self.odometer_reading += miles
class Battery():
    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            self.range = 260
        elif self.battery_size == 100:
            self.range = 315

        print(f"This car can go about {self.range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100



class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля.
        """
        super().__init__(make, model, year)
        self.battery = Battery()




car = ElectricCar('Citroen', 'C4', 2000)
car.battery.get_range()
car.battery.upgrade_battery()
car.battery.get_range()

