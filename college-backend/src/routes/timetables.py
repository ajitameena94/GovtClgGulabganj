from flask import Blueprint, request, jsonify
from src.models.college import Timetable, Faculty, db
from src.routes.auth import login_required

timetables_bp = Blueprint('timetables', __name__)

@timetables_bp.route('/timetables', methods=['GET'])
def get_timetables():
    try:
        program = request.args.get('program')
        semester = request.args.get('semester', type=int)
        day_of_week = request.args.get('day_of_week')
        
        query = Timetable.query.filter_by(is_active=True)
        
        if program:
            query = query.filter(Timetable.program.contains(program))
        if semester:
            query = query.filter_by(semester=semester)
        if day_of_week:
            query = query.filter_by(day_of_week=day_of_week)
        
        timetables = query.order_by(Timetable.day_of_week, Timetable.time_slot).all()
        
        timetables_data = []
        for timetable in timetables:
            timetable_dict = timetable.to_dict()
            if timetable.faculty:
                timetable_dict['faculty_name'] = timetable.faculty.name
            timetables_data.append(timetable_dict)
        
        return jsonify(timetables_data), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@timetables_bp.route('/timetables/<int:timetable_id>', methods=['GET'])
def get_timetable(timetable_id):
    try:
        timetable = Timetable.query.get_or_404(timetable_id)
        timetable_dict = timetable.to_dict()
        if timetable.faculty:
            timetable_dict['faculty_name'] = timetable.faculty.name
        
        return jsonify(timetable_dict), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@timetables_bp.route('/timetables', methods=['POST'])
