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
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USERNAME = os.getenv("EMAIL_USER")
    MAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
