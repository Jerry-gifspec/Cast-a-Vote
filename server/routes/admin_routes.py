# admin_routes.py
from flask import Blueprint, request, jsonify
from models import db, Election, Candidate
from flask_jwt_extended import jwt_required, get_jwt_identity

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/create_election', methods=['POST'])
@jwt_required()
def create_election():
    current_user = get_jwt_identity()
    # Assuming admin users have a role field
    if current_user.get('role') != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return jsonify({'error': 'Title and description are required'}), 400

    new_election = Election(title=title, description=description)
    db.session.add(new_election)
    db.session.commit()

    return jsonify({'message': 'Election created successfully', 'election': new_election.serialize()}), 201

@admin_bp.route('/add_candidate', methods=['POST'])
@jwt_required()
def add_candidate():
    current_user = get_jwt_identity()
    if current_user.get('role') != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    election_id = data.get('election_id')
    name = data.get('name')

    if not election_id or not name:
        return jsonify({'error': 'Election ID and candidate name are required'}), 400

    election = Election.query.get(election_id)
    if not election:
        return jsonify({'error': 'Election not found'}), 404

    new_candidate = Candidate(name=name, election_id=election_id)
    db.session.add(new_candidate)
    db.session.commit()

    return jsonify({'message': 'Candidate added successfully', 'candidate': new_candidate.serialize()}), 201
