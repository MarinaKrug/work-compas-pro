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
        self.Ex_privileges = Privileges()



class Privileges:
    def __init__(self):
        self.privileges =  ["разрешено добавлять сообщения", "разрешено удалять пользователей",
                           "разрешено банить пользователей"]

    def show_privileges(self):
        print(*self.privileges, sep=', ')