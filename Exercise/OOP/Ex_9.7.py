# 9.7. Администратор: администратор — особая разновидность пользователя. Напишите
# класс с именем Admin, наследующий от класса User из упражнения 9.3 или упражнения 9.5
# (с. 180). Добавьте атрибут privileges для хранения списка строк вида "разрешено добавлять
# сообщения", "разрешено удалять пользователей", "разрешено банить пользователей" и т. д." Напишите метод
# show_privileges() для вывода набора привилегий администратора. Создайте экземпляр Admin и вызовите свой метод.

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


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей",
                           "разрешено банить пользователей"]

    def show_privileges(self):
        print(*self.privileges, sep=', ')

admin = Admin("Alex", "Prid")
admin.show_privileges()