from flask import Flask
from config import config_by_name
import os

def create_app(config_name=None):
    if not config_name:
        config_name = os.getenv("FLASK_ENV","default")
        
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    return app