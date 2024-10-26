from dal.claim_dal import ClaimDAL
import uuid
from datetime import datetime

class ClaimService:
    def __init__(self):
        self.claim_dal = ClaimDAL()

    def create_claim(self, claim_data):
        claim_number = f"CLM-{uuid.uuid4().hex[:8].upper()}"
        
        claim_data['claim_number'] = claim_number
        claim_data['claim_date'] = datetime.utcnow()
        
        status_data = {
            'claim_number': claim_number,
            'status': 'PENDING'
        }
        
        return self.claim_dal.create_claim(claim_data, status_data)

    def get_claim_status(self, claim_number, policy_number, customer_id):
        return self.claim_dal.get_claim(claim_number, policy_number, customer_id)