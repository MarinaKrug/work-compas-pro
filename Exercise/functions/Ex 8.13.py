# 8.13. Профиль: начните с копии программы user_profile.py (с. 162). Создайте собственный
# профиль вызовом build_profile(), укажите имя, фамилию и три другие пары «ключзначение» для вашего описания.
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


profile = build_profile('mary', 'einstein', age='11',
                        hobby='read')
print(profile)