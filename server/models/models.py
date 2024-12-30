# models.py
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


db = SQLAlchemy()

class Voter(db.Model):
    __tablename__ = 'voters'
    
    voter_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    aadhar_number = db.Column(db.String(12), unique=True, nullable=False)  # Updated length
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
            'created_at': self.created_at.isoformat()
        }

    def __repr__(self):
        return f'<Voter {self.name}>'
    class Position(db.Model):
        __tablename__ = 'positions'
    
    position_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    position_name = db.Column(db.String(100), nullable=False)
    
    # Relationship with candidates
    candidates = db.relationship('Candidate', backref='position', lazy=True)

    def __repr__(self):
        return f'<Position {self.position_name}>'

class Candidate(db.Model):
    __tablename__ = 'candidates'
    
    candidate_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('positions.position_id'), nullable=False)
    
    # Relationship with votes
    votes = db.relationship('Vote', backref='candidate', lazy=True)

    def __repr__(self):
        return f'<Candidate {self.name}>'

class Vote(db.Model):
    __tablename__ = 'votes'
    
    vote_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    voter_id = db.Column(db.Integer, db.ForeignKey('voters.voter_id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    timestamp = db.Column(db.TIMESTAMP, default=datetime.utcnow)

def generate_aadhar():
    """Generate a 6-digit Aadhar number"""
    return ''.join(random.choices(string.digits, k=6))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)
    aadhar_number = db.Column(db.String(12), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    has_voted = db.Column(db.Boolean, default=False)

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    nationality = db.Column(db.String(100), nullable=False)
    policy = db.Column(db.Text, nullable=False)
    votes = db.Column(db.Integer, default=0)
    aadhar_number = db.Column(db.String(12), unique=True, nullable=False)
