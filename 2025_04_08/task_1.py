# Задача:
# 1. Отсортируй по возрастанию
# 2. Отсортируй по убыванию

numbers = [4, 1, 7, 3, 9, 2]


def main():
    increase_list = sorted(numbers)
    print(increase_list)

    decrease_list = sorted(numbers, reverse=True)
    print(decrease_list)


if __name__ == "__main__":
    main()
