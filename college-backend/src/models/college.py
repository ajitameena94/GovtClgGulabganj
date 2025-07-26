from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from src.models.user import db



class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enrollment_no = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    program = db.Column(db.String(50), nullable=False)  # BA History, BA Economics, etc.
    semester = db.Column(db.Integer, nullable=False)
    year_of_admission = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='active')  # active, inactive, graduated
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'enrollment_no': self.enrollment_no,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'program': self.program,
            'semester': self.semester,
            'year_of_admission': self.year_of_admission,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    department = db.Column(db.String(50), nullable=False)  # History, Economics, etc.
    designation = db.Column(db.String(50), nullable=False)  # Professor, Assistant Professor, etc.
    qualification = db.Column(db.String(200))
    experience = db.Column(db.Integer)  # years of experience
    photo_url = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'department': self.department,
            'designation': self.designation,
            'qualification': self.qualification,
            'experience': self.experience,
            'photo_url': self.photo_url,
            'created_at': self.created_at.isoformat()
        }

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # general, academic, admission, exam
    priority = db.Column(db.String(20), default='normal')  # high, normal, low
    target_audience = db.Column(db.String(50), default='all')  # all, students, faculty
    is_active = db.Column(db.Boolean, default=True)
    created_by = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'category': self.category,
            'priority': self.priority,
            'target_audience': self.target_audience,
            'is_active': self.is_active,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    marks_obtained = db.Column(db.Integer, nullable=False)
    total_marks = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(5))
    exam_type = db.Column(db.String(50), nullable=False)  # semester, annual
    exam_year = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    student = db.relationship('Student', backref=db.backref('results', lazy=True))
    
    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'semester': self.semester,
            'subject': self.subject,
            'marks_obtained': self.marks_obtained,
            'total_marks': self.total_marks,
            'grade': self.grade,
            'exam_type': self.exam_type,
            'exam_year': self.exam_year,
            'created_at': self.created_at.isoformat()
        }

class Timetable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    program = db.Column(db.String(50), nullable=False)  # BA History, BA Economics, etc.
    semester = db.Column(db.Integer, nullable=False)
    day_of_week = db.Column(db.String(10), nullable=False)  # Monday, Tuesday, etc.
    time_slot = db.Column(db.String(20), nullable=False)  # 09:00-10:00
    subject = db.Column(db.String(100), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))
    room_no = db.Column(db.String(20))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    faculty = db.relationship('Faculty', backref=db.backref('timetables', lazy=True))
    
    def to_dict(self):
        return {
            'id': self.id,
            'program': self.program,
            'semester': self.semester,
            'day_of_week': self.day_of_week,
            'time_slot': self.time_slot,
            'subject': self.subject,
            'faculty_id': self.faculty_id,
            'room_no': self.room_no,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat()
        }

class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # events, infrastructure, activities
    event_date = db.Column(db.Date)
    is_featured = db.Column(db.Boolean, default=False)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image_url': self.image_url,
            'category': self.category,
            'event_date': self.event_date.isoformat() if self.event_date else None,
            'is_featured': self.is_featured,
            'uploaded_by': self.uploaded_by,
            'created_at': self.created_at.isoformat()
        }

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    file_url = db.Column(db.String(200), nullable=False)
    file_type = db.Column(db.String(20), nullable=False)  # pdf, doc, xlsx
    category = db.Column(db.String(50), nullable=False)  # syllabus, forms, notices
    is_public = db.Column(db.Boolean, default=True)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'file_url': self.file_url,
            'file_type': self.file_type,
            'category': self.category,
            'is_public': self.is_public,
            'uploaded_by': self.uploaded_by,
            'created_at': self.created_at.isoformat()
        }

