from flask import Blueprint, request, jsonify
from src.models.college import Gallery, db
from src.routes.auth import login_required
import os
from werkzeug.utils import secure_filename
from datetime import datetime

gallery_bp = Blueprint('gallery', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
UPLOAD_FOLDER = 'uploads/gallery'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@gallery_bp.route('/gallery', methods=['GET'])
def get_gallery():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 12, type=int)
        category = request.args.get('category')
        featured_only = request.args.get('featured', type=bool)
        
        query = Gallery.query
        
        if category:
            query = query.filter_by(category=category)
        if featured_only:
            query = query.filter_by(is_featured=True)
        
        gallery_items = query.order_by(Gallery.created_at.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return jsonify({
            'gallery': [item.to_dict() for item in gallery_items.items],
            'total': gallery_items.total,
            'pages': gallery_items.pages,
            'current_page': page
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gallery_bp.route('/gallery/<int:gallery_id>', methods=['GET'])
def get_gallery_item(gallery_id):
    try:
        gallery_item = Gallery.query.get_or_404(gallery_id)
        return jsonify(gallery_item.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gallery_bp.route('/gallery/upload', methods=['POST'])
@login_required
def upload_gallery_image():
    try:
        from flask import session
        
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Allowed types: png, jpg, jpeg, gif, webp'}), 400
        
        # Get form data
        title = request.form.get('title')
        description = request.form.get('description', '')
        category = request.form.get('category', 'events')
        event_date = request.form.get('event_date')
        is_featured = request.form.get('is_featured', 'false').lower() == 'true'
        
        if not title:
            return jsonify({'error': 'Title is required'}), 400
        
        # Create upload directory if it doesn't exist
        upload_path = os.path.join('src/static', UPLOAD_FOLDER)
        os.makedirs(upload_path, exist_ok=True)
        
        # Generate unique filename
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
        filename = timestamp + filename
        file_path = os.path.join(upload_path, filename)
        
        # Save file
        file.save(file_path)
        
        # Create database entry
        image_url = f'/{UPLOAD_FOLDER}/{filename}'
        
        gallery_item = Gallery(
            title=title,
            description=description,
            image_url=image_url,
            category=category,
            event_date=datetime.strptime(event_date, '%Y-%m-%d').date() if event_date else None,
            is_featured=is_featured,
            uploaded_by=session['admin_id']
        )
        
        db.session.add(gallery_item)
        db.session.commit()
        
        return jsonify({
            'message': 'Image uploaded successfully',
            'gallery_item': gallery_item.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@gallery_bp.route('/gallery/<int:gallery_id>', methods=['PUT'])
@login_required
def update_gallery_item(gallery_id):
    try:
        gallery_item = Gallery.query.get_or_404(gallery_id)
        data = request.get_json()
        
        # Update fields if provided
        if 'title' in data:
            gallery_item.title = data['title']
        if 'description' in data:
            gallery_item.description = data['description']
        if 'category' in data:
            gallery_item.category = data['category']
        if 'event_date' in data:
            if data['event_date']:
                gallery_item.event_date = datetime.strptime(data['event_date'], '%Y-%m-%d').date()
            else:
                gallery_item.event_date = None
        if 'is_featured' in data:
            gallery_item.is_featured = data['is_featured']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Gallery item updated successfully',
            'gallery_item': gallery_item.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@gallery_bp.route('/gallery/<int:gallery_id>', methods=['DELETE'])
@login_required
def delete_gallery_item(gallery_id):
    try:
        gallery_item = Gallery.query.get_or_404(gallery_id)
        
        # Delete file from filesystem
        if gallery_item.image_url:
            file_path = os.path.join('src/static', gallery_item.image_url.lstrip('/'))
            if os.path.exists(file_path):
                os.remove(file_path)
        
        db.session.delete(gallery_item)
        db.session.commit()
        
        return jsonify({'message': 'Gallery item deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@gallery_bp.route('/gallery/categories', methods=['GET'])
def get_gallery_categories():
    try:
        categories = [
            {'value': 'events', 'label': 'Events'},
            {'value': 'infrastructure', 'label': 'Infrastructure'},
            {'value': 'activities', 'label': 'Activities'},
            {'value': 'faculty', 'label': 'Faculty'},
            {'value': 'students', 'label': 'Students'},
            {'value': 'achievements', 'label': 'Achievements'},
            {'value': 'campus', 'label': 'Campus Life'}
        ]
        
        return jsonify(categories), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gallery_bp.route('/gallery/featured', methods=['GET'])
def get_featured_gallery():
    try:
        limit = request.args.get('limit', 6, type=int)
        
        featured_items = Gallery.query.filter_by(is_featured=True).order_by(
            Gallery.created_at.desc()
        ).limit(limit).all()
        
        return jsonify([item.to_dict() for item in featured_items]), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gallery_bp.route('/gallery/by-category', methods=['GET'])
def get_gallery_by_category():
    try:
        category = request.args.get('category')
        limit = request.args.get('limit', 8, type=int)
        
        if not category:
            return jsonify({'error': 'Category is required'}), 400
        
        gallery_items = Gallery.query.filter_by(category=category).order_by(
            Gallery.created_at.desc()
        ).limit(limit).all()
        
        return jsonify({
            'category': category,
            'items': [item.to_dict() for item in gallery_items]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gallery_bp.route('/gallery/toggle-featured/<int:gallery_id>', methods=['PATCH'])
@login_required
def toggle_featured(gallery_id):
    try:
        gallery_item = Gallery.query.get_or_404(gallery_id)
        gallery_item.is_featured = not gallery_item.is_featured
        
        db.session.commit()
        
        status = 'featured' if gallery_item.is_featured else 'unfeatured'
        return jsonify({
            'message': f'Gallery item {status} successfully',
            'gallery_item': gallery_item.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@gallery_bp.route('/gallery/bulk-upload', methods=['POST'])
@login_required
def bulk_upload_gallery():
    try:
        from flask import session
        
        files = request.files.getlist('images')
        if not files or files[0].filename == '':
            return jsonify({'error': 'No files provided'}), 400
        
        # Get form data
        category = request.form.get('category', 'events')
        event_date = request.form.get('event_date')
        
        uploaded_items = []
        errors = []
        
        # Create upload directory if it doesn't exist
        upload_path = os.path.join('src/static', UPLOAD_FOLDER)
        os.makedirs(upload_path, exist_ok=True)
        
        for i, file in enumerate(files):
            try:
                if not allowed_file(file.filename):
                    errors.append(f'File {i+1}: Invalid file type')
                    continue
                
                # Generate unique filename
                filename = secure_filename(file.filename)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
                filename = f"{timestamp}{i+1}_{filename}"
                file_path = os.path.join(upload_path, filename)
                
                # Save file
                file.save(file_path)
                
                # Create database entry
                image_url = f'/{UPLOAD_FOLDER}/{filename}'
                
                gallery_item = Gallery(
                    title=f'Image {i+1}',
                    description='',
                    image_url=image_url,
                    category=category,
                    event_date=datetime.strptime(event_date, '%Y-%m-%d').date() if event_date else None,
                    is_featured=False,
                    uploaded_by=session['admin_id']
                )
                
                db.session.add(gallery_item)
                uploaded_items.append(gallery_item)
                
            except Exception as e:
                errors.append(f'File {i+1}: {str(e)}')
        
        if uploaded_items:
            db.session.commit()
        
        return jsonify({
            'message': f'{len(uploaded_items)} images uploaded successfully',
            'uploaded_items': [item.to_dict() for item in uploaded_items],
            'errors': errors
        }), 201 if uploaded_items else 400
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

