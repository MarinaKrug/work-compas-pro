# 10.2. Изучение C: метод replace() может использоваться для замены любого слова в строке другим словом. В следующем примере слово 'dog' заменяется словом 'cat':
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# Прочитайте каждую строку из только что созданного файла learning_python.txt и замените
# слово Python названием другого языка, например C. Выведите каждую измененную строку
# на экран

with open('learning_python.txt') as file:
    for line in file:
        print(line.replace('Python', 'C').strip())

