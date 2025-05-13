import csv


class ReportGenerator:
    def __init__(self, data: list[dict], fields):
        self.data = data
        self.fields = fields

    def export_to(self, file_name):
        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            if self.fields == 'all':
                columns = self.data[0].keys()
            else:
                columns = set()
                for item in self.data:
                    for key in item:
                        if key in self.fields:
                            columns.add(key)
            writer.writerow(columns)

        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            for line in self.data:
                row = []
                for key in line:
                    if key in columns:
                        row.append(line[key])
                writer.writerow(row)
