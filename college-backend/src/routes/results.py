from flask import Blueprint, request, jsonify, current_app
from datetime import datetime
import os
import uuid
import boto3
from botocore.exceptions import NoCredentialsError

from ..models.result import Result
from ..models.user import db

results_bp = Blueprint('results', __name__)

def get_db():
    return db.session

# S3 Configuration
S3_BUCKET = os.environ.get('S3_BUCKET_NAME')
S3_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
S3_SECRET = os.environ.get('AWS_SECRET_ACCESS_KEY')
S3_REGION = os.environ.get('S3_REGION')

s3 = boto3.client(
    's3',
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET,
    region_name=S3_REGION
)

@results_bp.route("/results", methods=["POST"])
# @login_required # Add your authentication decorator here
def create_result():
    session = get_db()
    title = request.form.get('title')
    file = request.files.get('file')

    if not title or not file:
        return jsonify({"message": "Title and file are required"}), 400

    if file:
        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        s3_file_path = f"uploads/results/{filename}"
        
        try:
            s3.upload_fileobj(file, S3_BUCKET, s3_file_path,
                              ExtraArgs={'ContentType': file.content_type})
            file_url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{s3_file_path}"
        except NoCredentialsError:
            return jsonify({"message": "Credentials not available"}), 500
        except Exception as e:
            return jsonify({"message": f"Error uploading file to S3: {str(e)}"}), 500
    else:
        return jsonify({"message": "File not provided"}), 400

    db_result = Result(title=title, file_url=file_url, uploaded_at=datetime.utcnow())
    session.add(db_result)
    session.commit()
    session.refresh(db_result)
    return jsonify({
        "id": db_result.id,
        "title": db_result.title,
        "file_url": db_result.file_url,
        "uploaded_at": db_result.uploaded_at.isoformat()
    }), 201

@results_bp.route("/results", methods=["GET"])
def read_results():
    session = get_db()
    results = session.query(Result).order_by(Result.uploaded_at.desc()).all()
    return jsonify([
        {
            "id": item.id,
            "title": item.title,
            "file_url": item.file_url,
            "uploaded_at": item.uploaded_at.isoformat()
        } for item in results
    ])

@results_bp.route("/results/<int:result_id>", methods=["GET"])
def read_result(result_id: int):
    session = get_db()
    item = session.query(Result).filter(Result.id == result_id).first()
    if item is None:
        return jsonify({"message": "Result not found"}), 404
    return jsonify({
        "id": item.id,
        "title": item.title,
        "file_url": item.file_url,
        "uploaded_at": item.uploaded_at.isoformat()
    })

@results_bp.route("/results/<int:result_id>", methods=["PUT"])
def update_result(result_id: int):
    session = get_db()
    db_result = session.query(Result).filter(Result.id == result_id).first()
    if db_result is None:
        return jsonify({"message": "Result not found"}), 404
    
    title = request.form.get('title', db_result.title)
    file = request.files.get('file')

    db_result.title = title

    if file:
        # Delete old file from S3 if it exists
        if db_result.file_url:
            old_filename = db_result.file_url.split('/')[-1]
            old_s3_file_path = f"uploads/results/{old_filename}"
            try:
                s3.delete_object(Bucket=S3_BUCKET, Key=old_s3_file_path)
            except Exception as e:
                print(f"Error deleting old file from S3: {str(e)}")

        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        s3_file_path = f"uploads/results/{filename}"
        try:
            s3.upload_fileobj(file, S3_BUCKET, s3_file_path,
                              ExtraArgs={'ContentType': file.content_type})
            db_result.file_url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{s3_file_path}"
        except NoCredentialsError:
            return jsonify({"message": "Credentials not available"}), 500
        except Exception as e:
            return jsonify({"message": f"Error uploading new file to S3: {str(e)}"}), 500

    session.commit()
    session.refresh(db_result)
    return jsonify({
        "id": db_result.id,
        "title": db_result.title,
        "file_url": db_result.file_url,
        "uploaded_at": db_result.uploaded_at.isoformat()
    })

@results_bp.route("/results/<int:result_id>", methods=["DELETE"])
def delete_result(result_id: int):
    session = get_db()
    db_result = session.query(Result).filter(Result.id == result_id).first()
    if db_result is None:
        return jsonify({"message": "Result not found"}), 404
    
    # Delete the file from S3
    if db_result.file_url:
        filename = db_result.file_url.split('/')[-1]
        s3_file_path = f"uploads/results/{filename}"
        try:
            s3.delete_object(Bucket=S3_BUCKET, Key=s3_file_path)
        except Exception as e:
            print(f"Error deleting file from S3: {str(e)}")

    session.delete(db_result)
    session.commit()
    return jsonify({"message": "Result deleted successfully"}), 200