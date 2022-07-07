# 9.12. Множественные модули: сохраните класс User в одном модуле, а классы Privileges
# и Admin в другом модуле. В отдельном файле создайте экземпляр Admin и вызовите метод
# show_privileges(), чтобы показать, что все работает правильно.
from other_users import Admin

admin_new = Admin('admin', 'Surname')
admin_new.Ex_privileges.show_privileges()