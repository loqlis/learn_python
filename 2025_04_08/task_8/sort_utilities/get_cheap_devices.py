from .group_categories import group_categories


def get_cheap_devices(device_list: list[dict]) -> dict:
    """
    Определяет самое дешевое устройство
    в каждой категории
    """

    category_dict = group_categories(device_list)
    cheap_device_dict = {}
    for key, value in category_dict.items():
        for device in value:
            if not cheap_device_dict.get(key):
                cheap_device_dict[key] = device

    return cheap_device_dict
