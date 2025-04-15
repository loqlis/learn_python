from .load_weak_passwords import load_weak_passwords


def check_symbols(password: str) -> str | None:
    password_ints = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    lower_letters = [
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
        'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'
    ]
    upper_letters = [
        'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'V',
        'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'B', 'N', 'M'
    ]

    symbols = {}
    for element in password:
        if symbols.get('ints') and element in password_ints:
            symbols['ints'].append(element)
        elif element in password_ints:
            symbols['ints'] = [element]
        if symbols.get('lower') and element in lower_letters:
            symbols['lower'].append(element)
        elif element in lower_letters:
            symbols['lower'] = [element]
        if symbols.get('upper') and element in upper_letters:
            symbols['upper'].append(element)
        elif element in upper_letters:
            symbols['upper'] = [element]

    all_symbols = []
    for value in symbols.values():
        all_symbols.append(value)
    if len(all_symbols) < 3:
        return 'symbol'


def validate_password(password: str) -> str | None:
    if len(password) < 8:
        return 'short'
    elif password in load_weak_passwords('weak_passwords.txt'):
        return 'weak'
    else:
        return check_symbols(password)
