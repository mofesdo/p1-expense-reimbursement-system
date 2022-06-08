from flask import render_template, make_response
from model.login_dao import *

def loginButtonClicked(usr,pwd):
    auth = authenticate(usr, pwd)

    if auth is None:
        return "Failed Login"
    else:
        response = make_response(render_template("dashboard.html"))
        response.set_cookie("authToken", auth)
        return response

