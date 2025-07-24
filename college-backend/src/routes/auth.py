from flask import Blueprint, request, jsonify, session
from src.models.college import Admin, db
from functools import wraps

auth_bp = Blueprint('auth', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_id' not in session:
            return jsonify({'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated_function

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400
        
        admin = Admin.query.filter_by(username=username).first()
        
        if admin and admin.check_password(password):
            session['admin_id'] = admin.id
            session['admin_username'] = admin.username
            return jsonify({
                'message': 'Login successful',
                'admin': admin.to_dict()
            }), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logout successful'}), 200

@auth_bp.route('/check-auth', methods=['GET'])
def check_auth():
    if 'admin_id' in session:
        admin = Admin.query.get(session['admin_id'])
        if admin:
            return jsonify({
                'authenticated': True,
                'admin': admin.to_dict()
            }), 200
    
    return jsonify({'authenticated': False}), 200

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if not username or not email or not password:
            return jsonify({'error': 'Username, email, and password are required'}), 400
        
        # Check if admin already exists
        existing_admin = Admin.query.filter(
            (Admin.username == username) | (Admin.email == email)
        ).first()
        
        if existing_admin:
            return jsonify({'error': 'Username or email already exists'}), 400
        
        # Create new admin
        admin = Admin(username=username, email=email)
        admin.set_password(password)
        
        db.session.add(admin)
        db.session.commit()
        
        return jsonify({
            'message': 'Admin registered successfully',
            'admin': admin.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

