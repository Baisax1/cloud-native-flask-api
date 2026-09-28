from flask import Flask
from config import config_by_name
from app.routes.home import home_blueprint
from app.api.v1.health import health_blueprint
import os

def create_app(config_name=None):
    if not config_name:
        config_name = os.getenv("FLASK_ENV","default")
        
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_blueprint(home_blueprint)
    app.register_blueprint(health_blueprint)

    return app