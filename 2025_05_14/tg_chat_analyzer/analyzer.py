import json, datetime
from json import JSONDecodeError

from sys import exit


class Analyzer:
    def __init__(self, file_path: str):
        self.chat_path = file_path
        self.loaded_chat = self.read_json_chat()
        self.chat = self._del_extra()

    def read_json_chat(self) -> list | None:
        """
        Получение данных из файла.
        :return:
        """
        try:
            with open(self.chat_path) as chat:
                return json.load(chat)
        except FileNotFoundError:
            print("Файл не найден.")
            exit()
        except JSONDecodeError:
            print('Файл пуст.')
            exit()

    def _del_extra(self) -> list:
        """
        Удаляет данные не участвующие в анализе чата.
        :return:
        """
        all_messages = []

        for message_list in self.loaded_chat.get("messages"):
            all_messages.append({
                "from": message_list.get("from"),
                "text": message_list.get("text"),
                "date": message_list.get("date")
            })

        return all_messages

    def count_messages_by_person(self) -> dict:
        """
        Считает количество сообщений по каждому
        пользователю и сортирует в порядке убывания.
        :return:
        """
        people_dict = {}

        for message in self.chat:
            if people_dict.get(message["from"]):
                people_dict[message["from"]] += 1
            else:
                people_dict[message["from"]] = 1

        people_dict.pop(None)
        sorted_people = sorted(people_dict.items(), key=lambda item: item[1], reverse=True)
        result_people_dict = {}

        for person in sorted_people:
            result_people_dict[person[0]] = person[1]

        return result_people_dict

    def sort_messages_by_weekdays(self) -> dict:
        """
        Подсчитывает количество сообщений по дням недели.
        :return:
        """
        dates = []

        for message in self.chat:
            dates.append(message["date"][:10].split('-'))

        days_dict = {
            'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0,
            'Friday': 0, 'Saturday': 0, 'Sunday': 0
        }

        for day in dates:
            day = [*map(int, day)]
            date = datetime.datetime(day[0], day[1], day[2])
            match date.weekday():
                case 0:
                    days_dict['Monday'] += 1
                case 1:
                    days_dict['Tuesday'] += 1
                case 2:
                    days_dict['Wednesday'] += 1
                case 3:
                    days_dict['Thursday'] += 1
                case 4:
                    days_dict['Friday'] += 1
                case 5:
                    days_dict['Saturday'] += 1
                case 6:
                    days_dict['Sunday'] += 1

        return days_dict

    def sort_messages_by_time(self) -> dict:
        """
        Подсчитывает количество сообщений по времени
        суток.
        :return:
        """
        time_dict = {
            'Morning': 0,
            'Afternoon': 0,
            'Evening': 0,
            'Night': 0
        }
        times = []

        for message in self.chat:
            times.append(message['date'][-8:-3])

        for time in times:
            if 0 <= int(time[:2]) < 6:
                time_dict['Night'] += 1
            elif 6 <= int(time[:2]) < 12:
                time_dict['Morning'] += 1
            elif 12 <= int(time[:2]) < 18:
                time_dict['Afternoon'] += 1
            elif 18 <= int(time[:2]):
                time_dict['Evening'] += 1

        return time_dict

    def count_words_and_links(self) -> dict:
        """
        Считает количество ссылок и слов в чате
        :return:
        """
        words = []
        links = []
        for message in self.chat:
            match message:
                case str(message.get('text')):
                    words.append(word for word in message['text'].split(' '))
                case _:
                    for item in message['text']:
                        match item:
                            case str(item):
                                words.append(word for word in item.split(' '))
                            case dict(item):
                                if item['type'] == 'link':
                                    links.append(item['text'])

        counter = {'Words': len(words), 'Links': len(links)}

        return counter

    def get_full_result(self):
        """
        Получение полной статистики
        с красивым выводом.
        :return:
        """
        result_people_dict = self.count_messages_by_person()
        result_people = f"Статистика по авторам\n"
        for key, value in result_people_dict.items():
            result_people += f"{key}: {value}\n"

        days_dict = self.sort_messages_by_weekdays()
        days_result = f"Распределение по дням:\n"
        for key, value in days_dict.items():
            days_result += f"{key}: {value}\n"

        time_dict = self.sort_messages_by_time()
        time_result = f"Распределение по времени:\n"
        for key, value in time_dict.items():
            time_result += f"{key}: {value}\n"

        counter = self.count_words_and_links()
        words_links_result = f"Слова и ссылки:\n"
        for key, value in counter.items():
            words_links_result += f"{key}: {value}\n"

        print(
            f"{result_people}\n"
            f"{days_result}\n"
            f"{time_result}\n"
            f"{words_links_result}"
        )
