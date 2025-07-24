from flask import Blueprint, request, jsonify, current_app
from sqlalchemy.orm import Session
from datetime import datetime
import os
import uuid

from ..models.gallery import GalleryItem
from ..database.database import SessionLocal, engine, Base

gallery_bp = Blueprint('gallery', __name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

UPLOAD_FOLDER = 'src/static/uploads/gallery'

@gallery_bp.route("/gallery", methods=["POST"])
def create_gallery_item():
    db = next(get_db())
    title = request.form.get('title')
    category = request.form.get('category')
    file = request.files.get('file')

    if not title or not category or not file:
        return jsonify({"message": "Title, category, and file are required"}), 400

    if file:
        # Ensure the upload directory exists
        upload_path = os.path.join(current_app.root_path, UPLOAD_FOLDER)
        os.makedirs(upload_path, exist_ok=True)

        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        file_location = os.path.join(upload_path, filename)
        file.save(file_location)
        image_url = f"/static/uploads/gallery/{filename}"
    else:
        return jsonify({"message": "File not provided"}), 400

    db_gallery_item = GalleryItem(title=title, category=category, image_url=image_url, uploaded_at=datetime.utcnow())
    db.add(db_gallery_item)
    db.commit()
    db.refresh(db_gallery_item)
    return jsonify({
        "id": db_gallery_item.id,
        "title": db_gallery_item.title,
        "category": db_gallery_item.category,
        "image_url": db_gallery_item.image_url,
        "uploaded_at": db_gallery_item.uploaded_at.isoformat()
    }), 201

@gallery_bp.route("/gallery", methods=["GET"])
def read_gallery_items():
    db = next(get_db())
    gallery_items = db.query(GalleryItem).order_by(GalleryItem.uploaded_at.desc()).all()
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
    db = next(get_db())
    item = db.query(GalleryItem).filter(GalleryItem.id == gallery_item_id).first()
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
    db = next(get_db())
    db_gallery_item = db.query(GalleryItem).filter(GalleryItem.id == gallery_item_id).first()
    if db_gallery_item is None:
        return jsonify({"message": "Gallery item not found"}), 404
    
    title = request.form.get('title', db_gallery_item.title)
    category = request.form.get('category', db_gallery_item.category)
    file = request.files.get('file')

    db_gallery_item.title = title
    db_gallery_item.category = category

    if file:
        # Delete old file if it exists
        if db_gallery_item.image_url and os.path.exists(os.path.join(current_app.root_path, db_gallery_item.image_url.lstrip('/'))):
            os.remove(os.path.join(current_app.root_path, db_gallery_item.image_url.lstrip('/')))

        upload_path = os.path.join(current_app.root_path, UPLOAD_FOLDER)
        os.makedirs(upload_path, exist_ok=True)
        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        file_location = os.path.join(upload_path, filename)
        file.save(file_location)
        db_gallery_item.image_url = f"/static/uploads/gallery/{filename}"

    db.commit()
    db.refresh(db_gallery_item)
    return jsonify({
        "id": db_gallery_item.id,
        "title": db_gallery_item.title,
        "category": db_gallery_item.category,
        "image_url": db_gallery_item.image_url,
        "uploaded_at": db_gallery_item.uploaded_at.isoformat()
    })

@gallery_bp.route("/gallery/<int:gallery_item_id>", methods=["DELETE"])
def delete_gallery_item(gallery_item_id: int):
    db = next(get_db())
    db_gallery_item = db.query(GalleryItem).filter(GalleryItem.id == gallery_item_id).first()
    if db_gallery_item is None:
        return jsonify({"message": "Gallery item not found"}), 404
    
    # Delete the file from the server
    if db_gallery_item.image_url and os.path.exists(os.path.join(current_app.root_path, db_gallery_item.image_url.lstrip('/'))):
        os.remove(os.path.join(current_app.root_path, db_gallery_item.image_url.lstrip('/')))

    db.delete(db_gallery_item)
    db.commit()
    return jsonify({"message": "Gallery item deleted successfully"}), 200