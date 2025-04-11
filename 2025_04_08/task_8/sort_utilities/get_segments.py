def get_segments(device_list: list[dict]) -> dict:
    """
    Распределяет устройства по 3 ценовым сегментам:
    бюджетные, средний сегмент и премиум устройства
    """
    sorted_list = sorted(device_list, key=lambda element: element['price'])

    segment_dict = {'бюджетные': [], 'средний сегмент': [], 'премиум': []}
    for device in sorted_list:
        if device['price'] < 600:
            segment_dict['бюджетные'].append(device)
        elif 600 <= device['price'] < 1000:
            segment_dict['средний сегмент'].append(device)
        else:
            segment_dict['премиум'].append(device)

    return segment_dict
