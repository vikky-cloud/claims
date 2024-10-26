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

    db.init_app(app)

    with app.app_context():
        db.create_all()  

    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(policy_bp, url_prefix='/api')
    app.register_blueprint(claim_bp, url_prefix='/api')
    
    return app