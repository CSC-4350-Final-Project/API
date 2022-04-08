# pylint: disable=no-member
"""Main app"""
import os
import flask
from flask import request, jsonify
from flask_login import login_required, current_user, login_user, logout_user
from dotenv import find_dotenv, load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
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

# Login
@app.route("/login", methods=["POST", "GET"])
def login():
    """If user is already registered, take them to main page"""
    # if current_user.is_authenticated:
    #     user_infor = {
    #         "id": current_user.id,
    #         "email": current_user.email,
    #         "username": current_user.username,
    #     }
    #     return jsonify(user_infor)

    if request.method == "POST":
        email = request.get_json()["email"]
        user = User.query.filter_by(email=email).first()
        if user is not None and check_password_hash(
            request.get_json()["password"], user.password
        ):
            return jsonify(
                {
                    "error": False,
                    "message": "Login Successfully",
                    "id": user.id,
                    "email": user.email,
                    "username": user.username,
                }
            )
        if user is None:
            return jsonify(
                {"error": True, "message": "Not registered. Please register."}
            )
    return jsonify(
        {
            "error": False,
            "message": "Please login with your registered credentials.",
            "page": "You are at Login page",
        }
    )


# Logout
@app.route("/logout", methods=["POST", "GET"])
def logout():
    """Logout the user"""
    logout_user()
    return jsonify(
        {
            "message": "You have been logged out",
            "error": False,
            "page": "You are at Logout page",
        }
    )


# Register
@app.route("/register", methods=["POST", "GET"])
def register():
    """Register the email to the database"""

    if current_user.is_authenticated:
        user_info = {
            "id": current_user.id,
            "email": current_user.email,
            "username": current_user.username,
        }
        return jsonify(user_info)

    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]

        if User.query.filter_by(email=email).first():
            return jsonify(
                {
                    "error": True,
                    "message": "Email taken. Try another",
                }
            )
        else:
            user = User(email=email, username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return jsonify(
                {
                    "error": False,
                    "message": "Registered successfully. Please login with the recently registered credentials",
                }
            )

    return jsonify(
        {
            "error": True,
            "message": "Wrong credentials",
            "page": "You are at Register page",
        }
    )


# Main
@app.route("/main")
@login_required
def main():
    """App's main page"""
    result = {
        "error": False,
        "message": "You have accessed to Main page",
        "email": current_user.email,
        "username": current_user.username,
        "page": "You are in Main page",
    }
    return result


# Profile
@app.route("/profile")
@login_required
def profile():
    """Profile page with current user information"""

    my_info = {
        "my_id": current_user.id,
        "my_email": current_user.email,
        "my_username": current_user.username,
        "error": False,
        "message": "You are in Profile page",
    }
    return jsonify(my_info)


if __name__ == "__main__":
    PORT = int(os.getenv("PORT", "4000"))
    HOST = os.getenv("IP", "0.0.0.0")
    app.run(debug=os.getenv("DEBUG"), host=HOST, port=PORT)
