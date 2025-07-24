from flask import Blueprint, request, jsonify
from datetime import datetime

from ..models.notification import Notification
from ..models.user import db

notifications_bp = Blueprint('notifications', __name__)

def get_db():
    return db.session

@notifications_bp.route("/notifications", methods=["POST"])
def create_notification():
    session = get_db()
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    
    if not title or not content:
        return jsonify({"message": "Title and content are required"}), 400

    db_notification = Notification(title=title, content=content, created_at=datetime.utcnow())
    session.add(db_notification)
    session.commit()
    session.refresh(db_notification)
    return jsonify({
        "id": db_notification.id,
        "title": db_notification.title,
        "content": db_notification.content,
        "created_at": db_notification.created_at.isoformat()
    }), 201

@notifications_bp.route("/notifications", methods=["GET"])
def read_notifications():
    session = get_db()
    notifications = session.query(Notification).order_by(Notification.created_at.desc()).all()
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
    session = get_db()
    notification = session.query(Notification).filter(Notification.id == notification_id).first()
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
    session = get_db()
    db_notification = session.query(Notification).filter(Notification.id == notification_id).first()
    if db_notification is None:
        return jsonify({"message": "Notification not found"}), 404
    
    data = request.get_json()
    db_notification.title = data.get('title', db_notification.title)
    db_notification.content = data.get('content', db_notification.content)
    
    session.commit()
    session.refresh(db_notification)
    return jsonify({
        "id": db_notification.id,
        "title": db_notification.title,
        "content": db_notification.content,
        "created_at": db_notification.created_at.isoformat()
    })

@notifications_bp.route("/notifications/<int:notification_id>", methods=["DELETE"])
def delete_notification(notification_id: int):
    session = get_db()
    db_notification = session.query(Notification).filter(Notification.id == notification_id).first()
    if db_notification is None:
        return jsonify({"message": "Notification not found"}), 404
    session.delete(db_notification)
    session.commit()
    return jsonify({"message": "Notification deleted successfully"}), 200