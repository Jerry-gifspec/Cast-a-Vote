# config.py
class Config:
    SECRET_KEY = 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/votingsystemdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False