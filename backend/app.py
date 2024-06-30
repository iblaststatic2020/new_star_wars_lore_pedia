from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from config import Config
from models import db

login_manager = LoginManager()

def create_app():
    app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')

     # Load configuration from config.py
    app.config.from_object(Config)

    # Initialize CORS
    CORS(app)

    # Initialize SQLAlchemy
    db.init_app(app)
    
    # Initialize Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = 'login'

   # Create database tables if they don't exist
    with app.app_context():
        from models import User, Article  # Import models here
        db.create_all()

    # Register main blueprint
    from routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

# Callback function to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    from models import User  # Import here to avoid circular import issues
    return User.query.get(int(user_id))

# Run the app if this script is executed directly
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)