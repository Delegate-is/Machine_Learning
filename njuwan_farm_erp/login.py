# In app.py add
import os

from flask import app, session, redirect, url_for, request

users = {
    "admin": {"password": "1234", "role": "Admin"},
    "worker": {"password": "1234", "role": "Worker"},
    "investor": {"password": "1234", "role": "Investor"}
}

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username]["password"] == password:
            session["user"] = username
            session["role"] = users[username]["role"]
            return redirect(url_for("dashboard"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))



#add to config.py
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-njuwan-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///njuwan.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False