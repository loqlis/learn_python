# Задача: отсортировать слова по последней букве

def get_last_letter(user_list: list) -> list:
    """
    определяет последние буквы каждого слова
    :param user_list:
    :return:
    """

    letter_list = sorted([element[-1] for element in user_list])

    return letter_list


words = ["apple", "banana", "cherry", "date"]


def main():
    get_last_letter(words)
    print(sorted(words, key=get_last_letter))


if __name__ == "__main__":
    main()
