from flask import Blueprint, request, jsonify
from src.models.college import Faculty, db
from src.routes.auth import login_required

faculty_bp = Blueprint('faculty', __name__)

@faculty_bp.route('/faculty', methods=['GET'])
def get_faculty():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        department = request.args.get('department')
        designation = request.args.get('designation')
        
        query = Faculty.query
        
        if department:
            query = query.filter(Faculty.department.contains(department))
        if designation:
            query = query.filter(Faculty.designation.contains(designation))
        
        faculty_members = query.order_by(Faculty.name).paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return jsonify({
            'faculty': [member.to_dict() for member in faculty_members.items],
            'total': faculty_members.total,
            'pages': faculty_members.pages,
            'current_page': page
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@faculty_bp.route('/faculty/<int:faculty_id>', methods=['GET'])
def get_faculty_member(faculty_id):
    try:
        faculty_member = Faculty.query.get_or_404(faculty_id)
        return jsonify(faculty_member.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@faculty_bp.route('/faculty', methods=['POST'])
@login_required
def create_faculty():
    try:
        data = request.get_json()
        
        required_fields = ['employee_id', 'name', 'email', 'department', 'designation']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field} is required'}), 400
        
        # Check if employee ID already exists
        existing_faculty = Faculty.query.filter_by(employee_id=data['employee_id']).first()
        if existing_faculty:
            return jsonify({'error': 'Employee ID already exists'}), 400
        
        # Check if email already exists
        existing_email = Faculty.query.filter_by(email=data['email']).first()
        if existing_email:
            return jsonify({'error': 'Email already exists'}), 400
        
        faculty_member = Faculty(
            employee_id=data['employee_id'],
            name=data['name'],
            email=data['email'],
            phone=data.get('phone'),
            department=data['department'],
            designation=data['designation'],
            qualification=data.get('qualification'),
            experience=data.get('experience'),
            photo_url=data.get('photo_url')
        )
        
        db.session.add(faculty_member)
        db.session.commit()
        
        return jsonify({
            'message': 'Faculty member created successfully',
            'faculty': faculty_member.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@faculty_bp.route('/faculty/<int:faculty_id>', methods=['PUT'])
@login_required
def update_faculty(faculty_id):
    try:
        faculty_member = Faculty.query.get_or_404(faculty_id)
        data = request.get_json()
        
        # Update fields if provided
        if 'name' in data:
            faculty_member.name = data['name']
        if 'email' in data:
            # Check if new email already exists (excluding current record)
            existing_email = Faculty.query.filter(
                Faculty.email == data['email'],
                Faculty.id != faculty_id
            ).first()
            if existing_email:
                return jsonify({'error': 'Email already exists'}), 400
            faculty_member.email = data['email']
        if 'phone' in data:
            faculty_member.phone = data['phone']
        if 'department' in data:
            faculty_member.department = data['department']
        if 'designation' in data:
            faculty_member.designation = data['designation']
        if 'qualification' in data:
            faculty_member.qualification = data['qualification']
        if 'experience' in data:
            faculty_member.experience = data['experience']
        if 'photo_url' in data:
            faculty_member.photo_url = data['photo_url']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Faculty member updated successfully',
            'faculty': faculty_member.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@faculty_bp.route('/faculty/<int:faculty_id>', methods=['DELETE'])
@login_required
def delete_faculty(faculty_id):
    try:
        faculty_member = Faculty.query.get_or_404(faculty_id)
        db.session.delete(faculty_member)
        db.session.commit()
        
        return jsonify({'message': 'Faculty member deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@faculty_bp.route('/faculty/departments', methods=['GET'])
def get_departments():
    try:
        departments = [
            {'value': 'History', 'label': 'History'},
            {'value': 'Economics', 'label': 'Economics'},
            {'value': 'Sociology', 'label': 'Sociology'},
            {'value': 'Political Science', 'label': 'Political Science'},
            {'value': 'Hindi Literature', 'label': 'Hindi Literature'},
            {'value': 'English Literature', 'label': 'English Literature'},
            {'value': 'General', 'label': 'General'}
        ]
        
        return jsonify(departments), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@faculty_bp.route('/faculty/designations', methods=['GET'])
def get_designations():
    try:
        designations = [
            {'value': 'Professor', 'label': 'Professor'},
            {'value': 'Associate Professor', 'label': 'Associate Professor'},
            {'value': 'Assistant Professor', 'label': 'Assistant Professor'},
            {'value': 'Lecturer', 'label': 'Lecturer'},
            {'value': 'Principal', 'label': 'Principal'},
            {'value': 'Vice Principal', 'label': 'Vice Principal'},
            {'value': 'Head of Department', 'label': 'Head of Department'}
        ]
        
        return jsonify(designations), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@faculty_bp.route('/faculty/by-department', methods=['GET'])
def get_faculty_by_department():
    try:
        department = request.args.get('department')
        
        if not department:
            return jsonify({'error': 'Department is required'}), 400
        
        faculty_members = Faculty.query.filter(
            Faculty.department.contains(department)
        ).order_by(Faculty.name).all()
        
        return jsonify({
            'department': department,
            'faculty': [member.to_dict() for member in faculty_members]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@faculty_bp.route('/faculty/search', methods=['GET'])
def search_faculty():
    try:
        employee_id = request.args.get('employee_id')
        name = request.args.get('name')
        
        query = Faculty.query
        
        if employee_id:
            query = query.filter(Faculty.employee_id.contains(employee_id))
        if name:
            query = query.filter(Faculty.name.contains(name))
        
        faculty_members = query.order_by(Faculty.name).all()
        
        return jsonify([member.to_dict() for member in faculty_members]), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@faculty_bp.route('/faculty/bulk-upload', methods=['POST'])
@login_required
def bulk_upload_faculty():
    try:
        data = request.get_json()
        faculty_data = data.get('faculty', [])
        
        if not faculty_data:
            return jsonify({'error': 'No faculty data provided'}), 400
        
        created_faculty = []
        errors = []
        
        for i, member_data in enumerate(faculty_data):
            try:
                # Verify required fields
                required_fields = ['employee_id', 'name', 'email', 'department', 'designation']
                for field in required_fields:
                    if field not in member_data:
                        errors.append(f'Row {i+1}: {field} is required')
                        continue
                
                # Check if employee ID already exists
                existing_faculty = Faculty.query.filter_by(employee_id=member_data['employee_id']).first()
                if existing_faculty:
                    errors.append(f'Row {i+1}: Employee ID already exists')
                    continue
                
                # Check if email already exists
                existing_email = Faculty.query.filter_by(email=member_data['email']).first()
                if existing_email:
                    errors.append(f'Row {i+1}: Email already exists')
                    continue
                
                faculty_member = Faculty(
                    employee_id=member_data['employee_id'],
                    name=member_data['name'],
                    email=member_data['email'],
                    phone=member_data.get('phone'),
                    department=member_data['department'],
                    designation=member_data['designation'],
                    qualification=member_data.get('qualification'),
                    experience=member_data.get('experience'),
                    photo_url=member_data.get('photo_url')
                )
                
                db.session.add(faculty_member)
                created_faculty.append(faculty_member)
                
            except Exception as e:
                errors.append(f'Row {i+1}: {str(e)}')
        
        if errors:
            db.session.rollback()
            return jsonify({'errors': errors}), 400
        
        db.session.commit()
        
        return jsonify({
            'message': f'{len(created_faculty)} faculty members uploaded successfully',
            'faculty': [member.to_dict() for member in created_faculty]
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

