# voter_routes.py
from flask import Blueprint, request, jsonify
from models import db, Election, Candidate, Vote
from flask_jwt_extended import jwt_required, get_jwt_identity

voter_bp = Blueprint('voter', __name__, url_prefix='/voter')

@voter_bp.route('/view_elections', methods=['GET'])
@jwt_required()
def view_elections():
    elections = Election.query.all()
    return jsonify({'elections': [election.serialize() for election in elections]}), 200

@voter_bp.route('/vote', methods=['POST'])
@jwt_required()
def vote():
    current_user = get_jwt_identity()
    voter_id = current_user.get('id')

    data = request.get_json()
    election_id = data.get('election_id')
    candidate_id = data.get('candidate_id')

    if not election_id or not candidate_id:
        return jsonify({'error': 'Election ID and candidate ID are required'}), 400

    election = Election.query.get(election_id)
    if not election:
        return jsonify({'error': 'Election not found'}), 404

    candidate = Candidate.query.get(candidate_id)
    if not candidate or candidate.election_id != election_id:
        return jsonify({'error': 'Invalid candidate for this election'}), 400

    # Ensure the voter hasn't already voted in this election
    existing_vote = Vote.query.filter_by(voter_id=voter_id, election_id=election_id).first()
    if existing_vote:
        return jsonify({'error': 'You have already voted in this election'}), 400

    new_vote = Vote(voter_id=voter_id, election_id=election_id, candidate_id=candidate_id)
    db.session.add(new_vote)
    db.session.commit()

    return jsonify({'message': 'Vote cast successfully'}), 201
