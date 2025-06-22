from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.models import db
import server.config as config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)
    
    # Import and register controllers
    from server.controllers.guest_controller import guest_bp
    app.register_blueprint(guest_bp)

    return app

app = create_app()
