from flask import Blueprint, request, jsonify
from src.models.college import Student, Result, db
from src.routes.auth import login_required

students_bp = Blueprint('students', __name__)

@students_bp.route('/students', methods=['GET'])
def get_students():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        program = request.args.get('program')
        semester = request.args.get('semester', type=int)
        
        query = Student.query
        
        if program:
            query = query.filter(Student.program.contains(program))
        if semester:
            query = query.filter_by(semester=semester)
        
        students = query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return jsonify({
            'students': [student.to_dict() for student in students.items],
            'total': students.total,
            'pages': students.pages,
            'current_page': page
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@students_bp.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    try:
        student = Student.query.get_or_404(student_id)
        return jsonify(student.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@students_bp.route('/students', methods=['POST'])
@login_required
def create_student():
    try:
        data = request.get_json()
        
        required_fields = ['enrollment_no', 'name', 'email', 'program', 'semester', 'year_of_admission']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field} is required'}), 400
        
        # Check if enrollment number already exists
        existing_student = Student.query.filter_by(enrollment_no=data['enrollment_no']).first()
        if existing_student:
            return jsonify({'error': 'Enrollment number already exists'}), 400
        
        student = Student(
            enrollment_no=data['enrollment_no'],
            name=data['name'],
            email=data['email'],
            phone=data.get('phone'),
            program=data['program'],
            semester=data['semester'],
            year_of_admission=data['year_of_admission'],
            status=data.get('status', 'active')
        )
        
        db.session.add(student)
        db.session.commit()
        
        return jsonify({
            'message': 'Student created successfully',
            'student': student.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@students_bp.route('/students/<int:student_id>', methods=['PUT'])
@login_required
def update_student(student_id):
    try:
        student = Student.query.get_or_404(student_id)
        data = request.get_json()
        
        # Update fields if provided
        if 'name' in data:
            student.name = data['name']
        if 'email' in data:
            student.email = data['email']
        if 'phone' in data:
            student.phone = data['phone']
        if 'program' in data:
            student.program = data['program']
        if 'semester' in data:
            student.semester = data['semester']
        if 'status' in data:
            student.status = data['status']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Student updated successfully',
            'student': student.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@students_bp.route('/students/<int:student_id>', methods=['DELETE'])
@login_required
def delete_student(student_id):
    try:
        student = Student.query.get_or_404(student_id)
        db.session.delete(student)
        db.session.commit()
        
        return jsonify({'message': 'Student deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@students_bp.route('/students/search', methods=['GET'])
def search_students():
    try:
        enrollment_no = request.args.get('enrollment_no')
        
        if not enrollment_no:
            return jsonify({'error': 'Enrollment number is required'}), 400
        
        student = Student.query.filter_by(enrollment_no=enrollment_no).first()
        
        if student:
            return jsonify(student.to_dict()), 200
        else:
            return jsonify({'error': 'Student not found'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@students_bp.route('/students/<int:student_id>/results', methods=['GET'])
def get_student_results(student_id):
    try:
        student = Student.query.get_or_404(student_id)
        results = Result.query.filter_by(student_id=student_id).all()
        
        return jsonify({
            'student': student.to_dict(),
            'results': [result.to_dict() for result in results]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

