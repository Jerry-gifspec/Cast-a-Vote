from flask import Flask, request, jsonify
from flask_cors import CORS
from server.models.models import db, Voter, Candidate
import os

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for cross-origin requests

    # Configure the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/votingsystemdb'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize the database
    db.init_app(app)

    # Create tables if they do not exist
    with app.app_context():
        db.create_all()

    # Register routes
    @app.route('/api/login', methods=['POST'])
    def login():
        data = request.json
        username_or_aadhar = data.get('usernameOrAadhar')
        password = data.get('password')

        # Mock authentication logic
        if username_or_aadhar == "test" and password == "password123":
            return jsonify({"token": "mock-jwt-token"}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401

    # Register voter
    @app.route('/api/voter/register', methods=['POST'])
    def register_voter():
        data = request.json
        try:
            new_voter = Voter(
                name=data["name"],
                city=data["city"],
                contact=data["contact"],
                aadhar=data["aadhar"]  # You can generate Aadhaar here if needed
            )
            db.session.add(new_voter)
            db.session.commit()
            return jsonify({"message": "Voter registered successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    # Register candidate
    @app.route('/api/candidate/register', methods=['POST'])
    def register_candidate():
        data = request.json
        try:
            new_candidate = Candidate(
                name=data["name"],
                age=data["age"],
                city=data["city"],
                contact=data["contact"],
                position=data["position"],
                nationality=data["nationality"],
                policy=data["policy"]
            )
            db.session.add(new_candidate)
            db.session.commit()
            return jsonify({"message": "Candidate registered successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    # Get all voters (Admin purpose)
    @app.route('/api/voters', methods=['GET'])
    def get_voters():
        voters = Voter.query.all()
        return jsonify([voter.serialize() for voter in voters]), 200

    # Get all candidates (Admin purpose)
    @app.route('/api/candidates', methods=['GET'])
    def get_candidates():
        candidates = Candidate.query.all()
        return jsonify([candidate.serialize() for candidate in candidates]), 200

    return app

from server import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
