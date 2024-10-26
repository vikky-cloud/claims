import os
from flask import Flask
from models.models import db
from config import Config
from api.auth import auth_bp
from api.policy import policy_bp
from api.claim import claim_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    
    # Create the database tables
    with app.app_context():
        db.create_all()  # This creates all tables based on your models

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(policy_bp, url_prefix='/api/policy')
    app.register_blueprint(claim_bp, url_prefix='/api/claim')
    
    return app
