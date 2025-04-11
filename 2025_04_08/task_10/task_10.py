# Задача:
# 1. Отсортировать действия по времени, сгруппировать по пользователю
# 2. Найти, сколько раз каждый пользователь логинился
#
# Итог:
# 1. Сортировка по времени:
# [
#  {'user': 'Bob', 'action': 'login', 'time': '2024-10-21 09:00'},
#  {'user': 'Bob', 'action': 'logout', 'time': '2024-10-21 09:30'},
#  {'user': 'Anna', 'action': 'login', 'time': '2024-10-21 10:00'},
#  {'user': 'Anna', 'action': 'logout', 'time': '2024-10-21 11:00'},
#  {'user': 'Anna', 'action': 'login', 'time': '2024-10-22 08:00'}
# ]
#
# 2. Кол-во логинов:
# {
#   "Anna": 2,
#   "Bob": 1
# }

from utilities import (
    sort_time,
    group_user,
    count_logins
)

logs = [
    {"user": "Anna", "action": "login", "time": "2024-10-21 10:00"},
    {"user": "Anna", "action": "logout", "time": "2024-10-21 11:00"},
    {"user": "Bob", "action": "login", "time": "2024-10-21 09:00"},
    {"user": "Anna", "action": "login", "time": "2024-10-22 08:00"},
    {"user": "Bob", "action": "logout", "time": "2024-10-21 09:30"}
]


def main():
    print(
        f"Сортировка действий по времени: {sort_time(logs)}\n"
        f"Группировка действий по пользователю: {group_user(logs)}\n"
        f"Количество входов каждого пользователя: {count_logins(logs)}"
    )


if __name__ == "__main__":
    main()
