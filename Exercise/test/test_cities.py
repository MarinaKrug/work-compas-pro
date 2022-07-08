import unittest
from city_functions import get_city_country

class CityTestCase(unittest.TestCase):
    """Тесты для 'city_functions'."""
    def test_city_country(self):
        """проверка, что города такие как 'santiago' и 'chile' работают правильно?"""
        formatted_name = get_city_country('chile', 'santiago')
        self.assertEqual(formatted_name, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()