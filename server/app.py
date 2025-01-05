from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
import random
# from routes import routes  # Import routes (Blueprint)
# from models import db  # Import db from models.py to initialize it


# Create Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
CORS(app)
db = SQLAlchemy(app)

#  
# Define database models
class Voter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    aadhar_number = db.Column(db.String(12), unique=True, nullable=False)
    voter_id = db.Column(db.String(50), unique=True, nullable=True)  # Optional field

    def __init__(self, username, email, password, aadhar_number):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.aadhar_number = aadhar_number

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Check for missing fields
        if not username or not email or not password:
            return jsonify({"error": "Missing required fields"}), 400

        # Check if the user already exists
        existing_voter = Voter.query.filter((Voter.username == username) | (Voter.email == email)).first()
        if existing_voter:
            return jsonify({"error": "Voter with this email or username already exists"}), 409

        # Generate Aadhar number
        aadhar_number = str(random.randint(100000000000, 999999999999))

        # Create and save the voter
        new_voter = Voter(username=username, email=email, password=password, aadhar_number=aadhar_number)
        db.session.add(new_voter)
        db.session.commit()

        return jsonify({"message": "Signup successful!", "aadhar_number": aadhar_number}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API!"}), 200


if __name__ == '__main__':
    app.run(debug=True)
