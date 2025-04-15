def load_weak_passwords(file) -> list:
    with open(file) as f:
        passwords_list = f.readlines()

    weak_passwords = []
    for password in passwords_list:
        weak_passwords.append(password[:-1])

    return weak_passwords
