def find_experienced_employees(employees_data: list[dict]) -> list:
    """
    Определяет топ 5 самых опытных сотрдников
    :param employees_data:
    :return:
    """

    experience_sort = sorted(employees_data, key=lambda item: item["experience"], reverse=True)
    much_experience = []
    for employee in experience_sort:
        much_experience.append(employee['name'])
        if len(much_experience) == 5:
            break

    return much_experience
