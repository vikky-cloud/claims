from models.models import Customer, db

class CustomerDAL:
    @staticmethod
    def create_customer(customer_data):
        customer = Customer(**customer_data)
        db.session.add(customer)
        db.session.commit()
        return customer

    @staticmethod
    def get_customer_by_email(email):
        return Customer.query.filter_by(email=email).first()
    
    @staticmethod
    def get_customer_by_phone(phone):
        return Customer.query.filter_by(phone=phone).first()

    @staticmethod
    def get_customer_by_id(customer_id):
        return Customer.query.filter_by(customer_id=customer_id).first()