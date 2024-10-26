from dal.policy_dal import PolicyDAL
from datetime import datetime, timedelta
import uuid

class PolicyService:
    def __init__(self):
        self.policy_dal = PolicyDAL()

    def create_policy(self, policy_data, customer_id):
        policy_data['policy_number'] = f"POL-{uuid.uuid4().hex[:8].upper()}"
        policy_data['customer_id'] = customer_id
        policy_data['policy_limit'] = float(policy_data['vehicle_price']) * 0.8
        policy_data['deductible'] = float(policy_data['vehicle_price']) * 0.05
        policy_data['expiration_date'] = datetime.utcnow() + timedelta(days=365)
        
        return self.policy_dal.create_policy(policy_data)

    def get_customer_policies(self, customer_id):
        return self.policy_dal.get_policies_by_customer(customer_id)