from flask import Blueprint, jsonify

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route("/",methods=["GET"])
def index():
    return jsonify({"message": "Bienvenido a la API de Flask!",
                    "status": "success"}), 200