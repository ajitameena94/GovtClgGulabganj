from flask import Blueprint, request, jsonify, current_app
from datetime import datetime
import os
import uuid

from ..models.timetable import Timetable
from ..models.user import db

timetables_bp = Blueprint('timetables', __name__)

def get_db():
    return db.session

UPLOAD_FOLDER = 'src/static/uploads/timetables'

@timetables_bp.route("/timetables", methods=["POST"])
# @login_required # Add your authentication decorator here
def create_timetable():
    session = get_db()
    title = request.form.get('title')
    file = request.files.get('file')

    if not title or not file:
        return jsonify({"message": "Title and file are required"}), 400

    if file:
        # Ensure the upload directory exists
        upload_path = os.path.join(current_app.root_path, UPLOAD_FOLDER)
        os.makedirs(upload_path, exist_ok=True)

        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        file_location = os.path.join(upload_path, filename)
        file.save(file_location)
        file_url = f"https://college-backend-api.onrender.com/static/uploads/timetables/{filename}"
    else:
        return jsonify({"message": "File not provided"}), 400

    db_timetable = Timetable(title=title, file_url=file_url, uploaded_at=datetime.utcnow())
    session.add(db_timetable)
    session.commit()
    session.refresh(db_timetable)
    return jsonify({
        "id": db_timetable.id,
        "title": db_timetable.title,
        "file_url": db_timetable.file_url,
        "uploaded_at": db_timetable.uploaded_at.isoformat()
    }), 201

@timetables_bp.route("/timetables", methods=["GET"])
def read_timetables():
    session = get_db()
    timetables = session.query(Timetable).order_by(Timetable.uploaded_at.desc()).all()
    return jsonify([
        {
            "id": item.id,
            "title": item.title,
            "file_url": item.file_url,
            "uploaded_at": item.uploaded_at.isoformat()
        } for item in timetables
    ])

@timetables_bp.route("/timetables/<int:timetable_id>", methods=["GET"])
def read_timetable(timetable_id: int):
    session = get_db()
    item = session.query(Timetable).filter(Timetable.id == timetable_id).first()
    if item is None:
        return jsonify({"message": "Timetable not found"}), 404
    return jsonify({
        "id": item.id,
        "title": item.title,
        "file_url": item.file_url,
        "uploaded_at": item.uploaded_at.isoformat()
    })

@timetables_bp.route("/timetables/<int:timetable_id>", methods=["PUT"])
def update_timetable(timetable_id: int):
    session = get_db()
    db_timetable = session.query(Timetable).filter(Timetable.id == timetable_id).first()
    if db_timetable is None:
        return jsonify({"message": "Timetable not found"}), 404
    
    title = request.form.get('title', db_timetable.title)
    file = request.files.get('file')

    db_timetable.title = title

    if file:
        # Delete old file if it exists
        if db_timetable.file_url and os.path.exists(os.path.join(current_app.root_path, db_timetable.file_url.lstrip('/'))):
            os.remove(os.path.join(current_app.root_path, db_timetable.file_url.lstrip('/')))

        upload_path = os.path.join(current_app.root_path, UPLOAD_FOLDER)
        os.makedirs(upload_path, exist_ok=True)
        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        file_location = os.path.join(upload_path, filename)
        file.save(file_location)
        db_timetable.file_url = f"https://college-backend-api.onrender.com/static/uploads/timetables/{filename}"

    session.commit()
    session.refresh(db_timetable)
    return jsonify({
        "id": db_timetable.id,
        "title": db_timetable.title,
        "file_url": db_timetable.file_url,
        "uploaded_at": db_timetable.uploaded_at.isoformat()
    })

@timetables_bp.route("/timetables/<int:timetable_id>", methods=["DELETE"])
def delete_timetable(timetable_id: int):
    session = get_db()
    db_timetable = session.query(Timetable).filter(Timetable.id == timetable_id).first()
    if db_timetable is None:
        return jsonify({"message": "Timetable not found"}), 404
    
    # Delete the file from the server
    if db_timetable.file_url and os.path.exists(os.path.join(current_app.root_path, db_timetable.file_url.lstrip('/'))):
        os.remove(os.path.join(current_app.root_path, db_timetable.file_url.lstrip('/')))

    session.delete(db_timetable)
    session.commit()
    return jsonify({"message": "Timetable deleted successfully"}), 200