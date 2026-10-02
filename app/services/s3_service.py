import os
import boto3
from botocore.exceptions import ClientError

def get_s3_client():
    return boto3.client(
        "s3",
        endpoint_url=os.getenv("AWS_ENDPOINT_URL","http://localhost:4566"),
        region_name=os.getenv("AWS_DEFAULT_REGION","us-east-1"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID","test"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY","test")
    )
    
    
def create_bucket(bucket_name):
    s3 = get_s3_client()
    try:
        s3.create_bucket(Bucket=bucket_name)
        return {"message": f"Bucket '{bucket_name}' creado exitosamente.", "success": True}
    except ClientError as e:
        return {"error": str(e), "success": False}
        
def upload_file(file_name, bucket_name, content):
    s3 = get_s3_client()
    try:
        s3.put_object(Bucket=bucket_name,Key=file_name,Body=content)
        return {"message": f"Archivo '{file_name}' subido exitosamente al bucket '{bucket_name}'.", "success": True}
    except ClientError as e:
        return {"error": str(e), "success": False}
    
def list_files_bucket(bucket_name):
    s3=get_s3_client()
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        files= [item["Key"] for item in response.get("Contents",[])]
        return {"files": files, "count": len(files),  "success": True}
    except ClientError as e:
        return {"error": str(e), "success": False}