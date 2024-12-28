from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import random

db = SQLAlchemy()
def generate_aadhar():
    return "".join([str(random.randint(0, 9)) for _ in range(12)])

class Voter(db.Model):
    __tablename__ = "voters"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False, unique=True)
    aadhar = db.Column(db.String(12), unique=True, default=generate_aadhar)

    def __init__(self, name, city, contact, aadhar):
        self.name = name
        self.city = city
        self.contact = contact
        self.aadhar = aadhar

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "contact": self.contact,
            "aadhar": self.aadhar,
        }

class Candidate(db.Model):
    __tablename__ = "candidates"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False, unique=True)
    position = db.Column(db.String(100), nullable=False)
    nationality = db.Column(db.String(100), nullable=False)
    policy = db.Column(db.Text, nullable=False)

    def __init__(self, name, age, city, contact, position, nationality, policy):
        self.name = name
        self.age = age
        self.city = city
        self.contact = contact
        self.position = position
        self.nationality = nationality
        self.policy = policy

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "city": self.city,
            "contact": self.contact,
            "position": self.position,
            "nationality": self.nationality,
            "policy": self.policy,
        }
