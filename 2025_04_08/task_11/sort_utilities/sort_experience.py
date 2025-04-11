def sort_experience(employees_data: list[dict]) -> list:
    """
    Сортирует сотрудников по возрастанию опыта
    :param employees_data:
    :return:
    """

    sorted_employees = sorted(employees_data, key=lambda item: item["experience"])

    return sorted_employees
