from flask import Flask, render_template, request
from controller.buttonActions import *
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


@app.route("/", methods=["GET"])
@CheckToken(request.cookies.get("authToken"))
def home():
    return get_index()


if __name__ == '__main__':
    app.run(debug=True)
