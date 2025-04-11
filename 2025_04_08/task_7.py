# Задача: сортировать слова по количеству гласных (по возрастанию)

def count_vowels(user_list: list) -> list:
    """
    Сортирует слова по количеству гласнх букв
    :param user_list:
    :return:
    """

    vowels = ['e', 'y', 'u', 'i', 'o', 'a']
    words_dict = {}
    for word in user_list:
        sum_vowels = 0
        for letter in word:
            if letter in vowels:
                sum_vowels += 1
        words_dict[word] = sum_vowels

    sorted_dict = sorted(words_dict.items(), key=lambda amount: amount[1])
    sorted_list = []
    for element in sorted_dict:
        sorted_list.append(element[0])

    return sorted_list


words = ["apple", "sky", "banana", "why", "orange"]


def main():
    print(count_vowels(words))


if __name__ == "__main__":
    main()
