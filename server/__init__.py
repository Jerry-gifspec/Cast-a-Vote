from flask import Flask
from flask_cors import CORS
from .database import db, init_db, shutdown_session
from config import Config

def create_app():
    """Application factory function"""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)
    
    # Initialize CORS
    CORS(app)
    
    # Initialize database
    db.init_app(app)
    
    # Register teardown function
    app.teardown_appcontext(shutdown_session)
    
    # Import and register blueprints
    from .routes.auth_routes import auth_bp
    from .routes.voter_routes import voter_bp
    from .routes.admin_routes import admin_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(voter_bp, url_prefix='/api/voter')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    
    # Initialize database tables
    with app.app_context():
        init_db()
    
    return app

# Error handlers
def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found_error(error):
        return {'message': 'Resource not found'}, 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return {'message': 'Internal server error'}, 500

# Create the application instance
app = create_app()
register_error_handlers(app)
