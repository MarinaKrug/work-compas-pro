# 10.3. Гость: напишите программу, которая запрашивает у пользователя его имя. Введенный
# ответ сохраняется в файле с именем guest.txt.

name = input("Введите ваше имя")
with open('guest.txt', 'w') as txt:
    txt.write(name)
