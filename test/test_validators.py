import pytest
from service.validateSanitize import *


@pytest.mark.parametrize("dummy_username, expected", (
    ("user_1", True),
    ("manager_1", True),
    ("*h@ckerMan_", False),
    ("^carrotMan", False),
    ("Not!user", False),
    ("Dude this ain't a name", False),
    ("/index.html", False),
    ("Bob", True),
    ("", False),
    (1, False),
    (True, False)
    )
)
def test_username(dummy_username, expected):
    assert (validate_username(dummy_username) != "") == expected


@pytest.mark.parametrize("dummy_password, expected", (
    ("pass_1", True),
    ("password", True),
    ("*h@ckerMan_", False),
    ("^carrotMan", False),
    ("Not!user", False),
    ("Dude this ain't a name", False),
    ("/index.html", False),
    ("Bob", True),
    ("", False),
    (None, False)
    )
)
def test_password(dummy_password, expected):
    assert (validate_password(dummy_password) != "") == expected


@pytest.mark.parametrize("dummy_token, expected", (
        (234454512, True),
        ("123456789", True),
        ("*h@ckerMan_", False),
        (True, True),
        (False, True),
        ("True", False),
        ("/index.html", False),
        ("Bob", False),
        ("", False),
        (1.1, True)
)
                         )
def test_number(dummy_token, expected):
    assert (validate_token(dummy_token) != -1) == expected
    assert (validate_requestId(dummy_token) != -1) == expected
