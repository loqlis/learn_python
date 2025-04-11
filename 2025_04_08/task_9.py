# Задача:
# 1. Отсортировать заказы сначала по имени пользователя, затем по дате
# 2. Для каждого пользователя посчитать сумму всех заказов
#
# 1. Итог сортировки:
# [
#  {'id': 101, 'user': 'Alice', 'total': 120.5, 'date': '2024-10-21'},
#  {'id': 103, 'user': 'Alice', 'total': 250.0, 'date': '2024-10-22'},
#  {'id': 102, 'user': 'Bob', 'total': 80.0, 'date': '2024-10-19'},
#  {'id': 104, 'user': 'Eve', 'total': 90.0, 'date': '2024-10-20'}
# ]
# 2. Итог по пользователям:
# {
#   "Alice": 370.50,
#   "Bob": 80.00,
#   "Eve": 90.00
# }

def sort_name_date(order_list: list[dict]) -> list:
    """
    Сортирует заказы по имени пользователя и дате
    """

    sorted_orders = sorted(order_list, key=lambda element: (element["user"], element["date"]))

    return sorted_orders


def count_user_sum(order_list: list[dict]) -> dict:
    """
    Считат сумму заказов каждого пользователя
    :param order_list:
    :return:
    """

    users_sum_dict = {}
    for order in order_list:
        if users_sum_dict.get(order["user"]):
            users_sum_dict[order["user"]].append(order["total"])
        else:
            users_sum_dict[order["user"]] = [order["total"]]

    for key, value in users_sum_dict.items():
        users_sum_dict[key] = sum(value)

    return users_sum_dict


orders = [
    {"id": 101, "user": "Alice", "total": 120.50, "date": "2024-10-21"},
    {"id": 102, "user": "Bob", "total": 80.00, "date": "2024-10-19"},
    {"id": 103, "user": "Alice", "total": 250.00, "date": "2024-10-22"},
    {"id": 104, "user": "Eve", "total": 90.00, "date": "2024-10-20"}
]


def main():
    print(
        f"Заказы, отсортированные по пользователю и дате: {sort_name_date(orders)}\n"
        f"Сумма заказов каждого пользователя: {count_user_sum(orders)}"
    )


if __name__ == "__main__":
    main()
