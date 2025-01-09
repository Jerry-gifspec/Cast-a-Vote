from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import bcrypt
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/votingsystemdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('voter', 'admin'), nullable=False)
    aadhar_number = db.Column(db.String(12), unique=True, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'

# Create tables
with app.app_context():
    db.create_all()

def generate_aadhar_number():
    """Generate a random 12-digit Aadhar number"""
    return str(random.randint(100000000000, 999999999999))

def validate_signup_data(data):
    """Validate signup input data"""
    if not all(key in data for key in ['username', 'email', 'password']):
        return False, "Missing required fields"
    
    if len(data['password']) < 6:
        return False, "Password must be at least 6 characters long"
    
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, data['email']):
        return False, "Invalid email format"
    
    if 'role' in data and data['role'] not in ['voter', 'admin']:
        return False, "Invalid role"
    
    return True, None

@app.route('/api/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()

        # Validate input data
        is_valid, error_message = validate_signup_data(data)
        if not is_valid:
            return jsonify({'message': error_message}), 400

        # Check if user already exists
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'message': 'Email already registered'}), 409
        
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'message': 'Username already taken'}), 409

        # Hash password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), salt)

        # Create new user
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=hashed_password.decode('utf-8'),
            role=data.get('role', 'voter')
        )

        # Generate Aadhar number for voters
        if new_user.role == 'voter':
            while True:
                aadhar = generate_aadhar_number()
                if not User.query.filter_by(aadhar_number=aadhar).first():
                    new_user.aadhar_number = aadhar
                    break

        # Save to database
        db.session.add(new_user)
        db.session.commit()

        # Prepare response
        response = {
            'message': 'User registered successfully',
            'role': new_user.role
        }
        
        if new_user.role == 'voter':
            response['aadhar_number'] = new_user.aadhar_number

        return jsonify(response), 201

    except Exception as e:
        db.session.rollback()
        print(f"Error in signup: {str(e)}")
        return jsonify({'message': 'Internal server error'}), 500


@app.route('/api/auth/voter/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')  # The username from the frontend
        aadhar_number = data.get('aadhar')  # The Aadhar number from the frontend
        password = data.get('password')

        # Ensure username, aadhar, and password are provided
        if not (username or aadhar_number) or not password:
            return jsonify({'message': 'Missing credentials'}), 400

        # Query the user based on either username or aadhar_number
        user = None
        if username:
            user = User.query.filter_by(username=username).first()
        elif aadhar_number:
            user = User.query.filter_by(aadhar_number=aadhar_number).first()

        # If user not found, return an error
        if not user:
            return jsonify({'message': 'Invalid credentials'}), 401

        # Verify password
        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return jsonify({'message': 'Invalid credentials'}), 401

        # Successful login
        response = {
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'username': user.username,
                'aadhar_number': user.aadhar_number,
                'role': user.role
            }
        }
        return jsonify(response), 200

    except Exception as e:
        print(f"Error in login: {str(e)}")
        return jsonify({'message': 'Internal server error'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
