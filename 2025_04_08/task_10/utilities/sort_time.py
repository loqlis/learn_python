def sort_time(logs_data: list[dict]) -> list:
    sorted_logs = sorted(logs_data, key=lambda log: log['time'])

    return sorted_logs
