from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from datetime import datetime

from ..models.notification import Notification
from ..database.database import SessionLocal, engine, Base

notifications_bp = Blueprint('notifications', __name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@notifications_bp.route("/notifications", methods=["POST"])
def create_notification():
    db = next(get_db())
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    
    if not title or not content:
        return jsonify({"message": "Title and content are required"}), 400

    db_notification = Notification(title=title, content=content, created_at=datetime.utcnow())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return jsonify({
        "id": db_notification.id,
        "title": db_notification.title,
        "content": db_notification.content,
        "created_at": db_notification.created_at.isoformat()
    }), 201

@notifications_bp.route("/notifications", methods=["GET"])
def read_notifications():
    db = next(get_db())
    notifications = db.query(Notification).order_by(Notification.created_at.desc()).all()
    return jsonify([
        {
            "id": notification.id,
            "title": notification.title,
            "content": notification.content,
            "created_at": notification.created_at.isoformat()
        } for notification in notifications
    ])

@notifications_bp.route("/notifications/<int:notification_id>", methods=["GET"])
def read_notification(notification_id: int):
    db = next(get_db())
    notification = db.query(Notification).filter(Notification.id == notification_id).first()
    if notification is None:
        return jsonify({"message": "Notification not found"}), 404
    return jsonify({
        "id": notification.id,
        "title": notification.title,
        "content": notification.content,
        "created_at": notification.created_at.isoformat()
    })

@notifications_bp.route("/notifications/<int:notification_id>", methods=["PUT"])
def update_notification(notification_id: int):
    db = next(get_db())
    db_notification = db.query(Notification).filter(Notification.id == notification_id).first()
    if db_notification is None:
        return jsonify({"message": "Notification not found"}), 404
    
    data = request.get_json()
    db_notification.title = data.get('title', db_notification.title)
    db_notification.content = data.get('content', db_notification.content)
    
    db.commit()
    db.refresh(db_notification)
    return jsonify({
        "id": db_notification.id,
        "title": db_notification.title,
        "content": db_notification.content,
        "created_at": db_notification.created_at.isoformat()
    })

@notifications_bp.route("/notifications/<int:notification_id>", methods=["DELETE"])
def delete_notification(notification_id: int):
    db = next(get_db())
    db_notification = db.query(Notification).filter(Notification.id == notification_id).first()
    if db_notification is None:
        return jsonify({"message": "Notification not found"}), 404
    db.delete(db_notification)
    db.commit()
    return jsonify({"message": "Notification deleted successfully"}), 200