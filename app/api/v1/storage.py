from flask import Blueprint, jsonify, request
from app.services.s3_service import create_bucket, upload_file, list_files_bucket

storage_blueprint = Blueprint("storage", __name__, url_prefix = "/api/v1/storage")

@storage_blueprint.route("/buckets", methods = ["POST"])
def handle_create_bucket():
    data = request.get_json() or {}
    bucket_name = data.get("bucket_name")
    
    if not bucket_name:
        return jsonify({"error": "El nombre del bucket es requerido", 
                        "success": False
                        }), 400
    
    result = create_bucket(bucket_name)
    status_code = 201 if result["success"] else 400
    return jsonify(result), status_code
    
@storage_blueprint.route("/upload", methods=["POST"])
def handle_upload_file():
    data = request.get_json() or {}
    bucket_name = data.get("bucket_name")
    file_name = data.get("file_name")
    content = data.get("content")
    
    if not bucket_name or not file_name or not content:
        return jsonify({"error": "Faltan parametros",
                        "success": False
                        }),400
    
    result = upload_file(file_name, bucket_name, content)
    status_code = 201 if result["success"] else 400
    return jsonify(result), status_code

@storage_blueprint.route("/buckets/<bucket_name>/files", methods=["GET"])
def handle_list_files(bucket_name):
    result = list_files_bucket(bucket_name)
    status_code = 200 if result.get("success") else 400
    return jsonify(result), status_code