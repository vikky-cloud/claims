from models.models import Policy, db

class PolicyDAL:
    @staticmethod
    def create_policy(policy_data):
        policy = Policy(**policy_data)
        db.session.add(policy)
        db.session.commit()
        return policy

    @staticmethod
    def get_policies_by_customer(customer_id):
        return Policy.query.filter_by(customer_id=customer_id).all()

    @staticmethod
    def get_policy_by_vehicle(vehicle_registration_number):
        return Policy.query.filter_by(vehicle_registration_number=vehicle_registration_number).first()