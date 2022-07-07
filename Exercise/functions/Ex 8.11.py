# 8.11. Архивированные сообщения: начните с программы из упражнения 8.10. Вызовите
# функцию send_messages() для копии списка сообщений. После вызова функции выведите
# оба списка и убедитесь в том, что в исходном списке остались все сообщения.
lst = ['hello', 'bye', 'good morning', 'good bye']
sent_message = []


def show_messages(roster, sent_mess):
    for i in range(len(roster)):
        elem = roster.pop()
        print(elem)
        sent_mess.append(elem)


show_messages(lst[:], sent_message)
print(sent_message)
print(lst)
