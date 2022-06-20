import re
from controller.logger import *


def validate_description(description):
    out = ""
    log_regular(f"validating description: {description}")
    try:
        r = r"""[A-Za-z0-9\.\s'"]{1,100}"""
        match = re.match(r, description)

        if match is not None:
            out = description
        log_error(f"match object is: {str(match)}")
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
    log_regular(f"validating {date}")
    try:
        r = r"[0-9]{2,4}[\/-][0-9]{2}[\/-][0-9]{2,4}"
        match = re.match(r, date)

        if match is not None:
            out = date
        log_error(f"error with date {str(match)}")
    except:
        out = ""

    return out


