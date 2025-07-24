from flask import Blueprint, request, jsonify
from src.models.college import Result, Student, db
from src.routes.auth import login_required

results_bp = Blueprint('results', __name__)

@results_bp.route('/results', methods=['GET'])
def get_results():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        semester = request.args.get('semester', type=int)
        exam_year = request.args.get('exam_year', type=int)
        program = request.args.get('program')
        
        query = Result.query.join(Student)
        
        if semester:
            query = query.filter(Result.semester == semester)
        if exam_year:
            query = query.filter(Result.exam_year == exam_year)
        if program:
            query = query.filter(Student.program.contains(program))
        
        results = query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        results_data = []
        for result in results.items:
            result_dict = result.to_dict()
            result_dict['student_name'] = result.student.name
            result_dict['student_enrollment'] = result.student.enrollment_no
            results_data.append(result_dict)
        
        return jsonify({
            'results': results_data,
            'total': results.total,
            'pages': results.pages,
            'current_page': page
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@results_bp.route('/results/<int:result_id>', methods=['GET'])
def get_result(result_id):
    try:
        result = Result.query.get_or_404(result_id)
        result_dict = result.to_dict()
        result_dict['student_name'] = result.student.name
        result_dict['student_enrollment'] = result.student.enrollment_no
        
        return jsonify(result_dict), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@results_bp.route('/results', methods=['POST'])
@login_required
def create_result():
    try:
        data = request.get_json()
        
        required_fields = ['student_id', 'semester', 'subject', 'marks_obtained', 'total_marks', 'exam_type', 'exam_year']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'{field} is required'}), 400
        
        # Verify student exists
        student = Student.query.get(data['student_id'])
        if not student:
            return jsonify({'error': 'Student not found'}), 404
        
        # Calculate grade based on percentage
        percentage = (data['marks_obtained'] / data['total_marks']) * 100
        if percentage >= 90:
            grade = 'A+'
        elif percentage >= 80:
            grade = 'A'
        elif percentage >= 70:
            grade = 'B+'
        elif percentage >= 60:
            grade = 'B'
        elif percentage >= 50:
            grade = 'C+'
        elif percentage >= 40:
            grade = 'C'
        else:
            grade = 'F'
        
        result = Result(
            student_id=data['student_id'],
            semester=data['semester'],
            subject=data['subject'],
            marks_obtained=data['marks_obtained'],
            total_marks=data['total_marks'],
            grade=grade,
            exam_type=data['exam_type'],
            exam_year=data['exam_year']
        )
        
        db.session.add(result)
        db.session.commit()
        
        return jsonify({
            'message': 'Result created successfully',
            'result': result.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@results_bp.route('/results/<int:result_id>', methods=['PUT'])
@login_required
def update_result(result_id):
    try:
        result = Result.query.get_or_404(result_id)
        data = request.get_json()
        
        # Update fields if provided
        if 'marks_obtained' in data:
            result.marks_obtained = data['marks_obtained']
        if 'total_marks' in data:
            result.total_marks = data['total_marks']
        if 'subject' in data:
            result.subject = data['subject']
        
        # Recalculate grade if marks changed
        if 'marks_obtained' in data or 'total_marks' in data:
            percentage = (result.marks_obtained / result.total_marks) * 100
            if percentage >= 90:
                result.grade = 'A+'
            elif percentage >= 80:
                result.grade = 'A'
            elif percentage >= 70:
                result.grade = 'B+'
            elif percentage >= 60:
                result.grade = 'B'
            elif percentage >= 50:
                result.grade = 'C+'
            elif percentage >= 40:
                result.grade = 'C'
            else:
                result.grade = 'F'
        
        db.session.commit()
        
        return jsonify({
            'message': 'Result updated successfully',
            'result': result.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@results_bp.route('/results/<int:result_id>', methods=['DELETE'])
@login_required
def delete_result(result_id):
    try:
        result = Result.query.get_or_404(result_id)
        db.session.delete(result)
        db.session.commit()
        
        return jsonify({'message': 'Result deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@results_bp.route('/results/search', methods=['GET'])
def search_results():
    try:
        enrollment_no = request.args.get('enrollment_no')
        semester = request.args.get('semester', type=int)
        exam_year = request.args.get('exam_year', type=int)
        
        if not enrollment_no:
            return jsonify({'error': 'Enrollment number is required'}), 400
        
        student = Student.query.filter_by(enrollment_no=enrollment_no).first()
        if not student:
            return jsonify({'error': 'Student not found'}), 404
        
        query = Result.query.filter_by(student_id=student.id)
        
        if semester:
            query = query.filter_by(semester=semester)
        if exam_year:
            query = query.filter_by(exam_year=exam_year)
        
        results = query.all()
        
        return jsonify({
            'student': student.to_dict(),
            'results': [result.to_dict() for result in results]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@results_bp.route('/results/bulk-upload', methods=['POST'])
@login_required
def bulk_upload_results():
    try:
        data = request.get_json()
        results_data = data.get('results', [])
        
        if not results_data:
            return jsonify({'error': 'No results data provided'}), 400
        
        created_results = []
        errors = []
        
        for i, result_data in enumerate(results_data):
            try:
                # Verify required fields
                required_fields = ['student_id', 'semester', 'subject', 'marks_obtained', 'total_marks', 'exam_type', 'exam_year']
                for field in required_fields:
                    if field not in result_data:
                        errors.append(f'Row {i+1}: {field} is required')
                        continue
                
                # Verify student exists
                student = Student.query.get(result_data['student_id'])
                if not student:
                    errors.append(f'Row {i+1}: Student not found')
                    continue
                
                # Calculate grade
                percentage = (result_data['marks_obtained'] / result_data['total_marks']) * 100
                if percentage >= 90:
                    grade = 'A+'
                elif percentage >= 80:
                    grade = 'A'
                elif percentage >= 70:
                    grade = 'B+'
                elif percentage >= 60:
                    grade = 'B'
                elif percentage >= 50:
                    grade = 'C+'
                elif percentage >= 40:
                    grade = 'C'
                else:
                    grade = 'F'
                
                result = Result(
                    student_id=result_data['student_id'],
                    semester=result_data['semester'],
                    subject=result_data['subject'],
                    marks_obtained=result_data['marks_obtained'],
                    total_marks=result_data['total_marks'],
                    grade=grade,
                    exam_type=result_data['exam_type'],
                    exam_year=result_data['exam_year']
                )
                
                db.session.add(result)
                created_results.append(result)
                
            except Exception as e:
                errors.append(f'Row {i+1}: {str(e)}')
        
        if errors:
            db.session.rollback()
            return jsonify({'errors': errors}), 400
        
        db.session.commit()
        
        return jsonify({
            'message': f'{len(created_results)} results uploaded successfully',
            'results': [result.to_dict() for result in created_results]
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

