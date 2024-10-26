from flask import Blueprint, request, jsonify
from services.policy_service import PolicyService
from decorators import token_required

policy_bp = Blueprint('policy', __name__)
policy_service = PolicyService()

@policy_bp.route('/policies', methods=['GET'])
@token_required
def get_policies(current_user):
    policies = policy_service.get_customer_policies(current_user.customer_id)
    return jsonify([{
        'policy_number': policy.policy_number,
        'vehicle_registration_number': policy.vehicle_registration_number,
        'vehicle_name': policy.vehicle_name,
        'policy_limit': policy.policy_limit,
        'expiration_date': policy.expiration_date.strftime('%Y-%m-%d')
    } for policy in policies])

@policy_bp.route('/policy', methods=['POST'])
@token_required
def create_policy(current_user):
    data = request.get_json()
    policy = policy_service.create_policy(data, current_user.customer_id)
    return jsonify({
        'message': 'Policy created successfully',
        'policy_number': policy.policy_number
    }), 201