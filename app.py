from flask import Flask, render_template
from database import db
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'your-secret-key-here'
    
    # Initialize database with app
    db.init_app(app)
    
    # Import models to ensure they're registered
    from models import User, UserSession, AppData
    
    # Import and register blueprints after app creation
    from api import api_bp
    from database_api import database_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(database_bp, url_prefix='/api/database')
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()
        print(f"Database created at: {os.path.abspath('database.db')}")
    
    return app

app = create_app()

if __name__ == '__main__':
    # Database is already created in create_app()
    app.run(debug=True)
