from app import app, bcrypt
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from server import create_app
from server.models.models.admin import Admin
from server.models. models.voter import Voter
from server.config.database import db

signup_routes = Blueprint("signup_routes", __name__)

app = create_app()

@signup_routes.route('/signup', methods=['POST'])
def signup():
    data = request.json
    role = data.get('role')

    if role == "admin":
        admin = Admin(username=data['name'], password=data['password'])
        db.session.add(admin)
    elif role == "voter":
        voter = Voter(name=data['name'], city="Unknown", contact="Unknown", aadhar="Generated_Aadhar")
        db.session.add(voter)

    db.session.commit()
    return jsonify({"message": f"{role.capitalize()} registered successfully!"})

@routes.route('/api/register-voter', methods=['POST'])
def register_voter():
    data = request.json
    aadhar = generate_aadhar()  # Implement Aadhaar generation logic
    new_voter = Voter(name=data['name'], city=data['city'], contact=data['contact'], aadhar=aadhar)
    db.session.add(new_voter)
    db.session.commit()
    return jsonify({"aadhar": aadhar})

@routes.route('/api/register-candidate', methods=['POST'])
def register_candidate():
    data = request.json
    new_candidate = Candidate(
        name=data['name'],
        age=data['age'],
        city=data['city'],
        contact=data['contact'],
        position=data['position'],
        nationality=data['nationality'],
        policy=data['policy'],
    )
    db.session.add(new_candidate)
    db.session.commit()
    return jsonify({"message": "Candidate registered successfully!"})

