class LogParser:
    def __init__(self, file_path):
        with open(file_path) as file:
            self.file = file.readlines()

    def get_all_entries(self):
        lines = [line.split(',') for line in self.file]
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

    def filter_by_level(self, level):
        entries = self.get_all_entries()
        filtered_entries = []
        for line in entries:
            if line['level'] == level:
                filtered_entries.append(line)

        return filtered_entries

    def count_by_level(self):
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
