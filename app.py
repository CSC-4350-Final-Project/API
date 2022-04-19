# pylint: disable=no-member
"""Main app"""
import os
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
from models import db, User, Comment, Going
from tm import get_event_data
from events import get_event_list, get_event_detail

load_dotenv(find_dotenv())

app = flask.Flask(__name__)
app.config.from_object("config.Config")
CORS(app)

jwt = JWTManager(app)

db.init_app(app)
with app.app_context():
    db.create_all()

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


# routes go here
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


@app.route("/event_detail/<string:event_id>", methods=["GET"])
def event_detail(event_id):
    """Get event detail"""

    event_data = get_event_detail(event_id)

    return flask.jsonify(event_data)


@app.route("/homepage")
def homepage():
    """This method gets us data for upcoming events from Ticketmaster API"""
    data = get_event_data()
    return flask.jsonify(data)


@app.route("/event/<string:event_id>/comment", methods=["GET", "POST"])
def post_comment(event_id):
    """Post and get comments for a specific event"""
    if flask.request.method == "POST":
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        text = flask.request.get_json()

        new_comment = Comment(user_id=user_id, text=text, event_id=event_id)

        db.session.add(new_comment)
        db.session.commit()

        return flask.jsonify({"success": True})

    comments = (
        db.session.query(Comment, User)
        .filter(User.id == Comment.user_id)
        .filter_by(event_id=event_id)
        .order_by(Comment.id.asc())
        .all()
    )

    output = []

    for comment, user in comments:
        output.append(
            {
                "username": user.username,
                "user_id": user.id,
                "text": comment.text,
                "date_posted": comment.date_posted,
            }
        )
    return flask.jsonify(output)


@app.route("/event/<string:event_id>/going", methods=["GET", "POST"])
def going(event_id):
    """Post and get comments for a specific event"""

    verify_jwt_in_request()
    user_id = get_jwt_identity()

    if flask.request.method == "POST":

        data = flask.request.get_json()
        going_id = data["id"]
        status = data["value"]
        date_updated = data["dateUpdated"]

        if not going_id:
            new_status = Going(user_id=user_id, status=status, event_id=event_id)
            db.session.add(new_status)
        else:
            db.session.query(Going).filter(Going.id == going_id).update(
                {"status": status, "date_updated": date_updated}
            )

        db.session.commit()

        return flask.jsonify({"success": True})

    going_status = (
        db.session.query(Going)
        .filter(Going.user_id == user_id)
        .filter(Going.event_id == event_id)
        .first()
    )

    output = {}

    if going_status is None:
        output["id"] = None
    else:
        output["id"] = going_status.id
        output["status"] = going_status.status
        output["date_updated"] = going_status.date_updated
    return flask.jsonify(output)


if __name__ == "__main__":
    PORT = int(os.getenv("PORT", "4000"))
    HOST = os.getenv("IP", "0.0.0.0")
    app.run(debug=os.getenv("DEBUG"), host=HOST, port=PORT)
