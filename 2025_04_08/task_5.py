# Задача: отсортировать по абсолютному значению
# -> [0, -1, 2, -3, 5, -7]

def sort_abs(user_list: list) -> list:
    """
    Сортирует числа по абсолютному значению
    :param user_list:
    :return:
    """

    unsorted_list = user_list
    sorted_list = sorted(unsorted_list, key=abs)

    return sorted_list


numbers = [5, -3, -7, 2, 0, -1]


def main():
    print(sort_abs(numbers))


if __name__ == "__main__":
    main()
