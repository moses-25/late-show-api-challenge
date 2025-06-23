from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config')
    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)
    # Register Blueprints here later
    return app

app = create_app()

