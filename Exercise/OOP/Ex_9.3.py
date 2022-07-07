# 9.3. Пользователи: создайте класс с именем User. Создайте два атрибута first_name и last_
# name, а затем еще несколько атрибутов, которые обычно хранятся в профиле пользователя.
# Напишите метод describe_user(), который выводит сводку с информацией о пользователе.
# Создайте еще один метод greet_user() для вывода персонального приветствия для пользователя.
# Создайте несколько экземпляров, представляющих разных пользователей. Вызовите оба
# метода для каждого пользователя

# 9.5. Попытки входа: добавьте атрибут login_attempts в класс User из упражнения 9.3
# (с. 175). Напишите метод increment_login_attempts(), увеличивающий значение login_
# attempts на 1. Напишите другой метод с именем reset_login_attempts(), обнуляющий значение login_attempts.
# Создайте экземпляр класса User и вызовите increment_login_attempts() несколько раз.
# Выведите значение login_attempts, чтобы убедиться в том, что значение было изменено правильно, а затем вызовите reset_login_attempts(). Снова выведите login_attempts
# и убедитесь в том, что значение обнулилось.

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f'Имя:{self.first_name} Фамилия:{self.last_name}')

    def greet_user(self):
        print(f'Hello, {self.first_name} {self.last_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def eset_login_attempts(self):
        self.login_attempts = 0


user1 = User('Pasha', 'italic')
user2 = User('Alex', 'Prod')
user2.greet_user()
user1.greet_user()
user2.describe_user()
user1.describe_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.eset_login_attempts()
print(user1.login_attempts)
