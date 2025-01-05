from flask import request, jsonify
from functools import wraps
import jwt
from datetime import datetime, timedelta
from ..models import Admin, voter  # Use the correct models
from ..config import Config

def get_user_by_token(token_data):
    user_id = token_data.get('user_id')
    user_type = token_data.get('user_type')  # Assume 'user_type' is part of the token payload
    if user_type == 'admin':
        return Admin.query.get(user_id)
    elif user_type == 'voter':
        return voter.query.get(user_id)
    return None

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or not token.startswith('Bearer '):
            return jsonify({'message': 'Token is missing or invalid format'}), 401
        
        token = token.split(' ')[1]
        data = decode_token(token)
        if 'error' in data:
            return jsonify({'message': data['error']}), 401
        
        current_user = get_user_by_token(data)
        if not current_user:
            return jsonify({'message': 'Invalid token'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or not token.startswith('Bearer '):
            return jsonify({'message': 'Token is missing or invalid format'}), 401
        
        token = token.split(' ')[1]
        data = decode_token(token)
        if 'error' in data:
            return jsonify({'message': data['error']}), 401
        
        current_user = get_user_by_token(data)
        if not current_user or not getattr(current_user, 'is_admin', False):
            return jsonify({'message': 'Admin privileges required'}), 403
        
        return f(current_user, *args, **kwargs)
    return decorated

def decode_token(token):
    try:
        return jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return {'error': 'Token has expired'}
    except jwt.InvalidTokenError:
        return {'error': 'Invalid token'}
    except Exception as e:
        return {'error': f'An error occurred: {str(e)}'}
