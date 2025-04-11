def sort_category_price(device_list: list[dict]) -> list:
    """
    Сортирует устройства по категории и цене
    """
    sorted_list = sorted(device_list, key=lambda element: (element['category'], element['price']))

    return sorted_list
