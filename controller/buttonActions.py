from flask import render_template, make_response, redirect
from model.login_dao import *
from model.dao import *


def loginButtonClicked(usr, pwd):
    auth = authenticate(usr, pwd)

    if auth is None:
        return "Failed Login"
    else:
        response = make_response(redirect("/"))
        response.set_cookie("authToken", auth)
        return response


def createRequestsClicked(usr, desc, price, urg, date):
    create_reimbursements(usr, desc, price, 0, urg, date)
    return redirect("/")


def cancelRequestClicked(request_id):
    cancel_reimbursement(request_id)
    return redirect("/cancelrequest")


def approveRequestClicked(request_id):
    approve_reimbursement(request_id)
    return redirect("/manager")


def declineRequestClicked(request_id):
    decline_reimbursement(request_id)
    return redirect("/manager")
