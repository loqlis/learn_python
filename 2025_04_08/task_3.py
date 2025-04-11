# Задача: отсортировать пользователей по возрасту

def sort_age(user_list: list[dict]) -> list:
    """
    Сортирует пользователей по возрасту
    :param user_list:
    :return:
    """

    sorted_list = sorted(user_list, key=lambda item: item["age"])

    return sorted_list


users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 24},
    {"name": "Charlie", "age": 28},
    {"name": "Mary", "age": 35}
]


def main():
    print(sort_age(users))


if __name__ == "__main__":
    main()
