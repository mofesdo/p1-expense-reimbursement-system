from flask import Flask, render_template, request
from controller.buttonActions import *

app = Flask(__name__)


@app.route('/login/input', methods=["POST"])
def user_login():
    return loginButtonClicked(request.form)

def main():
    pass


if __name__ == '__main__':
    main()
