# 11.3. Работник: напишите класс Employee, представляющий работника. Метод __init__()
# должен получать имя, фамилию и ежегодный оклад; все эти значения должны сохраняться
# в атрибутах. Напишите метод give_raise(), который по умолчанию увеличивает ежегодный оклад на $5000
# — но при этом может получать другую величину прибавки.
# Напишите тестовый сценарий для Employee. Напишите два тестовых метода, test_give_
# default_raise() и test_give_custom_raise(). Используйте метод setUp(), чтобы вам не
# приходилось заново создавать экземпляр Employee в каждом тестовом метода. Запустите
# свой тестовый сценарий и убедитесь в том, что оба теста прошли успешно
import unittest


class Employee:
    def __init__(self, name, lastname, salary):
        self.name = name
        self.lastname = lastname
        self.salary = salary

    def give_raise(self, increase=5000):
        self.salary += int(increase)


class TestAnonmyousSurvey(unittest.TestCase):
    """Тесты для класса Employee"""
    def setUp(self):
        """
        Создание экземпляра класса Employee
        """
        self.my_survey = Employee('Антон', 'Антонов', 5000)
    def test_giv_default_raise(self):
        """Проверяет, что оклад увеличивается на дефолтное значение"""
        val_salary = self.my_survey.salary
        self.my_survey.give_raise()
        new_value = self.my_survey.salary
        self.assertEqual(int(val_salary) + 5000, new_value)

    def test_giv_default_raise(self):
        """Проверяет, что оклад увеличивается на дефолтное значение"""
        val_salary = self.my_survey.salary
        self.my_survey.give_raise()
        new_value = self.my_survey.salary
        self.assertEqual(int(val_salary) + 5000, new_value)

    def test_give_custom_raise(self):
        """Проверяет, что с заданным значением оклад увеличивается"""
        val_salary = self.my_survey.salary
        self.my_survey.give_raise(2000)
        new_salary = self.my_survey.salary
        self.assertEqual(int(val_salary) + 2000, new_salary)

if __name__ == '__main__':
    unittest.main()
