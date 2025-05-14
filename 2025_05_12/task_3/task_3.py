# Класс ReportGenerator для CSV-отчетов
#
# Контекст: Автоматизация отчетности.
#
# Задача:
# Создай класс ReportGenerator, который:
# - принимает список словарей (например, данные по продажам),
# - умеет сохранять их в CSV,
# - метод export_to(filename)
#
# Добавь опциональный параметр fields, чтобы указать, какие колонки сохранять

from report_generator import ReportGenerator

products = [
    {'product': 'Яблоко', 'price': 1.50, 'quantity': 100},
    {'product': 'Банан', 'price': 0.75, 'quantity': 150},
    {'product': 'Апельсин', 'price': 2.00, 'quantity': 80},
    {'product': 'Молоко', 'price': 3.50, 'quantity': 50},
    {'product': 'Хлеб', 'price': 2.75, 'quantity': 75}
]


def main():
    file_name = input('Введите имя файла с расширением csv: ')
    fields = input('Введите поля, которые хотите сохранить, если все - all: ')
    ex = ReportGenerator(products, fields)
    ex.export_to(file_name)


if __name__ == "__main__":
    main()
