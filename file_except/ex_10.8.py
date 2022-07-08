# 10.8. Кошки и собаки: создайте два файла с именами cats.txt и dogs.txt.
# Сохраните по крайней мере три клички кошек в первом файле и три клички собак во втором.
# Напишите программу, которая пытается прочитать эти файлы и выводит их содержимое на экран.
# Заключите свой код в блок try-except для перехвата исключения FileNotFoundError и вывода
# понятного сообщения об отсутствии файла. Переместите один из файлов в другое место
# файловой системы; убедитесь в том, что код блока except выполняется как положено.

with open("../cats.txt", 'w') as f, open('dogs.txt', 'w') as dog:
    f.write('Murka\tMurzik\tVaska')
    dog.write('Rex\tTuzik\tKnopka')

try:
    with open("cats.txt") as f, open('dogs.txt') as dog:
        pass
except FileNotFoundError:
    print("запрошенный файл отсутствует")
