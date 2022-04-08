"""Schemas for our database"""
# pylint: disable=no-member
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
