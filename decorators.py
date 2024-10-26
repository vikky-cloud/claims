from functools import wraps
from flask import request, jsonify
import jwt
from config import Config
from dal.customer_dal import CustomerDAL

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        
        try:
            token = token.split()[1]
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            current_user = CustomerDAL.get_customer_by_id(data['customer_id'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated
