from .database import database


def validate_login(login: str) -> str | None:
    login_symbols = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y',
        'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
        'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S',
        'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'B', 'N', 'M', '_'
    ]

    for element in login:
        if element not in login_symbols:
            return 'symbol'

    if len(login) < 3:
        return 'short'
    elif login in database:
        return 'authorized'
    try:
        int(login[0])
    except ValueError:
        return None
    else:
        return 'starts'
