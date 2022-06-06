from flask import render_template

def render_home(param1, param2):
    return render_template("lol.html", r1=param1, r2=param2)

