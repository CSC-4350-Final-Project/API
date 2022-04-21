# pylint: disable=too-few-public-methods
"""Configs for Flask server"""
import os
from datetime import timedelta
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config:
    """Config Class"""

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    TM_API = os.getenv("TM_API")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 100
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
    MAIL_SERVER = "smtp.mailtrap.io"
    MAIL_PORT = 2525
    MAIL_USERNAME = "97e041d5e367c7"
    MAIL_PASSWORD = "cfaf5b99f8bafb"
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
