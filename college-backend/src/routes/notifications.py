from flask import Blueprint, request, jsonify
from src.models.college import Notification, db
from src.routes.auth import login_required
from datetime import datetime

notifications_bp = Blueprint('notifications', __name__)

@notifications_bp.route('/notifications', methods=['GET'])
def get_notifications():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        category = request.args.get('category')
        priority = request.args.get('priority')
        target_audience = request.args.get('target_audience')
        
        query = Notification.query.filter_by(is_active=True)
        
        if category:
            query = query.filter_by(category=category)
        if priority:
            query = query.filter_by(priority=priority)
        if target_audience:
            query = query.filter_by(target_audience=target_audience)
        
        notifications = query.order_by(Notification.created_at.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return jsonify({
            'notifications': [notification.to_dict() for notification in notifications.items],
            'total': notifications.total,
            'pages': notifications.pages,
            'current_page': page
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@notifications_bp.route('/notifications/<int:notification_id>', methods=['GET'])
def get_notification(notification_id):
    try:
        notification = Notification.query.get_or_404(notification_id)
        return jsonify(notification.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@notifications_bp.route('/notifications', methods=['POST'])
@login_required
def create_notification():
    try:
        from flask import session
        data = request.get_json()
        
        required_fields = ['title', 'content', 'category']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field} is required'}), 400
        
        notification = Notification(
            title=data['title'],
            content=data['content'],
            category=data['category'],
            priority=data.get('priority', 'normal'),
            target_audience=data.get('target_audience', 'all'),
            created_by=session['admin_id']
        )
        
        db.session.add(notification)
        db.session.commit()
        
        return jsonify({
            'message': 'Notification created successfully',
            'notification': notification.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@notifications_bp.route('/notifications/<int:notification_id>', methods=['PUT'])
@login_required
def update_notification(notification_id):
    try:
        notification = Notification.query.get_or_404(notification_id)
        data = request.get_json()
        
        # Update fields if provided
        if 'title' in data:
            notification.title = data['title']
        if 'content' in data:
            notification.content = data['content']
        if 'category' in data:
            notification.category = data['category']
        if 'priority' in data:
            notification.priority = data['priority']
        if 'target_audience' in data:
            notification.target_audience = data['target_audience']
        if 'is_active' in data:
            notification.is_active = data['is_active']
        
        notification.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'message': 'Notification updated successfully',
            'notification': notification.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@notifications_bp.route('/notifications/<int:notification_id>', methods=['DELETE'])
@login_required
def delete_notification(notification_id):
    try:
        notification = Notification.query.get_or_404(notification_id)
        db.session.delete(notification)
        db.session.commit()
        
        return jsonify({'message': 'Notification deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@notifications_bp.route('/notifications/recent', methods=['GET'])
def get_recent_notifications():
    try:
        limit = request.args.get('limit', 5, type=int)
        target_audience = request.args.get('target_audience', 'all')
        
        query = Notification.query.filter_by(is_active=True)
        
        if target_audience != 'all':
            query = query.filter(
                (Notification.target_audience == target_audience) |
                (Notification.target_audience == 'all')
            )
        
        notifications = query.order_by(Notification.created_at.desc()).limit(limit).all()
        
        return jsonify([notification.to_dict() for notification in notifications]), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@notifications_bp.route('/notifications/categories', methods=['GET'])
def get_notification_categories():
    try:
        categories = [
            {'value': 'general', 'label': 'General'},
            {'value': 'academic', 'label': 'Academic'},
            {'value': 'admission', 'label': 'Admission'},
            {'value': 'exam', 'label': 'Examination'},
            {'value': 'event', 'label': 'Events'},
            {'value': 'holiday', 'label': 'Holidays'},
            {'value': 'urgent', 'label': 'Urgent'}
        ]
        
        return jsonify(categories), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@notifications_bp.route('/notifications/priorities', methods=['GET'])
def get_notification_priorities():
    try:
        priorities = [
            {'value': 'low', 'label': 'Low'},
            {'value': 'normal', 'label': 'Normal'},
            {'value': 'high', 'label': 'High'}
        ]
        
        return jsonify(priorities), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@notifications_bp.route('/notifications/audiences', methods=['GET'])
def get_notification_audiences():
    try:
        audiences = [
            {'value': 'all', 'label': 'All'},
            {'value': 'students', 'label': 'Students'},
            {'value': 'faculty', 'label': 'Faculty'},
            {'value': 'staff', 'label': 'Staff'}
        ]
        
        return jsonify(audiences), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@notifications_bp.route('/notifications/toggle/<int:notification_id>', methods=['PATCH'])
@login_required
def toggle_notification(notification_id):
    try:
        notification = Notification.query.get_or_404(notification_id)
        notification.is_active = not notification.is_active
        notification.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        status = 'activated' if notification.is_active else 'deactivated'
        return jsonify({
            'message': f'Notification {status} successfully',
            'notification': notification.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

