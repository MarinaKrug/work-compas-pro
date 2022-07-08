# 11.2. Население: измените свою функцию так, чтобы у нее был третий обязательный параметр —
# население. В новой версии функция должна возвращать одну строку вида «Santiago,
# Chile — population 5 000 000». Снова запустите программу test_cities.py. Убедитесь в том,
# что тест test_city_country() на этот раз не проходит. Измените функцию так, чтобы параметр населения
# стал необязательным. Снова запустите test_cities.py и убедитесь в том, что тест test_city_country()
# снова проходит успешно. Напишите второй тест city_country_population(), который проверяет вызов функции со значениями
# 'santiago', 'chile' и 'population=5000000'. Снова запустите test_cities.
# py и убедитесь в том, что новый тест проходит успешно


import unittest
from city_functions import get_city_country


class CityTestCase(unittest.TestCase):
    """Тесты для 'city_functions'."""
    def test_city_country(self):
        """проверка, что города такие как 'santiago' и 'chile' работают правильно?"""
        formatted_name = get_city_country('chile', 'santiago')
        self.assertEqual(formatted_name, 'Santiago, Chile')
    def test_city_country_population(self):
        """Проверка, что с параметрами 'santiago', 'chile' и 'population=5000000' функция работает правильно"""
        formatted_name = get_city_country('chile', 'santiago', population=5000000)
        self.assertEqual(formatted_name, "Santiago, Chile, 5000000")




if __name__ == '__main__':
    unittest.main()