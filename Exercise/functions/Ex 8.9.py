# 8.9. Сообщения: создайте список с серией коротких сообщений. Передайте список функции show_messages(),
# которая выводит текст каждого сообщения в списке.

lst = ['hello', 'bye', 'good morning', 'good bye']


def show_messages(roster):
    for i in roster:
        print(i)


show_messages(lst)
