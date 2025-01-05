from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
import jwt
from models import db, Voter, Admin
from functools import wraps
from config import Config  # Assuming you have a config.py file with your SECRET_KEY

# Initialize Blueprint
auth_bp = Blueprint('auth', __name__)

# Token required decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            # Remove 'Bearer ' from token
            token = token.split(' ')[1]
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
            current_user = Voter.query.get(data['user_id']) or Admin.query.get(data['user_id'])
            if not current_user:
                return jsonify({'message': 'Invalid token'}), 401
        except Exception as e:
            print(e)
            return jsonify({'message': 'Invalid token'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

# Admin Registration Route
@auth_bp.route('/admin/register', methods=['POST'])
def register_admin():
    data = request.get_json()
    name = data.get('name')
    aadhar_number = data.get('aadhar_number')
    password = data.get('password')

    if not name or not aadhar_number or not password:
        return jsonify({'message': 'Missing required fields'}), 400

    # Check if admin already exists
    if Admin.query.filter_by(aadhar_number=aadhar_number).first():
        return jsonify({'message': 'Admin already exists'}), 400

    # Create new admin
    new_admin = Admin(name=name, aadhar_number=aadhar_number)
    new_admin.set_password(password)

    try:
        db.session.add(new_admin)
        db.session.commit()
        return jsonify({'message': 'Admin registered successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Admin Login Route
@auth_bp.route('/admin/login', methods=['POST'])
def login_admin():
    data = request.get_json()
    aadhar_number = data.get('aadhar_number')
    password = data.get('password')

    admin = Admin.query.filter_by(aadhar_number=aadhar_number).first()
    if not admin or not admin.check_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401

    # Generate JWT token
    token = jwt.encode({'user_id': admin.admin_id, 'exp': datetime.utcnow() + timedelta(hours=1)}, Config.SECRET_KEY, algorithm='HS256')

    return jsonify({'message': 'Login successful', 'token': token})

# Voter Registration Route
@auth_bp.route('/voter/register', methods=['POST'])
def register_voter():
    data = request.get_json()
    name = data.get('name')
    aadhar_number = data.get('aadhar_number')
    password = data.get('password')

    if not name or not aadhar_number or not password:
        return jsonify({'message': 'Missing required fields'}), 400

    # Check if voter already exists
    if Voter.query.filter_by(aadhar_number=aadhar_number).first():
        return jsonify({'message': 'Voter already exists'}), 400

    # Create new voter
    new_voter = Voter(name=name, aadhar_number=aadhar_number)
    new_voter.set_password(password)

    try:
        db.session.add(new_voter)
        db.session.commit()
        return jsonify({'message': 'Voter registered successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Voter Login Route
@auth_bp.route('/voter/login', methods=['POST'])
def login_voter():
    data = request.get_json()
    aadhar_number = data.get('aadhar_number')
    password = data.get('password')

    voter = Voter.query.filter_by(aadhar_number=aadhar_number).first()
    if not voter or not voter.check_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401

    # Generate JWT token
    token = jwt.encode({'user_id': voter.voter_id, 'exp': datetime.utcnow() + timedelta(hours=1)}, Config.SECRET_KEY, algorithm='HS256')

    return jsonify({'message': 'Login successful', 'token': token})

# Check if voter has voted
@auth_bp.route('/voter/has_voted', methods=['GET'])
@token_required
def has_voted(current_user):
    if isinstance(current_user, Voter):
        return jsonify({'has_voted': current_user.has_voted})
    return jsonify({'message': 'Unauthorized access'}), 403

# View all voters (for admin)
@auth_bp.route('/admin/voters', methods=['GET'])
@token_required
def view_voters(current_user):
    if isinstance(current_user, Admin):
        voters = Voter.query.all()
        return jsonify([voter.serialize() for voter in voters]), 200
    return jsonify({'message': 'Admin privileges required'}), 403

# View all admins (for admin)
@auth_bp.route('/admin/admins', methods=['GET'])
@token_required
def view_admins(current_user):
    if isinstance(current_user, Admin):
        admins = Admin.query.all()
        return jsonify([admin.serialize() for admin in admins]), 200
    return jsonify({'message': 'Admin privileges required'}), 403
