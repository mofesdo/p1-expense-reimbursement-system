import pytest
from service.validateReimbursement import *


@pytest.mark.parametrize("dummy_description, expected", (
    ("user_1", True),
    ("frogs #blessed", True),
    ("hackerMan_@gmail.com", True),
    ("lets dance! ~(^-^)~ ", True),
    ("Not user!", True),
    ("Dude this ain't a name", True),
    ("/index.html", True),
    ("|\/ index.html", False),
    ("```ayo````", False),
    ("me & you", True),
    ("", False),
    (1, False),
    (True, False)
    )
)
def test_description(dummy_description, expected):
    assert (validate_description(dummy_description) != "") == expected


@pytest.mark.parametrize("dummy_price, expected", (
        (234454512, False),
        ("123456789",False),
        ("*h@ckerMan_", False),
        (True, True),
        (False, False),
        ("True", False),
        (1.23, True),
        (420.69, True),
        ("", False),
        (999, True),
        (0, False)
)
                         )
def test_number(dummy_price, expected):
    assert (validate_price(dummy_price) != -1) == expected


@pytest.mark.parametrize("dummy_urgent, expected", (
        (234454512, False),
        ("123456789",False),
        ("*h@ckerMan_", False),
        (True, True),
        (False, True),
        ("True", False),
        (1.23, True),
        (420.69, False),
        ("", False),
        (999, False),
        (0, True),
        (1, True)
)
                         )
def test_urgent(dummy_urgent, expected):
    assert (validate_urgent(dummy_urgent) != -1) == expected


@pytest.mark.parametrize("dummy_date, expected", (
        (234454512, False),
        ("123456789", False),
        ("12/10/1998", True),
        (True, False),
        (False, False),
        ("1998/12/10", True),
        ("06/19/2022", True),
        (420.69, False),
        ("", False),
        (999, False),
        (0, False),
        (1, False)
)
                         )
def test_date(dummy_date, expected):
    assert (validate_date(dummy_date) != "") == expected