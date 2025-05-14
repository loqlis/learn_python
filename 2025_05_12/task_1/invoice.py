class Invoice:
    def __init__(self, products_list: list[dict]):
        self.products_list = products_list

    def add_date_and_status(self) -> list:
        """
        Добавляет дату и статусов товаров,
        если они не были внесены ранее.
        :return:
        """
        if not self.products_list[0].get('date'):
            date = input('Введите дату создания (год-месяц-день): ')
            self.products_list.insert(0, {
                'date': date
            })
        if not self.products_list[1].get('status'):
            self.products_list.insert(1, {
                'status': 'open'
            })

        return self.products_list

    def add_item(self) -> list | None:
        """
        Добавление товара в список.
        :return:
        """
        item = input('Введите товар, цену и количество: ').split()
        try:
            if item[0].isalpha() is False:
                raise ValueError
            float(item[1]),
            int(item[2])
        except ValueError:
            print('Ошибка ввода данных, товар не занесен в список.')
            return None

        if len(item) != 3:
            print('Ошибка ввода данных, товар не занесен в список.')
            return None

        products = [product['name'] for product in self.products_list if product.get('name')]
        if item[0] not in products:
            self.products_list.append({
                'name': item[0],
                'price': float(item[1]),
                'quantity': int(item[2])
            })

        return self.products_list

    def total_amount(self) -> float | int:
        """
        Считает общую выручку товаров.
        :return:
        """
        total = 0
        for item in self.products_list:
            if item.get("price") and item.get("quantity"):
                total += item.get("price") * item.get("quantity")

        return total

    def mark_paid(self) -> list:
        """
        Автоматичсеки изменяет статус товаров,
        если есть товары, которые в наличии.
        :return:
        """
        quantity = 0
        for item in self.products_list:
            if item.get('quantity'):
                quantity += item.get('quantity')

        if quantity > 0:
            self.products_list[1]['status'] = 'paid'
        else:
            self.products_list[1]['status'] = 'cancelled'

        return self.products_list
