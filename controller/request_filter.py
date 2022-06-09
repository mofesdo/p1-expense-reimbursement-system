from flask import render_template


def get_index():
    return render_template("index.html")


def get_dashboard():
    return render_template("dashboard.html")

