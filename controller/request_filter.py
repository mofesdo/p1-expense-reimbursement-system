from flask import render_template
import datetime
from model import dao


def get_index():
    return render_template("index.html")


def get_dashboard(usr, asc, ismngr):
    stuff = dao.getReimbursementRequests(usr, asc)
    return render_template("dashboard.html", returnedRequests=stuff, isManager=ismngr)


def get_request_form():
    return render_template("createNewReimbursement.html", currentDatetime=
                            str(datetime.datetime.now()).split("T")[0] )


def get_cancellation_page(usr, asc):
    ongoingRequests = dao.getOngoingRequests(usr, asc)
    return render_template("cancelRequests.html", returnedRequests=ongoingRequests)


def get_manager_page(asc):
    allOngoingRequests = dao.getAllReimbursementRequests(asc)
    return render_template("manager.html", returnedRequests=allOngoingRequests, hiddenRowCount=len(allOngoingRequests))


def render_log():
    f = open("project1log.txt", "r")
    out = "<br>".join(list(f.readlines()))
    return out

