from flask import Flask, render_template, request
from controller.buttonActions import *
from controller.request_filter import *
from controller.decorators import CheckToken, IsManager
from model.authentication import getUsername, isManager
import os

# template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# template_dir = os.path.join(template_dir, 'view')
# template_dir = os.path.join(template_dir, 'templates')
app = Flask(__name__, static_url_path="/static") #, template_folder=template_dir)


@app.route("/log", methods=["GET"])
def give_log():
    return render_log()


@app.route('/login/input', methods=["POST"])
def user_login():
    usr = request.form.get("username")
    pwd = request.form.get("password")
    return loginButtonClicked(usr, pwd)


@app.route("/login", methods=["GET"])
def login_page():
    return get_index()


@app.route("/logout", methods=["GET"])
def logout():
    response = make_response(redirect("/login"))
    response.delete_cookie("authToken")
    return response


@app.route("/", methods=["GET"])
@CheckToken(request)
def home():
    token = request.cookies.get("authToken")
    ismngr = isManager(token)
    usr = getUsername(token)
    return get_dashboard(usr, "asc", ismngr)


@app.route("/createrequest", methods=["GET"])
def createrequest():
    return get_request_form()


@app.route('/requests/input', methods=["POST"])
@CheckToken(request)
def create_requests():
    usr = getUsername(request.cookies.get("authToken"))
    desc = request.form.get("description")
    price = request.form.get("price")
    urg = request.form.get("urgent")
    date = request.form.get("date")
    return createRequestsClicked(usr, desc, price, urg, date)

# dan was here


@app.route("/cancelrequest", methods=["GET"])
def cancelrequest():
    usr = getUsername(request.cookies.get("authToken"))
    return get_cancellation_page(usr, "asc")


@app.route("/cancelrequest/input", methods=["POST"])
def processCancellation():
    request_id = request.form.get("request_id")
    return cancelRequestClicked(request_id)


@app.route("/manager", methods=["GET"])
@CheckToken(request)
@IsManager(request)
def manageRequests():
    return get_manager_page("asc")


@app.route("/manager/approve", methods=["POST"])
def managerApprove():
    rid = request.form.get("request_id")
    return approveRequestClicked(rid)


@app.route("/manager/decline", methods=["POST"])
def managerDecline():
    rid = request.form.get("request_id")
    return declineRequestClicked(rid)


if __name__ == '__main__':
    app.run(debug=True)
