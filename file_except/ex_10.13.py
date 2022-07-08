 #10.13. Проверка пользователя: последняя версия remember_me.py предполагает, что пользователь
 # либо уже ввел свое имя, либо программа выполняется впервые. Ее нужно изменить на тот случай,
 # если текущий пользователь не является тем человеком, который последним использовал программу.
# Прежде чем выводить приветствие в greet_user(), спросите, правильно ли определено имя
# пользователя. Если ответ будет отрицательным, вызовите get_new_username() для получения правильного имен

import json

def greet_user():
     """Приветствует пользователя по имени."""
     filename = 'username.json'
     try:
         with open(filename) as f:
             username = json.load(f)
     except FileNotFoundError:
         username = input("What is your name? ")
         with open(filename, 'w') as f:
             json.dump(username, f)
             print(f"We'll remember you when you come back, {username}!")
     else:
        print(f"Welcome back, {username}!")



def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")



def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
    print(f"We'll remember you when you come back, {username}!")

#Прежде чем выводить приветствие в greet_user(), спросите, правильно ли определено имя
# пользователя. Если ответ будет отрицательным, вызовите get_new_username() для получения правильного имен

print("Ваше имя", get_stored_username())
answer = input("введите ответ: yes/no")
if answer == 'no':
    get_new_username()

else:
    greet_user()