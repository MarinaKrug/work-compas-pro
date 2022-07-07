# 9.11. Импортирование класса Admin: начните с версии класса из упражнения 9.8 (с. 186).
# Сохраните классы User, Privileges и Admin в одном модуле. Создайте отдельный файл, создайте экземпляр
# Admin и вызовите метод show_privileges(), чтобы показать, что все работает правильно.


from users import *

admin_new = Admin('admin', 'Surname')
admin_new.Ex_privileges.show_privileges()