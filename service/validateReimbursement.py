import re


def validate_description(description):
    out = ""

    try:
        r = """[A-Za-z0-9_/?!"'-]{1,100}"""
        match = re.match(r, description)

        if match is not None:
            out = description
    except:
        pass

    return out


def validate_price(price):
    out = -1
    try:
        out = float(price)
        if out > 1000 or out < 1:
            1/0

    except BaseException as e:
        out = -1

    return out


def validate_urgent(urgent):
    out = -1
    try:
        out = int(urgent)
        if out != 0 and out != 1:
            1/0

    except BaseException as e:
        out = -1

    return out


def validate_date(date):
    pass


