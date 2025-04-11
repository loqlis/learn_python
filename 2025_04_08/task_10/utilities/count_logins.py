def count_logins(logs_data: list[dict]) -> dict:
    user_logins = {}
    for user in logs_data:
        if user_logins.get(user["user"]) and user["action"] == "login":
            user_logins[user["user"]] += 1
        else:
            user_logins[user["user"]] = 1

    return user_logins
