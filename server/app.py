from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Create Flask app
app = Flask(__name__)
app.config.from_object(Config)

from routes import *
from models import *

# Initialize extensions
CORS(app)
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
