# 10.9. Ошибки без уведомления: измените блок except из упражнения 10.8 так, чтобы при
# отсутствии файла программа продолжала работу, не уведомляя пользователя о проблеме.

with open("../cats.txt", 'w') as f, open('dogs.txt', 'w') as dog:
    f.write('Murka\tMurzik\tVaska')
    dog.write('Rex\tTuzik\tKnopka')

try:
    with open("cats.txt") as f, open('dogs.txt') as dog:
        pass
except FileNotFoundError:
    pass
