"""Final Project"""
import os
import flask
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user, login_user, logout_user
from dotenv import find_dotenv, load_dotenv
from models import db, User, login

load_dotenv(find_dotenv())
app = flask.Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
login.init_app(app)
login.login_view = "login"


db.init_app(app)
with app.app_context():
    db.create_all()


# ROUTES

# Landing
@app.route("/")
def landing():
    return render_template("landing.html")


# Login
@app.route("/login", methods=["POST", "GET"])
def login():
    # if user is already registered, take them to main page
    if current_user.is_authenticated:
        return redirect("/main")

    if flask.request.method == "POST":
        email = flask.request.form["email"]
        user = User.query.filter_by(email=email).first()
        if user is not None and user.check_password(flask.request.form["password"]):
            login_user(user)
            return redirect("/main")
    return render_template("login.html")


# Logout
@app.route("/logout", methods=["POST", "GET"])
def logout():
    logout_user()
    return redirect(url_for("landing"))


# Register
@app.route("/register", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect("/main")

    if flask.request.method == "POST":
        email = flask.request.form["email"]
        username = flask.request.form["username"]
        password = flask.request.form["password"]

        if User.query.filter_by(email=email).first():
            flash("Email used. Try another.")
        else:
            user = User(email=email, username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return redirect("/login")
    return render_template("register.html")


# Main
@app.route("/main")
@login_required
def main():
    return render_template("main.html")


if __name__ == "__main__":
    PORT = int(os.getenv("PORT", "4000"))
    HOST = os.getenv("IP", "0.0.0.0")
    app.run(debug=os.getenv("DEBUG"), host=HOST, port=PORT)
