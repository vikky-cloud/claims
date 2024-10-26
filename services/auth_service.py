from dal.customer_dal import CustomerDAL
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime
import uuid
from config import Config
import logging

class AuthService:
    def __init__(self):
        self.customer_dal = CustomerDAL()
        logging.basicConfig(level=logging.DEBUG)

    def register_customer(self, customer_data):
        try:
            # Check if the email is already registered
            existing_customer = self.customer_dal.get_customer_by_email(customer_data['email'])
            if existing_customer:
                logging.debug("Email already in use: %s", customer_data['email'])
                return {"error": "Email already in use."}, 409
            
            # Check for existing phone number
            existing_customer_by_phone = self.customer_dal.get_customer_by_phone(customer_data['phone'])
            if existing_customer_by_phone:
                logging.debug("Phone number already in use: %s", customer_data['phone'])
                return {"error": "Phone number already in use."}, 409

            # Generate a new customer ID and hash the password
            customer_data['customer_id'] = str(uuid.uuid4())
            customer_data['password'] = generate_password_hash(customer_data['password'], method='pbkdf2:sha256')

            # Create the new customer
            self.customer_dal.create_customer(customer_data)
            logging.debug("Customer registered successfully: %s", customer_data['customer_id'])

            return {"message": "Registration successful."}, 201

        except Exception as e:
            # Log any unexpected errors
            logging.error("An error occurred during registration: %s", str(e))
            return {"error": "Registration failed due to an internal error."}, 500

    def login(self, email, password):
        customer = self.customer_dal.get_customer_by_email(email)
        if not customer or not check_password_hash(customer.password, password):
            logging.debug("Invalid login attempt for email: %s", email)
            return {"error": "Invalid email or password."}, 401  # Return error message with 401 status code

        token = jwt.encode({
            'customer_id': customer.customer_id,
            'exp': datetime.utcnow() + Config.JWT_EXPIRATION
        }, Config.SECRET_KEY, algorithm="HS256")

        logging.info("Successful login for customer: %s", email)
        return {"message":"Login Successful","token": token}, 200  # Return the token and a 200 status code