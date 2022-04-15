import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
from datetime import timedelta


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    TM_API = os.getenv("TM_API")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 100
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
