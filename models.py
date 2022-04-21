"""Schemas for our database"""
# pylint: disable=no-member,too-few-public-methods,duplicate-code
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# Models
class User(db.Model):
    """User table"""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String(500))

    def set_password(self, password):
        """Create a unique password hash for user's passwords"""
        self.password_hash = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        """check a new hashed against the created hash"""
        return check_password_hash(self.password_hash, password)


# reviews
class Review(db.Model):
    """Review for the events"""

    __tablename__ = "reviews"
    id = db.Column(
        db.Integer, primary_key=True
    )  # primary keys are required by SQLAlchemy
    moiveid = db.Column(db.Integer)
    userid = db.Column(db.Integer)
    username = db.Column(db.String(1000))
    comment = db.Column(db.String(1000))
    rating = db.Column(db.Integer)

    def __init__(self, event_id, userid, username, comment):
        self.event_id = event_id
        self.userid = userid
        self.username = username
        self.comment = comment


class Favorites(db.Model):
    """Favorites table"""

    __tablename__ = "favorites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    event_id = db.Column(db.String(100))


class Comment(db.Model):
    """Comments table"""

    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    event_id = db.Column(db.Text)
    text = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=db.func.now())


class Going(db.Model):
    """Going/not going/unsure status"""

    __tablename__ = "going"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    event_id = db.Column(db.Text)
    status = db.Column(db.Text)
    date_updated = db.Column(db.DateTime, default=db.func.now())
