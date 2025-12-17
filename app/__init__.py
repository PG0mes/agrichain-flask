from flask import Flask
from flask_login import LoginManager
from config import Config

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = "Por favor, faça login para acessar."

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    login_manager.init_app(app)

    # Registrar Blueprints
    from app.routes import main, auth, products
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(products.bp)

    from app.models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    return app