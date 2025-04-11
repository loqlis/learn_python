def group_categories(device_list: list[dict]) -> dict:
    """
    Группирует устройства по категориям
    """
    sorted_list = sorted(device_list, key=lambda element: (element['category'], element['price']))
    categories = list(sorted({element["category"] for element in device_list}))

    grouped_dict = {}
    for category in categories:
        grouped_dict[category] = []
        for element in sorted_list:
            if element["category"] == category:
                grouped_dict[category].append(element)

    return grouped_dict
