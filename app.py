from flask import Flask, render_template, request
from controller.buttonActions import *
from controller.request_filter import *
from controller.decorators import CheckToken
import os

# template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# template_dir = os.path.join(template_dir, 'view')
# template_dir = os.path.join(template_dir, 'templates')
app = Flask(__name__) #, template_folder=template_dir)


@app.route('/login/input', methods=["POST"])
def user_login():
    usr = request.form.get("username")
    pwd = request.form.get("password")
    return loginButtonClicked(usr, pwd)


@app.route("/login", methods=["GET"])
def login_page():
    return get_index()


@app.route("/", methods=["GET"])
@CheckToken(request)
def home():
    return get_dashboard()


if __name__ == '__main__':
    app.run(debug=True)
