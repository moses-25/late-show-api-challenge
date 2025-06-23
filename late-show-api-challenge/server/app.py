from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.models import db
from server.controllers.auth_controller import auth_bp
from server.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config')
    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)
    app.register_blueprint(auth_bp)

    # Register Blueprints here later
    return app

app = create_app()

