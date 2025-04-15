import hashlib

from .validate_login import validate_login
from .validate_password import validate_password


def register_user(login: str, password: str) -> None:
    match validate_login(login):
        case 'short':
            print('Логин слишком короткий.')
        case 'starts':
            print('Логин не может начинаться с цифры.')
        case 'authorized':
            print('Такой логин уже существует.')
        case 'symbol':
            print('В логине использованы недопустимые символы.')
        case _:
            print('Логин корректный.')

    match validate_password(password):
        case 'short':
            print('Пароль слишком короткий.')
        case 'symbol':
            print(
                'Пароль не удовляетворяет требованиям.'
                'Используйте строчные и прописные буквы, цифры.'
            )
        case 'weak':
            print('Пароль небезопасен.')
        case _:
            print('Пароль корректный')


def hash_password(password: str) -> str:
    hashed_password = hashlib.sha256(password.encode())
    hashed_password = hashed_password.hexdigest()

    return hashed_password
