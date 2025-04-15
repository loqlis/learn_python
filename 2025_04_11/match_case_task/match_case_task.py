# Напишите программу, которая проверяет корректность логина и пароля и возвращает сообщение о результате проверки.
#
# # Условия:
# ## Проверка логина:
#
# - Логин должен быть не короче 3 символов.
# - Логин должен содержать только буквы латинского алфавита (a-z, A-Z), цифры (0-9) или символ подчеркивания (_).
# - Логин не должен начинаться с цифры.
# - Логин не должен быть уже занят, т. е. проверить его в "БД"
#
# ## Проверка пароля:
# - Пароль должен быть не короче 8 символов.
# - Пароль должен содержать:
# 1. хотя бы одну заглавную букву (A-Z),
# 2. хотя бы одну строчную букву (a-z),
# 3. хотя бы одну цифру (0-9).
# 4. Пароль не должен быть в списке слабых паролей (например, password123, qwerty, 12345678).
#
# Постарайся использовать `match case` для обработки данных, где это уместно и логично.
# При сохранении пароля в БД, хэшируй пароль
#
# ### Что я примерно хочу видеть:
# Можешь для валидации использовать `if-else`, но сопоставлении ошибок будет в `match-case`
#
# Cама валидация будет в `match-case`:
# ```python
# def validate_login(login: str) -> str:
#     match login:
#         case _ if len(login) < 3:
#             return "short"
# ...
# ```
#
# а далее проверка:
# ```python
# def register_user(login: str, password: str) -> None:
#     match validate_login(login):
#         case "short":
#             print("Логин слишком короткий.")
#             return
#         case "starts:
#             ...
# ```
#
# Либо пойти ещё дальше и создать отдельные словари с ошибками:
# ```python
# LOGIN_ERRORS = {
#     "short": "Логин должен быть не короче 3 символов.",
#     ...
#     "ok": "Логин корректный."
# }
# ```
#
# и вот такое сделать:
# ```python
# def register_user(login: str, password: str) -> str:
#     login_code = validate_login(login)
#     if login_code != "ok":
#         return LOGIN_ERRORS[login_code]
# ```

from check_utilities import register_user, hash_password
from check_utilities import database


def main():
    user_login = input('Введите логин: ')
    user_password = input('Введите пароль: ')
    register_user(user_login, user_password)
    database[user_login] = hash_password(user_password)


if __name__ == "__main__":
    main()
