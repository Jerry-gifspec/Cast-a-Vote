from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Initialize SQLAlchemy instance
db = SQLAlchemy()

# Database configuration
DATABASE_URL = "mysql+pymysql://root:@localhost/votingsystemdb"  

# Create engine
engine = create_engine(DATABASE_URL)

# Create db session
db_session = scoped_session(sessionmaker(autocommit=False,
                                       autoflush=False,
                                       bind=engine))

# Create base model
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    """Initialize the database and create all tables"""
    try:
        # Import all models here to ensure they are registered
        from models import Admin, Voter, Position, Candidate, Vote
        Base.metadata.create_all(bind=engine)
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")

def shutdown_session(exception=None):
    """Close the database session"""
    db_session.remove()



   