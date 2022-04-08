"""Schemas for our database"""
# pylint: disable=no-member
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

loggingIn = LoginManager()
db = SQLAlchemy()

# Models
class User(UserMixin, db.Model):
    """User table"""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String(500))

    def set_password(self, password):
        """Create a unique password hash for user's passwords"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """check a new hashed against the created hash"""
        return check_password_hash(self.password_hash, password)


@loggingIn.user_loader
def load_user(user_id):
    """Load the user based on their primary id"""
    return User.query.get(int(user_id))
