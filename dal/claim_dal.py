from models.models import Claim, ClaimStatus, db

class ClaimDAL:
    @staticmethod
    def create_claim(claim_data, status_data):
        claim = Claim(**claim_data)
        db.session.add(claim)
        db.session.flush()
        
        status = ClaimStatus(**status_data)
        db.session.add(status)
        db.session.commit()
        return claim

    @staticmethod
    def get_claim(claim_number, policy_number, customer_id):
        return Claim.query.filter_by(
            claim_number=claim_number,
            policy_number=policy_number,
            customer_id=customer_id
        ).first()