from flask import Blueprint, request, jsonify
from src.models.college import Admin, db
from functools import wraps
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
from werkzeug.exceptions import BadRequest

auth_bp = Blueprint('auth', __name__)

# This is a placeholder for your JWTManager initialization
# It should be initialized in your main app.py file
# jwt = JWTManager(app) 

def login_required(f):
    @wraps(f)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
    except BadRequest as e:
        return jsonify({'error': f'Invalid JSON in request: {e.description}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    
    admin = Admin.query.filter_by(username=username).first()
    
    if admin and admin.check_password(password):
        access_token = create_access_token(identity=str(admin.id))
        return jsonify({
            'message': 'Login successful',
            'access_token': access_token,
            'admin': admin.to_dict()
        }), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401
            

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # Token is revoked on client side by deleting it from localStorage
    return jsonify({'message': 'Logout successful'}), 200

@auth_bp.route('/check-auth', methods=['GET'])
@jwt_required()
def check_auth():
    current_admin_id = get_jwt_identity()
    admin = Admin.query.get(current_admin_id)
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

