from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zipcode = db.Column(db.String(10), nullable=False)
    policies = db.relationship('Policy', backref='customer', lazy=True)

class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy_number = db.Column(db.String(50), unique=True, nullable=False)
    customer_id = db.Column(db.String(50), db.ForeignKey('customer.customer_id'), nullable=False)
    vehicle_registration_number = db.Column(db.String(50), unique=True, nullable=False)
    vehicle_price = db.Column(db.Float, nullable=False)
    vehicle_name = db.Column(db.String(100), nullable=False)
    model_year = db.Column(db.Integer, nullable=False)
    car_make = db.Column(db.String(50), nullable=False)
    policy_limit = db.Column(db.Float, nullable=False)
    deductible = db.Column(db.Float, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    claims = db.relationship('Claim', backref='policy', lazy=True)

class Claim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    claim_number = db.Column(db.String(50), unique=True, nullable=False)
    policy_number = db.Column(db.String(50), db.ForeignKey('policy.policy_number'), nullable=False)
    customer_id = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    claim_date = db.Column(db.DateTime, nullable=False)
    status = db.relationship('ClaimStatus', backref='claim', lazy=True, uselist=False)

class ClaimStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    claim_number = db.Column(db.String(50), db.ForeignKey('claim.claim_number'), unique=True, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='PENDING')
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)