@login_required
def create_timetable():
    try:
        data = request.get_json()
        
        required_fields = ['program', 'semester', 'day_of_week', 'time_slot', 'subject']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field} is required'}), 400
        
        # Verify faculty exists if provided
        if data.get('faculty_id'):
            faculty = Faculty.query.get(data['faculty_id'])
            if not faculty:
                return jsonify({'error': 'Faculty not found'}), 404
        
        # Check for time slot conflicts
        existing_timetable = Timetable.query.filter_by(
            program=data['program'],
            semester=data['semester'],
            day_of_week=data['day_of_week'],
            time_slot=data['time_slot'],
            is_active=True
        ).first()
        
        if existing_timetable:
            return jsonify({'error': 'Time slot already occupied'}), 400
        
        timetable = Timetable(
            program=data['program'],
            semester=data['semester'],
            day_of_week=data['day_of_week'],
            time_slot=data['time_slot'],
            subject=data['subject'],
            faculty_id=data.get('faculty_id'),
            room_no=data.get('room_no')
        )
        
        db.session.add(timetable)
        db.session.commit()
        
        return jsonify({
            'message': 'Timetable created successfully',
            'timetable': timetable.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@timetables_bp.route('/timetables/<int:timetable_id>', methods=['PUT'])
@login_required
def update_timetable(timetable_id):
    try:
        timetable = Timetable.query.get_or_404(timetable_id)
        data = request.get_json()
        
        # Update fields if provided
        if 'subject' in data:
            timetable.subject = data['subject']
        if 'faculty_id' in data:
            if data['faculty_id']:
                faculty = Faculty.query.get(data['faculty_id'])
                if not faculty:
                    return jsonify({'error': 'Faculty not found'}), 404
            timetable.faculty_id = data['faculty_id']
        if 'room_no' in data:
            timetable.room_no = data['room_no']
        if 'is_active' in data:
            timetable.is_active = data['is_active']
        
        # Check for time slot conflicts if time-related fields are updated
        if any(field in data for field in ['day_of_week', 'time_slot', 'program', 'semester']):
            new_day = data.get('day_of_week', timetable.day_of_week)
            new_time = data.get('time_slot', timetable.time_slot)
            new_program = data.get('program', timetable.program)
            new_semester = data.get('semester', timetable.semester)
            
            existing_timetable = Timetable.query.filter(
                Timetable.id != timetable_id,
                Timetable.program == new_program,
                Timetable.semester == new_semester,
                Timetable.day_of_week == new_day,
                Timetable.time_slot == new_time,
                Timetable.is_active == True
            ).first()
            
            if existing_timetable:
                return jsonify({'error': 'Time slot already occupied'}), 400
            
            timetable.day_of_week = new_day
            timetable.time_slot = new_time
            timetable.program = new_program
            timetable.semester = new_semester
        
        db.session.commit()
        
        return jsonify({
            'message': 'Timetable updated successfully',
            'timetable': timetable.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@timetables_bp.route('/timetables/<int:timetable_id>', methods=['DELETE'])
@login_required
def delete_timetable(timetable_id):
    try:
        timetable = Timetable.query.get_or_404(timetable_id)
        db.session.delete(timetable)
        db.session.commit()
        
        return jsonify({'message': 'Timetable deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@timetables_bp.route('/timetables/weekly', methods=['GET'])
def get_weekly_timetable():
    try:
        program = request.args.get('program')
        semester = request.args.get('semester', type=int)
        
        if not program or not semester:
            return jsonify({'error': 'Program and semester are required'}), 400
        
        timetables = Timetable.query.filter_by(
            program=program,
            semester=semester,
            is_active=True
        ).order_by(Timetable.day_of_week, Timetable.time_slot).all()
        
        # Organize by day of week
        weekly_schedule = {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': [],
            'Saturday': []
        }
        
        for timetable in timetables:
            timetable_dict = timetable.to_dict()
            if timetable.faculty:
                timetable_dict['faculty_name'] = timetable.faculty.name
            
            if timetable.day_of_week in weekly_schedule:
                weekly_schedule[timetable.day_of_week].append(timetable_dict)
        
        return jsonify({
            'program': program,
            'semester': semester,
            'schedule': weekly_schedule
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@timetables_bp.route('/timetables/bulk-upload', methods=['POST'])
@login_required
def bulk_upload_timetables():
    try:
        data = request.get_json()
        timetables_data = data.get('timetables', [])
        
        if not timetables_data:
            return jsonify({'error': 'No timetables data provided'}), 400
        
        created_timetables = []
        errors = []
        
        for i, timetable_data in enumerate(timetables_data):
            try:
                # Verify required fields
                required_fields = ['program', 'semester', 'day_of_week', 'time_slot', 'subject']
                for field in required_fields:
                    if field not in timetable_data:
                        errors.append(f'Row {i+1}: {field} is required')
                        continue
                
                # Verify faculty exists if provided
                if timetable_data.get('faculty_id'):
                    faculty = Faculty.query.get(timetable_data['faculty_id'])
                    if not faculty:
                        errors.append(f'Row {i+1}: Faculty not found')
                        continue
                
                # Check for time slot conflicts
                existing_timetable = Timetable.query.filter_by(
                    program=timetable_data['program'],
                    semester=timetable_data['semester'],
                    day_of_week=timetable_data['day_of_week'],
                    time_slot=timetable_data['time_slot'],
                    is_active=True
                ).first()
                
                if existing_timetable:
                    errors.append(f'Row {i+1}: Time slot already occupied')
                    continue
                
                timetable = Timetable(
                    program=timetable_data['program'],
                    semester=timetable_data['semester'],
                    day_of_week=timetable_data['day_of_week'],
                    time_slot=timetable_data['time_slot'],
                    subject=timetable_data['subject'],
                    faculty_id=timetable_data.get('faculty_id'),
                    room_no=timetable_data.get('room_no')
                )
                
                db.session.add(timetable)
                created_timetables.append(timetable)
                
            except Exception as e:
                errors.append(f'Row {i+1}: {str(e)}')
        
        if errors:
            db.session.rollback()
            return jsonify({'errors': errors}), 400
        
        db.session.commit()
        
        return jsonify({
            'message': f'{len(created_timetables)} timetables uploaded successfully',
            'timetables': [timetable.to_dict() for timetable in created_timetables]
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

