# # ✅ Техническое задание
#
# ## 📌 Название: `gh-info`: CLI-инструмент для анализа GitHub-репозитория
#
# ---
#
# ## 1. 📍 Цель проекта
#
# Разработать утилиту командной строки, которая по названию публичного GitHub-репозитория получает и выводит три ключевых
# метрики:
#
# * ⭐ Количество звёзд (stars)
# * 🍴 Количество форков (forks)
# * 🐞 Количество открытых issues (open issues)
#
# ---
#
# ## 2. 🛠️ Функциональные требования
#
# ### 2.1 Аргументы командной строки:
#
# CLI-инструмент должен принимать следующие параметры:
#
# * `--repo` (или `-r`): обязательный аргумент в формате `owner/repo` (например, `pallets/flask`)
#
# Пример запуска:
#
# ```bash
# python gh_info.py --repo "pallets/flask"
# ```
#
# ### 2.2 Получение данных:
#
# * Инструмент делает HTTP-запрос к GitHub REST API:
#
#   ```
#   GET https://api.github.com/repos/<owner>/<repo>
#   ```
# * Из ответа извлекаются следующие поля:
#
#     * `stargazers_count`
#     * `forks_count`
#     * `open_issues_count`
#
# ### 2.3 Вывод:
#
# * Информация должна выводиться в человекочитаемом виде:
#
# Пример:
#
# ```
# 📊 GitHub Repo: pallets/flask
# ⭐ Stars: 64000
# 🍴 Forks: 15000
# 🐞 Open Issues: 532
# ```
#
# ---
#
# ## 3. 💡 Нефункциональные требования
#
# * Код должен быть написан на Python 3.8+
# * Используемые библиотеки:
#
#     * `requests` — для HTTP-запросов
#     * `argparse` (или `typer`) — для CLI (на выбор)
# * Код структурирован: выделена функция/класс, отвечающая за API-запрос
#
# ---
#
# ## 4. ⚠️ Обработка ошибок
#
# Программа должна корректно обрабатывать следующие ситуации:
#
# | Ошибка                          | Сообщение в консоль                |
# |---------------------------------|------------------------------------|
# | Неверный формат репозитория     | ❌ Repo format must be "owner/repo" |
# | Репозиторий не существует (404) | ❌ Repository not found             |
# | Превышен лимит запросов (403)   | ❌ Rate limit exceeded              |
# | Проблемы с интернетом / API     | ❌ Failed to connect to GitHub API  |
#
# ---
#
# ## 5. 🧪 Критерии приёмки
#
# | Критерий                              | Да/Нет |
# |---------------------------------------|--------|
# | CLI принимает аргумент `--repo`       | ✅      |
# | Запрашивает данные с GitHub API       | ✅      |
# | Выводит нужные метрики                | ✅      |
# | Обрабатывает ошибки                   | ✅      |
# | Код оформлен в виде классов и функций | ✅      |
#
# ---
#
# ## 6. 🔄 Возможные улучшения (по желанию)
#
# * 📁 Экспорт результата в JSON или Markdown (`--output`)
# * 🔍 Поддержка нескольких реп (через файл со списком)
#
# ---
#
# ## 7. 🧱 Пример структуры проекта (базовая, можно и другую)
#
# ```
# gh_info/
# ├── gh_info.py         # Основной файл CLI
# ├── github_api.py      # Класс/функция для работы с API
# ├── exceptions.py      # (опц.) собственные ошибки
# └── README.md          # Инструкция по использованию
# ```
#
# ---
#
# ## 8. 🚀 Как запускать
#
# ```bash
# python gh_info.py --repo "torvalds/linux"
# ```
#
# Пример вывода:
#
# ```
# 📊 GitHub Repo: torvalds/linux
# ⭐ Stars: 160000
# 🍴 Forks: 42000
# 🐞 Open Issus: 602
# ```
# import json
#
# import requests
# rep = requests.get('https://github.com/loqlis/learn_python')
# with open('rep.json', 'w') as f:
#      json.dumps(rep)

# def main():
#     pass
#
# if __name__ == '__main__':
#     pass

import requests

# Имя человека на GitHub
owner: str = "loqlis"
# Название репозитория
repo: str = "learn_python"
# Устанавливает url
url = f"https://api.github.com/repos/{owner}/{repo}"
# Передаем заголовки для запроса
headers = {
    "Content-Type": "application/json",
}
# Выполняем запрос
response = requests.get(url, headers=headers)
# Получаем ответ
data = response.json()

print(data.get("stargazers_count"))
print(data.get("forks_count"))
print(data.get("open_issues_count"))
