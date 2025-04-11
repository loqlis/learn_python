# Задача:
# 1. Отсортировать устройства по category, затем по price внутри категории
# 2. Разбить устройства по категориям в словарь
# (категории зараннее неизвсетны!!!)
# 3. Для каждой категории вывести самое дешёвое устройство
# 4. Раздели устройства по ценовым группам:
# - < 600: "бюджетные"
# - 600–1000: "средний сегмент"
# - > 1000: "премиум"
#
# Итог:
# 1. Отсортировано по category, потом по price:
#
# [
#  {'id': 6, 'name': 'Asus ZenBook', 'category': 'laptop', 'price': 950},
#  {'id': 3, 'name': 'MacBook Air', 'category': 'laptop', 'price': 1200},
#  {'id': 5, 'name': 'Pixel 7', 'category': 'smartphone', 'price': 699},
#  {'id': 1, 'name': 'iPhone 13', 'category': 'smartphone', 'price': 999},
#  {'id': 4, 'name': 'iPad Mini', 'category': 'tablet', 'price': 500},
#  {'id': 2, 'name': 'Galaxy Tab S8', 'category': 'tablet', 'price': 850}
# ]
#
# 2. Группировка по категориям:
# {
#  'laptop': [
#    {'id': 3, 'name': 'MacBook Air', 'category': 'laptop', 'price': 1200},
#    {'id': 6, 'name': 'Asus ZenBook', 'category': 'laptop', 'price': 950}
#  ],
#  'smartphone': [
#    {'id': 1, 'name': 'iPhone 13', 'category': 'smartphone', 'price': 999},
#    {'id': 5, 'name': 'Pixel 7', 'category': 'smartphone', 'price': 699}
#  ],
#  'tablet': [
#    {'id': 4, 'name': 'iPad Mini', 'category': 'tablet', 'price': 500},
#    {'id': 2, 'name': 'Galaxy Tab S8', 'category': 'tablet', 'price': 850}
#  ]
# }
#
# 3. Самое дешёвое устройство в каждой категории:
# {
#     "laptop": {'id': 6, 'name': 'Asus ZenBook', 'category': 'laptop',
#                'price': 950},
#     "smartphone": {'id': 5, 'name': 'Pixel 7', 'category': 'smartphone',
#                    'price': 699},
#     "tablet": {'id': 4, 'name': 'iPad Mini', 'category': 'tablet',
#                'price': 500}
# }
#
# 4. Группировка по ценовым сегментам
# {
#   "бюджетные": [
#     {'id': 4, 'name': 'iPad Mini', 'category': 'tablet', 'price': 500}
#   ],
#   "средний сегмент": [
#     {'id': 5, 'name': 'Pixel 7', 'category': 'smartphone', 'price': 699},
#     {'id': 6, 'name': 'Asus ZenBook', 'category': 'laptop', 'price': 950},
#     {'id': 2, 'name': 'Galaxy Tab S8', 'category': 'tablet', 'price': 850},
#     {'id': 1, 'name': 'iPhone 13', 'category': 'smartphone', 'price': 999}
#   ],
#   "премиум": [
#     {'id': 3, 'name': 'MacBook Air', 'category': 'laptop', 'price': 1200}
#   ]
# }

from sort_utilities import (
    sort_category_price,
    group_categories,
    get_cheap_devices,
    get_segments
)

devices = [
    {"id": 1, "name": "iPhone 13", "category": "smartphone", "price": 999},
    {"id": 2, "name": "Galaxy Tab S8", "category": "tablet", "price": 850},
    {"id": 3, "name": "MacBook Air", "category": "laptop", "price": 1200},
    {"id": 4, "name": "iPad Mini", "category": "tablet", "price": 500},
    {"id": 5, "name": "Pixel 7", "category": "smartphone", "price": 699},
    {"id": 6, "name": "Asus ZenBook", "category": "laptop", "price": 950}
]


def main():
    print(
        f"Отсортированные по категориям и цене устройства: {sort_category_price(devices)}\n"
        f"Сгруппированные по категориям устройства: {group_categories(devices)}\n"
        f"Самые дешевые устройства в каждой категории: {get_cheap_devices(devices)}\n"
        f"Распределение устройств по ценовым сегментам: {get_segments(devices)}"
    )


if __name__ == "__main__":
    main()
