from datetime import timedelta
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(24))
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost:3306/claims_microservice'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_EXPIRATION = timedelta(hours=24)