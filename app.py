# pylint: disable=no-member
"""Main app"""
import json
import os
from datetime import timedelta
import flask
from flask import request, jsonify
from dotenv import find_dotenv, load_dotenv
from werkzeug.security import check_password_hash
from flask_cors import CORS
from flask_jwt_extended import (
    create_access_token,
    JWTManager,
    get_jwt_identity,
    verify_jwt_in_request,
)
from models import db, User, Favorites
from tm import get_event_data
from events import get_event_list, get_event_detail

load_dotenv(find_dotenv())

app = flask.Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 100
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)

jwt = JWTManager(app)

db.init_app(app)
with app.app_context():
    db.create_all()
    #db.drop_all()

# ROUTES

# Login
@app.route("/login", methods=["POST", "GET"])
def login():
    """If user is already registered, take them to main page"""
    email = request.get_json()["email"]
    password = request.get_json()["password"]

    user = User.query.filter_by(email=email).first()

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

    return jsonify(
        {"error": True, "message": "Invalid username or password. Please try again."}
    )


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

        user = User(email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        return jsonify(
            {
                "error": False,
                "message": "Registered successfully. Please login with the recently\
                registered credentials",
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
@app.route("/profile", methods=["GET"])
def profile():
    """Profile page with current user information"""
    verify_jwt_in_request(optional=False)

    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()

    if request.method == "GET":
        user_info = {
            "user_id": user.id,
            "email": user.email,
            "username": user.username,
        }
    return jsonify(user_info)


# Search
@app.route("/search", methods=["GET", "POST"])
def index():
    """Returns root endpoint HTML"""
    if flask.request.method == "GET":
        postal_code = "30303"
        keyword = ""
    else:
        postal_code = flask.request.get_json()["postal_code"]
        keyword = flask.request.get_json()["keyword"]

    event_data = get_event_list(postal_code, keyword)

    return flask.jsonify(event_data)


@app.route("/event_detail/<string:event_id>", methods=["POST", "GET"])
def event_detail(event_id):
    """Get event detail"""
    
    event_data = get_event_detail(event_id) 

    return flask.jsonify(event_data)


@app.route("/homepage")
def homepage():
    """This method gets us data for upcoming events from Ticketmaster API"""
    data = get_event_data()
    return flask.jsonify(data)


@app.route("/favorites/<string:event_id>", methods=["POST", "GET"])
def favorites(event_id):
    """Returns a list of favorite events"""

    verify_jwt_in_request(optional=False)
    user_id = get_jwt_identity()

    if request.method == "POST":
        is_favorited = Favorites.query.filter_by(event_id=event_id, user_id=user_id).first()
        #if this event has been favorited, remove from database
        if is_favorited:
            Favorites.query.filter_by(event_id=event_id, user_id=user_id).delete()
            db.session.commit()
            print(is_favorited, event_id, user_id)
            return jsonify({})
        #Otherwise, add as a new favorite
        else:
            new_favorite = Favorites(user_id=user_id, event_id=event_id)
            db.session.add(new_favorite)
            db.session.commit()
            return jsonify({"message": "New favorite added to database"})  
    
    elif request.method == "GET":
        events = Favorites.query.filter_by(event_id=event_id, user_id=user_id).first()
        
        if events:
            return jsonify({"is_favorite": True})
        else:
            return jsonify({"is_favorite": False})

    return jsonify({"message": "Successfully added"})

    

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", "4000"))
    HOST = os.getenv("IP", "0.0.0.0")
    app.run(debug=os.getenv("DEBUG"), host=HOST, port=PORT)
