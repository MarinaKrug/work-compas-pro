#8.10. Отправка сообщений: начните с копии вашей программы из упражнения 8.9. Напишите функцию send_messages()
# , которая выводит каждое сообщение и перемещает его в новый список с именем sent_messages.
# После вызова функции выведите оба списка и убедитесь в том, что перемещение прошло успешно.


lst = ['hello', 'bye', 'good morning', 'good bye']
sent_message = []


def show_messages(roster, sent_mess):
    for i in range(len(roster)):
        elem = roster.pop()
        print(elem)
        sent_mess.append(elem)


show_messages(lst, sent_message)
print(sent_message)