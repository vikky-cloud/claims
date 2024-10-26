from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    response_data, status_code = auth_service.register_customer(data)
    return jsonify(response_data), status_code 

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    response, status_code = auth_service.login(email, password)  # Update to get response and status
    return jsonify(response), status_code  # Return response and status code