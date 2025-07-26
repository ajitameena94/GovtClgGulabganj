from flask import Blueprint, request, jsonify, current_app
from datetime import datetime
import os
import uuid
import boto3
from botocore.exceptions import NoCredentialsError

from ..models.gallery import GalleryItem
from ..models.user import db

gallery_bp = Blueprint('gallery', __name__)

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

@gallery_bp.route("/gallery", methods=["POST"])
# @login_required # Add your authentication decorator here
def create_gallery_item():
    session = get_db()
    title = request.form.get('title')
    category = request.form.get('category')
    file = request.files.get('file')

    if not title or not category or not file:
        return jsonify({"message": "Title, category, and file are required"}), 400

    if file:
        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        s3_file_path = f"uploads/gallery/{filename}"
        
        try:
            s3.upload_fileobj(file, S3_BUCKET, s3_file_path,
                              ExtraArgs={'ContentType': file.content_type})
            image_url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{s3_file_path}"
        except NoCredentialsError:
            return jsonify({"message": "Credentials not available"}), 500
        except Exception as e:
            return jsonify({"message": f"Error uploading file to S3: {str(e)}"}), 500
    else:
        return jsonify({"message": "File not provided"}), 400

    db_gallery_item = GalleryItem(title=title, category=category, image_url=image_url, uploaded_at=datetime.utcnow())
    session.add(db_gallery_item)
    session.commit()
    session.refresh(db_gallery_item)
    return jsonify({
        "id": db_gallery_item.id,
        "title": db_gallery_item.title,
        "category": db_gallery_item.category,
        "image_url": db_gallery_item.image_url,
        "uploaded_at": db_gallery_item.uploaded_at.isoformat()
    }), 201

@gallery_bp.route("/gallery", methods=["GET"])
def read_gallery_items():
    session = get_db()
    gallery_items = session.query(GalleryItem).order_by(GalleryItem.uploaded_at.desc()).all()
    return jsonify([
        {
            "id": item.id,
            "title": item.title,
            "category": item.category,
            "image_url": item.image_url,
            "uploaded_at": item.uploaded_at.isoformat()
        } for item in gallery_items
    ])

@gallery_bp.route("/gallery/<int:gallery_item_id>", methods=["GET"])
def read_gallery_item(gallery_item_id: int):
    session = get_db()
    item = session.query(GalleryItem).filter(GalleryItem.id == gallery_item_id).first()
    if item is None:
        return jsonify({"message": "Gallery item not found"}), 404
    return jsonify({
        "id": item.id,
        "title": item.title,
        "category": item.category,
        "image_url": item.image_url,
        "uploaded_at": item.uploaded_at.isoformat()
    })

@gallery_bp.route("/gallery/<int:gallery_item_id>", methods=["PUT"])
def update_gallery_item(gallery_item_id: int):
    session = get_db()
    db_gallery_item = session.query(GalleryItem).filter(GalleryItem.id == gallery_item_id).first()
    if db_gallery_item is None:
        return jsonify({"message": "Gallery item not found"}), 404
    
    title = request.form.get('title', db_gallery_item.title)
    category = request.form.get('category', db_gallery_item.category)
    file = request.files.get('file')

    db_gallery_item.title = title
    db_gallery_item.category = category

    if file:
        # Delete old file from S3 if it exists
        if db_gallery_item.image_url:
            old_filename = db_gallery_item.image_url.split('/')[-1]
            old_s3_file_path = f"uploads/gallery/{old_filename}"
            try:
                s3.delete_object(Bucket=S3_BUCKET, Key=old_s3_file_path)
            except Exception as e:
                print(f"Error deleting old file from S3: {str(e)}")

        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        s3_file_path = f"uploads/gallery/{filename}"
        try:
            s3.upload_fileobj(file, S3_BUCKET, s3_file_path,
                              ExtraArgs={'ContentType': file.content_type})
            db_gallery_item.image_url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{s3_file_path}"
        except NoCredentialsError:
            return jsonify({"message": "Credentials not available"}), 500
        except Exception as e:
            return jsonify({"message": f"Error uploading new file to S3: {str(e)}"}), 500

    session.commit()
    session.refresh(db_gallery_item)
    return jsonify({
        "id": db_gallery_item.id,
        "title": db_gallery_item.title,
        "category": db_gallery_item.category,
        "image_url": db_gallery_item.image_url,
        "uploaded_at": db_gallery_item.uploaded_at.isoformat()
    })

@gallery_bp.route("/gallery/<int:gallery_item_id>", methods=["DELETE"])
def delete_gallery_item(gallery_item_id: int):
    session = get_db()
    db_gallery_item = session.query(GalleryItem).filter(GalleryItem.id == gallery_item_id).first()
    if db_gallery_item is None:
        return jsonify({"message": "Gallery item not found"}), 404
    
    # Delete the file from S3
    if db_gallery_item.image_url:
        filename = db_gallery_item.image_url.split('/')[-1]
        s3_file_path = f"uploads/gallery/{filename}"
        try:
            s3.delete_object(Bucket=S3_BUCKET, Key=s3_file_path)
        except Exception as e:
            print(f"Error deleting file from S3: {str(e)}")

    session.delete(db_gallery_item)
    session.commit()
    return jsonify({"message": "Gallery item deleted successfully"}), 200