# Контекст: Вы автоматизируете учёт заказов для интернет-магазина.
#
# Задача:
# Создай класс Invoice:
# - список товаров (каждый товар — словарь с name, price, quantity),
# - дата создания,
# - статус счета: open, paid, cancelled.
#
# Методы:
# - add_item(name, price, quantity),
# - total_amount() — возвращает общую сумму,
# - mark_paid() — меняет статус на paid, но только если есть товары

from invoice import Invoice

products = [
    {'product': 'Яблоко', 'price': 1.50, 'quantity': 100},
    {'product': 'Банан', 'price': 0.75, 'quantity': 150},
    {'product': 'Апельсин', 'price': 2.00, 'quantity': 80},
    {'product': 'Молоко', 'price': 3.50, 'quantity': 50},
    {'product': 'Хлеб', 'price': 2.75, 'quantity': 75}
]


def main():
    invoice_ex = Invoice(products)
    invoice_ex.add_date_and_status()
    invoice_ex.add_item()
    invoice_ex.mark_paid()
    print(f"Список товаров: {products}\n"
          f"Общая сумма: {invoice_ex.total_amount()}")


if __name__ == "__main__":
    main()
