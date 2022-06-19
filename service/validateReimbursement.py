import re


def validate_description(description):
    out = ""

    try:
        r = """[A-Za-z0-9_/#^*(),.:;%?!&@~<>'"-][^\s-]{1,100}"""
        match = re.match(r, description)

        if match is not None:
            out = description
    except:
        out = ""

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
    out = ""

    try:
        r = """[0-9]{2,4}/[0-9]{2}/[0-9]{2,4}"""
        match = re.match(r, date)

        if match is not None:
            out = date
    except:
        out = ""

    return out


