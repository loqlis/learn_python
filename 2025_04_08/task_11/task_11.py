# Задача:
# 1. Сортировка сотрудников по зарплате(salary) (по убыванию)
# 2. Сортировка по опыту(experience) (по возрастанию)
# 3. Сортировка по отделу(department), а внутри — по зарплате(salary)
# 4. Топ-5 самых опытных сотрудников(experience)

import random
from sort_utilities import (
    sort_salary,
    sort_experience,
    sort_department_salary,
    find_experienced_employees
)


def generate_employees() -> list:
    """
    Генерирует список сотрудников
    (всегда рандомные данные о сотрудниках)
    """
    random.seed(42)

    names = [
        "Alice", "Bob", "Charlie", "Diana",
        "Eve", "Frank", "Grace", "Heidi",
        "Ivan", "Judy"
    ]
    departments = ["HR", "Engineering", "Sales", "Marketing", "Finance"]

    employees = [
        {
            "id": i,
            "name": random.choice(names),
            "department": random.choice(departments),
            "salary": random.randint(40000, 120000),
            "experience": round(random.uniform(1.0, 10.0), 1)
        }
        for i in range(50)
    ]

    return employees


def main():
    employees = generate_employees()
    print(
        f"Сортировка сотрудников по убыванию зарплаты: {sort_salary(employees)}\n"
        f"Сортировка сотрудников по воззрастанию опыта: {sort_experience(employees)}\n"
        f"Сортировка отдела и зарплат в нем: {sort_department_salary(employees)}\n"
        f"Топ 5 самых опытных сотрудников: {find_experienced_employees(employees)}"
    )


if __name__ == "__main__":
    main()
