def sort_salary(employees_data: list[dict]) -> list:
    """
    Сортирует сотрудников по убыванию зарплат
    :param employees_data:
    :return:
    """

    sorted_employees = sorted(employees_data, key=lambda item: item["salary"], reverse=True)

    return sorted_employees
