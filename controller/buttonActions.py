from flask import render_template, make_response
from model.login_dao import *
from model.dao import *


def loginButtonClicked(usr, pwd):
    auth = authenticate(usr, pwd)

    if auth is None:
        return "Failed Login"
    else:
        response = make_response(render_template("dashboard.html"))
        response.set_cookie("authToken", auth)
        return response


def createRequestsClicked(usr, desc, price, urg):
    create_reimbursements(usr, desc, price, 0, urg)
    return render_template("dashboard.html")
