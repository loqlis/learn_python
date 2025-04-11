def sort_department_salary(employees_data: list[dict]) -> dict:
    """
    Сортирует отделы и сотрудников в них по зарплате
    :param employees_data:
    :return:
    """

    department_dict = {}
    sorted_salary = sorted(employees_data, key=lambda item: (item["department"], item["salary"]))
    for employee in sorted_salary:
        if department_dict.get(employee['department']):
            department_dict[employee['department']].append(employee)
        else:
            department_dict[employee['department']] = [employee]

    return department_dict
