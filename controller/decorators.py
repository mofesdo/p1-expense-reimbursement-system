import model
from flask import render_template


class CheckToken:
    def __init__(self, token=""):
        self.token = token

    def __call__(self, func):
        def wrapper():
            if model.authentication.checkToken(self.token):
                return func()
            else:
                return render_template("Invalid Auth Token")

        return wrapper

