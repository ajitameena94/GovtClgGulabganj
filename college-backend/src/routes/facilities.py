from flask import Blueprint, request, jsonify, current_app
from datetime import datetime
import os
import uuid

from ..models.facility import Facility
from ..models.user import db

facilities_bp = Blueprint('facilities', __name__)

def get_db():
    return db.session

UPLOAD_FOLDER = 'src/static/uploads/facilities'

@facilities_bp.route("/facilities", methods=["POST"])
# @login_required # Add your authentication decorator here
def create_facility():
    session = get_db()
    name = request.form.get('name')
    description = request.form.get('description')
    file = request.files.get('file')

    if not name or not description or not file:
        return jsonify({"message": "Name, description, and file are required"}), 400

    if file:
        # Ensure the upload directory exists
        upload_path = os.path.join(current_app.root_path, UPLOAD_FOLDER)
        os.makedirs(upload_path, exist_ok=True)

        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        file_location = os.path.join(upload_path, filename)
        file.save(file_location)
        image_url = f"https://college-backend-api.onrender.com/static/uploads/facilities/{filename}"
    else:
        return jsonify({"message": "File not provided"}), 400

    db_facility = Facility(name=name, description=description, image_url=image_url, uploaded_at=datetime.utcnow())
    session.add(db_facility)
    session.commit()
    session.refresh(db_facility)
    return jsonify({
        "id": db_facility.id,
        "name": db_facility.name,
        "description": db_facility.description,
        "image_url": db_facility.image_url,
        "uploaded_at": db_facility.uploaded_at.isoformat()
    }), 201

@facilities_bp.route("/facilities", methods=["GET"])
def read_facilities():
    session = get_db()
    facilities = session.query(Facility).order_by(Facility.uploaded_at.desc()).all()
    return jsonify([
        {
            "id": facility.id,
            "name": facility.name,
            "description": facility.description,
            "image_url": facility.image_url if facility.image_url.startswith("http") else f"https://college-backend-api.onrender.com{facility.image_url}",
            "uploaded_at": facility.uploaded_at.isoformat()
        } for facility in facilities
    ])

@facilities_bp.route("/facilities/<int:facility_id>", methods=["GET"])
def read_facility(facility_id: int):
    session = get_db()
    facility = session.query(Facility).filter(Facility.id == facility_id).first()
    if facility is None:
        return jsonify({"message": "Facility not found"}), 404
    return jsonify({
        "id": facility.id,
        "name": facility.name,
        "description": facility.description,
        "image_url": facility.image_url,
        "uploaded_at": facility.uploaded_at.isoformat()
    })

@facilities_bp.route("/facilities/<int:facility_id>", methods=["PUT"])
def update_facility(facility_id: int):
    session = get_db()
    db_facility = session.query(Facility).filter(Facility.id == facility_id).first()
    if db_facility is None:
        return jsonify({"message": "Facility not found"}), 404
    
    name = request.form.get('name', db_facility.name)
    description = request.form.get('description', db_facility.description)
    file = request.files.get('file')

    db_facility.name = name
    db_facility.description = description

    if file:
        # Delete old file if it exists
        if db_facility.image_url and os.path.exists(os.path.join(current_app.root_path, db_facility.image_url.lstrip('/'))):
            os.remove(os.path.join(current_app.root_path, db_facility.image_url.lstrip('/')))

        upload_path = os.path.join(current_app.root_path, UPLOAD_FOLDER)
        os.makedirs(upload_path, exist_ok=True)
        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        file_location = os.path.join(upload_path, filename)
        file.save(file_location)
        db_facility.image_url = f"https://college-backend-api.onrender.com/static/uploads/facilities/{filename}"

    session.commit()
    session.refresh(db_facility)
    return jsonify({
        "id": db_facility.id,
        "name": db_facility.name,
        "description": db_facility.description,
        "image_url": db_facility.image_url,
        "uploaded_at": db_facility.uploaded_at.isoformat()
    })

@facilities_bp.route("/facilities/<int:facility_id>", methods=["DELETE"])
def delete_facility(facility_id: int):
    session = get_db()
    db_facility = session.query(Facility).filter(Facility.id == facility_id).first()
    if db_facility is None:
        return jsonify({"message": "Facility not found"}), 404
    
    # Delete the file from the server
    if db_facility.image_url and os.path.exists(os.path.join(current_app.root_path, db_facility.image_url.lstrip('/'))):
        os.remove(os.path.join(current_app.root_path, db_facility.image_url.lstrip('/')))

    session.delete(db_facility)
    session.commit()
    return jsonify({"message": "Facility deleted successfully"}), 200