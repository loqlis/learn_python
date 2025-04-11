# Задача: отсортировать слова по длине (короткие — сначала)


def sort_len(user_list: list) -> list:
    """
    Сортирует слова по длине
    :param user_list:
    :return:
    """

    sorted_list = sorted(user_list, key=len)
    return sorted_list


words = ["banana", "fig", "apple", "kiwi", "grapefruit"]


def main():
    print(sort_len(words))


if __name__ == "__main__":
    main()
