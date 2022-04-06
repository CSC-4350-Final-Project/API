# pylint: disable=no-member
"""Main app"""
import os
import flask
from flask import render_template, redirect, flash, request
from flask_login import login_required, current_user, login_user, logout_user
from dotenv import find_dotenv, load_dotenv
from models import db, User, loggingIn

load_dotenv(find_dotenv())
app = flask.Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 100

loggingIn.init_app(app)
loggingIn.login_view = "login"

db.init_app(app)
with app.app_context():
    db.create_all()

# ROUTES

# Landing
@app.route("/")
def landing():
    """This page contains an app overview and Login/Register buttons"""
    return render_template("landing.html")


# Login
@app.route("/login", methods=["POST", "GET"])
def login():
    """If user is already registered, take them to main page"""
    if current_user.is_authenticated:
        return redirect("/main")

    if request.method == "POST":
        email = request.form["email"]
        user = User.query.filter_by(email=email).first()
        if user is not None and user.check_password(request.form["password"]):
            login_user(user)
            return redirect("/main")
        if user is None:
            flash("Not registered. Please register below.")
    return render_template("login.html")


# Logout
@app.route("/logout", methods=["POST", "GET"])
def logout():
    """Logout the user"""
    logout_user()
    return redirect("/")


# Register
@app.route("/register", methods=["POST", "GET"])
def register():
    """Register the email to the database"""
    if current_user.is_authenticated:
        return redirect("/main")

    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]

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
    """App's main page"""
    return render_template("main.html")


if __name__ == "__main__":
    PORT = int(os.getenv("PORT", "4000"))
    HOST = os.getenv("IP", "0.0.0.0")
    app.run(debug=os.getenv("DEBUG"), host=HOST, port=PORT)
