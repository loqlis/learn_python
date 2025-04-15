def group_users_by_logs(logs_data: list[dict]) -> list:
    grouped_user = {}
    sorted_logs = sorted(logs_data, key=lambda log: log['time'])
    for user in sorted_logs:
        if grouped_user.get(user["user"]):
            grouped_user[user["user"]].append(user)
        else:
            grouped_user[user["user"]] = [user]

    return grouped_user
