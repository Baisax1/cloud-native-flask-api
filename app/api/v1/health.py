from flask import Blueprint, jsonify
import os

health_blueprint = Blueprint("health", __name__, url_prefix = "/api/v1")

@health_blueprint.route("/health", methods=["GET"])
def health_check():
    return jsonify({"message": "La API funciona",
                    "status": "healthy",
                    "environment": os.getenv("FLASK_ENV")}),200