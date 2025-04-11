# Задача:
# 1. Отсортируй по возрастанию
# 2. Отсортируй по убыванию

def sort_list(user_list: list) -> None:
    """
    Сортирует слова по возрастанию и убыванию
    :param user_list:
    :return:
    """

    increase_list = sorted(user_list)
    print(increase_list)

    decrease_list = sorted(user_list, reverse=True)
    print(decrease_list)


numbers = [4, 1, 7, 3, 9, 2]


def main():
    sort_list(numbers)


if __name__ == "__main__":
    main()
