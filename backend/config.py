import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Use a proper database URI for production
    SQLALCHEMY_TRACK_MODIFICATIONS = False
