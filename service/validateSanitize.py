import re


def validate_username(username):
    out = ""

    try:
        r = "^[a-zA-Z0-9_]{3,50}$"
        match = re.match(r, username)

        if match is not None:
            out = username
    except:
        pass

    return out


def validate_password(password):
    out = ""

    try:
        r = "^[a-zA-Z0-9_]{3,50}$"
        match = re.match(r, password)

        if match is not None:
            out = password
    except:
        pass

    return out


def validate_token(token):
    out = -1
    try:
        out = int(token)
    except BaseException as e:
        pass

    return out


def validate_requestId(requestId):
    out = -1
    try:
        out = int(requestId)
    except BaseException as e:
        pass

    return out

