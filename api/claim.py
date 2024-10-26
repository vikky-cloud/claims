from flask import Blueprint, request, jsonify
from services.claim_service import ClaimService
from decorators import token_required

claim_bp = Blueprint('claim', __name__)
claim_service = ClaimService()

@claim_bp.route('/claim', methods=['POST'])
@token_required
def create_claim(current_user):
    data = request.get_json()
    data['customer_id'] = current_user.customer_id
    claim = claim_service.create_claim(data)
    return jsonify({
        'message': 'Claim created successfully',
        'claim_number': claim.claim_number
    }), 201

@claim_bp.route('/claim/status', methods=['GET'])
@token_required
def check_claim_status(current_user):
    claim_number = request.args.get('claim_number')
    policy_number = request.args.get('policy_number')
    
    claim = claim_service.get_claim_status(
        claim_number, 
        policy_number, 
        current_user.customer_id
    )
    
    if not claim:
        return jsonify({'message': 'Claim not found or unauthorized'}), 404
    
    return jsonify({
        'claim_number': claim.claim_number,
        'status': claim.status.status,
        'updated_at': claim.status.updated_at.strftime('%Y-%m-%d %H:%M:%S')
    })