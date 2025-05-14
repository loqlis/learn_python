class LogParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_file(self) -> list:
        """
        Чтение файла, переданного классу.
        :return:
        """
        with open(self.file_path) as f:
            return f.readlines()

    def get_all_entries(self) -> list:
        """
        Преобразовывает переданные логи в список словарей.
        :return:
        """
        lines = [line.split(',') for line in self.read_file()]
        entries = []
        for line in lines:
            entries.append({
                'timestamp': line[0].strip(),
                'level': line[1].strip(),
                'message': line[2].strip()
            })

        for line in entries:
            if '\n' in line['message']:
                line['message'] = line['message'].replace('\n', '')

        return entries

    def filter_by_level(self, level: str) -> list | None:
        """
        Выводит список логов заданного уровня.
        :param level:
        :return:
        """
        entries = self.get_all_entries()
        levels = []
        for item in entries:
            if item['level'] not in levels:
                levels.append(item['level'])

        if level not in levels:
            print('Ошибка ввода уровня: такого уровня не существует.')
            return f"Не удалось отсортировать."

        filtered_entries = []
        for line in entries:
            if line['level'] == level:
                filtered_entries.append(line)

        return filtered_entries

    def count_by_level(self) -> dict:
        """
        Подсчитывает количсетво логов каждого
        уровня.
        :return:
        """
        entries = self.get_all_entries()
        levels = []
        for line in entries:
            if line['level'] not in levels:
                levels.append(line['level'])

        levels_amount = {}
        for level in levels:
            levels_amount[level] = 0

        for line in entries:
            for level in levels_amount:
                if level == line['level']:
                    levels_amount[level] += 1

        return levels_amount
