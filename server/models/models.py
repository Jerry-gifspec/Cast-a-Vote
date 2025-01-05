from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import random
import string

db = SQLAlchemy()

# Voter Model
class Voter(db.Model):
    __tablename__ = 'voter'

    voter_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    aadhar_number = db.Column(db.String(12), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    has_voted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    votes = db.relationship('Vote', backref='voter', lazy=True)

    # Password management
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Serialize to JSON-friendly format
    def serialize(self):
        return {
            'voter_id': self.voter_id,
            'name': self.name,
            'aadhar_number': self.aadhar_number,
            'is_admin': self.is_admin,
            'has_voted': self.has_voted,
            'created_at': self.created_at.isoformat(),
        }

    def __repr__(self):
        return f'<Voter {self.name}>'

# Admin Model
class Admin(db.Model):
    __tablename__ = 'admin'

    admin_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    aadhar_number = db.Column(db.String(12), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Password management
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Serialize to JSON-friendly format
    def serialize(self):
        return {
            'admin_id': self.admin_id,
            'name': self.name,
            'aadhar_number': self.aadhar_number,
            'created_at': self.created_at.isoformat(),
        }

    def __repr__(self):
        return f'<Admin {self.name}>'

# Position Model
class Position(db.Model):
    __tablename__ = 'positions'

    position_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    position_name = db.Column(db.String(100), nullable=False)

    # Relationship with candidates
    candidates = db.relationship('Candidate', backref='position', lazy=True)

    def serialize(self):
        return {
            'position_id': self.position_id,
            'position_name': self.position_name,
        }

    def __repr__(self):
        return f'<Position {self.position_name}>'

# Candidate Model
class Candidate(db.Model):
    __tablename__ = 'candidates'

    candidate_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('positions.position_id'), nullable=False)
    nationality = db.Column(db.String(100), nullable=False)
    policy = db.Column(db.Text, nullable=False)
    votes_count = db.Column(db.Integer, default=0)

    def serialize(self):
        return {
            'candidate_id': self.candidate_id,
            'name': self.name,
            'age': self.age,
            'city': self.city,
            'contact': self.contact,
            'position_id': self.position_id,
            'nationality': self.nationality,
            'policy': self.policy,
            'votes_count': self.votes_count,
        }

    def __repr__(self):
        return f'<Candidate {self.name}>'

# Vote Model
class Vote(db.Model):
    __tablename__ = 'votes'

    vote_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    voter_id = db.Column(db.Integer, db.ForeignKey('voter.voter_id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            'vote_id': self.vote_id,
            'voter_id': self.voter_id,
            'candidate_id': self.candidate_id,
            'timestamp': self.timestamp.isoformat(),
        }

    def __repr__(self):
        return f'<Vote voter_id={self.voter_id}, candidate_id={self.candidate_id}>'

# Function to generate aadhar number
def generate_aadhar():
    """Generate a 12-digit Aadhar number"""
    return ''.join(random.choices(string.digits, k=12))


