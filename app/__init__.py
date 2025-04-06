from flask import Flask
from flask_login import LoginManager
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Setup the user_loader
    from app.models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)
    
    # Import and register blueprints
    from app.routes.auth import auth_bp as auth
    from app.routes.main import main
    from app.routes.tracking import tracking
    from app.routes.rewards import rewards
    
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(tracking)
    app.register_blueprint(rewards)
    
    return app 