import secrets


def generate_key():
    part1 = secrets.token_hex(2).upper()
    part2 = secrets.token_urlsafe(2).upper()
    part3 = secrets.randbelow(100)
    new_key = "{}-{}-{}".format(part1, part2, part3)
    return new_key
