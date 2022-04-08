# pylint: disable=no-member
"""Main app"""
import os
import flask
from datetime import timedelta
from flask import request, jsonify
from dotenv import find_dotenv, load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
from flask_jwt_extended import (
    create_access_token,
    JWTManager,
    get_jwt_identity,
    verify_jwt_in_request,
)

load_dotenv(find_dotenv())
app = flask.Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 100
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)

jwt = JWTManager(app)

db.init_app(app)
with app.app_context():
    db.create_all()

# ROUTES

# Login
@app.route("/login", methods=["POST", "GET"])
def login():
    """If user is already registered, take them to main page"""
    if request.method == "POST":
        email = request.get_json()["email"]
        password = request.get_json()["password"]

        user = User.query.filter_by(email=email).first()
        print(user.password_hash, password)

        if user is not None and check_password_hash(user.password_hash, password):
            return jsonify(
                {
                    "error": False,
                    "message": "Login Successfully",
                    "id": user.id,
                    "email": user.email,
                    "username": user.username,
                    "token": create_access_token(identity=user.id),
                }
            )
        else:
            return jsonify({"error": True, "message": "Invalid username or password."})


# Register
@app.route("/register", methods=["POST", "GET"])
def register():
    """Register the email to the database"""
    if request.method == "POST":
        email = request.get_json()["email"]
        username = request.get_json()["username"]
        password = request.get_json()["password"]

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


# Profile
@app.route("/profile")
def profile():
    """Profile page with current user information"""
    verify_jwt_in_request(optional=False)
    user_id = get_jwt_identity()

    my_info = {
        "user_id": user_id,
        "error": False,
        "message": "You are in Profile page",
    }
    return jsonify(my_info)


if __name__ == "__main__":
    PORT = int(os.getenv("PORT", "4000"))
    HOST = os.getenv("IP", "0.0.0.0")
    app.run(debug=os.getenv("DEBUG"), host=HOST, port=PORT)
