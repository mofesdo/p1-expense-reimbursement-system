from model.authentication import checkToken
from flask import render_template


class CheckToken:
    def __init__(self, requestObject):
        self.r = requestObject

    def __call__(self, func):
        def wrapper():
            if checkToken(self.r.cookies.get("authToken")):
                return func()
            else:
                return render_template("error.html")

        wrapper.__name__ = func.__name__
        return wrapper

